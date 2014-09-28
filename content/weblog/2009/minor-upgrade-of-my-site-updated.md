---
title: Minor upgrade of my site - updated
slug: minor-upgrade-of-my-site
date: 2009-05-16 22:51
tags: [blog, plone]
---

Time for another small update of my site. I changed some 'back office
stuff' and improved my blog. Apparently this also triggered some
changes in the RSS feed, resulting in older entries popping up again
on planet.plone.org. Sorry about that!

Today I made several changes to my site. Some changes are not visible
from the outside:

- I upgraded to Plone 3.2.2. This was mainly just to keep
  up-to-date. Nothing fancy here.
- I changed my editor to TinyMCE. I've worked with TinyMCE on a couple
  of other sites and I liked it better than Kupu.

Other changes *are* visible for the visitors:

- I'm experimenting with allowing comments on blog entries. Let's see
  if it'll get used without attracting too much spam...
- I also added a few portlets for my blog.

# Squall?

For the latter I added the
[QuillsEnabled](http://pypi.python.org/pypi/Products.QuillsEnabled)
product to the mix. I was thinking about creating a tag cloud and then
I read Jon Stahl's
[blog entry](http://jstahl.org/archives/2009/05/01/squall-perfect-plone-blogging-with-scrawl-quills/)
about a combination of QuillsEnabled and
[Scrawl](http://pypi.python.org/pypi/Products.Scrawl), which he dubbed
"Squall". His instructions were really clear and it worked quite well.

However, I did some custom work. For starters I decided to override
the `weblogentry_view` template. The template QuillsEnabled (or
actually [quills.app](http://pypi.python.org/pypi/quills.app)) uses
for displaying weblog entries does not show the images of the Scrawl
blog entries. I also modified the weblog view a bit by adding some
dashed lines between the entries to separate them more clearly.

Since I expect that my entries will be far from evenly distributed
between the topics, I decided to use a logarithmic scale for the tag
cloud instead of a linear one. Otherwise I expect that most topics
will have the lowest rank and one or two (for instance Plone) topics
have the highest rank, without ahything in between. Hopefully the tag
cloud a bit more valuable by fiddling with logarithms.

Well, that's it. Time to actually create some more content instead of
talking about the tools...

# Update

Sorry about the flood of messages I created on planet.plone.org! As
soon as I found out, I changed my RSS feed to no longer export the
modification date but the creation date. So when the modification date
of an entry gets changed in the future (either by editing or some
unexpected event) it won't show up in the feed again.
