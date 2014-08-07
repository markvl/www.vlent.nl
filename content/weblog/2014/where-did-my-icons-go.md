---
title: Where did my icons go?
date: 2014-07-11 21:54:00
tags: [css, development, html, icons, svg]
---

When I was experimenting with an SVG sprite to replace my current icon
font, suddenly some of the icons disappeared without a clear
reason. It worked fine when I accessed the demo page via the
[file URI scheme](http://en.wikipedia.org/wiki/File_URI_scheme), but
as soon as I used an HTTP server, some of them did not show up.

![Missing icons](/images/icons-missing.png "Some of the icons are missing")

This puzzled me because I was using the (unmodified) demo page I
downloaded from [IcoMoon](http://icomoon.io/app) and more importantly:
I had seen the icons when I used the file URI scheme.

After inspecting one of the icons, I saw that a user agent stylesheet
had set the "`display`" property to "`none`" on that element (and a
bunch of others):

![User agent stylesheet sets display to none](/images/icons-missing-devtools.png "User agent stylesheet sets display to none")

I figured this must have been caused by one of my extensions. And
indeed: after disabling the
[Adblock Plus extension](https://adblockplus.org) the icons appeared
again. Some more tweaking revealed that
[Fanboy's Social Blocking List](https://easylist.adblockplus.org/en/#socialblocklist)
was the culprit. This immediately explained why only the social media
icons were missing. (I had not made that connection yet...)

For me the solution was to just use a different class name for the
social media icons. I can also disable the list on my machine, but
visitors of the site might have it enabled thus not see some of the
icons.
