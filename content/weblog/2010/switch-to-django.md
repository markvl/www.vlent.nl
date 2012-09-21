---
title: Switch to Django
slug: switch-django
author: None
date: 2010-05-30 18:25
tags: [django, plone, vlent.nl]
---

This site is now powered by Django instead of Plone. Yes, I've finally
made the switch!

*The migration also means my RSS feeds have changed. For more
information, look at the end of this entry.*

I've been planning this migration since late 2009, but initially I
lost myself in the details and had other things on my mind. But now,
I've finally finished it.

To be honest, it wasn't even complicated. I created a few apps for the
blog, a couple of templates and some view logic. And by adding the
Django packages (including my project and apps) to the Python path, I
could write a quick and dirty browser view which iterated over all
Plone weblog entries and saved them as Django weblog entries.

# Why?

There are a couple of reasons for switching to Django. The first is
quite simple: it's fun! Writing the blog engine can even be more
rewarding than writing the weblog entries themselves: tinkering with
the code to get it just the way I want it, putting the pieces
together, building the application step-by-step... I just love it.

Another reason is a bit more pragmatic. Plone is a complete content
management system with all the bells and whistles. But with my weblog
I was only using a fraction of it. I don't need events, news items,
groups, roles, et cetera. Sure, the Plone search functionality is
great, but all I need is 'good enough.'

# What did I gain?

I personally think the Django site requires less resources and is
faster. But I am biased and might just see what I want to see. Time to
gather data...

Let's start with the resources:

<table>
  <caption>
    Server side measurements comparing the Plone and Django version of
    this site. (Memory: measured the ZEO client and ZEO server
    processes of the Plone site (thus: no Varnish). For Django I took
    the WSGI process.)
  </caption>
  <thead>
    <tr>
      <th> </th>
      <th>Plone</th>
      <th>Django</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Files (under source control)</td>
      <td class="tabular-number">160</td>
      <td class="tabular-number">87</td>
    </tr>
    <tr>
      <td>Lines of code (under source control)</td>
      <td class="tabular-number">4336</td>
      <td class="tabular-number">3390</td>
    </tr>
    <tr>
      <td>Disk space (MB, complete running site)</td>
      <td class="tabular-number">383</td>
      <td class="tabular-number">67</td>
    </tr>
    <tr>
      <td>Memory (MB, <code>pmap &lt;pid&gt;</code>)</td>
      <td class="tabular-number">240</td>
      <td class="tabular-number">110</td>
    </tr>
  </tbody>
</table>

Measuring the speed is less straightforward. Although I've got the
feeling that the site is more responsive, I used
[ApacheBench](http://httpd.apache.org/docs/2.3/programs/ab.html) to
get some numbers. But before going to the results, a quick
disclaimer. I do not pretend this is representative at all. I do not
claim this test is in any way scientific. It's merely a way to get a
bit objective information.

The setup of the Plone site: Plone with CacheSetup installed (and
enabled) behind Varnish behind Apache. The Django site is deployed
with Apache and mod\_wsgi and I haven't setup any caching yet.

The command line for the test:

    $ ab -n 100 -c <x> http://vlent.nl/weblog/

where I used 1, 2, 4, 8, 16 and 32 for the concurrency parameter. I
tested Plone both directly (by adding the ZEO client port to the URL,
so even bypassing Apache) and via the normal Apache/Varnish/Plone
route.

<figure>
  <img src="/images/graph-min-request-time.png" alt="Graph showing the minimal total request times"
      width="370" height="300"/>
  <figcaption>
    The minimal request time of a 100 requests.
  </figcaption>
</figure>

As you can see in the graph above, Plone behind Apache and Varnish is
quite consistent. The fastest response takes 850 to 1050 milliseconds
with 32 concurrent requests. Plone also has a minimum of 850 but
climbes up to well over 4000 ms. Django sits in the middle with a
range from 510 ms to 2400 in the last test.

<figure>
  <img src="/images/graph-median-request-time.png" alt="Graph showing the median total request times."
      width="370" height="300"/>
  <figcaption>
    The time in which 50% of the 100 requests were served.
  </figcaption>
</figure>

The second number I looked at was the median request time. This means
that 50% of the requests were served within that time. With a
concurrency of 1, 2 and 4 Varnish doesn't seem to make that much of a
difference. Django seems to perform pretty nice compared to Plone,
even at a concurrency of 16 (and again: I did not setup any form of
caching here).

<figure>
  <img src="/images/graph-max-request-time.png" alt="Graph showing the maximal total request times."
      width="370" height="300"/>
  <figcaption>
    Maximal request time when serving 100 requests.
  </figcaption>
</figure>

The maximal time requests took actually surprised me. Especially since
the Apache/Varnish/Plone route seems to perform worse than just Plone
when the concurrency increases. Django seems to handle requests pretty
consistently: the maximum request time is about 1.3 times the median.

So although the Apache/mod\_wsgi/Django combination is not necessarily
the fastest, it does behave rather predictable: twice the concurrency
means that the minimum, median and maximal time a request takes also
is about two times as large.

(The graphs also might indicate that I've messed up my Plone (or
Varnish) configuration somewhere. However, since I've moved to Django
I don't want to investigate that any further now...)

To make a long story short: I'm happy with the end result and we'll
see how long I'll stick with Django before moving to the next (new)
framework. ;-)

# Syndication

One last thing: by switching to Django, I also could no longer benefit
from the feeds generated by one of the Plone products I used. I now
had to create the feeds myself and thus had to make my own
decisions. After reading
[RSS and Atom: Understanding and Implementing Content Feeds and Syndication](https://www.packtpub.com/rss/book)
by Heinz Wittenbrink I decided I liked the
[Atom format](http://en.wikipedia.org/wiki/Atom_%28standard%29) better
and choose to only implement Atom feeds and drop support for RSS.

As a result, the weblog now has a single feed:
[http://vlent.nl/weblog/atom.xml](http://vlent.nl/weblog/atom.xml). To
only get items on a specific topic, e.g django, subscribe to
http://vlent.nl/weblog/categories/**django**/atom.xml.
