---
title: Sending emails with embedded images in Django
date: 2014-01-15 21:53
tags: [django]
---

Django offers useful classes to easily send email. It is also easy to
add attachments to emails. I *did* have to puzzle a bit to get
embedded images working. This article describes the way I do it
now. I will first describe the most important elements and then I will
show a more complete example.

# The elements

Since I send a plain text and HTML version of the email, I use the
`EmailMultiAlternatives` class:

    msg = EmailMultiAlternatives(subject, text_content,
                                 sender, [to_mail])

The images are included as attachments. We do not use the
`attach_file` method because we want to set the `Content-ID`
header. This way we can refer to the image by that ID in the template.

    for f in ['logo.png', 'logo-footer.png']:
        fp = open(os.path.join(os.path.dirname(__file__), f), 'rb')
        msg_img = MIMEImage(fp.read())
        fp.close()
        msg_img.add_header('Content-ID', '<{}>'.format(f))
        msg.attach(msg_img)

As far as I have seen, the images can only actually be included if the
content type of the mail is correctly set. By default, the content
type is set to “`multipart/alternative`”. But this resulted in the
images just being displayed as attachments. What I needed was to set
the content type to “`multipart/related`”:

    msg.mixed_subtype = 'related'

(This is the thing that took the most time to figure out and triggered
me to write this article so I would not have to figure it out again in
the future. It also caused me to read up on multipart subtypes, see
e.g. the [Wikipedia article on MIME](http://en.wikipedia.org/wiki/MIME#Multipart_subtypes)
or [RFC 2046](http://tools.ietf.org/html/rfc2046#section-5.1) and
[RFC 2387](http://tools.ietf.org/html/rfc2387).)


# Complete example

Combining all these elements results in the following code:

    # Do these imports at the top of the module.
    import os
    from django.core.mail import EmailMultiAlternatives
    from django.template.loader import render_to_string
    from email.MIMEImage import MIMEImage

    # You probably want all the following code in a function or method.
    # You also need to set subject, sender and to_mail yourself.
    html_content = render_to_string('foo.html', context)
    text_content = render_to_string('foo.txt', context)
    msg = EmailMultiAlternatives(subject, text_content,
                                 sender, [to_mail])

    msg.attach_alternative(html_content, "text/html")

    msg.mixed_subtype = 'related'

    for f in ['img1.png', 'img2.png']:
        fp = open(os.path.join(os.path.dirname(__file__), f), 'rb')
        msg_img = MIMEImage(fp.read())
        fp.close()
        msg_img.add_header('Content-ID', '<{}>'.format(f))
        msg.attach(msg_img)

    msg.send()

Now you can use “`<img src="cid:img1.png">`” in your template. The
result should be that the email client shows the image embedded in the
mail at the place of the `img` element and not as an attachment.

# Result

Sending an email results in something like this:

    Content-Type: multipart/related; boundary="===============0527806758=="
    MIME-Version: 1.0
    Subject: ...
    From: ...
    To: ...
    Date: Tue, 14 Jan 2014 10:07:57 -0000
    Message-ID: <20140114100757.32546.81939@...>

    --===============0527806758==
    Content-Type: multipart/alternative; boundary="===============1211323952=="
    MIME-Version: 1.0

    --===============1211323952==
    Content-Type: text/plain; charset="utf-8"
    MIME-Version: 1.0
    Content-Transfer-Encoding: 7bit

    ...
    --===============1211323952==
    Content-Type: text/html; charset="utf-8"
    MIME-Version: 1.0
    Content-Transfer-Encoding: 7bit

    ...
    --===============1211323952==--
    --===============0527806758==
    Content-Type: image/png
    MIME-Version: 1.0
    Content-Transfer-Encoding: base64
    Content-ID: <logo.png>

    ...
    --===============0527806758==--

As you can see, the email consists of two parts: the body---which
itself consists of two parts (the plain text version and HTML
alternative)---and the related image.

# Improvements

Given the name of the class (`EmailMultiAlternatives`), the
`alternative` multipart subtype is logical. A better solution would
thus be to create an `EmailMultiRelated` class which has the proper
subtype from the get-go. And perhaps even has nice methods to attach
files with a `Content-ID` header.

As a matter of fact, there are a couple of snippets over on
[djangosnippets.org](https://djangosnippets.org/)
(e.g. [snippet 2215](https://djangosnippets.org/snippets/2215/)) that
do exactly that. I haven't tried any of these since they are overkill
for my project (for now), but they may prove to be more useful than my
code.
