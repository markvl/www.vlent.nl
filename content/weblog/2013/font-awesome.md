---
title: Font Awesome to PNG
date: 2013-10-27 17:09
tags: [development, python]
---

A site I'm working on uses
[Font Awesome](http://fontawesome.io/). Font Awesome is an iconic font
designed for use with
[Twitter Bootstrap](http://twitter.github.com/bootstrap/) and
currently (version 4.0.0) includes 370 icons. It is an easy to use and
nice icon font. But I needed `PNG` files of the icons so I could use
the same icons in a different system.

Enter
[Font Awesome to PNG](https://github.com/odyniec/font-awesome-to-png). It
is a Python script written by Michał Wojciechowski that allows you to do
exactly that: extract the icons from the Font Awesome `TTF` file and
save them as `PNG` files.

One example of how I used it to get a blue version of the comment
icon:

    ./font-awesome-to-png.py --color "#27a4cd" --size 48 comment

The result is a nice `PNG`:

![Comment icon](/images/comment.png "Comment icon")

A big thank you to Michał and everyone that contributed to this code.
