---
title: Real world intranets (Joel Burton)
slug: real-world-intranets-joel-burton
date: 2008-10-08 20:28
tags: [plone, ploneconf, ploneconf2008]
---

A talk about issues specific to intranet sites.

An intranet site is a different beast than a publicly available
internet site. Differences are

- High percentage logged in users
- Large(r) number of contributors
- Simpler, more trusting, workflows
- Re-use of content (e.g. for print)

When creating an intranet site, one should have a different mindset
than when creating a internet site.

Tips related to content creation:

- Use the presentation mode to create "powerpoint" type content.
- Plone can generate a table of contents for you and previous/next
  links, which will make large documents easier to navigate.
- You can prepare 'template' collections which other contributers can
  re-use. By adding specialised views for the collection, the client
  can use collections more often and have the result they need with
  minimal, one-off solutions. Collections can also be used to populate
  a portlet.
- Since the 'default page' construct can be quite confusing, it may be
  beneficial to add a folderish type which also allows for a chunk of
  text. By having this content type, most of the default page problems
  can be avoided.
- Use content rules! (You can, e.g. abuse the content rules to send an
  email when an object is added to remind the user to actually submit
  a page. Or use the notification action to help user when they have
  created their first item.) See
  [collective.contentrules.mail](http://dev.plone.org/collective/browser/collective.contentrules.mail)
  that provides sophisticated features for sending mail in a content
  rule.

Content managment

- Images and files have no own workflow, but inherrit the workflow of
  the folder they are in.
- Intranets are probably served best by another workflow then an
  internet site. (Allowing owners to edit published pages for
  instance.)
- You can even ask yourself the question whether you even need
  different workflow states... You can, for instance, use a single
  state workflow.
- Another approach is using a "pending" state signalling the owner
  asks for help on a content item.
- The owner of the item is probably the best person to decide whether
  content should be published just internally or world wide.
- The product
  [DCWorkflowGraph](http://www.zope.org/Members/panjunyong/DCWorkflowGraph)
  van be used to visualise the workflow in a help section.
- By using Placeful Workflow you can e.g. limit a strict workflow to a
  certain part of the site.

Add-on products often used

- [PloneFormGen](http://plone.org/products/ploneformgen)
- [Poi](http://plone.org/products/poi); intended for software but can
  be used in other contexts as well
- [plone.contentrating](http://plone.org/products/plone-contentratings)

Theming

- When theming, keep in mind that add-on products can leverage
  e.g. the document actions.
- The body HTML tag has a class name with the id of the item.
- [CSSManager](http://plone.org/products/cssmanager)

Deployment

- Single sign on can be very useful for intranets.
