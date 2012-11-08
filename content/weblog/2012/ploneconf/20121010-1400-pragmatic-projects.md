---
title: Pragmatic projects - getting things done with Plone (Andreas Jung)
slug: pragmatic-projects-getting-things-done-with-plone-andreas-jung
date: 2012-10-10 14:00
tags: [plone, ploneconf]
---

Andreas Jung talks about best practises.

There are always budget, human resources and time
constraints. Therefore it's almost impossible to find the "perfect"
solution. You have to do things withing a reasonable time-frame, stay
withing budget and can only use the human resources available.

You usually need to customise something in third party packages you
use. In old days this was easier with skin folders.

Maintainers of packages love bug reports, bug fixes and
contributions. If a project is on GitHub it's easy to contribute: fork
the code and issue a pull request. If the package in Subversion you
have to get permission to commit, create a branch and merge code
back. Either way: please contribute back and do not maintain a fork
yourself. (Unless it will not be useful for others. But in that case, keep
the fork for yourself.)

Monkey patching (dynamically modifying a class or module at run time)
is in general bad style. Monkey patching can have side-effects and can
cause problems when updating a package.

A simple example of a monkey patch to change the `bar` method of `Foo`:

    def my_bar(self):
        print 'Patched!'

    from foo import Foo
    Foo.bar = my_bar

If you have to monkey patch, have a look at
[collective.monkeypatcher](http://pypi.python.org/pypi/collective.monkeypatcher)
and
[collective.monkeypatcherpanel](http://pypi.python.org/pypi/collective.monkeypatcherpanel/1.0.3).

You might also be able to use the an `overrides.zcml` to override
configuration settings in your own package. There is also
[z3c.jbot](http://pypi.python.org/pypi/z3c.jbot/). This package allows
you to override resources of other packages inside your own (policy)
package. If you want to unregister something, use
[z3c.unconfigure](http://pypi.python.org/pypi/z3c.unconfigure/).

Reusing old content types can be made easier with
[archetypes.schemaextender](http://pypi.python.org/pypi/archetypes.schemaextender/).
With Dexterity there are "behaviours". You can use them to change the
behaviour of existing content types.

Andreas' project had a view which allowed the designer to generate
demo content by calling a URL. This way, the designer could
automatically create samples to style. This view installed a skeleton
site structure with example content for each content type, content
listings, et cetera. They used [lorempixel](http://lorempixel.com/) for images. You can also use
[collective.loremipsum](http://pypi.python.org/pypi/collective.loremipsum/).

Good hints:

   - *Never* perform customisations local in an existing third party
     package directly.
   - Customisations *always* belong in your own policy package.
   - Local customisations *will* be lost with the next version of the customised package.


[View the slides](http://www.slideshare.net/ajung/pragmatic-plone-projects-14668236)
or [watch the video](http://www.youtube.com/watch?v=I1b_j6j3jvc).
