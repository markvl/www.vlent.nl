---
title: "Deliverance: Theming Decoupled (Ian Bicking)"
slug: deliverance-theming-decoupled-ian-bicking
date: 2008-10-09 21:23
tags: [css, html, plone, ploneconf, ploneconf2008]
---

Deliverance can be used to theme a site without having to have any
knowlegde of Plone.

After
[installing Deliverance](http://deliverance.openplans.org/quickstart.html),
you can use paster to create a Deliverance project. Deliverance uses
"rules" to fetch HTML from a source and place it in the theme you
create. The source site doesn't have to be a Plone site by the way. It
can also be e.g. a PHP site or even a static site. As long as there is
HTML to process.

Deliverance is taking the resources (like the CSS files) from the
source and the theme itself and combines them. This makes the Kupu
editor work for example, but it can also result in strange situations
where the styles clash. The HTTP headers of the main content, like the
last modified header, are (almost) forwarded unchanged. So caching
with Squid is still possible.

Deliverance is, however, limited to modifying the HTML it recieved. It
doesn't know anything about the content. Reordering is possible,
hiding certain elements is also possible. Still, you regularly have to
dive into the underlying framework (Plone) to change the end result.

See the [Deliverance documentation](http://deliverance.openplans.org/)
for more information.
