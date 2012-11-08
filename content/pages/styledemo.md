---
title: Style demo
date: 2012-06-16 13:27
permalink: /styledemo/
type: page
---

Initially I was planning on writing a style guide. However, this is
not so much a *guide* on how to use certain elements, but more a
*demonstration* of how certain elements are styled.

This page roughly follows the chapters in the
[elements of HTML](http://www.w3.org/TR/2011/WD-html5-20110525/semantics.html#semantics)
section in the HTML5 spec. That is, I’ve picked the elements that are
relevant for this site and I also changed the order a bit (for
example, it makes sense to describe the ``<code>`` element together
with the ``<pre>`` element).

# Sections

## Headings

Usually there is just one ``<h1>`` element on a page and it is used
for the title of the page, as is the case in this page.

If an article is long enough that it needs to be split in several
sections, the ``<h2>`` element is used. This heading is smaller
smaller than the ``<h1>`` and is not bold. The ``<h2>`` is also used
in lists of articles where the titles of the articles are marked up
with an ``<h2>``.

Occasionally more hierarchy is necessary and this is where the
``<h3>`` comes in. To make it stand out from an ``<h2>``, the heading
is a lot smaller and bold. This makes it easier to determine the level
of the heading, especially in a longer text where the ``<h2>`` and
``<h3>`` might not appear on the screen at the same time.

The headings are set in
[Museo Sans Condensed](https://typekit.com/fonts/museo-sans-condensed).

# Grouping content

## Paragraph

Because this is a weblog, most of the content will be contained in
paragraphs, using the ``<p>`` element. Normal paragraphs are set in
18px [Calluna](https://typekit.com/fonts/calluna). I have chosen this
(serif) font because I liked the appearance and it has lowercase
numbers (which I'm really fond of). The fact that the font has been
created by a fellow Dutchman,
[Jos Buivenga](http://www.exljbris.com/), made it even more special.

Another important reason is that Calluna is a complete family. This
means I can use e.g. **bold** to increase the importance of text
(using ``<strong>``) and *italic* to put emphasis on other text (using
the ``<em>`` element). Should it be necessary, I can even combine them
to _**bold italic**_. Having separate fonts means that the result
looks better than when the browser tries to fake them. In other words,
I can
[say no to faux bold](http://www.alistapart.com/articles/say-no-to-faux-bold/).

## Code

As this is a technical weblog, pieces of code are often part of the
articles. They can be included in two separate ways: inline in a
paragraph and as a preformatted chunk of text. For both, the font
[Inconsolata](https://typekit.com/fonts/inconsolata) is used.

For code that needs to be displayed in a normal sentence, as
demonstrated earlier, use the ``<code>`` element. For preformatted text,
use ``<code>`` wrapped in a ``<pre>`` element, like so:

    <pre>
      <code>
        Put your source code here.
      </code>
    </pre>

## Blockquote

When quoting someone, use the ``<blockquote>`` element, optionally
combined with a ``<cite>`` element.

This is for example a quote from the <cite>HTML5 spec</cite>:

<blockquote cite="http://dev.w3.org/html5/spec/Overview.html#the-blockquote-element">
<p>
The blockquote element represents a section that is quoted from
another source.
</p><p>
Content inside a blockquote must be quoted from another source, whose
address, if it has one, may be cited in the cite attribute.
</p>
</blockquote>

The content of the ``<cite>`` element is set in italic, while the
quote itself is indented on both sides to distinguish it from 'normal'
text.

## Lists

There are three types of lists: ordered lists (using ``<ol>``) unordered
lists (``<ul>``) and finally description lists (``<dl>``).

In ordered lists each item is created by an ``<li>`` element and each item
is preceded by a number:

1. Here is an example of an item.
1. This is an item with a nested list.
    1. The first sub item.
    1. The second sub item.
1. And back to the original list but this time the list item is a bit longer just
   to see whether the line is nicely indented.

Unordered lists are similar to ordered lists in the sense that they
are consist of ``<li>`` elements. The difference is that the items are not
numbered.

   * An item in an unordered list
   * This item has a nested list:
     * Item one
     * Item two
   * And a last item that contains a bit more text. This mainly shows
     that if an item spans more than a single line, it is nicely
     indented.

Description lists are created a bit differently. The ``<dl>`` element
must contain one or more terms (``<dt>``) which are followed by one or
more definitions (``<dd>``). Note that one term may have more
definitions and multiple terms may be related to a single definition.

Single term
:   Single definition

First term
Second term
: Single definition

Single term
:   First definition
:   Second definition


## Figures

For figures, such as images, which are (according to the <cite>HTML5 spec</cite>)
<q>self-contained and [are] typically referenced as a single unit from
the main flow of the document</q> you can use the ``<figure>``
element. Optionally you can add a caption, using the ``<figcaption>``
element.

For example if I would talk about the Ubuntu Circle of Friends logo, I might want to
include an image of that logo.

<figure>
  <img src="/images/logo-ubuntu_cof-orange-hex.png" alt="Ubuntu Circle of Friends logo" />
  <figcaption>
    The caption of this image in which I can tell this is the Ubuntu Circle of Friends logo.
  </figcaption>
</figure>


# Text-level semantics

## Anchors

Using the ``<a>`` tag you can create links.

First an [example of a visited link](/styledemo/) and then an <a
href="/unvisited-link" rel="nofollow">example of an unvisited
link</a>.

## Emphasis

To stress emphasis on a certain piece of text, use the ``<em>``
element.

Example: You *must* try this fancy HTML element.

## Strong

To change the importance of text, use the ``<strong>`` element.

Example: Do **not** use this element too much.

## Small

For side comments, such as small print, you can us the ``<small>``
element. It typically contains disclaimers, caveats and copyright
information.

Example: <small>Copyright 2012. All rights reserved.</small>

## Strikethough

To mark text as no longer relevant or accurate, use the ``<s>``
element. To mark a text as having been removed, use the ``<del>``
element (for example on a "to do" list).

Example of ``<s>``: My favourite editor is <s>Vim</s> Emacs.

Example of ``<del>``:

- ~~Write style demo~~
- Update style demo

## Cite

To represent a title of a ‘work’ (e.g. a book, film, report, etc) use
the ``<cite>`` element. Most often found on this site in combination
with a quote (using the ``<blockquote>`` or ``<q>`` element).

Example: To know why 42 is an important number, you must have read <cite>The Hitchhiker’s Guide to the Galaxy</cite>.

## Phrasing content

Content quoted from another source, not being a block of code, should
use the ``<q>`` element. Note that the browser add the quotation
marks.

Example: Okay, I’ll tell you: 42 is <q>Ultimate Answer to the Ultimate Question of Life, The Universe, and Everything.</q>

## Code

To display code fragments inline, use the ``<code>`` element, as shown
earlier.

Example: To display code fragments inline, use the ``<code>`` element.

## Subscript and superscript

Subscript and superscript can be accomplished using the ``<sub>`` and
``<sup>`` elements.

Example: Since this is a software development blog and not a science
blog, this is the 1<sup>st</sup> time I’ve used something like
"H<sub>2</sub>O" on this site. And it will also probably be the last
time.

## Tabular data

For tabular data, the ``<table>`` element is available. There are a
number of elements related to tables, for instance ``<thead>``,
``<tbody>``, ``<tfoot>``, ``<tr>``, ``<th>``, ``<td>``,
``<caption>``. I’ve combined these in one example:

<table>
  <caption>The caption of this table</caption>
  <thead>
    <tr>
      <th>Item</th>
      <th class="tabular-number">Value 1 (%)</th>
      <th class="tabular-number">Value 2 (abs)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>A first item in this table</td>
      <td class="tabular-number">58</td>
      <td class="tabular-number">377.0</td>
    </tr>
    <tr>
      <td>Second item</td>
      <td class="tabular-number">14</td>
      <td class="tabular-number">91.0</td>
    </tr>
    <tr>
      <td>Third item</td>
      <td class="tabular-number">21</td>
      <td class="tabular-number">136.5</td>
    </tr>
    <tr>
      <td>Last item</td>
      <td class="tabular-number">7</td>
      <td class="tabular-number">45.5</td>
    </tr>
  </tbody>
  <tfoot>
    <tr>
      <td>Total</td>
      <td class="tabular-number">100</td>
      <td class="tabular-number">650</td>
    </tr>
  </tfoot>
</table>

Some notes:

- The caption has been placed at the bottom. (Although this is common,
  it is not the default.)
- The rows are separated by a horizontal line. This should make it
  easier to follow a row on larger tables while being less ‘heavy’
  than e.g. using a background colour every other row.
