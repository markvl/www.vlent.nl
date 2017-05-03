---
title: "PloneNG: What's new in Plone 4.2, 4.3, and beyond (David Glick)"
slug: ploneng-whats-new-in-plone-42-43-and-beyond-david-glick
date: 2012-10-12 11:00
tags: [plone, ploneconf]
---

A overview of the changes in Plone 4.2 and 4.3.

David split up the changes into categories. But first something about
the process.

# PLIP process

A PLIP (Plone improvement proposal, basically a ticket) first needs to
be approved by the Framework Team. Once it has been approved,
implementation starts. When the code is ready the Framework Team does
a review. If the Framework Team says "yes it's okay" there is still
more work to be done before it is completely integrated in Plone
(like final documentation, small changes).

PLIP criteria:

   - Feature balance (content managers **and** developers).
   - Useful for 80% (otherwise it should perhaps be an addon
     instead). Exception to this rule: marketing related features
     (e.g. content staging and versioning; not used much but important to have for software selection processes).
   - Maturity outside the code.
   - Code quality (clean code, tests, documentation, not over or under
     architected)
   - Migration path for current users and developers.


# What has been added?

## Changes for end users

   - *Improved search results* (Plone 4.2). No advanced search form
     anymore. (Tom Gross created
     [collective.searchform](http://pypi.python.org/pypi/collective.searchform/)
     for those that want to have the old functionality back.)
   - You can make the *document byline use the publication date* (Plone
     4.3).
   - *Plain text searches ignore accents* (Plone 4.3).

## Content managers

   - *New collections* (Plone 4.2). Completely new interface which
     includes a query widget and a preview of the results
     ([plone.app.collection](http://pypi.python.org/pypi/plone.app.collection/)). The
     old collections are still there. In a new Plone site they are
     disabled, but they can be enabled. If you upgrade it is the other
     way around: the new collections are not enabled by
     default. Adding custom indexes is harder now. (The UI has not
     been created for `plone.app.collection` yet.)
   - *In-Plone theme editor* (Plone 4.2 and 4.3). You can upload a `.zip`
     file with the theme which contains your `rules.xml` file. You can
     also edit theme with the ACE editor. And a rule builder to spit
     out the Diazo rules file.
   - *Dexterity* (Plone 4.3). Define content types through the web
     without having to be a programmer. Some more things need to be
     done to make this *really* useful. You can for instance not
     change the view or the way the items are searched on in the
     site. Note there are new instructions: you no longer need to
     include a special known good set (also known as a KGS). But might
     need to specify `plone.app.dexterity[grok,relations]` in your
     eggs. Both the `grok` and `relations` parts were not ready for
     default inclusion but are available and useful. If you used
     Dexterity already, definitely include `relations`.
   - *Improved Syndication* (Plone 4.3). There's a syndication control
     panel to configure syndication. Writing new feeds is much easier
     now.
   - Add *"test mail server" button* to the email configuration
     settings (Plone 4.2). After you changed the settings, you can
     have Plone test the connection to your mail server.

## Developer

   - Switch to *HTML5* (Plone 4.2). Also support for
     [Modernizr.js](http://modernizr.com/). Plus miscellaneous cleanup things
     (e.g. we now use the HTML5 `placeholder` attribute).
   - *Resource bundles for Resource Registries* (Plone 4.2). Different
     resources for different themes.
   - Add *z3c.form support to plone.app.portlets* (Plone 4.3).
   - *API for password validation policy* (Plone 4.3). You can
     implement custom logic for password policy (length, characters, etc).
   - Provide *subsection CSS classes on `<body>`*. (Plone 4.3) to make theming
     easier, e.g. when using Diazo.

## Infrastructure

   - Official *support for Python 2.7* (Plone 4.2). Continuous
     integration is now setup for Python 2.6 and 2.7. Python 2.7 is a
     more long term maintenance release than 2.6.
   - Declare *dependency on Pillow* (Plone 4.3) to solve problems with
     PIL from the past. A bit experimental since it might not work
     perfectly on all systems.
   - Upgrade to *jQuery 1.7* (Plone 4.3). Sizzle selectors are
     slightly more strict (class name should be placed in double
     quotes). Binding events is now preferred with "`on`" instead of
     using "`live`" or binding by event name.
   - *Fewer dependencies.* (Plone 4.3).
   - Upgrade to *newer version of TinyMCE* (Plone 4.3). This version
     of TinyMCE works with IE9. It also used to load a bunch of
     separate resources in separate requests, they are now served as
     one big file.

Tip: upgrade to DateTime 3.0: it uses far less memory!

## Cleanup

   - *Unified batch implementation* (Plone 4.3). [plone.batching](http://pypi.python.org/pypi/plone.batching/).
   - *Kupu is gone.* (Plone 4.3). It's an addon you explicitly have to
     list as an egg in your buildout.
   - *KSS is gone* (Plone 4.3). This is significant. It was a great
     feature, but it's been made obsolete by jQuery. A 40% improvement
     in page load speed has been seen by not having to parse KSS
     rules. If you are using KSS you can install
     [plone.app.kss](http://pypi.python.org/pypi/plone.app.kss/) as an
     addon.
   - The *`plone_deprecated` skin is no longer enabled* (Plone
     4.3). It is still there but it is just not used by default.


# What's next beyond 4.3?

There are bunch of packages under consideration for Plone 4.4, for instance:

   - [plone.app.contenttypes](https://github.com/plone/plone.app.contenttypes)
     (a reimplementation of the Archetypes content types as Dexterity content types)
   - [plone.app.event](http://pypi.python.org/pypi/plone.app.event/)
     (which adds recurring event support for Plone and contains
     cleanup)
   - [plone.app.deco](http://pypi.python.org/pypi/plone.app.deco/)
   - [plone.app.toolbar](http://pypi.python.org/pypi/plone.app.toolbar/)
   - [plone.app.multilingual](http://pypi.python.org/pypi/plone.app.multilingual/)
     (a replacement for LinguaPlone with Dexterity support)
   - Having a configurable CSS class for portlets

Interesting PLIPs David would like to see:

  - Change the logo in site settings.
  - Configure things without needing to go to the ZMI:
    - portal_actions
    - resource registries
    - portal_skins
    - portal_css
    - portal_javascripts
  - Standardise how things are done in Plone core to make Plone better example material
    - skin layer items (turn them into browser views)
    - formlib (use z3c.form instead)
    - portal_properties (move them to plone.app.registry)

David asks us to get involved in building the next version of Plone:

  - Review PLIPs to aid the FT by giving feedback on a PLIP. (See
    [the Plone roadmap](https://plone.org/roadmap) for
    the PLIPs.)
  - Champion a PLIP: take responsibility to make a PLIP happen
    (coordinate developers, make sure things are moving along).

What will be the next version, 4.4 or 5? If there is backwards
incompatible stuff we want to include, it's probably going to be
version 5. Then again, releasing version 5 might also 'just' be good
for marketing reasons. In short: David also does not know yet.

[View the slides](http://www.slideshare.net/davisagli/ploneng-whats-new-in-plone-42-43-and-beyond)
or [watch the video](http://www.youtube.com/watch?v=WFSDzpP4Ueg).
