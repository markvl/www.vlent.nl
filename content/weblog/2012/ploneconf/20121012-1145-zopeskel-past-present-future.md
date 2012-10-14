---
title: ZopeSkel - The past, present and future (Cris Ewing)
slug: zopeskel-past-present-and-future-cris-ewing
date: 2012-10-12 11:45
tags: [plone, ploneconf]
---

Cris is the maintainer of ZopeSkel for three years now. This is a
historical, non technical talk about ZopeSkel: where did it start and
where it is going.


# Beginning

We used to have ArchGenXML to generate code for us. But it only
created (Archetype) content types. This may have been the reason for
content type centric development. Later we needed eggs and other
scaffolding and this another tool.

On May 25th 2006, the first commit to ZopeSkel was made by Daniel
Nouri. From there it grew organically. Then local commands happened so
developers could enhance already created packages (for instance to
include portlets, content types). But most templates asked too many
questions.  And the descriptions around the question were not always
clear. Many templates looked similar so which one should your choose?
There was way too much (repeated!) code. That code was not updated
consistently so for example one template generated a `tests` directory
while another created a `tests.py` file.

To have local commands, your package has to depend on Paste. As a
result, the `Paste`, `PasteDeploy` and `PasteScript` eggs end up
*inside* your product. Even worse: if you are not careful, you can
accidentally add these packages to your version control system. This
is a big problem.


# ZopeSkel

On the
[No-Fun ZopeSkel BBQ Sprint](http://www.coactivate.org/projects/zopeskel-bbq-sprint/project-home)
in 2009 the question "Who is ZopeSkel for?" was answered. It was
decided that is it primarily a tool to help newcomers. For experienced
developers it's easier to start with empty structure and fill the
bits and pieces in themselves.

The outcome of the BBQ sprint was the "`bin/zopeskel`" script which:

   - hides the “`paste create -t`” command,
   - provides inline validation,
   - help for questions,
   - provides 'classes' of questions (easy, expert, all), and
   - gives good feedback while and after running.

However, the existing documentation was not cleaned up. As a result
people still use the "`paste create -t`" command and don't even know
what the "`zopeskel`" command is for.

Another outcome was that Cris became the official maintainer. And the
plan was formed to break up ZopeSkel (see the GitHub repository which
still contains a
[document](https://github.com/collective/ZopeSkel/blob/2.x-maintenance/SPLITTING-PROPOSAL.txt)
with the reasoning behind this).


# Templer

Work to break up started in early 2010. Templer provides templates in
packages of related functionality: a buildout package, Zope related
things, Plone related things, etc. But the commands for the user
should remain the same because there's so many documentation already
available.

Main difference between the old ZopeSkel and Templer: you cannot
create a shared structure in ZopeSkel. Templer provides structures,
which are similar to templates but they cannot be run individually and
only exist to be included in templates. For instance you can pull the
structure for the requested licence when creating a package.

The new ZopeSkel version of is a Templer application which bundles
stuff so you can use it as you were used to. You can just use
`easy_install` or `pip` to install ZopeSkel (your version of `pip`
needs to be new enough though).

 Or put it in your development
buildout by including a part which includes PasteScript and ZopeSkel, for example:

    parts =
       ...
       zopeskel

    [zopeskel]
    recipe = zc.recipe.egg
    eggs =
       PasteScript
       ZopeSkel


# What's next

   - Dexterity templates (underway)
   - Buildouts (unified with installers)
   - Theme templates (Diazo, traditional?)
   - Local commands for
    - viewlet
    - utility
    - z3c form
    - dexterity schema builder
    - ...

The
[next talk](/weblog/2012/10/12/jump-start-your-development-with-zopeskel-cris-ewing/)
teaches *how* to create templates, in the sprint following the
conference you can actually *create* templates.

Note that Templer currently still depends on Paster and uses Cheeta
templates. [Crushinator](https://github.com/jjmojojjmojo/Crushinator)
wants to solve these problems. The only dependency would be a package
for the templating language you want to use for your templates.
