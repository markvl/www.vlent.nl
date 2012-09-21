---
title: Using Grok to walk like a duck (Brandon Craig Rhodes)
slug: using-grok-to-walk-like-a-duck-brandon-craig-rhodes
date: 2008-10-09 20:29
tags: [plone, ploneconf, ploneconf2008]
---

Adapters are the way to go to change behaviour of objects.

ATFolder has 471 methods which can be called. This is because Zope 2 +
Plone just build on top of each other to add functionality. Zope 3 uses
adapters to keep things more clean.

To change behaviour of object, there are a couple of options:
subtyping, mixin classes, monkey patching and adapters. The first
three all have problems. Adapters aren't perfect either, but
acceptable. The problem is that we need to explicitly call the adapter
ourselves. By using Zope's interfaces we can define an interface,
register it and then we can just request it. Zope will identify the
need and handle the adaption.

Grok, the framework represented by the friendly caveman with a large
club, makes Zope 3 simple to use.

Zope 3 is the best example of code using adapters. Also look at the
[Vice product](http://plone.org/products/vice) which uses adapters to
give every AT content type item RSS feed powers.

For details, take a look at the similar talk Brandon gave at the North
American Plone Symposium earlier this year:
[http://rhodesmill.org/brandon/static/2008/nola-zope3-talk.pdf](http://rhodesmill.org/brandon/static/2008/nola-zope3-talk.pdf). Presumably
Brandon will also make the PDF of this talk available on the web.
