---
title: A week with Firefox instead of Chromium
tags: tools
---

My browser of choice has been [Chromium](http://www.chromium.org/Home)
for quite a while now. A couple of podcasts recently discussed how
Chrome has become a memory hog and how
[Firefox](https://www.mozilla.org/en-US/firefox/) has improved over
the years. Time for an experiment.

Before I started using Chrome (and later Chromium), Firefox was my
favourite browser. Chrome offered a separate process per tab and nice
developer tools. And it was---or at least felt---faster. But that was
a couple of years ago and since I heard about other people switching
back to Firefox, I also wanted to give it a chance again.

For the record, I am comparing Firefox 36 with Chromium 41 here, both
running on Ubuntu 14.04 (Trusty Tahr).


# Comfortable start

In my opinion there's only one way to properly do this experiment: use
Firefox exclusively and not even start Chromium. And that was exactly
what I did for a week. (Well... almost, but I'll get back to that
later.)

My first actions were to import my bookmarks and history from Chromium
to Firefox. This helped me to feel at home straight away. Next up were
a few add-ons: Adblock Plus, Firebug, NoScript and Privacy Badger.
Time to get some actual work done.

# Good times

There were a couple of things I really liked when using Firefox.

For instance, the developer tools that ship with Firefox include a
[Responsive Design View](https://developer.mozilla.org/en-US/docs/Tools/Responsive_Design_View)
which makes it easy to test a site on different resolutions without
having to resize your browser window each time.

![Responsive Design View](/images/firefox-responsive-design-view.png)


Speaking of which, the built in tools have improved quite a bit since
the last time I professionally used Firefox. Unfortunately I found out
about this a bit late, but I think I could have done my work perfectly
without using the Firebug add-on.

![Firefox Inspector](/images/firefox-inspector.png)

During the week I also enjoyed the
[NoScript](https://addons.mozilla.org/En-us/firefox/addon/noscript/)
add-on: simple to use yet so powerful. Although I have to admit that I
had a couple of occasions where I wondered why something did not work
as expected and 99% of the time it was because of blocked JavaScript.

As a bonus of this experiment I caught a problem in the project I am
working on. I was reviewing a change on a page and something did not
seem to work. After firing up Chromium (the only time I 'cheated') I
discovered that this problem only existed on Firefox.


# Things I disliked

There were also a few things I noticed during my work week that I did
not like.

I really disliked the way the tabs worked for instance. If you've got
too many of them, they start to scroll. Using the
[Tab Mix Plus](https://addons.mozilla.org/nl/firefox/addon/tab-mix-plus/)
add-on I could get Firefox to at least show me all tabs again, but I
did not really fancy the multi-row tabs.

<figure>
  <img src="/images/firefox-scrolling-tabs.png" alt="Scrolling tabs" />
  <figcaption>
    Scrolling tabs in Firefox
  </figcaption>
</figure>

<figure>
  <img src="/images/firefox-multi-row-tabs.png" alt="Multi-row tabs" />
  <figcaption>
    Multi-row tabs in Firefox with Tab Mix Plus
  </figcaption>
</figure>

Compare this with Chromium where the tabs can become so small that
they are almost impractical, but at least I've got a sense where a tab
is relative to the first and last tab I opened.

<figure>
  <img src="/images/chromium-many-tabs.png" alt="Many tabs in Chromium" />
  <figcaption>
    Many tabs in Chromium
  </figcaption>
</figure>

A final thing that I will mention is that Firefox was not as fast as
Chromium. First and foremost because Firefox seemed to 'pause' more
frequently than Chromium. That is, the window went grey and was
unresponsive for a couple of seconds.

Related to this, at least from
an end users point of view: (some) sites loaded slower. Some hardly
noticeable (e.g. this site took 400ms in Chromium and 500ms in
Firefox), others were more obvious and annoying like loading a patch
set in our code review tool took 1.21s in Chromium and 2.65s in
Firefox.


# Result

I went into this experiment with an open mind, completely intended to
make Firefox my default browser if I liked it better than
Chromium. After having used it for a week I can agree that Firefox is
a better browser than it was a couple of years ago.

But although Firefox brought me good things, it also failed to
convince me at the moment. I might use it a bit more often now, but my
default and main browser will remain Chromium for now.
