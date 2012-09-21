---
title: "PloneFormGen: Past, present, future (Steve McMahon)"
slug: ploneformgen-past-present-future-steve-mcmahon
date: 2008-10-10 15:17
tags: [plone, ploneconf, ploneconf2008]
---

A talk by the creator and release manager of PloneFormGen (PFG).

# Past (where does PFG come from)

The ancestors:

- Formulator (Martijn Faassen, heavilly using property sheets)
- PloneFormMailer (Jens Klein, Reinout van Rees, wrapper around
   Formulator)

The concept of PFG was to reuse Archetypes and make it simpler
(Simplicity had a priority over being complete). Fields are individual
content types. Each field contains an embedded Archetypes field which
knows how to render itself.

Even actions adapters are content types, which can be copied, moved,
et cetera. Note that despite the name, they are not Z3 adapters! Each
action adapter has an OnSuccess method. You can have multiple action
adapters which are executed in order.

# Present (the way PFG is being used, what is possible)

Extensions for PFG:

- Salesforce adapter
- CAPTCHAs (which draws it's own CAPTCHs by default, but can also use
  other sources)
- GetPaid

Simple tricks:

- Ad-hoc validators / defaults
- Multiple controlled actions
- Chained forms (required hidden fields at the moment)
- Turn fields on and off based on the context (e.g. hide fields for
  anonymous users)
- [SQL CRU(D)](http://plone.org/products/ploneformgen/documentation/tutorial/sql-crud)

Amazing tricks:

- [Javascript/CSS injection](http://plone.org/products/ploneformgen/documentation/how-to/installing-a-javascript-event-handler-in-a-form)
- [Highly customized thanks pages](http://plone.org/products/ploneformgen/documentation/how-to/customizing-an-individual-thanks-page)
- Posting to the outside world
- Creating content (Steve will create a tutorial on this subject)

Gotchas:

- Incredibly inefficient due to Plone 2.1 architecture
- Not interactive enough

# Future (what do we want the UI to look)

Things PFG needs/Steve wants to use:

- Zope 3 events
- Zope 3 Schema
- z3c.form
- KSS (for inline validation and form editing)
- Smooth migration
- Stay simple
- Dexterity
- [Cross-site request forgery (CSRF)](http://en.wikipedia.org/wiki/Cross-site_request_forgery) protection

Steve would like more people to be involved in the development. You
are more than welcome to join
[the sprint](http://www.openplans.org/projects/plone-conference-2008-dc/ploneformgen)
and translations are also needed.

The vertical presentation of the fields is in many cases not the
layout one needs. However, since PFG uses the Plone form framework,
it's unlikely that PFG will solve this by itself any time soon. You'll
need CSS to get the layout you want.

For more information, see
[the PloneFormGen page](http://plone.org/products/ploneformgen).
