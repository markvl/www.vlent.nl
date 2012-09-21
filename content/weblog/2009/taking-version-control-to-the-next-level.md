---
title: Taking version control to the next level
slug: taking-version-control-to-the-next-level
date: 2009-04-30 18:20
tags: [git, subversion]
---

After using Subversion for a couple of years, it's time for me to look
to the next generation of source control management systems.

# What's wrong with Subversion?

Before I start with this section: this isn't meant as a rant. Nor do I
want to call Subversion users
[ugly or stupid](http://www.youtube.com/watch?v=4XpnKHJAok8). Subversion
remains a great improvement compared to CVS. However, there are a
couple of things I miss in my daily work.

My main issue with Subversion is that I need the central repository on
the server. Not just to make commits, but also when I want to see what
happened in the past (review the logs or annotate a file with `svn
blame`). This can be a problem:

- As a consultant I travel frequently. Most of the times I take the
  train and try to get some work done. But whenever there is the need
  to access the repository, I'm dead in the water.
- The communication with the server can be slow. I don't care whether
  it's because I don't have a broadband connection at that moment or
  that I'm not the only one trying to connect to the server; I just
  don't want to wait too long for the result.
- The server could be unreachable. Coincidentally I've encountered
  this twice in the last period. Once the Apache configuration of our
  company server had a problem. The other time there was a hardware
  problem on the server where our client hosts his repository. In both
  cases I could not continue to work on the project.

Another annoyance of Subversion is that merging is required before you
commit. Say I'm working on file X. A coworker was also been working on
that file and committed after I updated, but before I was
finished. Now *before* I can commit, Subversion requires me to update
the file. This isn't a big problem if there are no conflicts, but if
there are, I can only commit my changes after I resolved them.

In other words: the changes as I intended them are never committed. I
first need to make more changes. The only way to prevent this is by
working on a branch. Then I can commit my changes and will only need
to resolve the conflicts if I decide to merge my branch back. But
while creating branches is easy in Subversion, merging is more a
pain. I know this is supposed to be better in Subversion 1.5, but I
still have to talk to version 1.4 repositories.

# Distributed version control systems to the rescue

For quite some time now, distributed version control systems (DVCS)
like Bazaar, Git and Mercurial are available. By design these systems
should take care of my number one problem with Subversion. At first
glance all three of the DVSCs I just mentioned seem suitable. But
which one is the best solution for me?

## Mercurial

[Mercurial](http://www.selenic.com/mercurial/wiki/) (or hg) is one of
the contestants. But since there is little to no chance of convincing
all my coworkers to switch from svn, I need to be able to talk to our
Subversion repository. There is set of scripts to do this, called
[hgsvn](http://pypi.python.org/pypi/hgsvn), but as the project page
states, it has the limitation that <q>there is no straightforward way to
push back changes to the SVN repository.</q>
[Other options](http://www.selenic.com/mercurial/wiki/index.cgi/WorkingWithSubversion)
also seem very laborious. This is a showstopper for me.

## Bazaar

On to the next candidate: [Bazaar](http://bazaar-vcs.org/) (or bzr)
does have a plugin to access Subversion repositories:
[bzr-svn](http://bazaar-vcs.org/BzrForeignBranches/Subversion). This
keeps Bazaar in the race.

## Git

The final DVCS I investigated was [Git](http://git-scm.com/). Git
natively supports bidirectional operation with Subversion.

## The decision

Although both Bazaar and Git seem to provide the most important
features I'll need, I chose Git. The first reason for no choosing
Bazaar was the way it handles
[branches and revision numbers](http://doc.bazaar-vcs.org/bzr.dev/en/user-guide/index.html#bazaar-zen). Although
I admit that I'm new to DVCS, if feels more natural to me to
consistently use globally unique revision numbers than having local
revision numbers and branches with
[their own view of history](http://doc.bazaar-vcs.org/bzr.dev/en/user-guide/index.html#each-branch-has-its-own-view-of-history).

The other reasons for selecting Git over Bazaar are speed and
repository size. Robert Fendt did recently did
[research](http://ldn.linuxfoundation.org/article/dvcs-round-one-system-rule-them-all-part-3)
and this confirms the results of
[other](http://www.infoq.com/articles/dvcs-guide)
[speed](http://laserjock.wordpress.com/2008/05/09/bzr-git-and-hg-performance-on-the-linux-tree/)
and
[repository size](http://vcscompare.blogspot.com/2008/06/git-mercurial-bazaar-repository-size.html)tests.

# Git: additional benefits

I have worked with Git for a little while now and there are some
additional benefits of it over Subversion:

- [Stashing changes](http://www.kernel.org/pub/software/scm/git/docs/git-stash.html)
  allows me to e.g. store local changes and go back to a clean working
  directory to work on something different for a while.
- Changing history may be a bit controversial in version control, but
  it can be very useful. It allows me to, for instance, squash commits
  while
  [merging](http://www.kernel.org/pub/software/scm/git/docs/git-merge.html),
  rearrange the order of commits with
  [rebase](http://www.kernel.org/pub/software/scm/git/docs/git-rebase.html)
  or add something to the previous commit with
  [`git-commit --amend`](http://www.kernel.org/pub/software/scm/git/docs/git-commit.html). Obviously
  you don't want to do this when you've already published your
  changes, but I has served me well already.
- I can create branches on my local repository to work on features or
  experiment, without bothering others with it.
- Committing is *really fast*. Although I still regularly push my
  changes to the svn repository, a 'normal' commit is blazing
  fast. While a commit used to be a pause in my work flow, commits now
  hardly have any impact. This makes it easy to commit more often and
  thus have commits do only one thing at a time.
- The last two benefits can be combined: since the commits are
  initially only local, I don't have to postpone committing until the
  code is in a workable state. I can for instance create a failing
  test, commit it and then continue to write the code to make it pass,
  without having to worry about coworkers running into the failing
  test.

(Note that other DVCSs also have (most of) these options. I'm only
comparing Git with Subversion here.)

All in all I am very enthusiastic! Granted: using Git is more complex
than Subversion and there were some problems I had to overcome in my
day-to-day work. (I'll talk about them in
[a next post](/weblog/2009/05/03/using-git-when-developing-plone-applications/).)
But the flexibility I gained! Incredible!
