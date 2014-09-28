---
title: How I solved the comment spam for my Django site
slug: how-i-solved-comment-spam-my-django-site
date: 2010-08-30 18:33
tags: [blog, django]
---

After this website migrated from Plone to Django, the comment spammers
found my site more interesting. Instead of five spam comments a year,
I suddenly got the same amount per week. Although those comments were
never published (more on that later), it did annoy me. By no longer
displaying the comment form below the blog entries, the problem of the
spam seems to be solved. While this wasn't my goal, it *is* a nice
side effect.

It appears that the initial comment system (I'm using
[Django's comment framework](https://docs.djangoproject.com/en/1.6/ref/contrib/comments/))
was more interesting for comment spammers than the implementation of
comments on my old Plone site was. I think this is because there is a
URL field on the form now. And if the URL is present, the name of the
commenter becomes a link to that URL.

Since I saw that coming, I am using a similar setup as in
[Practical Django Projects](http://apress.com/book/view/9781590599969):
for blog entries older than 60 days I'm assuming comments are most
likely spam and they need to be moderated before they become
visible. For the other comments, I run them past Akismet. This seems
to work fine for now. (However, since I want to prevent false
positives to go unnoticed for too long, an email is sent for every
comment posted on the site. That is why comment spam is still a little
annoying.)

Initially my comment form was displayed at the bottom of every blog
entry. I didn't like this, so I decided to only display a "post
comment" link. If you've got JavaScript enabled, the form is inserted
in the page dynamically after clicking on the link. Without JavaScript
the link acts as an ordinary link and the page is reloaded with the
form appended to the end. (I'm using an ordinary GET parameter so in
my view function I can detect whether the comment form should be shown
or not.)

Apparently this has the nice side effect that the comment spammers
cannot find the comment form anymore. That is, I haven't received any
spam since this change. I'm curious how long this will last, but for
now I'm happy.

<small>
  Disclaimer: I don't want to claim this is a guaranteed way of
  preventing comment spam. I'm just reporting my observations here...
</small>
