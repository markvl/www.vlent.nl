---
title: "Getting Dates with Plone: Connecting People with Events (Aaron VanDerlip)"
slug: getting-dates-with-plone-aaron-vanderlip
date: 2008-10-09 15:12
tags: [plone, ploneconf, ploneconf2008]
---

An overview of Plone4ArtistsCalendar, targeted at integrators.

Plone4ArtistsCalendar was a big monolith at the beginning, but it has
be refactored to have a more modular design:

- dateable.chronos: the user interface (provides calendar views, calls
  event providers, reusable outside p4a)
- datable.kalends: the interfaces
- p4a.plonecalendar: extention of calendar framework (register folders
  and topic types to implement IPossibleCalendar, hooks for
  import/export of iCal feeds)
- p4a.ploneevents: extension of event type (implements
  dateable.kalends.IRecurringEvent, uses schemaextender to add
  Recurrence support)
- p4a.subtypes: provide a way for adding marker interfaces through the
  Plone UI.

After installing Plone4ArtistsCalendar, folders + topics can be marked
as calendar subtype. And since collections can also be subtyped to be
a calendar, one can show only the events belonging to the category X.

Plone events do not support recurrence. With Plone4ArtistsCalendar you
can have an event recurring e.g. every day, instead of having just a
single start and end date. A practical example, you can add the Plone
Conference event and have that start at 9 AM and end at 5 PM each day
for October 8 - 10, instead of having a single event starting October
8th, 9 AM and end at October 10th at 5 PM.

Plone4ArtistsCalendar can also import either iCal files from file
system or from a URL. To do this, add a folder, mark it as being a
calendendar and you can instantly import the iCal. Importing the same
iCal file, events are not duplicated since a hash of the event is
stored. As long as the event hasn't changed, the event is left
alone. Changes in the event could result in duplicates however. Note
that the events are not synchronised when you import from an URL;
importing is only done once. (Unless you manually import it again
obviously.)

By having the `ICalendarEnhanced` interface, it's quite easy to
e.g. add a viewlet to the calendar views. There is no need to subtype
anything. A piece of ZCML and a page template could be enough to do
the job. (Depending on the complexity of the content of the viewlet
obviously.)
