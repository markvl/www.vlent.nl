---
title: Merge a separate Git repository into an existing one
date: 2013-11-02 15:35
tags: [development, git]
---

When I started on a project it seemed to make sense to put a part of
the project in a separate Git repository. In hindsight that wasn't
such a smart move. Here's how I fixed it.

# The old situation

In the old situation I had two Git repositories: `<project>` and
`<package>`. In this case `<project>` was the project repository and
`<package>` contained only one part of it. (For those interested:
`<package>` is a Python package which I included into the project
using [mr.developer](https://pypi.python.org/pypi/mr.developer/).) A
simplified version of the situation looks like this:

    <project>
    ├── bootstrap.py
    ├── buildout.cfg
    └── src
        └── <package>

For several reasons I wanted to merge the `<package>` repository into
the `<project>` repository in the `src/package` path.

There are several ways to approach this. I wanted to end up in a
situation where in my day to day work I would not notice that the two
repositories were separate up until a certain point.

# What I did *not* do

At first I tried the approach outlined by Jason Karns in his article
[Merge Two Git Repositories Into One](http://jasonkarns.com/blog/merge-two-git-repositories-into-one/). That
is, I did not create a new empty repository to merge the two existing
repositories in. I just merged one existing repository into the other,
essentially only doing the second set of steps he described.

After I finished, I discovered that I could not easily use "`git log`"
to see the history of a file. Sure, I could use the "`--follow`" option
but that only works for a single file---not a complete
directory. Apparently this is caused by the "`git read-tree`" step. And
although
[you can fix this](http://stackoverflow.com/a/19402332/122661), I
wanted to avoid the situation.

In his article
[Merge Git Repositories and Preserve Commit History](http://scottwb.com/blog/2012/07/14/merge-git-repositories-and-preseve-commit-history/),
Scott W. Bradley describes a way to do the merge without using the
"`git read-tree`" command. However, the result is similar due to the
"`git mv`" step that is in there.

# The method I used

What I wanted apparently was a bit more complex. As a result the
process is also a little more complex. Thankfully I could combine the
previously mentioned articles with a
[helpful answer on Stack Overflow](http://stackoverflow.com/a/13060513/122661). This
resulted in the following 'recipe':

First clone the `<package>` repository and go to that directory:

    $ git clone ssh://<package-repo> /tmp/package
    $ cd /tmp/package

Just to be sure we do not commit something in the original repo,
remove the remote:

    $ git remote rm origin

Then use "`git filter-branch`" to rewrite the existing commits so that
the files are already in the right directory (`src/package` in my case):

    $ git filter-branch --index-filter \
          'git ls-files -s | sed "s-\t\"*-&src\/package/-" |
           GIT_INDEX_FILE=$GIT_INDEX_FILE.new \
           git update-index --index-info &&
           mv "$GIT_INDEX_FILE.new" "$GIT_INDEX_FILE"
          ' HEAD

(Note that
[according to Frederik](http://stackoverflow.com/questions/13060356/git-log-shows-very-little-after-doing-a-read-tree-merge/13060513#comment44550628_13060513)
you have to replace the `\t` in the `sed` command with `Ctrl-V + tab` when
using OS X.)

You can now verify that everything is still all-right, the history is
preserved and all files are located in the new directory.

Now make a fresh clone of the `<project>` repo:

    $ git clone ssh://<project-repo> /tmp/project
    $ cd /tmp/project

Add the `<package>` clone as a remote:

    $ git remote add -f package /tmp/package

Next, merge the new remote:

    $ git merge --allow-unrelated-histories package/master

(Updated on 2017-05-03 to add `--allow-unrelated-histories`, which is
needed since Git 2.9. Thanks to Josef, Maurits and Duncan for pointing
this out.)

Cleanup time: you can remove the temporary `<package>` remote:

    $ git remote rm package

By now all code should be in the same place as it was before we
started, but now it's in a single repository. Now would be a nice time
to run your tests to verify that everything went well.

If everything checks out, don't forget to push the result to the
`<project>` repository. (What you do with the `<package>` repository
is up to you. I would probably remove it.)
