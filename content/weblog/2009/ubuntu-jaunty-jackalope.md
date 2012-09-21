---
title: Ubuntu Jaunty Jackalope
date: 2009-05-30 18:14
tags: [apple, python, ubuntu]
---

My experiences with upgrading Ubunty 8.10 (Intrepid Ibex) to Ubuntu
9.04.

This time I decided to not
[wait for four months](/weblog/2009/02/19/upgrade-ubuntu-8.04-to-8.10/)
before updating to the new Ubuntu version. Especially since colleagues
reported to work successfully with this new version. I've worked with
this setup for a week or two now and everything seems to work. Here's
what I encountered:

# Python

I expected to run into problems with python since the Ubuntu packages
for e.g. python imaging and xml (which I need for my day-to-day work)
aren't available for version 2.4 anymore. While
[Maurits van Rees](http://maurits.vanrees.org/weblog/archive/2009/03/using-ubuntu-9-04-beta)
and [Sam Stainsby](http://sam.stainsby.id.au/blog/?p=28) chose to work
with virtualenv, I installed the required packages globally.

[Setuptools](http://peak.telecommunity.com/DevCenter/setuptools) and
[PIL](http://www.pythonware.com/products/pil/) were relatively easy to
install. Just a matter of downloading and running "`/usr/bin/python2.4
setup.py install`" (IIRC, to be honest I didn't document this.)
However, the libxml2 python bindings proved to be a bit harder. I
needed the following steps to get it up and running (thanks to
[Hedley Roos and Izak Burger](http://www.upfrontsystems.co.za/Members/hedley/my-random-musings/compile-and-install-libxml2-python)):

  - [Download](ftp://xmlsoft.org/libxml2/) version 2.6.32 since that is
    the version of the Ubuntu limxml2 package.
  - Unpack the tarball, run "`./configure`" and "`make`"
  - Go to the python directory and execute:
    - `CFLAGS=-I/usr/include/libxml2 /usr/bin/python2.4 setup.py build`
    - `sudo CFLAGS=-I/usr/include/libxml2 /usr/bin/python2.4 setup.py install`

# Loud beep on shutdown

The new version of Ubuntu also brought a loud surprise: every time I
powered down my laptop a beep was audible. Since it seemed to bypass
the sound driver (muting the sound didn't help) I could not even turn
it down. Changing the Gnome settings
[as recommended](http://ubuntuforums.org/showthread.php?p=7215341) did
not work; my Dell Precision M65 kept on making the noise.

Luckily the solution provided on
[another thread](http://ubuntuforums.org/showthread.php?t=1151784) did
work. I added the following line to `/etc/modpobe.d/blacklist.conf`:

    blacklist pcspkr

And I enjoy the silence once again. As an additional benefit: no more
lound beeps if I make mistakes (e.g. trying to scroll pas the end of
my Tomboy note, try to use backspace at the beginning of a line in
XChat, et cetera). So in a way I'm grateful of the loud beeps at
shutdown: I wasn't annoyed enough by the other beeps to silence them
but I'm glad I got rid of them. And so do the people in my
environment. :)

# Apple keyboard

At [Zest](http://zestsoftware.nl) we use the thin (wired)
[Apple keyboards](http://images.apple.com/keyboard/images/gallery/wired_1_20070813.jpg). They
look slick and work quite well. The problem I had with them (besides
that we've got the Dutch keyboard layout, which has the tilde placed
near the "z" instead of where if should be: next to the "1" key) is
that the function keys didn't work. That is: I had to push the "fn"
key. Otherwise pressing F12 turned up the volume instead of bringing up
Firebug.

On Intrepid I solved this already by having a file called
`/etc/modprobe.d/applekeyboard` with the following contents:

    options hid pb_fnmode=2

Apparently this didn't work anymore. Neither did the solutions I
[initially](http://dancingpenguinsoflight.com/2009/01/fixing-the-function-keys-on-the-apple-keyboard-in-ubuntu/)
[found](http://nardusg.blogspot.com/2009/03/apple-keyboard-on-ubuntukubuntu-jaunty.html).
[Brian K. White](http://tipotheday.com/2008/04/30/slim-aluminum-apple-keyboard-with-ubuntu-hardy-heron/#comment-2085)
on the other hand presented a solution that worked for me.

I've now got `/etc/modprobe.d/hid_apple.conf` with this line:

    options hid_apple fnmode=2

Updating initramfs (“``update-initramfs -k `uname -r` -u``”) and a
reboot later the function keys worked as I like them. (While writing
this blog entry and checking my sources, I see that this information
is now also available on the
[AppleKeyboard](http://help.ubuntu.com/community/AppleKeyboard#Ubuntu%209.04%20(Jaunty%20Jakalope))
page in the Ubuntu Community Documentation.)
