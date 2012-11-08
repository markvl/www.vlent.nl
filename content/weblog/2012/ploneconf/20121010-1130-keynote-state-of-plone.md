---
title: "Keynote: The State of Plone (Matt Hamilton and Eric Steele)"
slug: keynote-state-of-plone-matt-hamilton-eric-steele
date: 2012-10-10 11:30
tags: [plone, ploneconf]
---

Matt Hamilton, president of the Plone Foundation Board and Eric Steele,
release manager, talk about the state of Plone.

# The last 12 months

The last year, five Plone conferences took place up until the current
conference. There were 500--600 attendees on the four conferences,
the Plone conference 2011 not included.

Plone 4.2 has been released and Plone 4.3 is in alpha state
currently. Most work is done during sprints. Eric counted 12 sprints
over the last year. Development is happening on a very fast pace now!
In the last year 5597 commits were done by 208 contributors. Last
month 66 contributors committed and 13 of them were new contributors.

Matt is also very happy with how many countries participated in World
Plone Day. The map however does show a big gap in Africa and Asia. We
should try to give the local communities there more energy.

Recently the 60th Plone Tuneup was held. This time 31 developers
attended and 34 out of 70 tickets were closed. A great success.

The [Plone Roadmap](http://plone.org/roadmap/) is an
important---living---document that is updated every six months. Its
goals: iteration, more frequent releases, introducing new
technologies early (before they become standard).

This year Plone Core migrated to GitHub. This makes the life of Eric a
lot easier since merges in Subversion were a nightmare. It also lowers
the barrier to contribute. Much of the Collective repository has also
moved to GitHub.

Although the experienced developers probably do not see the
installers, they are the first thing someone new to Plone sees. Last
year a new Windows installer was created. This one is much more native
for Windows users. And it uses the same base buildout as other
installers. This makes switching platforms a lot easier. Other
approaches are also investigated: [Bitnami](http://bitnami.org/),
[Turnkey](http://www.turnkeylinux.org/), [Ploud](https://ploud.com/).


In the area of quality assurance: a lot of tickets in Trac have been
cleared, bug reporting has been simplified and tickets are
triaged. Jenkins, Travis-CI and Robot Framework are used to perform
automated testing.


# The next decade

The Plone Foundation Board deals with the intellectual property and
trademark issues. The Roadmark team 'determines' the direction of
Plone and gathers input from the community to do so. The Framework
team deals with the code itself and sets the direction what goes in
each release and what doesn't.

Three areas of focus: approachability, integration,
involvement. Documentation is the biggest sore point. There is a lot
already, but it is not always actively maintained and not all new
features/code has documentation. Writing/translating documentation is
a great way to get started if you want to become involved in the
community.

The UI team is going to review some of the core features. Content rules
for example are awesome but are not used enough because they are
complex. Collections are another example: they have been completely
redone so it's easier to use them.

To make the development for Plone easier, plone.api has been
created. It should have been done way earlier! By realising that we
didn't need an API for *everything* this became possible. Note: they
wrote the documentation for it **first**.

In the past we talked about the three D's: Diazo (new theming),
Dexterity (new content types) and Deco/Tiles (new layout
system). These things allow us to be a bit more Pythonic. You could
e.g. use Diazo combined with Pyramid.  Diazo is already there since
Plone 4.2 (known as plone.app.theming), Dexterixy is in Plone 4.3,
Deco/Tiles will be in Plone 4.4 or 5.

Over the years it became harder to theme a Plone site. But the new
theme editor for Diazo, created by Martin Aspeli, really lowers the
barriers to give a Plone site a new look. But it's not only an easy way to get
started, the result can also be used by a more experienced person to
pick up where the 'novice' left off.

To make contributing easier, the contributor agreement process is
being revised. New contributors will get a welcome email with an
introduction on why, how and where we do things. Mentorship is also on
the radar to help the new developers.


# Call to action

The biggest problem for Plone, according to Eric, is organisational:
we are not taking enough opportunity of the capabilities available in
the community.

Eric asks us to think about three things wrong with the code,
community, or process of Plone. Please find someone with matching
'things' and act upon it! What are **you** going to do to
make Plone better this year?

[View the slides](http://www.slideshare.net/esteele/the-state-of-plone-plone-conference-2012).
