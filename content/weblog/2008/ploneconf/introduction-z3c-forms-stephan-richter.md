---
title: Introduction Z3C Forms (Stephan Richter)
slug: introduction-z3c-forms-stephan-richter
date: 2008-10-10 16:19
tags: [plone, ploneconf, ploneconf2008]
---

Mastering the bureaucracy perfectly.

Stephan Richter took over from Kamon Ayeva. Due to the large group
attending, Stephan gave a talk instead of a tutorial.

Writing forms and form handlers is labourous. You have to do the same
things over and over again. Schemas/Fields can be used to generate
forms. Z3c.form was initially created to overcome formlib
limitations. And while formlib isn't actively developed at the moment,
there is an active community around z3c.form. The best ways to learn
about it are:

-   Read the extensive documentation (409Kb, about 400 pages)
-   Install, run and study [z3c.formdemo](http://pypi.python.org/pypi/z3c.formdemo)

To get the dictionary straight: a **form** is a presentation
component; it is not a full page. It uses (form) fields and widgets to
render a form, defines buttons that generate form actions and commonly
there is a template for layout.

(Form) **fields** represent small units of data (see
z3c.form.field). They wrap the Zope Schema fields and extend them with
form-specific information (like name prefixes, editability). Form
fields are communicators between the widget and the Python object.

A **widget** represents an input method in a particular UI (e.g. a
"text" input field in HTML forms). See z3c.form.widget and
z3c.form.browser. Modes determine whether a display, edit or hidden
widget is displayed. Related to widgets are:

- converters (internal Python representation -\> string representation
  and the other way around),
- validators (validate the submitted input and raise ValidationErrors,
  which can be customized by the way, using ErrorViewSnippet), and
- data managers (to store the values).

What z3c.form can do and formlib cannot, is create custom attribute
values for several widget attributes. This allows for default values
quite easily.

**Buttons** define actions of a form (see z3c.form.button) and are a
simple extension to schema fields. The availability is determined by
conditions. A single form can have multiple sets of buttons.

Note that subclassing a button would also inherrit the base class
button manager. Since it's an inmutable, when changing this manager,
you change the manager for all buttons. By using .extends() we can
prevent this, since we get a copy of the base class.

**Actions** are the widgets for buttons. Handlers define a set of
instructions when an action is called, i.e. the button is
clicked. These handlers can be registered for specific buttons or
types of buttons. Handlers are declared by high-level decorators.

There are several form classes:

- BaseForm, for basic machinery.
- DisplayForm, for standard forms to display values. This saves all
  manual conversion work. This makes it really easy to display data in
  the same way as they are entered.
- Form, for basic machinery with buttons.
- AddForm, for standard add forms.
- EditForm, for standard edit forms.

The future (z3c.form 2.0):

- Integration of z3c.pt (so form generation is 2-3 times faster)
- New widgets:
   - TextLinesWidget, to edit a sequence of simple values in a text area to edit tuples or lists
   - MultiWidget, to manage a sequence of simple types
   - ObjectWidget, provides a simple way to edit Object fields

- Translations

Extensions:

- z3c.formjs, javascript and Ajax (see z3c.formjsdemo)
- z3c.formwidget.query, widget to query a large collection and select
  a value from the query results
- [plone.z3cform](http://pypi.python.org/pypi/plone.z3cform),
  integration of z3cform into CMF and Plone
- megrok.z3cform, integration of z3cform into Grok
- five.megrok.z3cform, five bridge of megrok.z3cform
- z3c.formext, soon to come. :)

Additional information:

- This talk: [http://svn.zope.org/z3c.talk/trunk/](http://svn.zope.org/z3c.talk/trunk/)
- [http://pypi.python.org/pypi/z3c.form](http://pypi.python.org/pypi/z3c.form)
