---
title: Ways to investigate for the future of Plone (Encolpe Degoute)
slug: ways-to-investigate-for-future-of-plone-encolpe-degoute
date: 2012-10-10 15:00
tags: [plone, ploneconf]
---

How can we improve Plone?


What *is* Plone? The simple answer: Plone is a stack upon Zope on CMF.

The more complex answer: Plone is build with Python and C with Twisted
for Zope and the ZODB. It's using some frameworks: CMF, Archetypes,
Dexterity, jQuery, KSS, ... It's a CMS but it can be seen as a
framework to build a web application on.

There are several layers we can improve on.

# Python

What's the next Python to use? There are CPython 2.7, CPython 3.3,
PyPy and Stackless Python. Encolpe thinks Python 3 would be a good
move. We need to invest more in Python development.

# Network layer

Regarding the network layer (Twisted). Some tests show that Twisted is
more or less the worst framework in place for the job. If we want to
replace it, we need to choose between synchronous or
asynchronous. Options: Gunicorn, Gevent, Tornado. However: it will
take a lot of work and it will have to be added to a next version
Zope.

# Storage

The ZODB is storing objects in Python pickle format. We can use a file
as storage (FileStorage) or some databases (RelStorage). All
transactions are stored until a ZODB pack.

Problem with the pickle format: it's too Python centric and needs a C
binding (cPickle) to get good performance. To replace pickle we can
use e.g. JSON or XML. Problems with JSON: no schema validation and the
binary format is not normalised. XML was created as an exchange
format, but it's now also used to store data. The problem with XML is
the opposite of JSON: **everything** needs to be specified in a
schema.

Ideas to improve the ZODB: use stratified B-Trees, use relational
databases for the catalog to improve indexes and have a sub process
that cleans up old transactions automatically.

Replace the ZODB completely with e.g. Cassandra or MongoDB?

*[... Here I missed a bit because I got distracted by some work related issues ...]*

When should we switch to Bluebream (Zope 3) and ZTK? We are still not
ready at the moment. Should we keep CMF or push it in the ZTK?
Everyone agreed that that would be useful, but no-one wanted to do the
work.

Which visual editor should we use? TinyMCE, CKeditor, Aloah, VIE and
Create.js? The problem lies in the Plone integration. For instance,
TinyMCE is not up to date with the latest versions of the original
product.

Ideas for Plone:

   - We need to start using Dexterity and migrate all products for
     Plone 4.3.
   - Plone should be able to automatically create e.g. Open Documents,
     PDFs, ..., from the existing content.
   - How can we include microformats and schema.org in a Plone site?
   - There is no Python library to connect with RESTful services.
