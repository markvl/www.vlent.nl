---
title: Glances
date: 2013-04-10 11:45
tags: [devops, python, tools]
---

Since I keep forgetting the name of this monitoring tool, I decided to
create an article so I can jog my memory more easily.

To get some basic information about your system
[top](http://en.wikipedia.org/wiki/Top_(software)) is a very useful
tool. But sometimes you need a little bit more.

If that is the case, you may want to check out
[Glances](https://github.com/nicolargo/glances). Here's an example of
Glances in action on my virtual machine:

![Glances example](/images/glances.png "Glances example")

Besides the basics (like CPU usage, load, memory usage) it also
displays information like network usage and disk I/O. And incidentally
Glances is written in Python.
