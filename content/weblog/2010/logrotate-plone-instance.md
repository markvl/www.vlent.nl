---
title: Logrotate Plone instance
slug: logrotate-plone-instance
date: 2010-09-08 21:02
tags: [devops, plone]
---

While reading
[Plone 3 Intranets](http://www.packtpub.com/plone-3-design-build-deploy-full-featured-secure-enterprise-intranet/book?utm_source=vlent.nl&utm_medium=bookrev&utm_content=blog&utm_campaign=mdb_004175)
by Víctor Fernández de Alba, I discovered the "logreopen" command.

This means that this snippet in the logrotate configuration file:

    ${buildout:directory}/var/log/instance.log {
        postrotate
            /bin/kill -USR2 $(cat ${buildout:directory}/var/instance.pid)
        endscript
    }

Can be replaced by this:

    ${buildout:directory}/var/log/instance.log {
        postrotate
            ${buildout:directory}/bin/instance logreopen
        endscript
    }

I don't know how well-known this command is, but at least for me it
was a new one.

(I will write a review of the book soon, but I already wanted to share
this with you. For those of you that cannot wait, check out the
[sample chapter](https://www.packtpub.com/sites/default/files/9089-chapter-8-using-content-type-effectively.pdf)
from the Packt Publishing website.)
