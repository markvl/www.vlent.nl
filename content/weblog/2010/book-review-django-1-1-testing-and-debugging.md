---
title: "Book review: Django 1.1 Testing and Debugging"
slug: book-review-django-11-testing-and-debugging
date: 2010-06-20 15:05
tags: [development, django]
---

In April Packt published
[Django 1.1 Testing and Debugging](https://www.packtpub.com/django-1-1-testing-and-debugging/book)
by Karen M. Tracey. After reading it I figured I might as well write a
review.

The book is written for Django application developers and requires
basic knowledge of Python and Django. And although the code samples
are indeed explained, the context is not always expanded on. This
makes sense for this book and the author recommends to at least do the
[Django tutorial](http://docs.djangoproject.com/en/dev/intro/tutorial01/). I
think you'll get even more out of the book if you've got a bit more
experience with building Django applications.

As the title already gives away, the book focusses on two subjects:
testing and debugging. These topics are discussed while developing a
survey application. Because this application is used consistently in
the book, the examples require less explanation which means that the
focus in more on the subject at hand (e.g. writing a unit test)
instead of developing this specific application.

# Testing

The first five chapters dive into the world of testing. Karen starts
with explaining how to run the tests and what success and failure
looks like. The second chapter has a focus on
[doctests](http://docs.python.org/library/doctest.html). Not only does
she show examples of tests, she also lists pros and cons of using
doctests. Meanwile she also discusses whether a test is even useful
(example: you should not test Django itself). The examples in the book
consist of doctests that are placed in the docstring of functions. She
does not show how to run a doctest in a separate file
(e.g. `README.txt`) which can be more useful for explaining or
demonstrating the API of the application as a whole, or doing
integration tests.

[Unit tests](http://docs.python.org/library/unittest.html) are
discusses more extensively in chapters three to five. Karen starts by
reimplementing the doctests as unit tests and continues by showing
things like the `setUp` and `tearDown` methods and also
`django.test.Client` to test views. In the last chapter about testing
she introduces the reader to test runners, test coverage and using
[twill](http://pypi.python.org/pypi/twill) instead of
`django.test.Client`. The only thing I want to nag about is the style
of some of the examples. Occasionally she writes things like:

    def testHome(self):
        from django.core.urlresolvers import reverse
        ...

Where I would write:

    from django.core.urlresolvers import reverse
    def testHome(self):
        ...

In my opinion every programming book should pay attention to
programming style. Although it does not have to be addressed
explicitly, the style of the examples should be consistent and follow
the appropriate coding standards/guides (like
[PEP8](http://www.python.org/dev/peps/pep-0008/) for example which
states that imports must be at the top of the file).

# Debugging

Anyway, on with the book review... The remainder of the book is about
debugging and troubleshooting. Karen first describes the functionality
Django offers to debug your application. For instance, the debug error
pages are explained in detail. The style Karen chose for this part of
the book resembles watching a programmer at work: a mistake is made
and results in an error page, the error reported by Django is
investigated to discover the cause of the problem and the code is
fixed.

Next subject is how to find errors that are less obvious: Django does
not show an error page, but the application does not work as it
should. Initially some custom code is created to show the SQL queries
involved in a view. Although this code is replaced by the
[Django Debug Toolbar](http://pypi.python.org/pypi/django-debug-toolbar)
later on, it is also used to show how to package the custom code for
reuse. (Personally, I would have kept the custom query display section
a bit shorter and skip the packaging altogether. It's beyond the scope
of the book and I think there are other resources that describe
developing for reuse much better.) Karen does a great job describing
the features offered by the Django Debug Toolbar. She also explains
why using print statements is evil and using logging is good.

The next subject (chapter nine) is the Python debugger (pdb). Not only
is this chapter a thorough description of the debugger, there's also a
number of pages devoted to
[race conditions](http://en.wikipedia.org/wiki/Race_condition#Computing). Although
this is an important subject, I personally sometimes forget about it
when developing an application. So I think it's great that it the
subject is brought up in this book!

Chapter ten ("When All Else Fails: Getting Outside Help") is a nice
description about what you should do when you encounter a problem in
Django. Karen points the reader to the
[Django documentation](http://docs.djangoproject.com/) (to confirm you
are using the API as it was intended) and the
[Trac site](http://code.djangoproject.com/) (where you can may already
find a fix for your problem). She also gives clear instructions and
tips on what to do when the problem isn't already fixed or perhaps
hasn't even been reported yet.

The last chapter of the book is about moving your code to production
and making it accessible for the world. It gives an example for the
required WSGI script and the Apache configuration. Furthermore, it
also describes debugging the production environment and load testing
with siege. Finally Karen discusses the use of Apache and mod\_wsgi
during development. Although she claims that the Apache/mod\_wsgi
setup can be made nearly as convenient as using the Django development
server I think it really depends on the situation. I agree that it may
be a good way to tackle some problems and setup issues early on. But
if you are working with a number of developers on the project and each
developer is working on several different projects (sometimes even
switching projects throughout the day), I'm not sure whether it's
worth the effort.

# Conclusion

I've been developing in Python a couple of years, mainly working on
Plone projects since 2007 and doing Django applications since 2009. I
was already more than familiar with the topics in the book (doctests,
unit test, logging, debugging, et cetera) and have also done a bit of
test driven development. As a result, the book did not open a whole
new world for me. However, I do think that the book was worth the
read. I picked up a few new tricks and gained an even better insight
in testing and debugging Django applications.

One last complaint though: the title of the book could have been a bit
better: by putting the Django version number in the title, the book
seems to target Django 1.1 specifically. Sure, Django 1.1 and 1.1.1
have been used in the book. And sure, some examples might not work in
earlier or later versions of Django. However, the principles remain
the same! In my opinion the version should have been left out of the
title.

Although I may not agree with everything, I think
[Django 1.1 Testing and Debugging](https://www.packtpub.com/django-1-1-testing-and-debugging/book)
is a good book. So I'd like to thanks Karen and Packt for writing and
publishing it.
