---
title: Lightning talks
slug: lightning-talks
date: 2012-10-11 16:45
tags: [plone, ploneconf]
---

The lightning talks of the second day of the Plone Conference. This
time they were just three minutes due to the large number of talks.


# Balázs Ree

SlickGrid Touch: Making a complex Javascript table widget work on
mobile devices. Although you'll want your website to work on mobile,
older Javascript widgets don't work on touch
devices. [SlickGrid](http://github.com/mleibman/SlickGrid) doesn't
support touch devices.

What does touch support mean: select/unselect, follow link, select
row, show menu, scroll, reorder row, delete row.


# Maurizio Delmonte

Maurizio is a project manager. He needed a project management
tool. ScrumDo is a Django tool, but integration with Plone is hard.
They created a Dexterity based tool and also want to sprint on it on
Saturday. Have a look at the
[abstract.simplemanagement](https://github.com/abstract-open-solutions/abstract.simplemanagement)
repository.


# Armin Stroß-Radschinski

The Python Software Foundation created Python Brochure. 32 pages A4
full colour. Their aim: 10.000 distributions world wide. Diverse target
groups. Check out
[brochure.getpython.info](http://brochure.getpython.info/).


# Elizabeth Leddy

Sometimes you can easily fix your own system by watching your
logs. Plone logs you want to watch are located in `var/log`. The two
interesting logs are `event.log` and `instance-Z2.log`. You can also
find them using e.g. "`locate event.log`" on *nix based system.

On Linux systems also check out `/var/log`. Interesting files are
e.g. `faillog`, `messages` and `secure.log` or `auth.log`.

You can monitor a log file with `tail -f`.

Need help with your logs? Ask Elizabeth.


# Martijn Faasen

Martijn presented [Crom](https://github.com/faassen/crom). Basically
it is zope.component redone: the same API but less cruft. He gave lots
of code examples. Unfortunately it's backwards incompatible so we
cannot use it in Plone.


# Manabu Terada

Fuzzy search in Plone. In an intranet the could not use Google but
they did want to have similar suggestions. They did not want to use
Solr because they found it too hard to install and config.

Their solution uses the Levenshtein distance, is Python only and the
Japanese language is supported (using MeCab).


# Philip Bauer

They reimplemented [CorkboardMe](http://corkboard.me/) in Plone for
use on an intranet:
[collective.noticeboard](https://github.com/starzel/collective.noticeboard).
It is currently in a personal repository but it will be moved to the
collective mid November once it is finished.


# Lars van de Kerkhof

Lars created a post install hook for virtualenv:
[buildout bash completion](https://github.com/specialunderwear/buildout-bash-completion). With
it you can easily add the `bin` directory of your buildout to you
path. It also contains some commands that make working with a buildout
and virtualenv easier.


# Wolfgang Thomans

They had 460GB of data in an Oracle database. Everything was stored
three times and 90% of the data was not used. After they cleaned up,
'only' 130Gb was left. They dumped the binary data on file system and
exported the relational data to a new database with a sane
structure. They used
[transmogrifier](http://pypi.python.org/pypi/collective.transmogrifier/). For
the files (that were already on file system) they created stubs in the
ZODB and then moved the files to the right location in the blob
storage.


# Jamie Lentin

Jamie showed a product he is working on. It shows which Diazo theme
rules work and which not by colouring them green and red. The product
is not yet available.


# Tom Gross

How to make Plone fast? Avoid Plone and serve Javascript and CSS
directly from file system. See
[collective.assets](https://github.com/tomgross/collective.assets) and
the
[webassets](http://webassets.readthedocs.org/en/latest/index.html).


# Eric Brehault

Eric presented
[Resurrectio](https://github.com/ebrehault/resurrectio), a Chrome
extension. From the documentation: "Resurrectio is a Chrome extension
allowing to record a sequence of browser actions and to produce the
corresponding CasperJS script."


# Jonas Baumann

His company created a book publishing addon:
[ftw.book](https://github.com/4teamwork/ftw.book). It uses
[ftw.pdfgenerator](https://github.com/4teamwork/ftw.pdfgenerator)
(which is based on LaTeX) to generate PDFs out of content.

They used it for financial reports, court reports, end user product
documentation, ...


# Domen Kožar

There is an Ubuntu bug in the network manager since 2008. To prevent
issues to remain open for that long, he launched
[fundhub.org](https://fundhub.org/) today. It's a crowdfunding site to
fix free software one bug at a time. It currently only supports
bitcoins because paying is hard and bitcoins made it easier.

Multiple pledgers per issue are possible.
