---
title: Essential development tools (Kim Chee Leong)
slug: essential-development-tools-kim-chee-leong
date: 2012-10-11 15:00
tags: [development, plone, ploneconf]
---

Kim shows us a collection of tools that can be useful during
development.

When you want to get started with Plone development, you need to know
where to get help:

   - [collective-docs.readthedocs.org](http://collective-docs.readthedocs.org/)
   - Search via [DuckDuckGo](http://duckduckgo.com/),
     [Google](http://www.google.com),
     [Stack Overflow](http://stackoverflow.com/questions/tagged/plone)
     or the [Plone mailing lists](http://plone.org/support/lists)
   - IRC (`#plone` on Freenode)
   - [Plone books](http://plone.org/documentation/books)

To get started with a buildout, theme or product, use
[ZopeSkel](http://templer-manual.readthedocs.org/en/latest/applications/zopeskel.html)
or
[Templer](http://templer-manual.readthedocs.org/en/latest/index.html). Also
check out the local commands these provide.

To speed up buildout, you can:

   - Use version 1.6+
   - Use `allow-hosts` to limit where buildout is looking
   - Use timeout `-t 5`.
   - Use `-N` so buildout doesn't look for newer packages
   - Create a shared local buildout cache
   - Check out Ross Patterson's blog post about [buildout performance improvements](http://rpatterson.net/blog/buildout-performance-improvements).

Use mr.developer to check out the code of eggs in your buildout so you
can easily develop on them. (And to update them all at once when you
continue working on a later moment, use `bin/develop up`.)

The package [sauna.reload](http://pypi.python.org/pypi/sauna.reload/)
picks up changes in the files of your packages and restart Zope
automatically. But somehow Zope is restarted very quickly. For Plone 3
use [plone.reload](http://pypi.python.org/pypi/plone.reload/), which
requires manual action to reload Python code or ZCML.

With
[collective.recipe.omelette](http://pypi.python.org/pypi/collective.recipe.omelette/)
it is easier to look into the code of Plone and third party addons.

[plone.app.debugtoolbar](http://pypi.python.org/pypi/plone.app.debugtoolbar/)
shows debug information and it allows you to do stuff you normally
need to do from the ZMI.

[plone.app.themeing](http://pypi.python.org/pypi/plone.app.theming/)
allows you to install a zip file with the theme (works with Diazo).

If a site is unresponsive, you can use
[mr.freeze](http://pypi.python.org/pypi/mr.freeze/) to
investigate. You can use it print a stack trace for all threads so you
can see what's going on.  Kim used to use
[Products.signalstack](http://pypi.python.org/pypi/Products.signalstack/),
but mr.freeze can do more, like drop Zope to a `pdb` debug prompt.

Use [jarn.mkrelease](http://pypi.python.org/pypi/jarn.mkrelease/) or
[zest.releaser](http://pypi.python.org/pypi/zest.releaser/) to
release a package. It beats performing all the steps individually by
hand.

Continuous integration with [Travis CI](https://travis-ci.org/) for
open source GitHub projects or [Jenkins](http://jenkins-ci.org/) for
internal company projects. Travis *can* be used for closed source
projects but they don't advertise with it and it's quite expensive.

[plone.api](http://pypi.python.org/pypi/plone.api/) is still under
development but already very useful!

[products.pdbdebugmode](http://pypi.python.org/pypi/Products.PDBDebugMode/)
allows for post-mortem debugging, but it can conflict with
sauna.reload.

Finally: see
[collective.exampledevtools](https://github.com/collective/collective.exampledevtools)
for more details.

[View the slides](http://www.slideshare.net/kaceeleong/plone-conf-2012-essential-dev-tools)
or [watch the video](http://www.youtube.com/watch?v=JojegotBiF4).
