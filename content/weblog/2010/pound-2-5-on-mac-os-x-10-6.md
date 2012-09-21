---
title: Pound 2.5 on Mac OS X 10.6
slug: pound-25-mac-os-x-106
date: 2010-07-02 12:28
tags: [apple, development, plone]
---

While updating a buildout, [Pound](http://www.apsis.ch/pound/) would
not compile anymore. "All" I did was update it from version 2.4.4 to
2.5.

When running the buildout, which uses the
[plone.recipe.pound](http://pypi.python.org/pypi/plone.recipe.pound)
by the way, it ended with this:

    An internal error occured due to a bug in either zc.buildout or in arecipe being used:Traceback (most recent call last):  File "/private/var/folders/jt/jtv7gTB4GgqMNrztzYnFoU+++TI/-Tmp-/tmpWzlOWE/zc.buildout-1.5.0b2-py2.4.egg/zc/buildout/buildout.py", line 1660, in main  File "/private/var/folders/jt/jtv7gTB4GgqMNrztzYnFoU+++TI/-Tmp-/tmpWzlOWE/zc.buildout-1.5.0b2-py2.4.egg/zc/buildout/buildout.py", line 532, in install  File "/private/var/folders/jt/jtv7gTB4GgqMNrztzYnFoU+++TI/-Tmp-/tmpWzlOWE/zc.buildout-1.5.0b2-py2.4.egg/zc/buildout/buildout.py", line 1204, in _call  File "/Users/mark/projects/prettigpersoneel/svn_trunk/eggs/plone.recipe.pound-0.5.5-py2.4.egg/plone/recipe/pound/build.py", line 78, in install    installed = CMMIRecipe.install(self)  File "/Users/mark/projects/prettigpersoneel/svn_trunk/eggs/zc.recipe.cmmi-1.3.1-py2.4.egg/zc/recipe/cmmi/__init__.py", line 159, in install    self.cmmi(dest)  File "/Users/mark/projects/prettigpersoneel/svn_trunk/eggs/zc.recipe.cmmi-1.3.1-py2.4.egg/zc/recipe/cmmi/__init__.py", line 187, in cmmi    system("make")  File "/Users/mark/projects/prettigpersoneel/svn_trunk/eggs/zc.recipe.cmmi-1.3.1-py2.4.egg/zc/recipe/cmmi/__init__.py", line 32, in system    raise SystemError("Failed", c)SystemError: ('Failed', 'make')

Looking a bit further back, I saw this:

    pound.h:188:2: error: #error "You have libpcreposix, but the header files are missing. Use --disable-pcreposix"

And before that:

    checking pcreposix.h usability... nochecking pcreposix.h presence... nochecking for pcreposix.h... nochecking pcre/pcreposix.h usability... nochecking pcre/pcreposix.h presence... nochecking for pcre/pcreposix.h... no

Okay, now we're getting somewhere... Apparently I had to make sure
`pcreposix.h` was available. However, I had already installed `pcre`
and `pcre++` via [MacPorts](http://www.macports.org/). Google also
didn't turn up any hints on where to get the needed header file.

Luckiliy I remembered that I had installed
[Homebrew](http://github.com/mxcl/homebrew) a while back. A quick

    $ brew install pcre

solved my problem: pound compiled and the buildout ran without
problems again.
