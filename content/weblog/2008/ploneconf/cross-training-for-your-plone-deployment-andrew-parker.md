---
title: Cross-training for your Plone deployment (Andrew Parker)
slug: cross-training-for-your-plone-deployment-andrew-paker
date: 2008-10-09 17:12
tags: [devops, plone, ploneconf, ploneconf2008]
---

Best practices for Plone deployment.

Andrew discussed a set of tips for Plone deployement.

Regarding the hardware: the most important aspect is to have as much
RAM as possible.

# Caching: Squid

There are several types of caching: a proxy cache (e.g. Squid and
Varnish), ZEO client RAM cache and browser cache. To be able to use
Squid, Plone should send the right headers. Enter CacheFu. You'll need
to install it, enable it and set the purge type to simple purge. Note
that templates are stored in the ZEO RAM cache by default. (Note that
the RAM cache is fast, but it also increases the memory footprint of
the instance.)

To check the headers sent out by Plone, you can use the Firefox
extension Firebug.

# HTTP Server: Nginx

Nginx is much more flexible in URL rewriting compared to Squid.

- Nginx is lightweight.
- It supports SSL.
- A default Apache install includes many modules and thus takes up
  valuable RAM.

# ZEO Cluster

Using the setup described above, the site is much faster for anonymous
users but not for logged in users. By having several ZEO clients, you
can use a load balancer like Pound to spread the traffic.

Advice: use as many clients as you can until you run out of
RAM. Andrew hasn't done a setup with more than 6--8 clients. If you do,
monitor the ZEO server logs for conflict errors.

# Final setup

This leads to a final setup where each request is first processed by
Squid. If it cannot serve a cached version, it forwards the request to
Nginx. Nginx can do its rewriting and then passes it to Pound, which
in turn sends it to one of the ZEO clients.

When a page has changed, Zope can send a purge request to Squid.

# Other considerations

- Have a `robots.txt` to keep robots from hammering your site and thus
  prevent them from taking up too much processor time.
- Use repozo scripts for backups.
- Institute ZODB packing to save on disk space
- Log rotation: Squid, Nginx, Pound, the ZEO clients and the ZEO
  server all have logs by default. Advice: log through Squid for web
  statistics and ditch the other logs.
- For HTTPS sites, you'll have to bypass Squid, but can still have
  Nginx (or Apache).
- If you don't need complex rewrite rules, you could also use the
  Squid load balancing (and thus remove Nginx and Pound from the
  equation).
- Having Nginx behind Squid (instead of the other way around) allows
  you to have squid allow/disallow domains. It's also easier to purge
  the cache this way.
- You can use ab and JMeter for load metering.
- Andrew has experienced some problems with Varnish sucking up all of
  the resources of the server. This was 6--7 months ago however. The
  Six Feet Up site has been running with Varnish for quite a while now
  without problems though.
