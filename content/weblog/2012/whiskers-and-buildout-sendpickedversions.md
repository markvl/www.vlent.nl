---
title: Whiskers and buildout.sendpickedversions
slug: whiskers-and-buildoutsendpickedversions
date: 2012-04-27 14:01
tags: [devops, django, plone, tools]
---

Last year I participated in a
[deployment knowledge sharing session](/weblog/2011/06/20/deployment-knowledge-sharing-session/)
and I started implementing changes at my company pretty soon
after. The result is that we are using
[Puppet](http://puppetlabs.com/) for some parts of our server
configuration. We also added [Munin](http://munin-monitoring.org/) to
our monitoring toolset (and I used Puppet to deploy Munin and manage
its configuration). But an important piece that was still missing in
our setup was an overview of which packages we use in the buildouts of
our clients and more specifically which version each client uses.

Apparently I was not the only one that wanted to have such an
overview: [Jukka Ojaniemi](http://twitter.com/jukkao) created Whiskers
([PyPI](http://pypi.python.org/pypi/whiskers/),
[GitHub](http://github.com/pingviini/whiskers)) and released version
0.1 in December 2011. Whiskers is a Pyramid application and it is
intended to be used in combination with the buildout extension
buildout.sendpickedversions
([PyPI](http://pypi.python.org/pypi/buildout.sendpickedversions),
[GitHub](http://github.com/pingviini/buildout.sendpickedversions)).

Setting up Whiskers is very simple (see the
[Whiskers README](https://github.com/pingviini/whiskers#readme) for
details) and since the data is stored in an SQLite database there is
little infrastructure needed. The buildout side is even less work,
just only have to add the following:

    [buildout]
    ...
    extensions += buildout.sendpickedversions
    buildoutname = <buildout-name>
    whiskers-url = <whisker-server-url>/buildouts/add

And the result after modifying several buildout configurations is a
nice overview of which packages (and versions) are used by each
buildout.

![Buildout details](/images/edition1-whiskers-buildout-details.png
 "Buildout details")

But you can also view a package and see which versions are used in
which buildouts.

![Package details](/images/edition1-whiskers-package-details.png
 "Package details")

For the Edition1 Whiskers server, I wanted to change the CSS to make
the header and footer match our company colors and change the used
font. Perhaps Pyramid provides a solution to override static files
included in a package, but I chose to copy the `whiskers.css` file to
another directory, modify it and have Apache serve my file.

~~Note that currently Whiskers has some rough edges. For instance: not
all packages are registered properly. I am using a checkout of
[my fork](https://github.com/markvl/whiskers) for now until there is a
new release where this is fixed (yes, I issued a
[pull request](https://github.com/pingviini/whiskers/pull/2)).~~

~~The package view (which was shown in the second screenshot),
currently does not sort the versions and does not hide versions that
are not used by any buildout. I personally don't like that so I issued
[another pull request](https://github.com/pingviini/whiskers/pull/3) in
the hope it will be included in a next release.~~

Although Whiskers may not be perfect yet, I quite like it and am happy
that I finally took the time to set things up.

**Update (2012-04-28):** Both issues are solved in version 0.2. Which
means I can recommend Whiskers even more. :)
