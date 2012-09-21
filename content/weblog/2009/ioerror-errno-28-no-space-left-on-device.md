---
title: "IOError: [Errno 28] No space left on device"
slug: ioerror-errno-28-no-space-left-on-device
date: 2009-05-27 20:58
tags: [plone]
---

For the second time in the one month, I ran into this problem. Here's
how I solved it. (As a reminder for myself the next time I need it...)

During a migration of the Plone site of one of our customers, I ran
out of space on `/tmp`. Frustrating, especially if you've been waiting
for quite some time already. If you've ran into this problem or expect
that you will not have enough space in the tmp directory, start the
instance like this:

    $ TMPDIR=/path/to/alternative/tmp/dir bin/instance start

Now the temporary stuff will be written to
`/path/to/alternative/tmp/dir` instead of `/tmp`.

**Update (2009-05-30):**

After the comment by Wouter, I tried to include the alternative tmp
directory in the buildout configuration. I'm under the impression that
just adding the lines in the `[instance]` section doesn't work directly:
the `<buildout>/var/tmp` directory doesn't seem to be generated when running
"`bin/buildout`" and thus Zope doesn't use it. I solved this by using
the [ore.recipe.fs](http://pypi.python.org/pypi/ore.recipe.fs)
package:

    [parts]
        ...
        tmp

    [tmp]
    recipe = ore.recipe.fs:mkdir
    path = ${buildout:directory}/var/tmp

    [instance]
    ...
    environment-vars =
        TMP ${tmp:path}

If anyone knows a better way (Wouter?) please leave a comment...
