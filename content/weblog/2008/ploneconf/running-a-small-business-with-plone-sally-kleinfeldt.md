---
title: Running a small business with Plone (Sally Kleinfeldt)
slug: running-a-small-business-with-plone-sally-kleinfeldt
date: 2008-10-08 19:45
tags: [plone, ploneconf, ploneconf2008]
---

What tools can be used to run a business?

Sally talked about the tools Jazkarta uses:

# Operations

- Google Apps: start page, mail, documents, calendar, etc. The
  documents can also be used to share information with customers for
  instance. The start page can also show SalesForce information. Since
  Google is reliable and everything can be exported from Google,
  Jazkarta does not see using Google as a risc.
- Dropbox: a shared file system
- Plone can draw information from e.g. the Google Calendar and show it
  in a site.

# Marketing/Sales

   - Plone site
     - hosted via Amazon EC2
     - Buildout and fabric for deployment
     - Data.fs and logs use Elastic Block Storage (faster)
     - Backups use S3 storage (to be able to setup another server if the
       virtual EC2 server would go down)
   - Vertical Response for emails to the clients.
   - Salesforce, a relational database to store information about
     relations. Gmail, Google Docs, Google Adwords, Vertical Response and
     PayPal can be integrated. Integration of Salesforce in Plone:
     - Salesforce Connector
     - PloneFormGen
     - SalesForceAdapter

# Customers

- ClueMapper: "super-charged" Trac, including a time tracker.

Sally showed screenshots of the path from a (PloneFormGen generated)
form to the Salesforce database, to the Vertical Response mail.
