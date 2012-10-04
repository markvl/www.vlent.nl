---
title: Upgrade Ubuntu 8.04 to 8.10
slug: upgrade-ubuntu-8.04-to-8.10
date: 2009-02-19 20:44
tags: [python, ubuntu]
---

Almost flawless upgrade from Hardy Heron to Intrepid Ibex. Only
python-setuptools needed manual attention. Other than that: I love it!

Although Intrepid Ibex has been released quite a while ago, and the
new release is only a few months away, I finally decided to upgrade. A
colleague reported problems with his Nvidia chipset last year and he
downgraded to Hardy again. Since I have setup my X so I can use my
laptop with an extra monitor, I was afraid I'd also run into
problems. A dying hard disk gave me the last push to finally upgrade.

(The hard drive in my laptop made a high pitched noize indicating a
problem with the ball bearings. To replace it, I created an image with
`ddrescue` to a USB drive, which worked great! After restoring it I
decided this was the right moment to also test whether the upgrade of
Ubuntu would work. If anything would go wrong, restoring the image
again would be a breeze.)

All in all the upgrade went pretty smooth. There was just a small
problem with upgrading the `python-setuptools` package. It probably
went wrong because I
[upgraded it manually a while ago](/weblog/2008/09/18/setuptools-and-subversion-1.5
"Setuptools and subversion 1.5"). Uninstalling the package (`apt-get
remove python-setuptools`) and reinstalling it again (yep: `apt-get
install python-setuptools`) solved it. Okay, I also had to install two
additional packages which were removed since they depended on
python-setuptools, but that was it.

Since I haven't done any actual work with this upgraded version, I
cannot confirm everything works exactly as it used to. But I am
confident I won't be disappointed. Two things I noted and am very
enthousiastic about:

1. Suspending the system finally works! This will make working while
   traveling a lot easier.
2. The new `nvidia-settings` utility makes it possible to apply changed
   settings immediately without having to log out and in again.

Especially the last will help me improve my daily routine! Now I can
more easily disconnect the extra monitor I use at the office and take
my laptop to e.g the desk of a colleague to pair program without
losing the panels and half of my windows or logging out of X. Need to
show something on a beamer? No problem, I can just connect it and a
couple of quick clicks later it just works.

Thanks Ubuntu community and Canonical!
