---
title: How to have a real site factory with buildout (Encolpe Degoute)
slug: how-to-have-real-site-factory-with-buildout-encolpe-degoute
date: 2012-10-11 09:45
tags: [plone, ploneconf]
---

How to deploy tens of sites that are not really identical but share the
same infrastructure.

You can use [zc.buildout](http://www.buildout.org/) to have repeatable
installations. With [Zopeskel](http://pypi.python.org/pypi/ZopeSkel/)
you can get a buildout configuration really easy, however. But this is
for your team and not ready for production (hosting, load balancing,
etc). You also want to be able to test everything with
[Jenkins](http://jenkins-ci.org/).

To make it even easier to deploy more sites for e.g. large
organisations they needed something more. Goals:

  - To be able to switch applications in the same stack level.
    - Nginx/Apache
    - Squid/Varnish
    - Pound/HAProxy
  - May have profiles.
  - Manage known good sets for addons.

This became [zopeskel.unis](http://pypi.python.org/pypi/zopeskel.unis). Important building blocks that are used:

   - `extends`
   - `+=` (Do not mix "`+=`" and "`=`" because the latter one clears previous stuff)
   - `<=` (it will copy the content *before* the interpretation)
   - `${:_buildout_section_name_}` (gives you the name of the current section)

The `buildout.cfg` file is almost empty, it just extends a profile. Some folders
to manage configuration (e.g. `profiles/etc`, `profiles/modules`). There
are four working profiles: development, standalone, preproduction,
production. They are working on a profile for Jenkins.

In `profiles/etc`:

  - `defines.cfg`: password for supervisor, IP addresses, ports, etc.
  - `base.cfg`: main buildout config shared by all profiles.
  - `project.cfg`: all eggs specific for a project that you don't want
    to add to an external profile.
  - `versions.cfg`: the versions pins (and downloads) buildout should use.

In `profiles/modules` are configurations for e.g. LDAP, GetPaid,
theming (Diazo), ploneIDE. Make your modules as small as possible:
just the eggs that need to be added to `[project-settings]` and
version pins. (You can for instance use
[good-py.appspot.com](http://good-py.appspot.com/) to get the right
versions for a product.)

You can use zopeskel.unis as an example for your own setup.

[View the slides](http://encolpe.degoute.free.fr/conferences/PloneConf%202012%20-%20Building%20a%20site%20factory%20with%20Plone)
or [watch the video](http://www.youtube.com/watch?v=EFEf6QvV7Bo).
