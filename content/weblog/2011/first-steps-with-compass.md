---
title: First steps with Compass
slug: first-steps-compass
date: 2011-10-11 21:10
tags: [css, development, django, plone, tools]
---

A [lightning talk](http://maurits.vanrees.org/weblog/archive/2011/09/plone-gebruikersdag#lightning-talks)
by Thijs Jonkman at the Dutch Plone User Day once again brought
[Compass](http://compass-style.org/) to my attention. I've read about
it on other occasions, but I never actually tried it. But Thijs really
wet my appetite.

First of all a bit of explanation about Compass. According to the
website it's an "open source CSS authoring framework which uses the
Sass stylesheet language." Let's process this backwards...

[Sass](http://sass-lang.com/), which stands for "Syntactically Awesome
Stylesheets", is an extension of CSS3 and it adds a lot of useful
features (e.g. [variables](http://sass-lang.com/#variables), and
[mixins](http://sass-lang.com/#mixins)). These features make CSS
development a lot easier. (And, speaking as a Python developer, more
fun.)

[Compass](http://compass-style.org/) is a framework that makes working
with Sass even better. Its core contains all kinds of useful mixins
for e.g. CSS resets, CSS3 borders, a footer that sticks to the bottom
of the page and code to help you with sprites, to name just a few. And
if you need more than Compass delivers out of the box, there are many
more
[plugins](https://github.com/chriseppstein/compass/wiki/Compass-Plugins)
available.

# Getting started

To get an impression of Compass, I decided to retrofit the CSS for
this website with Compass. Luckily Brandon Craig Rhodes wrote the
article
[Adding Compass to your project](http://rhodesmill.org/brandon/2011/adding-compass/)
earlier this year. The article not only has instructions and tips on
how to get started, it also contains two bash shell scripts to install
and use Compass. Brilliant!

The
[Sass reference](http://sass-lang.com/docs/yardoc/file.SASS_REFERENCE.html)
is also a read I can recommend. It explains the syntax and the
available constructs.

Having both resources meant I could get started pretty quick. Another
fact that got me underway fast is that one of the available Sass
syntaxes, SCSS (Sassy CSS), is an extension of CSS3. This means that I
only had to change the extension of my `.css` file to `.scss` to have
a valid SCSS file.

The last thing that was missing was Sass support for my editor of
choice, [Emacs](http://www.gnu.org/s/emacs/). (I know, I'm
old-fashioned. ;-) ). But that was easily solved with the
[sass-mode](https://github.com/nex3/sass-mode) by Nathan Weizenbaum,
who is also the primary designer of Sass by the way.

# Project integration

## Django

For this first experiment I used my own, Django site. I decided to put
the `compass` directory directly in the buildout, next to my project
directory (`vlent`). The structure of my buildout looks similar to
this:

    .
    ├── buildout.cfg
    ├── compass
    │   ├── compass.sh
    │   ├── config.rb
    │   ├── install.sh
    │   └── sass
    │       └── screen.scss
    ├── fabfile.py
    └── vlent
        ├── __init__.py
        ├── settings.py
        ├── static
        │   └── css
        │       └── screen.css
        ├── templates
        │   └── base.html
        └── urls.py

(In reality there's much more in there, but I think this effectively
represents the idea.)

Alternatively I could have put the `compass` directory inside the
`vlent` project directory, but somehow this feels a bit 'cleaner' to
me. I guess I like the idea of not cluttering my project with the
Compass stuff.

The most important setting I changed in my `config.rb` file was the
`css_dir`:

    css_dir = "../vlent/static/css"

I personally didn't compress the generated CSS files since
[django\_static](http://pypi.python.org/pypi/django-static) is taking
care of that for me, but Compass can also handle this for you.

I put both the Sass files and the compiled CSS files under version
control. The main reason is to still be able to just checkout (clone)
a tag of the buildout on the production machine and instantly have my
CSS files, without having to install Compass there as well.

## Plone

I experimented with Compass on a Django project, but using it for
Plone theming could also be useful.

When you use the Plone 3 way of creating a theme (using the
`plone3_theme` from [ZopeSkel](http://pypi.python.org/pypi/ZopeSkel)),
there is a challenge. The skeleton suggests to put your own
stylesheets in `browser/stylesheets` but if you need to override
Plone's stylesheets, you'll probably put them in
`skins/my_theme_styles`. But, as far as I can see, you can only have
one output directory for your generated CSS files with Compass. A
solution would be to just put all your CSS files in the skins
`my_theme_styles` folder.

If you create a [Diazo](http://diazo.org/) theme, things should be
easier since there's only one folder where the CSS files are
located. But since I haven't created a Diazo theme myself yet, I
cannot comment on the best way to integrate Compass in such a theme. I
guess you could just put the Compass stuff in the theme and make sure
it's excluded in the ZIP file you distribute?

To make a long story short: regarding the integration of Compass in
Plone themes, I've still got more questions than answers.

# First impressions

I must admit that I had expected that my file `.scss` would be shorter
than my `.css` file. That did not happen. (In hindsight I could have
known that by looking at the examples on the Sass website.) Nesting
selectors and using mixins does make my code more readable. The
variables make the CSS more maintainable since e.g. a color or font
family only needs to be changed in a single place. Using Compass
mixins for
[transitions](http://compass-style.org/reference/compass/css3/transition/)
and
[text shadow](http://compass-style.org/reference/compass/css3/text-shadow/)
definitely makes my life easier since I don't have to worry about the
vendor prefixes.

Another small advantage is that single-line comments (marked with
`//`) are removed from the output. This means I can now put hints in
my code without it cluttering the CSS which will be served to the
visitors of the site.

# Conclusion

I must say I like using Compass and writing Sass. I get the feeling
I've only scratched the surface yet and it will probably shine more
when I start coding from scratch instead of converting existing CSS. I
definitely intend to keep using it for this website and would love to
use it on a bigger (customer) project!
