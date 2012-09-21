---
title: "Content Migration: Quantum Leap (Vitaliy Podoba)"
slug: content-migration-quantum-leap-vitaliy-podoba
date: 2008-10-10 21:25
tags: [plone, ploneconf, ploneconf2008]
---

The migration of www.contentmanagementsoftware.info in an nutshell.

Plone portal migration is available and
[documented](http://plone.org/documentation/manual/upgrade-guide), but
there are rough egdes. Especially with content. The problems:

-   It can fail (especially when coming from Plone 2.0 and 2.1).
-   You can lose control.
-   It is an iterative (step-by-step) process.
-   There is no way back.

The more customisation, the more time is necessary to migrate the
site.

The use case discussed by Vitaliy is the migration of
[www.contentmanagementsoftware.info](http://www.contentmanagementsoftware.info/)
(CMS.Info for short) from Plone 2.0.5 to 3.1. The quantum leap from
the title refers the skipping of Plone 2.5 in the migation.

Functionality wasn't a target in the migration, it was just about
content to a clean database. The content can be transfered back and
forth, even between different Plone versions. Portal types are
transformed on the fly. However, the import/export isn't perfect.

Vitaliy looked at:

-   [collective.plone.gsxml](http://pypi.python.org/pypi/collective.plone.gsxml)
-   [collective.transmogrifier](http://svn.plone.org/svn/collective/collective.transmogrifier/) and [plone.app.transmogrifier](http://svn.plone.org/svn/collective/plone.app.transmogrifier)

Since they did not provide everything needed, additional products were
created:

-   [quintagroup.transmogrifier](http://svn.quintagroup.com/products/quintagroup.transmogrifier/)
-   quintagroup.transmogrifier.simpleblog2quills
-   quintagroup.transmogrifier.pfm2pfg
