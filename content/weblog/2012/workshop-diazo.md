---
title: Workshop: Theming with Diazo
tags: [css, development, html, plone, xslt]
date: 2012-12-14 20:30
---

On Wednesday the 12th of December,
[Goldmund, Wyldebeast & Wunderliebe](http://www.goldmund-wyldebeast-wunderliebe.com/)
organised a Diazo workshop. Douwe van der Meij and Kim Chee Leong
introduced us to the wonderful world of theming Plone the easy way (my
words, not theirs). Since this workshop took a full day, this is not a
complete summary but a more an extended version of the notes I took
during the day.


# Introduction

Diazo is for (re)theming websites. Not just Plone sites, it works on
any technology. Diazo combines the HTML of the website---the
content---with the HTML of the theme provider---the theme---to deliver
a themed website.

With Diazo there is a natural separation between the HTML delivered by
the designer or frontend developer and the logic (calculations, data,
etc) which is usually handled by the backend developer. It adds an
additional level of abstraction to the stack. To put it differently:
Diazo offers an interface between the developers and the designers,
while keeping a clear separation of responsibility. Because the
developer does not have to transform the HTML from the designer into
([TAL](http://wiki.zope.org/ZPT/TAL)) templates, this also removes a
step from the process where normally errors can creep in.

Diazo can be put in front of your existing website; the technology
used for the website does not matter. The existing website is still
there. You can have the multiple designs for a single website at the
same time. You can even use Diazo to only apply the theme when you are
on a subsite.

Diazo uses XSLT but, theoretically, you do not have to write XSLT
yourself. Which is good because XSLT is hard to read. So if you do
write XSLT, don't forget to place comments so a month from now you
still understand what you wrote today.

To make the rules you have to write less complex and require as little
XSLT as necessary, you could change the Plone output so it delivers
what the Diazo theme expects. You can also create a theme that takes
the output of Plone into account so less transformation is required.

Speaking of those rules: for an overview of available rules and the
order in which they are processed (for instance `<drop />` is
executed before `<replace />`), see the
[Diazo documentation](http://docs.diazo.org/en/latest/).


# Tooling

The package
[plone.app.theming](http://pypi.python.org/pypi/plone.app.theming)
provides an interface to modify themes. It allows you to edit your
`rules.xml` file and the rest of the them from within Plone. By using
the inspectors you can also select elements in your theme and content
(Plone site) and have the editor create a rule for you. (From what
I've seen during the workshop you likely want to tweak the rule
somewhat but it's a starting point.)

It's possible to set hostnames that use the unthemed version of
the site in the advanced settings of the theming control panel. By
default `127.0.0.1` is listed there.


# Creating a theme

A Diazo theme expects a specific layout. Obviously you'll need to have
your theme: an HTML file (`index.html` for example) and accompanying
assets (CSS, JavaScript, images). Besides those files, you also need
to have the files `manifest.cfg`, `rules.xml` and an image with a
preview of the theme, `preview.png`.

An example of a `manifest.cfg` file:

    [theme]
    title = Demo Theme
    description = My first Diazo theme
    preview = preview.png

For details on the content of the `manifest.cfg` file, check out the
[manifest file section](http://pypi.python.org/pypi/plone.app.theming/#the-manifest-file)
plone.app.theming documentation.

A very basic `rules.xml` file to get started:

    <?xml version="1.0" encoding="UTF-8"?>
    <rules
        xmlns="http://namespaces.plone.org/diazo"
        xmlns:css="http://namespaces.plone.org/diazo/css"
        xmlns:xsl="http://www.w3.org/1999/XSL/Transform">

        <theme href="index.html" />

    </rules>

The `<theme href="..." />` line makes sure that the `index.html` file
from the theme is used. Otherwise you would still see the Plone theme.

Note that you can split up the rules into several files. For instance:

    <?xml version="1.0" encoding="UTF-8"?>
    <rules
        xmlns="http://namespaces.plone.org/diazo"
        xmlns:css="http://namespaces.plone.org/diazo/css"
        xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
        xmlns:xi="http://www.w3.org/2001/XInclude">

        <theme href="index.html" />

        <xi:include ref="rules_normal.xml" />

        <rules if-content="/html/head/title[.='foo']">
        	<xi:include ref="rules_foo.xml" />
        </rules>
    </rules>


To make the Plone site editable in the themed site, you need to add
the following to your rules:

    <after
    	css:theme-children="html head"
    	css:content="html head script"
    />

    <after
    	css:theme-children="html head"
    	css:content="html head base"
    />

Note that this only includes the JavaScript and the `<base />` element
from Plone. To actually show the edit bar, you'll need to add some
additional rules and also include some CSS in your theme to style it
properly.

You could also try to use
[plone.app.toolbar](http://pypi.python.org/pypi/plone.app.toolbar). But
note that currently (plone.app.toolbar 1.1 and plone.app.theming
1.1b1) there is a small user interface problem: the toolbar is on top of the
controls when you expanded the HTML mockup or unthemed content
inspector.

<figure>
  <img src="/images/theming-plain.png" alt="Inspecting the unthemed content without the Plone Toolbar">
  <figcaption>
    Inspecting the unthemed content <strong>without</strong> the Plone Toolbar
  </figcaption>
</figure>

If you do not have the Plone Toolbar installed, you can toggle the
source view and fullscreen mode of the inspector. But when the Plone Toolbar **is** installed, it overlaps
with these controls.

<figure>
  <img src="/images/theming-toolbar.png" alt="Inspecting the unthemed content without the Plone Toolbar">
  <figcaption>
    Inspecting the unthemed content <strong>with</strong> the Plone Toolbar
  </figcaption>
</figure>

As long as the page is long enough that you can scroll down, you can
do just that to reveal the controls again. (Since the controls scroll
with the page while the position of the toolbar is fixed, they show up
when you scroll on the page.)


# Summary

Diazo is a wrapper around XSLT. It provides a seamless integration to
(re)theme your website. It provides a higher level of abstraction, but
you can also use XSLT as a fallback.

Although you can use Diazo without Plone, there currently is only tooling
within Plone.


# My conclusion

This was my first introduction to Diazo. My initial reaction is that I
like the separation of concerns and responsibility between front- and
backend. I can also imagine that it is easier to work with other
parties that build the theme (HTML and CSS) and do not require
in-depth Plone knowledge.  I cannot yet judge on potential gains in
time when comparing the development of a Plone theme with building a
Diazo theme.

I am glad that you can edit the rules from within Plone and have the
inspectors to help you selecting the elements. At the same time I can
imagine that someone with more knowledge about Diazo, XSL and the
actual output of Plone (which isn't my expertise) rather just works on
file system with his/her editor.

There are also a few things that we at
[Edition1](http://www.edition1.nl) need to investigate and/or solve
before we can even think about using Diazo for every
[SwordFish](http://www.swordfish.nl) customer. For instance, we use
[collective.editskinswitcher](http://pypi.python.org/pypi/collective.editskinswitcher/)
combined with
[collective.lineage](http://pypi.python.org/pypi/collective.lineage/).
Our customers have a separate edit skin (with a preview of the content
as the visitors of the site will see it) and can select a theme per
child site. We'll have to see how we can replicate something similar
with Diazo, perhaps by using
[lineage.themeselection](http://pypi.python.org/pypi/lineage.themeselection/). That
is: assuming we want to keep this setup---the Plone Toolbar also looks
really nice!

Either way, I learnt a lot. So thanks Douwe, Kim Chee and Goldmund,
Wyldebeast & Wunderliebe for organising the workshop!
