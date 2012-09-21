---
title: "Upgrade Ubuntu 8.04 to 8.10, part two: firwall fun"
slug: upgrade-ubuntu-8.04-to-8.10-part-two-firewall-fun
date: 2009-02-21 13:07
tags: [ubuntu]
---

The new network-manager package in Intrepid messed up my firewall
(managed by Firestarter) by connecting to the wired and wireless
network at the same time. The solution for me: Gufw.

When I got to the office after I
[upgraded Ubuntu to the 8.10 release](/weblog/upgrade-ubuntu-8.04-to-8.10
"Upgrade Ubuntu 8.04 to 8.10"), I could not log in on one of our
servers, not a single web page loaded and I wasn't even allowed to
ping to other machines. Disconnecting the network cable and using the
wireless connection made everything work again.

After spending some time where I found out that the wired network
wasn't to blame, I asked our sysadmin for help. It appeared that the
network manager in Intrepid (version 0.7)
[connects to both](https://bugs.launchpad.net/ubuntu/+source/network-manager/+bug/262152)
[the wired and wireless network](https://bugs.launchpad.net/ubuntu/+source/network-manager/+bug/278485)
if it can. This doesn't have to be a problem though. All traffic was
routed via the wired connection. So that wasn't the problem.

What took me a while to figure out was that I used Firestarter to
manage the firewall for my wireless connection. (I tend to connect to
WLANs at customers, train stations, etc. And since I'm too lazy to
manage which ports my laptop listens to, I just want to block all
incoming traffic.) Since I installed it a while ago and it just
worked, I had forgotten all about it.

I don't know the exact details, but apparently Firestarter, correctly,
saw that I had a wireless connection and it blocked all traffic via
the wired connection. But that was the default route... Disabling the
firewall solved the problem so the culprit had been found.

Unfortunately, I could not figure out how to get Firestarter to
behave. It has been a while since I configured a firewall manually and
I really didn't fancy diving into the iptables documentation. I
therefore decided to use the
[Uncomplicated Firewall](https://wiki.ubuntu.com/UbuntuFirewall)
topped off with [Guwf](http://gufw.tuxfamily.org/index.html) for easy
configuration.

Installation and configuration was a breeze. After using your
favourite tool to install packages, you can find Gufw via *System*,
*Administration*, *Firewall configuration*. All I needed to do was
enabling it and making sure it was configured to deny incoming
traffic. As an extra I also allowed SSH access since I regularly want
to copy stuff to and from other machines. That was it; I'm all set
again.
