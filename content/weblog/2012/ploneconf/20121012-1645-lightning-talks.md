---
title: Lightning talks (Friday)
slug: lightning-talks
date: 2012-10-12 16:45
tags: [plone, ploneconf]
---

The lightning talks of the last day of the Plone Conference
2012. Again only three minutes each since we had 14 talks!


# Paul J Stevens

Paul had a project where PDFs were workflowed to several sites using
MultiSite. This meant there was lots of duplication. After migrating
to Plone 4 and blob storage, there was still a lot of data.

He created a script ([bscompress](https://github.com/pjstevns/bscompress)) for:

   - De-duplication of blobs using hard-links
   - Less disk-space, faster copy/move actions

In his case, the blob storage went from 14625 Megabytes to 2395 Megabytes.

Todos:

   - Patch `ZODB/src/ZODB/blob.py`.
   - Maintain compatibility and coordinate with other efforts
     (like [collective.recipe.backup](http://pypi.python.org/pypi/collective.recipe.backup/)).


# Philip Bauer

Dylan Jay talked about attracting more new people to get started in
Plone. Dexterity and PloneIDE are great, but we need more. David Glick
started to build a theme editor
([plone.app.themeeditor](http://pypi.python.org/pypi/plone.app.themeeditor/)). It
uses jQuery UI and is a lot better than the Zope Management Interface
(ZMI). There is going to be a PLIP about it.


# Johannes Raggam

Johannes made a new release of
[plone.app.event](http://pypi.python.org/pypi/plone.app.event/). Please
take note of the installation instructions. They include configuring
the right time zone.

Johannes did a quick demo of the packages. There are still
[issues](https://github.com/plone/plone.app.event/issues), but it's
safe to call it a beta version.

Johannes thanks all the contributors for their work.

*Mark: note that the package was moved from the Collective to the
Plone organisation on GitHub on October 13th.*


# Elizabeth Leddy / Eric Steele

All the team leaders (security team, UI team, etc) went on stage so
people would know who is who. And whom to talk to if you want to get
involved.


# Lukas Graf

His company (4teamwork) created
[ftw.tabbedview](http://pypi.python.org/pypi/ftw.tabbedview/). It can
be integrated with
[collective.js.extjs](http://pypi.python.org/pypi/collective.js.extjs/),
[collective.quickupload](http://pypi.python.org/pypi/collective.js.extjs/)
(if installed) and
[ftw.table](http://pypi.python.org/pypi/ftw.table/).

The package `ftw.tabbedview` contains filtering, sorting, grouping,
managing columns, batching, flexible sources (catalog, SQLAlchemy,
...), data transformation (icon, authors, dates, ...) and is highly
configurable. It can also be used on pretty much any context.


# Philip Bauer

Philip helped to organise the
[Plone Konferenz München 2012](http://konferenz.plone.de/). About 150
people attended and there were lots of new people. The goal of the
conference was to attract decision makers. It was a very successful
conference.

Tip: include a sprint lounge where people can sprint the whole
conference. This way you can attract people that want to code and
work together, but do not speak the language the conference is held
in.

Such local conferences increase the visibility of the Plone
community and can attract new members to join the community.

They were able to donate &euro; 3000 to the Plone Foundation.


# Mikko Ohtamaa

Solving problems in plone package at a time:

   - [visualtitle](http://pypi.python.org/pypi/visualtitle/): To have
     a different title on your page and in your navigation.
   - [imageportlet](https://github.com/miohtama/imageportlet): A new
     portlet type to show images.
   - [silvuple](https://github.com/miohtama/silvuple) (That's
     French...): Force the user interface to use your native language
     an show untranslated items.
   - [**plo**mobile](https://github.com/miohtama/plomobile): A
     responsive design for Plone.
   - [sevabot](https://github.com/opensourcehacker/sevabot): A Skype
     bot.

*Mark: When the video of this lightning talk becomes available online,
 it's definitely worth watching it!*


# Franco Pellegrini

If we have to believe the Mayan symbols, this year will be the end of
the world. What better way to experience that day than by joining a
sprint? So join the "End of the world" sprint in Ushuaia, Provincia de
Tierra del Fuego, Argentina on December 21st, 2012.


# Jukka Ojaniemi

[Whiskers](http://pypi.python.org/pypi/whiskers/) is a Pyramid
application that collects all packages used in your buildouts. That
is, if you use
[buildout.sendpickedversions](http://pypi.python.org/pypi/buildout.sendpickedversions/). This
way you can quickly see which buildouts use a certain version of a
package. You might even be able to use this data to find out which
eggs in your buildout cache are not used anymore.


# Érico Andrei

A new solution to change how we collaborate: desk surfing. There is a
Plone core developer dedicated desk in São Paulo. (You can also use it
if you are not a core developer by the way.) If you are in São Paulo?
go there, contact Érico.

(Calvin Hendryx-Parker adds that you are also welcome in Fortville.)


# Calvin Hendryx-Parker

Since Calvin missed is own presentation earlier that day, he did the
three minute version of his talk "Playing With Blocks: 6 Pro Tips for
Building Your Next Super-Charged Plone Site":

   - Use APIs instead of embedded iFrames.
   - Criteria for evaluating your options:
     - Mailing lists taken over by spam?
     - Mailing list neglected?
     - What is the activity in source control?
     - Was there a corporate takover?
     - Hope
   - Leverage Single Sign On (like OpenID).
   - Supercharge your search with Solr (which can also index external
     content).
   - Beware of over customisation.
   - Testing, testing, testing.

The talk he would have held this morning will be recorded and put online.


# Radek Jankiewicz

STX Next created a small addon for Plone:
[stxnext.grayscale](http://pypi.python.org/pypi/stxnext.grayscale/). This
package transforms content of a page to grey scale. It has been
developed for Polish user requirements related to national mourning
after a tragedy has occurred. Governmental sites and bank sites change their colour
scheme to grey scale out of respect. The images are cached on file
system and are thus not generated each request.


# Johannes Raggam

A talk about amplify.cc, a prototype to replace PostNuke based
community portals. It uses only one content type. They use Dexterity
behaviours on content instances instead of on a class. Their
conclusion is that having one content type for everything is possible
and even works really nice.


# Maurizio Delmonte

A lot of countries have their own localised Plone site,
e.g. [Italy](http://plone.it/),
[the Netherlands](http://www.plone.nl/),
[Brazil](http://plone.org.br/), [Spain](http://plone.es/),
[France](http://plone.fr/) and [Poland](http://plone.org.pl/). They
all look different. But by using a bar at the top of the page which
links to other Plone sites in the world, we can unite those sites and
make it easier to discover them.
