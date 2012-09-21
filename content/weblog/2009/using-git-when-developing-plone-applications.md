---
title: Using Git when developing Plone applications
slug: using-git-when-developing-plone-applications
date: 2009-05-03 10:20
tags: [git, plone]
---

While I'm enthusiastic about Git, I still have to communicate with
Subversion repositories like the Plone Collective. I also like my
editor (Emacs) to help me interact with Git. In this blog entry I'll
explain how I setup my work environment.

Choosing a distributed version control system was
[step one](/weblog/taking-version-control-to-the-next-level). Step two
is incorporating it in my working life. This starts with retrieving
and storing the source code for the projects I'm working on.

# Git-svn

On of the reasons I chose Git was the "bidirectional flow of
changes" that will be necessary. The Git repository on my computer
will have to pull in the changes from the Subversion
repository. Likewise, I have to make my changes available for others
by pushing them back to the central repo.

Git-svn allows me to clone the necessary part of a Subversion
repository. For instance, to clone the buildout of project X I can
easily do:

    git svn clone https://svn..../projectX/buildout -s

This will clone (checkout) the project X buildout. By adding the "`-s`"
parameter I tell Git that the buildout directory has the standard
Subversion layout. (In other words: it contains trunk, branches and
tags directories.) There is plenty git-svn documentation out there, so
I won't describe it any further here. For more information see for
example
[the man page](http://www.kernel.org/pub/software/scm/git/docs/git-svn.html),
[blog](http://flavio.castelli.name/howto_use_git_with_svn)
[entries](http://www.viget.com/extend/effectively-using-git-with-subversion/)
or [google](http://www.google.com/search?q=git+svn).

# svn:externals

Okay, we've got the buildout. Now at [Zest](http://zestsoftware.nl/)
we basically have two type of buildout configurations. We either
include the products for the policy, theme, et cetera by using the
`svn:externals` property in the src directory, or we include those
products by using
[infrae.subversion](http://pypi.python.org/pypi/infrae.subversion).

I haven't found a proper solution for projects that use the latter
approach (other than restructuring the buildout that is). At the
moment I just use Subversion instead of Git. However if the project
collects all the products with the svn:externals property, there are
options...

Personally I use the `git-svn-clone-externals` script that can be
found on github. To be precise, I use the
[fork by Paul J Stevens](http://github.com/pjstevns/git-svn-clone-externals/tree/master). By
starting this script in the root directory of the Git repository (in
my case the buildout directory) it finds the products in `src` and
clones each of them.

Since I have a couple of buildouts with more than five products as
svn:externals, I got tired of manually making sure all changes in them
are committed *and* pushed back to the subversion
repository. Therefore I
[forked the git-svn-clone-externals repository](http://github.com/markvl/git-svn-clone-externals/tree/master)
and added two scripts that help me with this. By running the
`git-svn-externals-check` script in the src directory I can be pretty
sure everything is back in Subversion so my coworkers can access it.

# Emacs

I use Emacs to code, thus I also wanted to use it to help me with the
version control stuff. For Subversion I use
[`psvn.el`](http://www.xsteve.at/prg/emacs/psvn.el) and I was looking
for something similar. I first tried `git.el` (which comes with Git)
because the key bindings were similar. But although it got me started
quickly, it didn't feel quite right. For instance, I could not find a
way to work with staged changes. And this is a feature I really
started to like and use.

To make a long story short: I switched to
[Magit](http://philjackson.github.com/magit/) for the
moment. Although it took me a while to get used to the key bindings, I
actually really like it! It allows me to work with Git from Emacs and
the command line in a similar fashion. Actions taken in one of them do
not get in the way of the other.

I'm not completely settled yet, but I do love working with Git. I hope
to be able to use it on more and more projects.
