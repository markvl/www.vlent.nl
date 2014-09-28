---
title: Setuptools and subversion 1.5
slug: setuptools-and-subversion-1.5
date: 2008-09-18 11:06
tags: [plone, python, subversion, tools]
---

Setuptools doesn't seem to like subversion 1.5

Earlier this week I ran into problems with setuptools on my Ubuntu
Hardy Heron system, which uses subversion 1.5. Luckily I wasn't the
first as proven by
[several](http://mrtopf.de/blog/plone/using-subversion-15-with-setuptools-in-python-technical/)
[other](http://bugs.debian.org/cgi-bin/bugreport.cgi?bug=489263)
[reports](http://bugs.python.org/setuptools/issue4).

To be able to develop Plone products properly I had to do two things:

1. Globally install this patched version.
2. Make sure buildout uses a patched version of setuptools.

The first part was the easiest:
[following the instructions](http://bugs.python.org/setuptools/msg62)
I was finished in no time. This prevents the scrambled eggs
[reported by Maurits](http://maurits.vanrees.org/weblog/archive/2008/09/scrambled-eggs).

The second task was a bit more labour intensive (albeit just
slightly). First I had to unpin the version of setuptools in the
buildout configuration. However, since there is no egg available on
[PyPI](https://pypi.python.org/pypi) at the moment with a fix,
buildout still uses an unpatched version. But I didn't like the idea
of inserting a find-link in the buildout configuration. The simple
solution was to download an egg which contained a fix and put it in my
`eggs` directory. (On a sidenote: I use a single egg directory for all
my Plone instances on my development machine. This makes this solution
viable.)

I'm not completely happy with the current situation, but at least I
can continue working. Let's hope a fixed version of setuptools will be
released soon...

**Update (2008-09-26):** setuptools 0.6c9 has been released. This new
  version solves the problem. Normality restored!
