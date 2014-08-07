---
title: RelStorage and PostgreSQL
slug: relstorage-and-postgresql
date: 2010-09-25 11:13
tags: [development, plone, postgres]
---

After a bit of experimentation I've succeeded in moving an existing
Plone 3.3.5 from the normal FileStorage storage (in other words a ZODB
in a Data.fs file) to RelStorage using PostgreSQL. This is a blog post
about what I needed to change in the buildout configuration and which
resources I used.

The first thing on the todo list was making sure there is a database
which can be used to store the data. Since the installation of
PostgreSQL is rather platform dependent, I won't describe it
here. Creating the database itself and a user are described clearly on
the
[Relstorage PyPI](http://pypi.python.org/pypi/RelStorage#postgresql)
page.

The part I found most interesting was the setup of the
buildout. Fortunately this is also nicely documented. Have a look at
[Shane Hathaway's weblog](http://shane.willowrise.com/) and
specifically the entries
[How to Install Plone with RelStorage](http://shane.willowrise.com/archives/how-to-install-plone-with-relstorage-and-mysql/)
and
[MySQL and RelStorage 1.3.0b1, Now With Blob Support](http://shane.willowrise.com/archives/relstorage-130b1-now-with-blob-support/). Another
source of information is the
[Plone on RelStorage presentation](http://www.slideshare.net/W9ZEB/pse2010-rel-storage)
by Lars R. Noldan.

This resulted in the following changes to the buildout:

    [buildout]
    find-links =
        ...
        http://packages.willowrise.org
    parts =
        ...
        zodbscripts

    [zope2]
    additional-fake-eggs =
        ...
        psycopg2

    [instance]
    zeo-client = false
    eggs =
        ...
        RelStorage
    rel-storage =
        type postgresql
        dbname zodb
        user zodbuser
        host localhost
        password zodbuser

    [zodbscripts]
    recipe = zc.recipe.egg
    eggs = ${instance:eggs}
    interpreter = zopepy
    extra-paths = ${instance:zope2-location}/lib/python
    scripts = zodbpack zodbconvert

    [versions]
    ...
    RelStorage = 1.4.0c4
    ZODB3 = 3.7.3-polling

You need additional configuration files to use the zodbconvert and
zodbpack scripts. It took me a while to get this setup properly since
initially I could not find examples on how to configure the connection
to the PostgreSQL database. The solution was hidden in the
[RelStorage presentation](http://www.slideshare.net/gsroma/relstorage-rogerio-ferreira-presentation)
by Rogerio Ferreira.

    <filestorage source>
      path /tmp/Data.fs
    </filestorage>
    <relstorage destination>
      <postgresql>
        dsn dbname='zodb' user='zodbuser' host='localhost' password='zodbuser'
      </postgresql>
    </relstorage>

And the zodbpack configuration file:

    <relstorage>
      pack-gc true
      pack-duty-cycle 0.9
      <postgresql>
        dsn dbname='zodb' user='zodbuser' host='localhost' password='zodbuser'
      </postgresql>
    </relstorage>

Once I found out how to connect to the database with these scripts I
noticed that a similar connection string was also used in the
rel-storage option in the
[RelStorage 1.3.0b1](http://shane.willowrise.com/archives/relstorage-130b1-now-with-blob-support/)
weblog entry.

This is basically all that I needed to start using RelStorage on the
Plone 3.3.5 site of the customer.
