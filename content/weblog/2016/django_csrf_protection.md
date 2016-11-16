---
title: How does the Django Cross-site request forgery protection work?
date: 2016-11-16
tags: [django, security]
---

Dan Poirier wrote an article on the Caktus Group blog about common web
site security vulnerabilities. In it he talked about the CSRF
protection in Django. Although he is right about a CSRF token having
to be part of the POST request, this is not the entire story.

**It is _not_ my intention to claim that mister Poirier does not
know how the CSRF protection in Django works. I only want to present a
more complete version.**

First things first, for those of you that have not read the
[Dan Poiriers article](https://www.caktusgroup.com/blog/2016/11/10/common-web-site-vulnerabilities-Django-security/),
here's a short summary of the CSRF related parts.

Cross-site request forgery (CSRF or XSRF) is a type of attack where a
malicious site is trying to make your browser send requests to another
site in an attempt to leverage the permissions of the user---you. (For
more information and examples, check the original article or the
[OWASP page on CSRF](https://www.owasp.org/index.php/Cross-Site_Request_Forgery_(CSRF)).)



Besides making sure that GET requests do not change data the article
talks about the
[CSRF protection provided by Django](https://docs.djangoproject.com/en/dev/ref/csrf/). Specifically
it states the following (emphasis mine):

<blockquote cite="https://www.caktusgroup.com/blog/2016/11/10/common-web-site-vulnerabilities-Django-security/">
<p>
Django's protection is to always include a user-specific, unguessable
string as part of such requests, and reject any such request that
doesn't include it. This string is called the CSRF token. Any form on
a Django site that does a POST etc has to include it as one of the
submitted parameters. <strong>Since the malicious site doesn't know the token,
it cannot generate a malicious POST request that the Django site will
pay any attention to.</strong>
</p>
</blockquote>

This is where the author is not incorrect (the POST request indeed has
to include the CSRF token), but **this is only one half of the
mechanism**. The other half is a cookie that is set by the original
site where the user is logged in. Only when the server receives
**both** values from the browser (and they match) will the POST
request be valid. This is described as the "Double Submit Cookie"
defence in the
[Cross-Site Request Forgery (CSRF) Prevention Cheat Sheet](https://www.owasp.org/index.php/CSRF_Prevention_Cheat_Sheet#Double_Submit_Cookie)
by OWASP.


## Example

Here's an example with a very simple form
([source code on GitHub](https://github.com/markvl/csrf_example)). Let's
first request the form:

    $ curl -i http://localhost:8000/post_to_me/

The response will look something like this:

    HTTP/1.0 200 OK
    Date: Tue, 15 Nov 2016 20:25:58 GMT
    Server: WSGIServer/0.2 CPython/3.4.3
    Content-Type: text/html; charset=utf-8
    Vary: Cookie
    X-Frame-Options: SAMEORIGIN
    Set-Cookie:  csrftoken=wVFdNQ1Hz487w7yk2mVjre2qlsclXi99w2jEcGyvXorojDLd7jH09NGhmbavG3tx; expires=Tue, 14-Nov-2017 20:55:58 GMT; Max-Age=31449600; Path=/

    <!doctype html>
    <html>
      <body>
        <form action="/post_to_me/" method="post">
          <input type='hidden' name='csrfmiddlewaretoken' value='JBWuPGvKU54xW9YIwEIknst1azSkBmg3JIAVew2yipnOJFbBBBu1517SbiQuk7Ar' />
          <tr><th><label for="id_name">Name:</label></th><td><input id="id_name" name="name" type="text" required /></td></tr>
          <input type="submit" value="Post" />
        </form>
      </body>
    </html>

Note the `csrftoken` value in the `Set-Cookie` header. Also note the
`csrfmiddlewaretoken` value in the form in the body of the
response. We'll use these values in our examples where we send POST
requests.

First a demonstration that we can successfully post a value using both
the cookie and the value in the form (in the `--data` parameter):

    $ curl -s -D - -o /dev/null \
    -H 'Cookie: csrftoken=wVFdNQ1Hz487w7yk2mVjre2qlsclXi99w2jEcGyvXorojDLd7jH09NGhmbavG3tx' \
    --data 'csrfmiddlewaretoken=JBWuPGvKU54xW9YIwEIknst1azSkBmg3JIAVew2yipnOJFbBBBu1517SbiQuk7Ar&name=mark' \
    http://localhost:8000/post_to_me/

The response is a nice `200 OK`:

    HTTP/1.0 200 OK
    Date: Tue, 15 Nov 2016 20:30:35 GMT
    Server: WSGIServer/0.2 CPython/3.4.3
    X-Frame-Options: SAMEORIGIN
    Content-Type: text/html; charset=utf-8

If we do not send the cookie along, we expect that the POST request
will fail:

    $ curl -s -D - -o /dev/null \
    --data 'csrfmiddlewaretoken=JBWuPGvKU54xW9YIwEIknst1azSkBmg3JIAVew2yipnOJFbBBBu1517SbiQuk7Ar&name=mark' \
    http://localhost:8000/post_to_me/

And indeed the server responds with a `403 Forbidden` status:

    HTTP/1.0 403 Forbidden
    Date: Tue, 15 Nov 2016 20:32:47 GMT
    Server: WSGIServer/0.2 CPython/3.4.3
    X-Frame-Options: SAMEORIGIN
    Content-Type: text/html

We could try to include the cookie but leave out the value in the form
to check if the cookie alone is enough:

    curl -s -D - -o /dev/null \
    -H 'Cookie: csrftoken=wVFdNQ1Hz487w7yk2mVjre2qlsclXi99w2jEcGyvXorojDLd7jH09NGhmbavG3tx' \
    --data 'name=mark' \
    http://localhost:8000/post_to_me/

However, this has the same result:

    HTTP/1.0 403 Forbidden
    Date: Tue, 15 Nov 2016 20:33:35 GMT
    Server: WSGIServer/0.2 CPython/3.4.3
    X-Frame-Options: SAMEORIGIN
    Content-Type: text/html

As you can see Django requires both components to be present. The
actual value of the token is less relevant. Sure, it is "unguessable",
but that is (in my humble opinion) not the most relevant part. The
CSRF token is also not stored. Django could not care that much about
the actual value---as long as the value in the cookie matches the one
in the POST data, the token is considered valid.

To demonstrate that I can make up my own values if I want to (as
long as they are 32 or 64 characters in length):

    $ curl -s -D - -o /dev/null \
    -H 'Cookie: csrftoken= markmarkmarkmarkmarkmarkmarkmark' \
    --data 'csrfmiddlewaretoken=markmarkmarkmarkmarkmarkmarkmark&name=mark' \
    http://localhost:8000/post_to_me/

This succeeds:

    HTTP/1.0 200 OK
    Date: Tue, 15 Nov 2016 20:35:55 GMT
    Server: WSGIServer/0.2 CPython/3.4.3
    X-Frame-Options: SAMEORIGIN
    Content-Type: text/html; charset=utf-8

This example uses an older version of the CSRF token. As of Django
1.10 the CSRF form token value is salted and changed every
request. (For details, see
[this commit](https://github.com/django/django/commit/5112e65ef2df1dbb95ff83026b6a962fb2688661)
and the [related issue](https://code.djangoproject.com/ticket/20869).)
This does not change the mechanism behind the defence though.


## Why does this defence work?

Back to the attack. Why does it matter that the POST request has to
have matching tokens both via the cookie and the POST data?

Cookies are set for a specific domain. Your browser protects this in
two ways:

  - You cannot set a cookie for a different domain.
  - Cookies for one domain are not sent to another domain.

This defence against CSRF works because although the evil site _can_
force the browser to make a request to the site it wants to abuse, the
attacker can only manipulate the request and its data. The attacker
_cannot_ set, modify or even read a cookie for a different domain than
its own. As a result the attacker cannot determine or even guess which
CSRF token should be in the request and thus the request will fail.


Note that this is the protection chosen by Django. Other forms of
defence are possible. See the aforementioned
[Cross-Site Request Forgery (CSRF) Prevention Cheat Sheet](https://www.owasp.org/index.php/CSRF_Prevention_Cheat_Sheet)
for more information.

_As already stated at the top of the article, I do not want to imply
that mister Poirier does not know how the CSRF protection in Django
works; perhaps he decided to leave out some of these details to make
his article more succinct. Either way, in my opinion his article only
told half of the story with regards to CSRF protection. So I decided
to talk about the other half._
