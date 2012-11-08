---
title: "Acrylamid: a first evaluation"
date: 2012-11-08 17:17
slug: acrylamid-first-evaluation
tags: [acrylamid, blog]
---

About a month ago I officially migrated this weblog to Acrylamid. This
is a first evaluation.

On the one hand, a month may not seem like a long time. So why
evaluate [Acrylamid](http://posativ.org/acrylamid/) now? Well, for one
thing, I started working with it a bit earlier than
[October 1st](/weblog/2012/10/01/migrating-to-acrylamid/) since I had
to migrate existing content and develop this site. Another reason is
that during the [Plone Conference 2012](http://www.ploneconf.org/) I
published more articles about those three days than I normally do in
a whole year.


# Writing articles

During the conference I was not able to publish all articles
immediately after the talk was over. So I got into the habit of
writing my notes in a drafts folder. When I started making the notes
ready for publication, I would move the file to the normal
directory. (Alternatively I could have added a `draft` field, but this
way it was easier to see which articles were not published yet.)

Although the Wi-Fi at the conference was almost perfect and the hotel
also offered free Wi-Fi, there were a couple of times where I did not
have a connection to the Internet while I *did* want to edit my
articles. But since I could do the writing on my own laptop, that
hardly mattered. The biggest issues were that I could not look up
things easily (I had to use my phone) and that the pages were not
rendered with the right fonts (since I use
[Typekit](https://typekit.com/)).

Another thing I liked was my tool set. I am still really happy with
Emacs as an editor. I love that I am able to hit `C-x C-s` as often as
I need---no matter the network state. That beats having to edit
articles online using e.g. TinyMCE. Not that the latter is a bad thing
by the way, I just prefer my good old Emacs.

As for marking up the articles: Markdown also proved to be a good
syntax to do so. Only once was I not able to get the result that I was
after. I wanted to have a code block inside an unordered list. I an
pretty sure it is possible, I just did not know how exactly and
rewrote the article a little bit. Lets chalk this up to me being too
lazy and inexperienced with Markdown.


# Output

One of the things I am currently still struggling with is my URL structure. Years
ago I used URLs like `/weblog/title-of-the-article/`. I switched to
URLs with dates (`/weblog/2012/02/04/title-of-the-article`) when I
[switched to Django](/weblog/2010/05/30/switch-django/). In Django it
was very easy to write a view that redirected the old URLs to the new
ones. But now I only added *some* of the 2008--2010 URLs to my
`.htaccess` files. But since
[cool URIs don't change](http://www.w3.org/Provider/Style/URI.html) I
have to list all the old URLs in that `.htaccess` file or else I have
to find a more generic solution---for instance by writing a custom
view for Acrylamid that uses a `<meta>` element or JavaScript to
redirect visitors to the new URL. In the mean while: to mitigate the
problem for visitors, I am using Google to
[make my 404 pages more useful](http://googlewebmastercentral.blogspot.nl/2008/08/make-your-404-pages-more-useful.html). Most
of the times, the search does return the page the visitor was after.

Another thing that bothers me is that I do not (yet) have views that
show the articles for a year/month/day. For instance
`/weblog/2012/10/10/` to see all articles for the first day of the
Plone conference.


# Conclusion

I am quite happy with the current setup. I am not completely done yet,
but for me it is a huge improvement over the Django (and Plone) setups
I had earlier. I find it a really nice lightweight
blogging system.
