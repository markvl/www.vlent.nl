---
title: Using a jQuery plugin in Django admin and getting a “$().foo is not a function” or “Object ... has no method foo” error?
slug: jquery-plugin-django-admin-foo-not-function-error-or-object-has-no-method-foo
date: 2011-11-07 21:52
tags: [development, django, jquery]
---

Are you using a jQuery plugin, for instance
[jQuery UI](http://jqueryui.com), to spice up the Django admin site?
Then you might get either an error like "foo is not a function"
([Firebug](http://getfirebug.com/)) or "Object ... has no method foo"
([Chrome Developer Tools](https://developer.chrome.com/devtools/index)). Confused
because `foo` should be defined in the plugin? Don't worry, the
solution is simple.

Actually, the reason *and* solution are in the
[Django admin site documentation](https://docs.djangoproject.com/en/dev/ref/contrib/admin/#modeladmin-media-definitions)
if you know where to look. The reason is this:

> Django's jQuery is namespaced as `django.jQuery`

This prevents collisions with other scripts or libraries. It also
prevents you from blindly using code you find on the internet. ;-)

Possible solutions are:

1.  Include your own copy of jQuery which does 'pollute' the global namespace.
2.  Make sure your plugin/code uses `django.jQuery` instead of just `$` or `jQuery`.
3.  Create a `jQuery` (or `$`) variable yourself.

As the documentation says, the benefit of the first option is that you
can use a different (newer) version of jQuery, if your want or need
to.

The second option might mean that you'll have to download the
development version of the plugin, change the code, and minify it
yourself.

I found the third option as
[an answer](http://stackoverflow.com/questions/7188563/django-admin-jquery-namespace/7250616#7250616)
to a question about the
[jQuery namespace in Django admin](http://stackoverflow.com/q/7188563/122661)
on Stack Overflow.

For what it's worth, I chose the second option and changed the custom
jQuery UI code I had downloaded. Your use case might benefit from
another solution...
