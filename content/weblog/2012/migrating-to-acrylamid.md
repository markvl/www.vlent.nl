---
title: Migrating to Acrylamid
slug: migrating-to-acrylamid
date: 2012-10-01 08:26
tags: [acrylamid, blog]
---

In the last year several people I know or follow have switched to a
static weblog. I was in the middle if a redesign myself and thought it
was a great opportunity to investigate the concept. The result: I replaced Django with [Acrylamid](http://posativ.org/acrylamid/) for this site.


# How it started

The redesign I was working on was about two things: creating a
responsive (grid based) design and going back to the essentials. I
think I was about 90% done when my attention was drawn to static
weblogs. I immediately saw the performance benefit: generate a page
once and just serve that static file. No database or processing is
involved---it's just a web server returning files.

I already knew
[reStructuredText](http://docutils.sourceforge.net/rst.html) and
because
Tarek Ziadé [moved to Pelican](http://ziade.org/2012/03/05/moving-to-pelican/)
and
Daniel Greenfeld also created [a new blog](http://pydanny.com/my-new-blog.html)
using Pelican, that is what I started experimenting with:
[Pelican](http://getpelican.com/). However, I did not like the HTML it
generated. This is a web development blog and I use a lot of code
samples. Plus I like to have (somewhat) semantic HTML. But inline code
was turned into `<tt class="docutils literal">example</tt>`. And I wanted
`<code>example</code>`. And code blocks were only wrapped in a `<pre>`,
but I also want to wrap it in a `<code>` element.

In hindsight this was probably more a problem with docutils and/or the
code highlighting than Pelican itself, but it made me investigate other
static blog engines. I found [Acrylamid](http://posativ.org/acrylamid/) and
[StrangeCase](http://pypi.python.org/pypi/StrangeCase).

The latter seems to provide a lot of flexibility. But by reading the
documentation I got the impression that that same flexibility would make
writing a simple article too complex for me as it requires you to
write Jinja2 in your article content. Jinja2 *as such* is not a
problem for me, I just don't want to be bothered with it when writing
an article.


# Acrylamid and Markdown

Acrylamid on the other hand made it very easy to start. But because it
showed the same problems with reStructuredText I decided to switch to
[Markdown](http://daringfireball.net/projects/markdown/)---something I
should have done earlier.

The syntax of Markdown is a bit more limited than reStructuredText. For
instance: it does not have a way to write definition lists (`<dt>`) or
tables, as far as I know. But Markdown allows you to simply write HTML for
the things not covered by its syntax. And since 95% (if not more) of my
articles only need the stuff Markdown provides a syntax for, that's
fine by me.

But back to Acrylamid... A few things I like about it: like I said it
was very easy to get started and the author is very responsive if
you've got questions, bugs or improvements (pull requests). What's
even more important: it has all the features I need for this blog:
articles (entries), pages, (paginated) lists of articles, tags and feeds.


# Migration

Acrylamid provides an easy way to import content from e.g. an Atom
feed. This was great since I already provided feeds on the previous
version of my site (using
[django-atompub](https://code.google.com/archive/p/django-atompub/)). So
all I needed to do on the Django side was to add was a feed that
listed *all* articles. (Note that I already
[migrated from django.contrib.comments to Disqus](/weblog/2012/09/07/migrating-djangocontribcomments-disqus/)).

Although the migration of the HTML to Markdown wasn't flawless. There were three
things I had to correct manually:

   * The categories were not included in the migration. Even though
     they were provided in the Atom feed (using the `<category>`
     element).
   * HTML-ish looking content that could not be converted to Markdown
     was just left out. For instance, I use angled brackets in command
     line examples (e.g. “`git rebase -i <sha1>`”). After the migration
     the whole “`<sha1>`” part was gone.
   * The code blocks were indented three spaces instead of four and
     thus were not converted into `<pre>` blocks.

These three combined made me go over all my articles to make sure they
had the right tags and the content was still okay. But to be honest, I
did not mind that since it also provided an excuse to review the tags
I used. Plus, I don't have that many articles.


# Decisions I made along the way

One reason I started the redesign at all was that I wanted a
responsive (grid based) design. Although this blog should now be more
pleasant to read on so called 'mobile' devices, I dropped the grid
based design since it was overkill and I also doubt whether it can be
called a
[responsive web design](http://en.wikipedia.org/wiki/Responsive_web_design). I
do intend to make better use of wider screens somewhere in the future,
e.g. by placing the meta data of articles to the left of the main
content column. But I don't think it will be completely responsive.

I also decided to drop the images included in (almost) every
article since 2009. It usually didn't add anything to the content of
the article. And it frequently took me just as long to write the
article as I spent trying to find a good image.

To clean up the pages I removed the list of tags and the latest entries. Judging by the
number of page views per visitor, they weren't used that much
anyway. Speaking of which: the Dutch Telecommunications Act now
requires <q>unambiguous consent</q> to place tracking cookies from
e.g. Google Analytics. I did not want to place a mechanism on this
site to get that consent, so I decided to remove Google Analytics
altogether.


# Tools I use

Although I haven't been working with Acrylamid (or any static blog)
for long, I do want to share my current approach.

I guess I am getting old because I still prefer using Emacs over
e.g. TextMate, Sublime Text or other fancy editors and IDEs. Perhaps it is because you
can find a nice mode for just about any file type you can find. I'm
currently using:

   * [jinja2-mode](http://github.com/paradoxxxzero/jinja2-mode) to
     edit my templates.
   * [markdown-mode](http://jblevins.org/projects/markdown-mode/) for
     the content.
   * [sass-mode](https://github.com/nex3/sass-mode) to work on the
     Sass files. And speaking of which, my Sass files are written in
     the older, indented, syntax (because if feels kind of
     'Pythonic').
   * [typopunct mode](http://www.emacswiki.org/emacs/typopunct.el) for the occasional inclusion of typographical punctuation marks in my
     content. But usually I have this mode turned off and let the Acrylamid
     `typography` filter handle this kind of stuff.
   * [Magit](https://github.com/magit/magit) to manage the git
     repository (combined with using the command line).

The environment I use to combine all the components into what you are reading
now, is described in the
[README](https://github.com/markvl/www.vlent.nl/blob/master/README.md)
of the [GitHub repo for this site](https://github.com/markvl/www.vlent.nl). One thing I want to highlight is
[virtualenvwrapper.gem](http://pypi.python.org/pypi/virtualenvwrapper.gem). This
plugin for
[virtualenvwrapper](http://pypi.python.org/pypi/virtualenvwrapper)
allows me to install the gems for [Sass](http://sass-lang.com) and
[Compass](http://compass-style.org/) inside my virtualenv. Yay!

The checkout of the repository lives in
a [Dropbox](https://www.dropbox.com/) folder. This way I can
use e.g. the
[Nocs app](http://itunes.apple.com/nl/app/nocs-markdown-dropbox-your/id396073482)
to prepare articles via an iOS device.


# Pros and cons

Again: I haven't been using this approach for *that* long, but here are
the pros and cons I discovered so far.

## The disadvantages

Let's first list the downsides of Acrylamic (or any static blog)
compared to a CMS or my previous Django based solution:

   * I cannot publish new articles if I've only got access to a
     browser, e.g. when using a smartphone. After creating/editing a file it needs to be
     compiled. (Then again: I usually have my laptop at hand when
     publishing an article anyway. I have very rarely published an
     article while not working on my laptop.)
   * I have less control over the HTML that is generated from the text
     file. This is something that held me back initially from
     switching to a static blog engine. However, since I can also
     write HTML in my Markdown files, I can regain full control if I
     really want to.

## The advantages

Now for the benefits:

   * I can host my blog anywhere! No complex setup needed. Just some
     HTML, CSS and Javascript files combined with some images and a
     limited `.htaccess` file (mostly for redirects of old URLs) and
     that's it.
   * For most of my articles I can just write a bit of Markdown and
     that's it. No need to worry about or tweak HTML in TinyMCE.
   * The code *and content* live in a single place: my Git
     repository---no separate database (ZODB, SQL or otherwise) required. The only
     dependencies are the Python eggs and Ruby gems I use. But
     everything specific for my blog is in one place. And with my
     setup that combines Git and Dropbox I think I also don't need to
     worry about an elaborate (off site) backup mechanism. (Famous
     last words? Time will tell...)
   * I can prepare the content completely offline: creating new files,
     editing existing ones, previewing the result and even storing
     them in Git can be done in isolation. I only need to be online
     when I want to push my changes to GitHub or to actually publish
     the content. This will make it easier to blog on conferences
     where the WiFi connection isn't always capable of providing a
     stable connection to a whole bunch of nerds. ;-)


# End result

When I started with the redesign about a year ago I wanted to have a
responsive (grid based) design and I wanted to go back to the
essentials. I think I can say I succeeded in the latter. It doesn't
get more basic than simple HTML and CSS. As for the responsive design:
I think the site got more readable and that is what counts, not what
label can be attached to it.

I am happy with the current status even though I'm not completely done
yet. I just wanted to get this live *before* the
[Plone Conference](http://www.ploneconf.org/) and improve
iteratively. I'll be attending that conference and will try to write
an article about each talk I attend. That will be a good test to see
how my current setup works...


# Thanks

Moving from Django to Acrylamid means I can host my site anywhere. So
it now resides on a server of
[bHosted.nl](http://www.bhosted.nl/). But until today it was still
running on a server of [Zest Software](http://zestsoftware.nl/), the
company I left almost two years ago. They were kind enough to tolerate
me and spare me the trouble of finding a new location for the old Django
site without even charging me. Thanks guys, I really appreciate that!
