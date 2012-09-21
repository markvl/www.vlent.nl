---
title: "RelStorage and plone.recipe.zope2instance: UnboundLocalError"
slug: relstorage-and-plonerecipezope2instance-unboundloc
date: 2010-09-23 13:22
tags: [development, plone]
---

Yesterday I was experimenting with RelStorage and ran into an error:
"UnboundLocalError: local variable 'blob_storage' referenced before
assignment."

Although I'm a bit ashamed to admit my mistake, I already made a fool
out of myself by opening
[a bug report](https://bugs.launchpad.net/collective.buildout/+bug/645100)
about it. So I figured I just as well might help out someone else with
a blog entry.

The cause of the error is pretty simple. I still had the `zeo-client`
option in my `[instance]` section set to true. The solution is thus
equally simple: just set it to false.
