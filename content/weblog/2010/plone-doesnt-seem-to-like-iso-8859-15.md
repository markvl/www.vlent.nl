---
title: Plone doesn't seem to like ISO-8859-15
slug: plone-doesnt-seem-iso-8859-15
date: 2010-11-16 13:41
tags: [development, plone]
---

After migrating a Plone 2.5 site to Plone 3, I got a
`UnicodeEncodeError` when viewing the site.

Apparently the site was configured to use
[ISO-8859-15](http://en.wikipedia.org/wiki/ISO/IEC_8859-15) as the
default character set. However, `plone.app.contentmenu.menu` contains
a class `FactorySubMenuItem` and the title property contains an
[ellipsis](http://en.wikipedia.org/wiki/Ellipsis) as unicode
character:

    _(u'label_add_new_item', default=u'Add new\u2026')

Rendering a page resulted in this error:

    Traceback (innermost last):
      Module ZPublisher.Publish, line 122, in publish
      Module ZServer.HTTPResponse, line 262, in setBody
      Module ZPublisher.HTTPResponse, line 327, in setBody
      Module ZPublisher.HTTPResponse, line 482, in _encode_unicode
      Module encodings.iso8859_15, line 18, in encode
    UnicodeEncodeError: 'charmap' codec can't encode character u'\u2026' in position 10551: character maps to <undefined>


This 'problem' exist at least in version 1.1.7 and 2.0.1 of
`plone.app.contentmenu` (and thus at least Plone 3.3.5 and 4.0.1).

Switching the encoding to [UTF-8](http://en.wikipedia.org/wiki/Utf-8)
solved the problem. (I also had to clear and rebuild the catalog by
the way, a good tip from
[Maurits van Rees](http://maurits.vanrees.org/).) The funny thing is
that the Plone migration set the default language from Dutch to
English. Otherwise I would not even have noticed this issue: the
translation for the `label_add_new_item` does not contain the
ellipsis.

I cannot directly come up with a good reason to **not** use UTF-8 as
the default character set for a Plone site. If you do know a reason,
please leave a comment, I'd love to hear about it! Either way: beware
of this issue.
