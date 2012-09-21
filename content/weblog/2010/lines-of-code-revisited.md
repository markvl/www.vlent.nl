---
title: Lines of code revisited
slug: lines-code-revisited
date: 2010-05-31 22:20
tags: [django, plone, vlent.nl]
---

After [a comment](http://twitter.com/HammerToe/status/15102276578) by
Matt Hamilton on Twitter about the lines of code in my website project
I listed in
[my previous weblog entry](/weblog/2010/05/30/switch-django/), I
decided to dive in a bit deeper.

First of all, I think I should start by explaining better **what** I
measured. Both my Plone website and the current Django site are
managed via [buildout](http://www.buildout.org/). So when I wanted to
count the line numbers of the files under source control, I started by
checking out the buildout, and making sure there were no files related
to the version control system (.git or .svn directories). Then I
simply ran "``find . | xargs wc -l``" from the buildout directory.

So what I'm counting here is, in the case of the Plone site, the stuff
needed for the buildout and my own products to customize the way Plone
or installed add-ons behave or look like (basically a policy and theme
product). In case of Django that translates in applications that
provide the blogging functionality, configuration of the Django
project, the templates and CSS and, again, buildout related files. In
both cases I've removed unneeded files (like ``HISTORY.txt``,
``LICENSE.txt``, et cetera) and stuff I didn't use anymore.

The score now:

<table>
  <thead>
    <tr>
      <th> </th>
      <th>Plone</th>
      <th>Django</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Files</td>
      <td class="tabular-number">98</td>
      <td class="tabular-number">83</td>
    </tr>
    <tr>
      <td>Lines of code</td>
      <td class="tabular-number">1927</td>
      <td class="tabular-number">2234</td>
    </tr>
  </tbody>
</table>

Wow I didn't see that coming. So first of all there apparently was was
more cruft in the custom code for my Plone site than I figured. And in
Django I need more custom code to end up with only the functionality I
actually used.

That last conclusion isn't surprising actually: I decided to build the
blogging related code myself on top of Django, instead of reusing a
ready-made application.

So my conclusion now is that Matt's comment was an understatement: I
wrote *more* code and ended up with less...
