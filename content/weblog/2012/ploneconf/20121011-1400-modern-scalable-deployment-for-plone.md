---
title: Modern scalable deployment for Plone (Christian Theune)
slug: modern-scalable-deployment-for-plone-christian-theune
date: 2012-10-11 14:00
tags: [plone, ploneconf]
---

Steve McMahon
[talked](http://localhost:8000/weblog/2012/10/11/plone-production-deployment-secrets-tricks-steve-mcmahon/)
about Plone specific stuff, Christian is going to talk about the stuff
around that.

A few years ago Gocept already did hosting, but it was neither ideal
for the customers nor for Gocept itself. They changed that and this
talk looks back on that.

Infrastructure basically marries software with entropy. The developer
environment is clean and you can always start fresh. Operations can
only start clean exactly once. Infrastructure make handling the
entropy bearable. For Gocept, infrastructure is building a platform
that the application developer can count on.

The first thing to have is having a data centre. At Gocept they just
buy that; they do not want to manage the building, air conditioning,
etc. They take a data centre for granted and plug in their
hardware. The are four types of hardware: routers, storage servers,
vitalisation servers and backup servers.

Everything is run in a virtualised environment (which is really
affordable). The OS is also maintained by Gocept. There are only a few
components an application developer or customer can change. They
rather run five smaller Zope servers than a single bigger one. They
try to make all the pieces as small as possible.

Automation is handled via [Puppet](http://puppetlabs.com/). They want
the automation to be convergent and idempotent: regardless of the
initial state it should converge to a certain state, no matter how
much the scripts run. The scripts should also be versioned and have
everything as code so there is not much manual work necessary. Puppet
is triggered by cron but they are thinking about moving it to some
sort of message queue so machines can figure out if they are affected
by the change and can act on it.

Management was binary: either *I* manage something or *you*. But
there are also tools where you can allow someone to add a
snippet. Backups and other day-to-day operations also fall under
management. It's not something a application developer should need
to worry about.

For monitoring they use [Nagios](http://www.nagios.org/). It's good
enough.

You need a helpdesk for support. One reason is that you want
shield your developers from getting interrupted continuously.

There's still a lot left for developers to do on the application
level. For instance deployment. It has to be quick, repeatable,
platform-independent and a single click. They currently use
[Batou](http://pypi.python.org/pypi/batou/) which is inspired by
[Fabric](http://fabfile.org/).

Good components are e.g. Nginx, Varnish, HAProxy, PostgreSQL,
Memcached, Supervisor and Postfix. Bad components: Apache (because although
configtest says the config is okay, Apache might still crash), MySQL (BDB)
and OpenLDAP.

They use a "production-ready" checklist. It contains items like log
rotation, database maintenance, system startup/shutdown and monitoring
(processes and ports).

One config file per environment (ini style) and they AES encrypt
it. This way they can check in secret stuff into source control. Using
PGP would be better because then they can encrypt is for certain
developers.

The staging environment should be identical to production. And the
configuration of your development environment should be structurally
identical (but you can e.g. leave out Nginx, etc).

Tips for web applications: share nothing in your app (e.g. require a
single server, or share something on file system), have many small
processes, do not listen on a port if you are not ready (the opposite of what Zope does) and
never store runtime configuration in the database. Avoid synchronous
external request and accidental write requests. However, do use
feature switches. This mean you can, at runtime, turn of a feature
that is misbehaving or to handle heavy load.

Use [Supervisor](http://supervisord.org/) and
[Superlance](http://pypi.python.org/pypi/superlance) (httpok and
memmon) to kill of processes. Use the 3.0 release candidate of
Supervisor, it's stable.

Use virtualenv and buildout combined. Use buildout to configure python
environment. Don't compile stuff with it. Use small configuration
files and extend them. Don't allow it to pick versions. Use "`-t 3`"
to timeout. Use buildout => 1.6 for performance enhancement. Do not
use mr.developer in production. Use "`allowed-hosts=`" to limit the
places where buildout tries to fetch packages. Using several small
buildout configuration. Use
[pypi-mirrors.org](http://www.pypi-mirrors.org/).

Use as much ram as you can afford to prevent read requests. Plan for
less than 40% disk usage so you can put the backup database next to
the (still running) production database you are going to replace.

Load balancer: use "leastconn" to balance. HAProxy has live statistics
UI.

Nagios: model the dependencies so a broken router doesn't trigger many, many mails.
Use [`check_webpage.rb`](https://github.com/Toubib/check-webpage).

SLAs set expectations. How much availability do you need? That depends
on how much you can afford. Don't think in "nines": 99% means 72 hours
down/year. Does that mean you can just take down a server for three
days straight and still perform according to the SLA? 99.99% is just
54 minutes per year, this is really not much time!

Instead talk about how many hours downtime
per day/month are acceptable. How much does that downtime cost for the
customer? By having this cost clear, it's also clear what it's
worth.

Align technical and organisational measures (when will someone be able
to handle a problem). Failover is just a temporary measure to bridge
until someone can solve the problem.

# Resources

You can read the book "The practice of system and network
administration" (Limoncelli et.al.). Gocept also has
[documentation](http://gocept.net/doc/) you can check out.
