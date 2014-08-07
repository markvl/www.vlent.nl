---
title: Products.enablesettrace now available as an egg!
slug: products.enablesettrace-now-as-an-egg
date: 2010-04-02 21:19
tags: [development, plone, tools]
---

The summary: as of today, you no longer need to checkout
enablesettrace from the Zope subversion repository. You can just use
the Products.enablesettrace egg to debug your restricted Python code.

As a Plone developer you still sometimes have to deal with Script
(Python) objects and Python scripts in the skins folder. There are
even times you want to break into the debugger in one of those
scripts. Up until now, you needed to do a subversion checkout of the
Products.enablesettrace product from the
[Zope svn repo](http://svn.zope.org/repos/main/Products.enablesettrace/trunk/). Not
a problem as such, but it does feel a bit old-fashioned. Especially
given the fact that Plone is fully egg-based since version 3.2
(February 2009).

Another 'issue' I had with the original version was that it didn't
allow me to use [ipdb](http://pypi.python.org/pypi/ipdb). And since
I'm a fan of [IPython](http://ipython.scipy.org/), I prefer ipdb over
pdb any day.

My initial approach to the latter issue was to store a customized
version of enablesettrace in our company subversion repo. Which worked
out fine until we had a third party using our buildout (which used our
custom enablesettrace version). To make a long story short, I decided
to eggify the product and share it with the world by releasing it to
[PyPI](http://pypi.python.org/pypi/Products.enablesettrace).

By the way: I don't have write access to the Zope subversion
repository, so I though that was a good enough excuse to put the code
on [GitHub](http://github.com/markvl/Products.enablesettrace)
instead. But given the fact that the original code hasn't changed in 4
years, I suppose that this won't be a problem...

# Update (2010/05/30)

Today I reverted the Products.enablesettrace package to the original
code as it can be found in the Zope Subversion Repository. If you want
to be able to import ipdb use the old version, 0.2, or even better:
use the
[Products.Ienablesettrace](http://pypi.python.org/pypi/Products.Ienablesettrace)
package.
