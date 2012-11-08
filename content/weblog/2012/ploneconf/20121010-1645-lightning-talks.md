---
title: Lightning talks (Wednesday)
slug: lightning-talks
date: 2012-10-10 16:45
tags: [plone, ploneconf]
---

Several five minute talks about various subjects.


# Érico Andrei on behalf of Plone.Gov.Br

Érico is selling Brasília as the location for the Plone conference in
October 2013.


# PloneEdu

Universities are special kind users of Plone: large setups, large number of
sites. However a limited number of people are working on it. To
discuss best practises, meetups are organised, e.g. in Germany.

If you are working in a university, please come to the open space
session and join our effort.


# Dylan Jay

[Victorian SES](http://www.ses.vic.gov.au/) wanted a secure,
multi-site CMS that they could theme themselves and have 99.99%
uptime. They used Diazo to theme the site themselves, and they are not
Plone people.

They are using CDN, Nginx, Varnish, Haproxy, Zope/Plone and MySQL
(RelStorage).

During an earthquake *everyone* feeling the quake potentially will go
to the site. That are a lot of people suddenly hitting your site. So
there is no time to spin up additional servers. Therfore, they cache
every page for one minute to handle the load.

They tried to use Funkload and jmeter to generate enough traffic to
test the site but eventually ended up using the hosting provider to do
so. Otherwise they could not get to the level they needed to properly
test the site.

Two months after they went live, an earthquake hit the area. And the
site could handle it---in contrast to their competitors.


# Godefroid Chapelle

A talk about
[collective.jekyll](https://github.com/gotcha/collective.jekyll). This
product adds diagnostic data when viewing a page. There's also an
overview to show the states of multiple (all?) objects.


# Davide Moro

Davide presented [Ploomcake](http://www.ploomcake.org). It is a Plone
distribution that provides an easy way to quickly evaluate Plone. It
contains, amongst other things: a responsive theme, LinguaPlone if
needed and captcha support.


# Domen Kožar

Chris McDonough wrote
[Substance D](http://substanced.repoze.org/). Domen worked on it
during the last Google Summer of Code. It's basically Zope 2 in
Pyramid. Not released yet, so use at your own risk. However, it is
already in use on a couple of production sites.


# Patrick Gerken

A talk about [Sentry](https://www.getsentry.com). It's very easy to
get Sentry up and running. It will show you the errors that occurred
and how many times. It will only send an email once per problem. For
each error, details like which site, the used browser, etc. are
shown. You can also see a lot about the environment at the time the
error happened. And even get information about the user that
experienced the error.

There is documentation on how to get Sentry
[configured in Zope/Plone](http://raven.readthedocs.org/en/latest/config/zope.html).

You can get a hosted version, there is even a (limited) free plan. But
you have to make sure that you are not sending secret stuff to another
server (like passwords).


# Maurits van Rees

Maurits presented a couple of useful packages. See his
[presentation on GitHub](https://github.com/mauritsvanrees/talks/blob/master/fivepackages.rst)
for the details.
