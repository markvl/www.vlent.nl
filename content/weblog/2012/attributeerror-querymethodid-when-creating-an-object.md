---
title: “AttributeError: queryMethodId” when creating an object
slug: attributeerror-querymethodid-when-creating-object
date: 2012-08-09 14:05
tags: [development, plone]
---

While working on a client project, I created an (Archetypes based)
content type with a text field. After adding a custom view as the
default view, I got an `AttributeError` when I tried to add a new
object.

Some details about the content type:

- It includes a `TextField` which uses the `RichWidget` (read: TinyMCE).
- I changed the `default_view` setting from `folder_listing` to `view`
  in the Generic Setup configuration file (`types/WikiPage.xml` in
  my case).

Whenever I tried to add a new object, I got the following traceback:

      ...
      Module zope.tal.talinterpreter, line 583, in do_setLocal_tal
      Module zope.tales.tales, line 696, in evaluate
       - URL: file:home/mark/eggs/Products.TinyMCE-1.2.11-py2.6.egg/Products/TinyMCE/skins/tinymce/tinymce_wysiwyg_support.pt
       - Line 6, Column 2
       - Expression: <PathExpr standard:u'object|here'>
       - Names:
          {'container': <PloneSite at /site>,
           ...
           'user': <PropertiedUser 'admin'>}
      Module zope.tales.expressions, line 217, in __call__
      Module Products.PageTemplates.Expressions, line 155, in _eval
      Module Products.PageTemplates.Expressions, line 117, in render
      Module Products.CMFDynamicViewFTI.browserdefault, line 76, in __call__
      Module Products.CMFPlone.PloneFolder, line 122, in __call__
    AttributeError: queryMethodId

If I removed the text field or set the default view back to
`folder_listing`, the error did not present itself.

To make a long story short: in the end it appears to be an issue with
Products.TinyMCE version 1.2.11. And since that version is included in
Plone 4.1.5, I spent quite some time figuring out why my new content
type didn't work while a similar content type in an older project
did. Figuring I had done something wrong, I did not immediately
realise that the older project was using Plone 4.1.4 (and thus an
older version of Products.TinyMCE that does *not* have this issue)...

**The solution:** pin Products.TinyMCE to version 1.2.12. Or you could
just use Plone 4.1.6 or 4.2, which both include the fixed version by
default.
