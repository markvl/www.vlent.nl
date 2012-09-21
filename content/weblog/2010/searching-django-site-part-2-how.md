---
title: "Searching in a Django site - part 2: how"
slug: searching-django-site-part-2-how
date: 2010-10-15 08:28
tags: [development, django]
---

One of the things that was still on my wish list for this site, was a
proper search. In two articles I will explain how I've done this. The
previous article described
[why I picked Djapian](/weblog/2010/10/14/searching-django-site-part-1-what-and-why/). This
article focusses on some of the technical aspects of my setup.

# Buildout

If you've read other articles from me, you may know that I'm a big fan
of [buildout](http://www.buildout.org/). Thus the first step of adding
search functionality starts with updating the buildout configuration.

    [buildout]
    parts =
        xapian
        xapian-bindingseggs =
        djapian

    [versions]
    djapian = 2.3.1
    zc.recipe.cmmi = 1.3.2

    [django]
    recipe = djangorecipe
    extra-paths =
        ${xapian:location}/lib/python

    [xapian]
    recipe = zc.recipe.cmmi
    url = http://oligarchy.co.uk/xapian/1.0.22/xapian-core-1.0.22.tar.gz

    [xapian-bindings]
    recipe = zc.recipe.cmmi
    url = http://oligarchy.co.uk/xapian/1.0.22/xapian-bindings-1.0.22.tar.gz
    extra_options =
        PYTHON_LIB=${xapian:location}/lib/python
        XAPIAN_CONFIG=${xapian:location}/bin/xapian-config
        --with-python
        --with-php=no
        --with-ruby=no
        --with-java=no
        --with-csharp=no

Should you want to use Djapian yourself, note that
[version 2.3.1](http://pypi.python.org/pypi/Djapian/2.3.1) is not
compatible with the Xapian 1.2 series. Building the index works fine,
but when you start searching you'll get the following error:

    'MSetItem' object has no attribute 'get_document'

According to
[issue 113](http://code.google.com/p/djapian/issues/detail?id=113)
this will be solved in Djapian version 2.4. For now I just used Xapian
1.0.22.

# Django

Using Djapian in your Django project is simple so I won't waste to
many words on it:

    INSTALLED_APPS = (
        'djapian',
    )

    DJAPIAN_DATABASE_PATH = path/to/djapian_spaces

Don't forget to run the `syncdb` management command afterwards.

# Application

In your (weblog) application you'll need to add an `index.py` file
where you'll define how your model(s) will be indexed. I just have one
model, BlogEntry, which I want to index. So my `index.py` can be
simple:

    from djapian import space, Indexer
    from blog.models import BlogEntry

    class BlogEntryIndexer(Indexer):
        fields = [('title', 2), 'intro', 'body', 'caption']

        def trigger(indexer, object):
            return object.is_published

    space.add_index(BlogEntry, BlogEntryIndexer, attach_as='indexer')

As you can see I think the title of the article is a bit more
important. I also only want to index published articles.

To make sure the index is loaded when the application starts, a small
addition to `urls.py` does the trick:

    from djapian import load_indexes
    load_indexes()

Then there is the actual search view. I'll spare you the boring part
and only show the code that performs the search action:

    from djapian.resultset import xapian
    from blog.models import BlogEntry

    def search(request):
        # Get the search string as "query"
        resultset = BlogEntry.indexer.search(query).flags(
            xapian.QueryParser.FLAG_BOOLEAN |
            xapian.QueryParser.FLAG_PHRASE |
            xapian.QueryParser.FLAG_LOVEHATE |
            xapian.QueryParser.FLAG_WILDCARD |
            xapian.QueryParser.FLAG_PARTIAL).prefetch()
        ...

(See the
[Xapian API documentation](http://xapian.org/docs/apidoc/html/classXapian_1_1QueryParser.html#e96a58a8de9d219ca3214a5a66e0407e)
for more flags.)

# The index

There's only two things left. The first is creating the index for the
first time:

    $ bin/django index --rebuild

The other thing is making sure the index is updated. In my case I run
the following command once every hour. This means that for up to one
hour after publishing an article, it cannot be found with the
search. I think this is quite acceptable for my publishing
rate. Anyway, the command:

    $ bin/django index

And that's all there is to it. If you want more information, read the
[Djapian Tutorial](http://code.google.com/p/djapian/wiki/Tutorial). It
covers most of the above in greater detail.
