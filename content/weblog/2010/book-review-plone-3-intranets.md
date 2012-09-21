---
title: "Book review: Plone 3 Intranets"
slug: book-review-plone-3-intranets
date: 2010-09-13 08:31
tags: [plone, webmaster]
---

One of the latest Plone books from Packt Publishing is
[Plone 3 Intranets](http://www.packtpub.com/plone-3-design-build-deploy-full-featured-secure-enterprise-intranet/book?utm_source=vlent.nl&utm_medium=bookrev&utm_content=blog&utm_campaign=mdb_004175)
(Design, build, and deploy a reliable, full-featured, and secure
Plone-based enterprise intranet easily from scratch) by Víctor
Fernández de Alba. Packt sent me a copy and asked me to review it.

My first observation: since I've been developing Plone sites for a
couple of years now, I'm not really part of the targeted audience. The
book is meant for people without Plone experience and the reader
doesn't need any programming or CMS knowledge.

As a result the book starts with an introduction to Plone (and Python)
and guides the reader through the installation of an instance. While
the unified installer is demonstrated, the book also shows
[buildout](http://pypi.python.org/pypi/zc.buildout). The latter may
seem unnecessary for the target audience, but later chapters also use
buildout, for instance to install add-on products.

Chapters three through eight are devoted to core concepts of Plone:
managing content, configuration, users, groups, workflow, security,
and so on. These chapters give the reader a good overview of what
Plone has to offer for intranets. The author also suggests a number of
third party products to add even more functionality (see the
[table of contents](https://www.packtpub.com/toc/plone-3-intranets-table-contents?utm_source=vlent.nl&utm_medium=bookrev&utm_content=blog&utm_campaign=mdb_004175)
for details).

Chapter ten is where the book surprised me a bit. Suddenly the author
starts developing a product himself. This wasn't exactly what I had
suspected given the target audience. Chapter eleven switches back to
using the available functionality (like content rules, WebDAV and
external editing). Yet in chapter twelve there's more code: subjects
like TAL, METAL, viewlets, acquisition and resource registries are
briefly explained.

The last chapter is devoted to deploying the intranet. It demonstrates
Apache configurations, but also discusses the usage of a ZEO
server/client setup, load balancing and caching.

# Verdict

It's hard for me to put myself in the shoes of someone unknown with
programming, Plone or even a CMS, so I might underestimate the target
audience of this book. However, I feel that the chapters about
creating a custom product and theme (chapters ten and twelve) might
not be suitable for them and leave them with a lot of questions. On
the other hand, the author has experience training non-technical
end-users and so let's give him the benefit of the doubt.

By the way, don't let the fact that the book is based on Plone 3 scare
you: the author frequently points out where it differs from
[Plone 4](http://plone.org/products/plone/releases/4.0), which has
recently been released.

Overall
[Plone 3 Intranets](http://www.packtpub.com/plone-3-design-build-deploy-full-featured-secure-enterprise-intranet/book?utm_source=vlent.nl&utm_medium=bookrev&utm_content=blog&utm_campaign=mdb_004175)
is a good introduction and a really nice overview of the broad
functionality Plone has to offer. After reading the book you should
probably be able to get a nice intranet up and running with the
practical tips and examples in the book.
