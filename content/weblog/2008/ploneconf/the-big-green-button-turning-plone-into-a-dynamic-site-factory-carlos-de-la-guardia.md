---
title: "The Big Green Button: Turning Plone into a dynamic site factory (Carlos de la Guardia)"
slug: the-big-green-button-turning-plone-into-a-dynamic-site-factory-carlos-de-la-guardia
date: 2008-10-09 19:52
tags: [plone, ploneconf, ploneconf2008]
---

Plone is a great CMS but is it the best product to actually deliver
the content?

Carlos dreams of "the big green button": export a Plone site as a
static HTML site with the push of a single button. Plone is a great
CMS, but is not necessarily the best way to deliver the content to the
users. One of the problems of Plone is that it isn't very
fast. Performance cannot originate from caching alone. Logged in users
also need to have quick resonse.

By using Content Mirror, you can have your content automatically
stored in a database layer. This allows you to get to your data
without having to use Plone, while all the data is still maintained by
Plone.

Now the content is out, we need to present it. This is where WSGI
comes in. This allows us to use different pieces of python software
and connect them. The python community sees Zope/Plone a bit as
'unpythonic'. By using Repoze we can make stuff that can also be used
by the Python community through WSGI, without having to use Zope. This
should bring us a bit closer to the Python community. The repoze.bfg
framework can use the ZODB, page templates, while still being a simple
framework.

Deliverance is a WSGI 'fake frontend' to make the technology in the
back look nice. Not just Zope/Plone output, but any HTML. This way one
doesn't have to have any knowlegde about the technology (page
templates, skins, etc.) to create a look-and-feel of a site. You just
have to worry about the front end.

As Carlos demonstrated: using repoze.bfg and deliverance as a front
end for the Plone site is fast!
