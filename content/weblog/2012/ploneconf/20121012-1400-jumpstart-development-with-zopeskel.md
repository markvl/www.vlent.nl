---
title: Jump start your development with ZopeSkel (Cris Ewing)
slug: jump-start-your-development-with-zopeskel-cris-ewing
date: 2012-10-12 14:00
tags: [plone, ploneconf]
---

Tutorial on how to write templates for ZopeSkel.

This is the second half of his
[previous talk](/weblog/2012/10/12/zopeskel-past-present-and-future-cris-ewing/). This
talk is about using and extending ZopeSkel.  By creating your own
templates you can start with a customer project really fast.


# Why and when

Do you have code you write over and over again? Is the code almost the
same each time and are the places where you change stuff always the
same?  You can avoid writing all that code by creating a template.

You can write the template the way *you* want. This is just a
system. This means you can version control your own process by
documenting it in a template.


# Basics of template writing

The first question you need to ask yourself is "what do I want?". The
next thing you will want to investigate is what you have already got.
You can use "`bin/templer --list`" and "`bin/templer <template_name>
--list-variables`" to find out more about the templates ZopeSkel has
to offer. Then have a look at the code provided by the template.

To wire everything up, you need to do four basic:

1. Create a class.
2. Import the class to a package namespace.
3. Provide an entry point.
4. Write the actual template itself.


# Tips

*Cris has already written the documentation for this tutorial. It
 currently lives on his laptop, but it should be posted online soon. I
 (Mark) decided to just write down some notes instead of trying to
 replicate Cris' documentation.*

The related documentation can be found here:

   - [Templer System Manual](http://templer-manual.readthedocs.org/en/latest/index.html)
   - [Templer quick start](http://templer-manual.readthedocs.org/en/latest/quickstart.html)
   - [ZopeSkel documentation](http://templer-manual.readthedocs.org/en/latest/applications/zopeskel.html)

Tips:

   - Do not install ZopeSkel in your global Python! Always use a
     [virtualenv](http://pypi.python.org/pypi/virtualenv/) or
     [buildout](http://pypi.python.org/pypi/zc.buildout/).
   - If you want to use [pip](http://pypi.python.org/pypi/pip/), use version 1.1 or later.
   - To use the package while developing, use "`python setup.py
     develop`" (so "`develop`" instead of "`install`").
   - If you are using a buildout, you can also use
     [mr.developer](http://pypi.python.org/pypi/mr.developer/).
   - The modes are incrementally inclusive: the questions for the
     "easy" mode are also asked in the "expert" mode, etc.
   - Which namespace to choose: if you want to contribute the
     templates and they might be useful for others: use the `templer`
     namespace; for your own project/infrastructure specific
     templates, use your company's namespace.

[View the slides](http://www.slideshare.net/cewing/jumpstart-your-development-with-zopeskel-14719067).
