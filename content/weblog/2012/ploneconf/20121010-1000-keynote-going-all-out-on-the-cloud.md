---
title: "Keynote: Going all out on the cloud (Jan Jongboom)"
slug: keynote-going-all-out-on-the-cloud-jan-jongboom
date: 2012-10-10 10:00
tags: [plone, ploneconf]
---

The first technical talk of the 10th Plone conference is by Jan Jongboom, who
works for [Cloud9](https://c9.io/).

In 1995 Livescript appeared and was shipped with Netscape
2.0. Although the name is similar to Java, Javascript is not like
Java, but more like
[Scheme](http://en.wikipedia.org/wiki/Scheme_(programming_language)). The
name was chosen to ride the wave of Java's popularity. Until 1999 it
wasn't too interesting. However, Microsoft needed XMLHttpRequest (that
basis of what we now call Ajax) and that sparked new development. In
2000 Google launched Gmail and used this technology to show mails in
your page without having to refresh the whole page.

Problems with Javascript is that the implementation differs between
browsers and browser versions. The best sold Javascript book is
[Javascript: The Good Parts](http://shop.oreilly.com/product/9780596517748.do).

The DOM was never meant to be scripted! And dealing with the DOM in
Javascript was a reason for Jan to dislike Javascript. But then
[jQuery](http://jquery.com/) appeared in 2006. The big power from
jQuery comes from [Sizzle](http://sizzlejs.com/) which allows nice
selectors. And this makes working with the DOM way better.

Then Javascript really started to pick up. With
[Node.js](http://nodejs.org/) you can even use Javascript on the
server. But the actual power comes from the underlying platform:
[LibUV](https://github.com/joyent/libuv), which abstracts away the
operating system calls.

Writing synchronous code is easy. *Asynchronous* code however... A
simple thread on a Linux system uses 2Mb. And every time someone does
a request, a thread is started. This can become a problem when there
are requests that take a long time. And if e.g. Apache is limited to a
certain amount of memory, you are limiting the number of possible
requests. With LibUV this is managed so you don't need the 2Mb per
thread. So if you have a web application that requires a lot of
concurrent connections, you are no longer limited by the memory usage
of the threads.

Node.js is basically a Javascript binding to LibUV, with standard
libraries in Javascript, using the Google V8 engine.

Why use Node.js over e.g. [Twisted](http://twistedmatrix.com/trac/)?
There was no module system in Javascript, so one could be
invented. And Javascript is already written asynchronous, in contrast
to most Python code. This made it easier to get started.

# Cloud9

Cloud9 wanted to bring the cool stuff from other languages to
Javascript. It's an on-line, open source, IDE. It used
[ACE](http://ace.ajax.org/) for their editor. It's completely written
in HTML, CSS and Javascript and has many features. Currently it's only
supported by Node.js. However, you should be able to run it with
Python in a couple of months.

With Cloud9 you get a free Linux
[OpenShift](https://openshift.redhat.com/app/) VM. Including a real
terminal. But the coolest feature is collaboration. Someone else can
come into your IDE and see the same things you see. He/she can see
your cursor and see you type. (Also: If you close a file, the files is
also closed in the IDE of the other person.) So you can easily debug
and work together on something. You also don't even have to leave your
browser to deploy your code.

Plone doesn't run on the OpenShift VM yet because of a LibXML
problem. But you can also bring your own server. So Jan used an Amazon
EC2 instance for his VM. The Plone Unified installer ran fine
there. He can just open and edit the files (e.g. the buildout
configuration files) from his browser.

Cloud9 is very proud of their code completion. It should become
available for Python as well in the next few months.

Since Cloud9 in open source, you can fork the
[GitHub repository](https://github.com/ajaxorg/cloud9) and contribute
if you want to. Or join Cloud9 since they are hiring.
