---
title: Performance for product developers (Matthew Wilkes)
slug: performance-for-product-developers-matthew-wilkes
date: 2012-10-12 09:00
tags: [plone, ploneconf]
---

What can product developers do to make their products faster to use
and easier to cache.

Plone is currently pretty fast, especially for low edit sites. It runs
fine on a 256Mb VM. Things that help us: Varnish,
[plone.app.caching](http://pypi.python.org/pypi/plone.app.caching/). It's
easy to setup. Portal implementations are different because there are
a lot of authenticated users there.

But that's for integrators and users. What about product developers?

We've got a blind spot for performance and security. We don't
deliberately write 'bad' code. We do think about our data structures
(some even over do it).

A recap on tips from an earlier presentation Matthew gave:

   - The catalog is already really big. Don't add things to the
     catalog if you can help it, this especially goes for indexes.
   - If you have to, please use an adapter based indexer not a raw
     FieldIndex.
   - Use Dexterity, not Archetypes if you build custom content
     types. You'll be sorry in a couple of years otherwise.
   - Not sure about what structure to use for your data? Use OOBTree.
   - Avoid big objects churn by storing `Lengths` of things you need
     instead of iterating over all items just to find out how many
     items there are.
   - Find a balance between huge objects and annotation soup. Too many
     annotations are not good.
   - `For` loops inside `for` loops are a recipe for slow code.
   - Don't forget `sets` and `itertools`. They are good.

Very few people use already available tools. For instance: a show of
hands proved that `cache:ruleset` ZCML declaration are not used
much. If you *do* use this, you can get an enormous performance
boost. You can go from 79 milliseconds for a request without
`cache:ruleset` to zero milliseconds with the ruleset. You can
directly assign a ruleset to an interface. Integrators can help here
by adding these rulesets to products you use.

Edge side includes (ESIs) are generally used to do package
composition. But it's easy to leak data so be careful. An ESI is a way
to say you want to include a certain URL on a certain location. That
way you can cache the rest of the page and include e.g. the user name
dynamically. Again, make sure you don't cache secret stuff for
everyone. Don't trust on ETags since they can be faked. You will have
to have a custom VCL and code. ESIs can give your site a good boost,
but it's also hard work. It's a lot easier if addons are written with
ESI in mind. So plan your templates for ESIs:

- Create many small templates that can be easily customised.
   - Split out user and role based stuff in separate templates.

Integrators should not need more than a couple of minutes to add
ESI to your templates.

As said, it's easy to make a mistake regarding testing. So you really
need to test the caching. This goes for integrators, but *also* for
product developers. Far too few people run automated tests on their
caching. If you already have `plone.app.testing` based tests, it is
easy to do: create a new layer using a ZServer, start up Varnish and
make some testbrowser calls.

We need helper classes and methods for writing cache tests and actual
tests in popular packages. That way they can serve as an example.

The current `plone.app.caching` rulesets are targeted at
integrators. Product developers need a series of rules which we agree
to use so configuration would be easier.

Want to help put this into practice? Mail to `sales` at
`thedistillery.eu`.
