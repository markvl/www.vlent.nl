---
title: "Plone Production Deployment: Secrets & Tricks (Steve McMahon)"
slug: plone-production-deployment-secrets-tricks-steve-mcmahon
date: 2012-10-11 11:45
tags: [plone, ploneconf]
---

A special version of this talk: no secrets or tricks. It discusses the
things that are in mainstream use.

The target audience is a (Linux, BSD, OS X) sysadmin or friend of
sysadmin. Steve is a sysadmin and person who talks to sysadmins. There
won't be very advanced stuff or code in this talk.


# Simple deployment

The simple deployment: Zope/Plone running on port 80 directly
connected to the internet. It's really easy for development, but lacks
versatility, SSL and this setup does not work well with other web
applications. So we add a web server and use it as a reverse proxy. A
web server can:

   - Handle SSL.
   - Efficiently queue request.
   - Handle URL rewrites.
   - Battle-hardened logging and request sanitizing.
   - Plays well with others (e.g. a Django/PHP application).

Don't optimize to early. First measure and find the bottlenecks in
your system. Measure before *and after* to see if the optimisation was
successful and doesn't just make your setup more complex than needed.


# Load Blancing

Load balance by having several ZEO clients connecting to a single ZEO
server. The rendering process (taking the parts of the page and
turning them into HTML) takes most processor time. The load the
database related stuff generates (in the ZEO server) is mainly
IO. With ZEO clients you can use the multiple cores on a single CPU,
or even put the ZEO clients on several machines.

Steve advises to have a ZEO setup installed anyway even if you don't
need to load balance. That way you can fire up another client to do
some debugging on the production environment. You don't really *want*
to do this, but sometimes you *need* to do so. Then it's better to be
prepared and have that ZEO client ready to go.

To use the ZEO clients, you need an actual load balancer that sends
the incoming requests to the different ZEO clients. Note that the
balancing scheme
matters. [Round robin](http://en.wikipedia.org/wiki/Round-robin_scheduling)
is the simplest. Binding requests from a certain source to a certain
ZEO client (a sticky session) can be useful.


# Proxy caching

You can place a reverse proxy cache between the web server and the
load balancer (this is the most typical setup anyway). That way you
don't have to have Zope render a page, CSS or spit out a file over and
over again---the cache can just serve the requested resource which is
always faster.

Caching is hard though and there are tradeoffs. Cached content may not be
as current as you'd want. However, currency may not matter as much as
actually being able to stay up when your site suddenly becomes
popular.

Plone is---in theory---smart enough to send a message to e.g. Varnish
to tell it that a resource is out of date (cache invalidation). But
pages are a composition of different pieces of content (e.g. via
portlets). So it's very hard to determine what resources need to be
invalidated when some object gets changed. Steve suggests to start
conservative and turn it up when possible. He also distinguishes
between authenticated and unauthenticated users. Authenticated users
need current information while unauthenticated users can probably get
by with a bit older pages. As
[Dylan Jay said yesterday](/weblog/2012/10/10/lightning-talks/#dylan-jay):
caching pages for one minute can make a huge difference.


# Tools

Web server: Nginx makes better use of your server's memory than
Apache. (Although it may not be te best for you if you e.g. need to
mix with other web applications.)

Proxy cache: Varnish is currently the best choice.

Load balancer: Steve finds HAProxy the easiest to configure and has
good results with it. However older versions have problems with SSL
(IP forwarding doesn't work, but Steve says that they can also be
worked around). There is an addon for HAProxy to add and remove
clients from the command line. This can be useful because HAProxy can
be fooled by Zope startup.

Note that you could collapse these three into the web server: Apache
and Nginx can behave as load balancers and proxy caches. They do not
do as good a job as the specialised tools, but it is less complex
because it's just one tool instead of 3.


# Backup

Steve: "If you haven't tested your backup scheme, you don't have a
backup!" So how do you backup? Create a backup and rsync it to a
separate system. Use
[collective.recipe.backup](http://pypi.python.org/pypi/collective.recipe.backup/)
for the backup.


# Log files

Log rotation is very important. Otherwise your server could die
because they fill up your hard drive. The
[zope2instance recipe](http://pypi.python.org/pypi/plone.recipe.zope2instance/4.2.5#logging)
can rotate the logs automatically. You can also use the traditional
way by using the `logrotate` package of your operation system. If you
use logrotate, don't forget to send a signal (`kill -USR2`) to Zope
after the rotate so it starts using new logs.

While on the topic: read your event logs regularly! There will be
'known issues', but something new might also pop up.


# Database packing

If you use a ZEO setup, use `bin/zeopack` (available via
[plone.recipe.zeoserver](http://pypi.python.org/pypi/plone.recipe.zeoserver/)). Additional
hint: if you cannot pack your database, something is wrong with it.


# Advice

Steve uses system packages as much as possible. Distributions are so
good nowadays you can use a lot from your OS. This way you can just
use the package management system of your OS to keep up to date with
security fixes.

Never use buildout as root. Use separate accounts! Otherwise if there
is hostile code in a `setup.py` it will be run by buildout---as
root---and then you have a big problem.


# Tips from the audience

An extension for Apache and Nginx (xsendfile?) can help you server
large files directly from file system so you can bypass Plone.

Fewer components are not necessarilty better. Three simple tools might
be better than one complex one.

Using mailinglog(?) or Senty can help you detect uncaught exceptions.


# Resources

How to learn this all? Have a look at the
[hosting documentation](http://collective-docs.readthedocs.org/en/latest/hosting/).

If there's anything that has not been documented, please add it to the
hosting documentation. And also put a pointer to those details in the
[deployment documentation](http://collective-docs.readthedocs.org/en/latest/deployment/).
