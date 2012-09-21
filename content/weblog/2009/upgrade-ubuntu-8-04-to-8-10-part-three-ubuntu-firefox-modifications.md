---
title: "Upgrade Ubuntu 8.04 to 8.10, part three: Ubuntu Firefox Modifications"
slug: upgrade-ubuntu-8.04-to-8.10-part-three-ubuntu-firefox-modifications
date: 2009-02-24 12:15
tags: [ubuntu]
---

After the upgrade to Intrepid the web developer Firefox add-on didn't
show it's toolbar anymore.

To my surprise I could not find the toolbar of the
[web developer add-on](https://addons.mozilla.org/en-US/firefox/addon/60)
anymore when I wanted to debug a site. Some experimenting with
disabling add-ons didn't indicate which combination of add-ons
resulted in the problem.

Next attempt: use a new profile, install Web Developer and then add
the other extensions one by one. This lead me to believe the
[Tab Mix Plus add-on](https://addons.mozilla.org/en-US/firefox/addon/1122)
was the one to blame. However, I really, really like that extension!

Using Google once again, I finally stumbled upon
[Bug \#281348](https://bugs.launchpad.net/bugs/281348) which revealed
the real problem: the Ubuntu Firefox Modifications add-on (from the
ubufox package). Disabling this add-on didn't immediately result in
the return of the toolbar though. I had to remove the "localstore.rdf"
file from my profile (located in `~/.mozilla/firefox/xkq1i1qg.default`
in my case) and restart Firefox as well. Another solution may be to
use a package for Intrepid which contains the fix (see
[this comment on the bug report](https://bugs.launchpad.net/ubuntu/intrepid/+source/ubufox/+bug/281348/comments/32)).
