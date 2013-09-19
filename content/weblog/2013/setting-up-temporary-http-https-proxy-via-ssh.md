---
title: Setting up a temporary HTTP/HTTPS proxy via SSH
date: 2013-09-19 06:32
tags: [development, devops]
---

Currently I'm working on a project where I have the staging
environment running on a virtual machine in a vlan. However, the
virtual machine cannot directly access the internet for security
reasons. This is inconvenient when I want to e.g. run a
[buildout](http://www.buildout.org/) to update the project.

A colleague told me to use
[micro_proxy](http://acme.com/software/micro_proxy/) and
[micro_inetd](http://www.acme.com/software/micro_inetd/) to proxy
traffic via my laptop. This is a description of how you can set things up.

# Ad hoc

Obviously the first step is to install the relevant packages on the
local machine (Ubuntu in my case):

    $ sudo apt-get install micro-proxy micro-inetd

The next step is to run the proxy (again: on my laptop) and make sure
it accepts connections on port `3128`:

    $ micro-inetd 3128 /usr/sbin/micro_proxy

Then, when you SSH into the remote machine you will have to forward
the right port:

    $ ssh box.example.com -R 3128:localhost:3128

Whenever you want to access the internet, you'll have to use the proxy
listening on port `3128`. For instance to run `wget` and `buildout`,
you can set the following environment variables:

    $ export http_proxy=http://localhost:3128
    $ export https_proxy=http://localhost:3128

(Note that I'm also proxying HTTPS traffic here, which is supported by
`micro_proxy`.)

The following `wget` command should now succeed:

    $ wget http://www.google.com/


# Repeatable

Assuming the ad hoc setup works, you may want to configure things so
things are a little bit easier the next time you want to use it. This
is what I did.

So I don't have to remember how to start the proxy, I added this line
to the `~/.bashrc` file on my local machine:

    alias start_proxy='echo Running proxy on port 3128 && micro-inetd 3128 /usr/sbin/micro_proxy'

The SSH command is also too much typing for my liking. So I added this
to my `~/.ssh/config` file:

    Host box
        HostName box.example.com
        RemoteForward 3128 localhost:3128

To make sure that the HTTP(S) proxy is used on the remote machine, I
added this to my `~/.bashrc` file on the remote:

    export http_proxy=http://localhost:3128
    export https_proxy=http://localhost:3128


# End result

So whenever I want to work on the staging environment, I open a
terminal and run:

    $ start_proxy

In another terminal I type:

    $ ssh box

And I'm good to go.

Now, there may be better solutions (especially if you want to
permanently setup a proxy), but for my purposes this works great.
