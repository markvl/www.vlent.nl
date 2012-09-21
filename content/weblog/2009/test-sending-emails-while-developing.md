---
title: Test sending emails while developing
slug: test-sending-emails-while-developing
date: 2009-10-03 12:14
tags: [development, django, plone, python, testing]
---

I frequently have to send emails from web applications. But before I
deploy to a production environment, I want to make sure the mechanism
works and the right mails are constructed. Here's two ways to do that.

# Monkey patching the Zope MailHost

When developing a Zope based application, the
[Products.PrintingMailHost](http://pypi.python.org/pypi/Products.PrintingMailHost)
package can really help you out. By including this package in your
setup, the Zope MailHost class is patched so no actual emails are
sent. Instead the content of email is printed to the standard output.

# SMTP server

But when working on a Django application (or any other non Zope
project) there is no MailHost class that can be monkey
patched. Python's
[smtpd module](http://docs.python.org/library/smtpd.html) to the
rescue. The first step is to configure the application to use
localhost as the SMTP server on a random port (say: 1025). Next, go to
the command line and type:

    $ python -m smtpd -n -c DebuggingServer localhost:1025

Just like the PrintingMailHost, this SMTP server prints the emails to
standard output. For more information see the
["Testing e-mail sending" section](http://docs.djangoproject.com/en/dev//topics/email/#testing-e-mail-sending)
in the Django documentation.

## Update 2010-08-09

For the developer with a deadline: install
[django-extensions](http://pypi.python.org/pypi/django-extensions/0.5)
which has a couple of usefull extra features. One of them is the
`mail_debug` management command. This commands starts the same SMTP
debugging server, but you don't have to remember the right
incantation.

# HTTP server

Somewhat related to this: if you want to test your application against
an HTTP server, you can use this command:

    $ python -m SimpleHTTPServer

The
[SimpleHTTPServer module](http://docs.python.org/library/simplehttpserver.html)
can be used to get server up-and-running quickly. It can also be a
simple way to, for instance, copy files from one machine to
another. By running the HTTP server in the directory containing the
files, you can access the files via your browser on another
machine. Safe? No. Convenient? Yes.
