---
title: Migrating django.contrib.comments to Disqus
slug: migrating-djangocontribcomments-disqus
date: 2012-09-07 13:52
tags: [django, vlent.nl]
---

As of today I am using Disqus for comments on this site. This meant
that I had to migrate the old comments (which used
django.contrib.comments) to Disqus. Here's a short description of how
I did this.

Obviously I'm not the first one doing this. As a matter of fact, the
article [Bye-bye django.comments, hello
Disqus](http://blog.roseman.org.uk/2010/04/21/bye-bye-djangocomments-hello-disqus/)
by Daniel Roseman provided a very good tip: use
[django-disqus](http://django-disqus.readthedocs.org/). I just did not
use the `disqus-export` command.

Here's what I did:

- I installed the app as described in the
  [instructions](http://django-disqus.readthedocs.org/en/latest/installation.html).
- I added the required
  [template tags](http://django-disqus.readthedocs.org/en/latest/templatetags.html)
  to my templates and removed the old code to show the comments and
  the comment form.
- To migrate the old comments I created an additional feed to
  [export the comments as WXR](http://django-disqus.readthedocs.org/en/latest/exporting_wxr.html).
- In Disqus I imported the XML from the feed as a generic WXR.

It was a smooth ride (it just took a little over 24 hours for the
import to actually finish) and one less thing to do when I move to a
static blog based on
[Acrylamid](https://github.com/posativ/acrylamid/).
