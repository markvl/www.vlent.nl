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


# Eric ---
title: "Keynote: Going all out on the cloud (Jan Jongboom)"
slug: keynote-going-all-out-on-the-cloud-jan-jongboom
date: 2012-10-10 10:00
tags: [plone, ploneconf]
---

The first technical talk of the 10th Plone conference is by Jan Jongboom, who
works for [Cloud9](https://c9.io/).

In 1995 Livescript appeared and was shipped with Netscape
2.0. Although the name is similar to Java, Javascript is not like
Java, but more like
[Scheme](http://en.wikipedia.org/wiki/Scheme_(programming_language)). The
name was chosen to ride the wave of Java's popularity. Until 1999 it
wasn't too interesting. However, Microsoft needed XMLHttpRequest (that
basis of what we now call Ajax) and that sparked new development. In
2004 Google launched Gmail and used this technology to show mails in
your page without having to refresh the whole page.

Problems with Javascript is that the implementation differs between
browsers and browser versions. The best sold Javascript book is
[Javascript: The Good Parts](http://shop.oreilly.com/product/9780596517748.do).

The DOM was never meant to be scripted! And dealing with the DOM in
Javascript was a reason for Jan to dislike Javascript. But then
[jQuery](http://jquery.com/) appeared in 2006. The big power from
jQuery comes from [Sizzle](http://sizzlejs.com/) which allows nice
selectors. And this makes working with the DOM way better.

Then Javascript really started to pick up. With
[Node.js](http://nodejs.org/) you can even use Javascript on the
server. But the actual power comes from the underlying platform:
[LibUV](https://github.com/joyent/libuv), which abstracts away the
operating system calls.

Writing synchronous code is easy. *Asynchronous* code however... A
simple thread on a Linux system uses 2Mb. And every time someone does
a request, a thread is started. This can become a problem when there
are requests that take a long time. And if e.g. Apache is limited to a
certain amount of memory, you are limiting the number of possible
requests. With LibUV this is managed so you don't need the 2Mb per
thread. So if you have a web application that requires a lot of
concurrent connections, you are no longer limited by the memory usage
of the threads.

Node.js is basically a Javascript binding to LibUV, with standard
libraries in Javascript, using the Google V8 engine.

Why use Node.js over e.g. [Twisted](http://twistedmatrix.com/trac/)?
There was no module system in Javascript, so one could be
invented. And Javascript is already written asynchronous, in contrast
to most Python code. This made it easier to get started.

# Cloud9

Cloud9 wanted to bring the cool stuff from other languages to
Javascript. It's an on-line, open source, IDE. It used
[ACE](http://ace.ajax.org/) for their editor. It's completely written
in HTML, CSS and Javascript and has many features. Currently it's only
supported by Node.js. However, you should be able to run it with
Python in a couple of months.

With Cloud9 you get a free Linux
[OpenShift](https://openshift.redhat.com/app/) VM. Including a real
terminal. But the coolest feature is collaboration. Someone else can
come into your IDE and see the same things you see. He/she can see
your cursor and see you type. (Also: If you close a file, the files is
also closed in the IDE of the other person.) So you can easily debug
and work together on something. You also don't even have to leave your
browser to deploy your code.

Plone doesn't run on the OpenShift VM yet because of a LibXML
problem. But you can also bring your own server. So Jan used an Amazon
EC2 instance for his VM. The Plone Unified installer ran fine
there. He can just open and edit the files (e.g. the buildout
configuration files) from his browser.

Cloud9 is very proud of their code completion. It should become
available for Python as well in the next few months.

Since Cloud9 in open source, you can fork the
[GitHub repository](https://github.com/ajaxorg/cloud9) and contribute
if you want to. Or join Cloud9 since they are hiring.
Brehault

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


# Domen Koẑar

There is an Ubuntu bug in the network manager since 2008. To prevent
issues to remain open for that long, he launched
[fundhub.org](https://fundhub.org/) today. It's a crowdfunding site to
fix free software one bug at a time. It currently only supports
bitcoins because paying is hard and bitcoins made it easier.

Multiple pledgers per issue are possible.
