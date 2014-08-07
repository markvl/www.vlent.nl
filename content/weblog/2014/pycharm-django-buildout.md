---
title: Using PyCharm with Django in a Buildout
date: 2014-05-08 22:26:00
tags: [buildout, development, django, tools]
---

To introduce a coworker to our project and Django in general, I
suggested that he would try
[PyCharm](http://www.jetbrains.com/pycharm/), a Python IDE. One of the
(many) nice things of PyCharm is that you can easily jump to the place
where something is declared---ideal for exploring a project.

When you use for instance a
[virtualenv](https://virtualenv.pypa.io/en/latest/), PyCharm will
automatically detect which packages are installed. But PyCharm also
supports [buildout](http://www.buildout.org/en/latest/).

As the
[documentation](http://www.jetbrains.com/pycharm/webhelp/buildout-support.html)
rightfully claims, PyCharm can automatically detect the use of
buildout and enables support for it automatically. However, it defaults
to using the path from the ``bin/buildout`` script. This usually only
adds the setuptools and zc.buildout eggs, so it is of little use.

Assuming you are using the
[djangorecipe](https://pypi.python.org/pypi/djangorecipe/1.7) buildout
recipe, there is also a ``bin/django`` script available. And *that*
script includes the paths to all the packages you have specified in
your buildout.

To do this, go to the settings, search for "buildout" and point
PyCharm to the right script.

![PyCharm Buildout settings](/images/pycharm-buildout-settings.png "PyCharm Buildout settings")

Once you have done that, you can immediately see that code completion
works, but CTRL+click also takes you to the declarations inside
e.g. the Django package.

![PyCharm code completion in action](/images/pycharm-buildout-completion.png "PyCharm code completion in action")
