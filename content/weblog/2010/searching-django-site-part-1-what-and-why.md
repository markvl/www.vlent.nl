---
title: "Searching in a Django site - part 1: what and why"
slug: searching-django-site-part-1-what-and-why
date: 2010-10-14 22:24
tags: [development, django]
---

One of the things that was still on my wish list for this site, was a
proper search. In two articles I will explain how I've done this. The
[next article](/weblog/2010/10/15/searching-django-site-part-2-how/)
will describe the way I have currently set things up. This article
will primarily focus on the journey I made to come to my choice
(Djapian).

# Background

Coming from Plone, I'm quite spoiled in the search department: Plone
has great search functionality out of the box. When launching the
Django version of this site, I didn't want to spend too much time on
the search feature since it isn't used that much, according to the
access logs.

As a result I implemented the simple solution where I just searched
for weblog entries containing the search term:

    BlogEntry.objects.published().filter(
        Q(title__icontains=query) |
        Q(intro__icontains=query) |
        Q(body__icontains=query))

This works for simple queries, but it's far from perfect since it
literally searches for a string. Searching for "plone django" for
example only returns articles where I used the word "plone" and then
"django" separated by a space.

# Haystack

In my quest to improve the search function, I started looking for
Django applications to help me out. Although I didn't fully research
this area, [Haystack](http://haystacksearch.org/) seemed to be the
right tool for the job.

And it's indeed a really nice application to use. A few highlights:

- The clear documentation gets you up-and-running pretty quickly.
- Haystack is using a class based views, so it's really easy to
  customize.
- You can use a data template to feed the indexer the right
  data. (Which implies that you can use template tags to e.g. strip
  out HTML tags. And since I'm storing the body text of my entries as
  HTML, this can be useful.)

# Whoosh

Haystack provides a nice API to search but you still have to decide on
which backend to use. Initially I chose [Whoosh](http://whoosh.ca/)
since it's pure Python. (This makes is easier to integrate in my
buildout configuration.) I used
[Haystack 1.0.1-final](http://pypi.python.org/pypi/django-haystack/1.0.1-final)
as that is the latest version on PyPI. However, using the last release
of Whoosh results in an `AttributeError` when reindexing:

    AttributeError: 'FileIndex' object has no attribute 'commit'

This means I had to use
[Whoosh 0.3.18](http://pypi.python.org/pypi/Whoosh/0.3.18) since
Haystack 1.0.1 does not seem to be compatible with the Whoosh 1.x
series.

And to be fair: searching indeed worked. But when I viewed the
results, the score was always zero. Which isn't useful if you want to
sort on that score. (Note that this might be due to the fact that I'm
not using the most recent code of both Whoosh and Haystack. I did not
want to spend time on researching this to be honest.)

# Xapian

I figured that switching backends might be an easy solution. So I
chose [Xapian](http://xapian.org/) in combination with
[xapian-haystack version 1.1.3beta](http://pypi.python.org/pypi/xapian-haystack/1.1.3beta). (Mainly
because I didn't like the idea of running
[Solr](http://lucene.apache.org/solr/).) And initially everything
seemed to work the way I wanted. That is: searching for "plone django"
gave me results and those results had a nice score I could sort on.

But there was no difference between the results of "plone AND djano"
and "plone OR django". And worse: searching for "postgres" or
"postgres\*" did not return articles containing the string
"PostgreSQL". This was not acceptable.

I know that the Xapian backend supports all kinds of
[feature flags](http://xapian.org/docs/apidoc/html/classXapian_1_1QueryParser.html#e96a58a8de9d219ca3214a5a66e0407e)
to enable these kind of things, but I could not immediately figure out
how to do it via Haystack.

# Djapian

An article by Nizam Sayeed about
[full text search in Django](http://www.nomadjourney.com/2009/05/full-text-search-across-multiple-django-models-using-djapian/)
sent me in the direction of
[Djapian](http://code.google.com/p/djapian/). And judging by the
subversion logs of the code, it's still actively developed.

This switch from Haystack to Djapian meant that I could not use the
class bases view. Then again, I did not have to either. Using Djapian
meant that I only had to make relatively small changes in my original
code. But that's something for a next article.

By the way: the documentation of Djapian may look less polished than
Haystack's, but it contained all the information I needed.

# Conclusion

There's more than one way to implement search in a Django site. The
Djapian/Xapian based approach is a good solution for me. Perhaps I
could have ended up with a similar result with Haystack/Whoosh if I
had wanted to. This just seemed liked the easiest way to go for now.
