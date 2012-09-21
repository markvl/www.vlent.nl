---
title: Hybrid Vigor Plone / Salesforce integration (Andrew Burkhalter)
slug: hybrid-vigor-plone-salesforce-integration-andrew-burkhalter
author: Jean-Paul Ladage
date: 2008-10-09 22:40
tags: [plone, ploneconf, ploneconf2008]
---

Constituent Relationship Management

**(Contribution by Jean-Paul Ladage)**

Safesforce is:

- a web based CRM
- an online accessible relational database

Goals for integration:

- Login again Salesforce records and update profile data (PAS)
- Simple event registration
- View salesforce data

He provided a few demo's.

# Sale data from PloneFormGen to Salesforce using Salesforce
PloneFormGen adapter. This allows you to create forms and directly
submit the data to salesforce.

- Account adapter, you can map the form fields to fields in the account table in the sf database.
- Contact adapter, you can map the form fields to fields in the contact table in the sf database. you can even configure
- Attachments can also be added.

# RSVP for Salesforce

Event registration e.g. call for proposals

CRM has a campaign feature. Any piece of content in Plone can be
associated with a campaign in sales force by selecting the object type
and uid. As a result is that in Plone below the content a contact form
is shown. It adds a lead in SF and shows how we got in contact with
that person (by showing the related campaign.

In SF you can create a waitlist state, to signal that you have to
process the contact.

# Login and edit user profile data (PASPlugin)

- You can add a password field to Salesforce.
- In the plugin you can configure which fields to authenticate with
  and map additional properties like department, or assistent name
  with an object type in SF e.g. a Contact or Lead.

# Local Cache of Salesforce records

The Zope catalog is used to cache information from SF. Using an
overnight scheduled job.
