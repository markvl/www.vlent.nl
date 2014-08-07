---
title: Whiskers behind SSL
date: 2013-01-15 22:44
tags: [devops, django, https, plone, tools]
---

Since April 2012
[we are using Whiskers](/weblog/2012/04/27/whiskers-and-buildoutsendpickedversions/)
to store information about our Plone and Django buildouts. But when I
moved the setup behind SSL, the browser started to complain about
unsafe content.

While I could access [Whiskers](http://pypi.python.org/pypi/whiskers/)
via **https**://whiskers.example.com, references in the HTML to the
favicon and the CSS were to
**http**://whiskers.example.com/static/... And that either generates a
warning about unsafe content or the browser might decide to not load
the assets at all. And especially the missing CSS was severely
endangered the usability.

First I tried to solve this in Whiskers itself. But I soon discovered
that the `master.pt` template in Whiskers contains several
[static_url](http://docs.pylonsproject.org/projects/pyramid/en/latest/api/request.html#pyramid.request.Request.static_url)s,
for instance:

    <link rel="stylesheet" href="${request.static_url('whiskers:static/css/bootstrap.css')}" ... />
    <link rel="stylesheet" href="${request.static_url('whiskers:static/whiskers.css')}" ... />

And those resolved to **http**://whiskers.example.com/static/... so I
had to convince Whiskers (or actually Pyramid) that we were using
SSL. As a result my next attempts involved changing the Apache
configuration. But after trying several options I could not get it
working (possibly also due to an older version of Apache).

So I left the configuration unchanged:

    <VirtualHost <ip>:443>
        ... basic stuff about the server name, logs and SSL certificates ...

        RewriteEngine on
        ProxyPreserveHost on

        # We use a custom CSS file.
        Alias /static/whiskers.css /var/www/whiskers/static/whiskers.css
        RewriteRule ^/static/whiskers.css - [L]

        RewriteRule ^(.*) http://127.0.0.1:6543$1 [P]

        <Location />
                AuthName "Whiskers"
                AuthType Basic
                AuthUserFile /path/to/htpasswd
                require user spam eggs ham
        </Location>
        <Location /buildouts/add>
                Satisfy Any
        </Location>
    </VirtualHost>


# Waitress

After stumbling on a link to
[a part of the Waitress documentation](https://github.com/Pylons/waitress/blob/master/docs/index.rst#using-behind-a-reverse-proxy)
I decided to try a different approach. My `production.ini` was
basically a copy from the
[example on GitHub](https://raw.github.com/pingviini/whiskers/master/production.ini)
and it contained this section:

    [server:main]
    use = egg:Paste#http
    host = 0.0.0.0
    port = 6543

I installed [Waitress](http://pypi.python.org/pypi/waitress/) in my
[virtualenv](http://pypi.python.org/pypi/virtualenv/) and replaced the
above section by this:

    [server:main]
    use = egg:waitress#main
    host = 0.0.0.0
    port = 6543
    url_scheme = https

And now the CSS is properly loaded!

I don't know if there are easier/better ways to solve this, but this
works fine for us.
