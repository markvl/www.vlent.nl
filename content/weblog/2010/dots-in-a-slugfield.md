---
title: Dots in a SlugField
slug: dots-slugfield
date: 2010-07-19 10:31
tags: [development, django, vlent.nl]
---

When migrating from Plone to Django, I had problems with editing
weblog entries with a dot in the url. Apparently Django doesn't allow
dots in a SlugField. Here's how I solved it.

First a bit of background information. My previous site was in Plone
and I had a number of weblog entries with a dot in the URL. I did not
want to change those URLs but I also wanted to be able to edit the
weblog entries.

The biggest problem I had, was getting the SlugField being validated
if there was a dot in it. There's an
[old ticket (\#5368)](http://code.djangoproject.com/ticket/5368) where
this is discussed, but it has been closed as "wontfix." The
[last comment](http://code.djangoproject.com/ticket/5368#comment:9)
pointed me in the right direction:

> Slug fields are for a particular style of string. Underneath,
> though, they are just character fields with a validator. So if you
> want different validation requirements, just use a CharField and
> your own validator.

However, instead of using a CharField, I chose to create my own
SlugField (`MySlugField`). This subclasses the Django SlugField but
has a modified validator. In other words, my admin.py looks very
similar to this:

    import re
    from django.contrib import admin
    from django.core.validators import RegexValidator
    from django.forms.fields import SlugField
    from django.forms.models import ModelForm

    from blog.models import BlogEntry


    slug_re = re.compile(r'^[-\w.]+$')
    validate_slug = RegexValidator(slug_re,
        u"Enter a valid 'slug' consisting of letters, numbers, underscores, "
        u"dots or hyphens.", 'invalid')


    class MySlugField(SlugField):
        """A custom field where dots *are* allowed in the slug.
        This is needed for backwards compatibility with my Plone weblog items.
        """
        default_error_messages = {
            'invalid': u"Enter a valid 'slug' consisting of letters, numbers, "
                       u"underscores, dots or hyphens.",
        }
        default_validators = [validate_slug]


    class BlogEntryForm(ModelForm):
        slug = MySlugField()

        class Meta:
            model = BlogEntry


    class BlogEntryAdmin(admin.ModelAdmin):
        form = BlogEntryForm
        prepopulated_fields = {'slug': ['title']}

    admin.site.register(BlogEntry, BlogEntryAdmin)

Now SlugFields with dots can just be saved. Making sure they can also
be retrieved is easy. All you need to do is change `(?P<slug>[-\w]+)` in
your URL pattern with `(?P<slug>[-\w.]+)`.

(Note that by default dots are still filtered out by the script that
prepopulates the SlugField. That's okay for me: I only did this for
the old entries and can still insert the dot manually if I really want
to.)
