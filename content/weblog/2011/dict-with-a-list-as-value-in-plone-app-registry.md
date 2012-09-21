---
title: Dict with a list as value in plone.app.registry
slug: dict-list-value-ploneappregistry
date: 2011-09-07 08:44
tags: [development, plone]
---

This article is a short example of how to use a list as a value of a
dict when using
[plone.app.registry](http://pypi.python.org/pypi/plone.app.registry). Perhaps
a similar example is already in the docs, but I could not find it when
I was looking for it. And since it took me some trial and error to get
it right, I figured I could just as well post my solution.

My goal is to be able to store something similar to this in the
registry:

    {u'foo': [u'one.html', 'two.html'],  u'bar': [u'three.html', u'four.html']}

My `registry.xml` file:

    <record name="my.package.example">
     <field type="plone.registry.field.Dict">
       <title>Verification filesnames</title>
       <key_type type="plone.registry.field.TextLine">
         <title>Key</title>
       </key_type>
       <value_type type="plone.registry.field.List">
         <title>Value list</title>
         <value_type type="plone.registry.field.TextLine">
           <title>Values</title>
         </value_type>
       </value_type>
     </field>
     <value purge="false" />
   </record>

Note the `<value>` tag. By adding it, you are sure that an empty dict is
already in place so you can manipulate its content straight away
(e.g. add items). This is what you will get when you leave out the
`<value>` tag, the record is None:

    >>> from zope.component import getUtility
    >>> from plone.registry.interfaces import IRegistry
    >>> registry = getUtility(IRegistry)
    >>> registry['my.package.example'][u'foo'] = [u'one.html', 'two.html']
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    TypeError: 'NoneType' object does not support item assignment

You may want to include the purge attribute on the `<value>` tag (like
the example), otherwise the dictionary might be reset to the values as
stored in your `registry.xml` file (e.g. when you reinstall the
product).

# plone.supermodel

You'll also want to make sure you are using
[plone.supermodel](http://pypi.python.org/pypi/plone.supermodel)
version 1.0b7 or later. That version adds support for serialization of
nested dicts/lists. If you don't, exporting/importing your values will
be messed up. For example, you will get this XML upon export:

    ...
    <value>
      <element key="foo">[u'one.html', 'two.html']</element>
    </value>
    ...

But what you want is this (plone.supermodel 1.0b7 and up):

    ...
    <value>
      <element key="foo">
        <element>one.html</element>
        <element>two.html</element>
      </element>
    </value>
    ...

Because the first version (plone.supermodel < 1.0b7) results in:

    >>> registry['my.package.example']
    {u'foo': [u'[', u'u', u"'", u'o', u'n', u'e', u'.', u'h', u't', u'm', u'l', u"'", u',', u' ', u"'", u't', u'w', u'o', u'.', u'h', u't', u'm', u'l', u"'", u']']}


While you actually want:

    >>> registry['my.package.example']
    {u'foo': [u'one.html', u'two.html']}

Again: use a recent version of plone.supermodel. The current version,
1.0.3, is the one I worked with.
