---
title: Delivering egg-based applications with zc.buildout, using a distributed model (Tarek Ziadé)
slug: delivering-egg-based-applications-with-zc.buildout-using-a-distributed-model-tarek-ziade
date: 2008-10-10 19:32
tags: [plone, ploneconf, ploneconf2008]
---

A talk about working with packages, zc.buildout and managing the
application lifecycle.

# Part 1: Working with packages

Distutils: builds and distributes a package, registers and uploads it
to PyPi. The standard in the whole Python community. It's not actively
developed however and there are features missing.

[Setuptools](http://peak.telecommunity.com/DevCenter/setuptools) sits
on top of distutils. It corrects some of the problems with
distutils. There is a simple dependencies mechanism, namespaces
packages and other nice stuff. Tarek encourages us to create source
distributions (python setup.py sdist) instead of eggs. Eggs can be
interesting for some use caes though, but in the Plone world, please
use source distributions. Another advantage of setuptools:if you
upload your package to PyPi, everyone can just run `easy_install
my_package` to get your software and install it.

Setuptools is the de facto standard in the Plone community. But it is
also broken since it inherits from distutils. The future of packaging
is unclear at the moment. There will be a
[sprint](http://www.openplans.org/projects/plone-conference-2008-dc/distribute)
about it though.

Problems with packaging:

1. PyPi is a single point of failure
2. Non open source packages cannot be but on PyPi
3. plone.org/products is "dying" since people put stuff in PyPi and
   'forget' to update the plone.org page.

Solutions:

1.  Make a PyPi mirror
2.  Run your own private PyPi
3.  Make plone.org/products PyPi compatible

Tared expanded on these three solutions:

## Make a PyPi mirror

Instead of creating a full mirror of PyPi , you can use
[collective.eggproxy](http://pypi.python.org/pypi/collective.eggproxy). When
using this proxy, it will give you the requested package from its
cache. If it isn't in the cache, it will download it from PyPi, give
it to you and store it in the cache for the next time. You can use it
in your buildout by using the index option:

    [buildout]
    ...
    index=http://my.mirror:8888

## Private PyPi

To have your own private PyPi, use
[PloneSoftwareCenter](http://plone.org/products/plonesoftwarecenter)
(PSC). This allows you to create your own egg repository. However,
there is a problem. The `~/.pypirc` file holds username and password
for PyPi. But having your private PyPi will mess things up: you'll
need several accounts to upload to both PyPi and your private
repository.

In Python 2.6 you have the `register` and `upload` commands. For
Python 2.5 and 2.4 you'll need to use
[collective.dist](http://pypi.python.org/pypi/collective.dist). This
package gives the `mregister` and `mupload` commands and you can now
store multiple accounts:

    [distutils]
    index-servers =
        pypi
        another

    [pypi]
    username:user
    password:password

    [another]
    repository:http://another.pypi.server
    username:user2
    password:password2

To make your private PyPi really private you can put the packages in a
password protected directory. To be able to use them in buildout, you
can use
[lovely.buildouthttp](http://pypi.python.org/pypi/lovely.buildouthttp/)
to access them.

## plone.org/products

By using PSC on plone.org it's easy to update the product pages on
plone.org. But you get even more: there is a rating system available,
which PyPi doens't have. When the new site is live, we will have a
PyPi compatible products section! :)

# Part 2: Working with zc.buildout (reminders)

*Since Clayton Parker already had a talk about buildout this morning, Tarek just gave some reminders.*

Instead of needing 5 hours to get up-and-running (download Zope,
Plone, install the right products in the right version, etc.), you can
start working within 5 minutes.

The main reason for creating zc.buildout wasn't this efficiency issue
however. In 2005 Zope was a big monolithinc package. Now, Zope is
eggified and there are over 100 packages. And since you don't want to
install all those packages manually, a solution was needed. Enter
zc.buildout.

Another advantage is that zc.buildout creates an isolated
environment. You don't need to install all the Zope and Plone packages
system wide. This also proves to be a problem: you've got packages all
over the place. If something needs to be fixed on a production server
for instance, you need to visit several locations.

Best practices for using zc.buildout:

1. Use the same layout for all your projects.
2. Make sure all developers have the same environment.
3. Use one `.cfg` file per target (development, production, etc.).

## Same layout

[collective.releaser](http://pypi.python.org/pypi/collective.releaser)
provides a paste script which will give you a default layout for the
project.

## Same environment

Windows developers/deployments are harder in this context. By using a
[package created by Tarek](http://tarekziade.wordpress.com/2008/01/20/an-installer-for-a-buildout-ready-windows) you
can easily install the necessary stuff under Windows.

## One .cfg per target

Suggestion:

- `buildout.cfg`
- `dev.cfg` (extends `buildout.cfg`)
- `prod.cfg` (extends `buildout.cfg`)

[At Zest we use [another setup](http://reinout.vanrees.org/weblog/versions-buildout)
by the way.]

# Part 3: Application lifecycle

Once you are done developing, run buildout on the target platform
(Windows, 64-bit Linux, whatever). Turn on the offline mode and create
an archive of your buildout. Now you can use the archive and get your
buildout without having to use the network.

Besides setting up the project,
[collective.releaser](http://pypi.python.org/pypi/collective.releaser)
also provides help for releasing packages. You can add a
`release-command` and `release-packages` variables in your `.pypirc` to
get it working. collective.releaser does make a lot of assumptions
(e.g. that subversion is used). Releasing the project can also be
accomplished with collective.releaser via e.g. the `project_release`
command.
