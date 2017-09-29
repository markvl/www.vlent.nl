---
title: How to create a Debian VirtualBox machine with Packer with an additional host-only adapter
date: 2017-09-29 13:50
tags: [devops, packer, tools, virtualbox]
---

For a project I am working on, there is this virtual machine we can
use to do our development work in. This machine has grown organically
and I want to replace it with something I can reproduce. I wanted to
experiment with Packer but had problems with generating a machine with
two network adapters where the second one is connected to a host-only
network.

# Context

Before getting into the details, first a bit of context. The virtual
machine (VM) we are using is really convenient. It was created by a
co-worker and was exported some time in the past and is now available
as an `.ova` for other developers in the team.  But the machine itself
has been built over a longer period of time, using Debian Jessie
(which is now the
“[oldstable](https://wiki.debian.org/DebianOldStable)”) and some
project requirements have changed.

I could upgrade the VM to Stretch, update the packages and export the
VM again. But I'd rather get something reproducible. Something I can
build again and again and know exactly _how_ it was created, _what_
was installed, et cetera. (And truth be told, perhaps there's
also a bit of
“[not invented here](https://en.wikipedia.org/wiki/Not_invented_here)”
involved.)


# Problem

To get to such a reproducible VM I decided to try out
[Packer](https://www.packer.io/). I also found a great Git repository
which you can use to generate a Debian 9 Vagrant Box:
[https://github.com/geerlingguy/packer-debian-9](https://github.com/geerlingguy/packer-debian-9). This
got me started fairly quickly.

_(As a side note: if you are interested in Ansible, you should
definitely check out
[Jeff Geerling's other GitHub repositories](https://github.com/geerlingguy?tab=repositories).)_

The problem was that I needed not one, but **two** network adapters
for my VM, where the second interface had to be connected to a
[host-only](https://www.virtualbox.org/manual/ch06.html#network_hostonly)
network.


# The solution

First of all, I needed to add the second adapter to the
configuration. In the `debian9.json` file, I replaced the original
`vboxmanage` section with the following:

    "vboxmanage": [
      [
        "modifyvm",
        "{{.Name}}",
        "--memory",
        "1024"
      ],
      [
        "modifyvm",
        "{{.Name}}",
        "--cpus",
        "1"
      ],
      [
        "modifyvm",
        "{{.Name}}",
        "--nic2",
        "hostonly"
      ],
      [
        "modifyvm",
        "{{.Name}}",
        "--hostonlyadapter2",
        "vboxnet0"
      ]
    ]

In other words I added the `--nic2` and `--hostonlyadapter2` options.

But when I tried to build the VM, Packer kept waiting for SSH to
become available. After starting the build again with the "`headless`"
option set to "`false`" I could see the problem: the Debian installer
was waiting for me to select which interface to use (since there were
two now).

I solved this by inserting the following line to the `boot_command`
section in the `debian9.json` file:

    "interface=enp0s3 <wait>",

Now the first interface was automatically chosen and the build
succeeded again. The result: a VM with two network adapters, where the
first one is attached to the NAT network, and the second one to the
host-only network `vboxnet0`.
