---
title: Web designer's skills
slug: web-designers-skills
date: 2010-01-02 19:47
tags: [design, development, opinion]
---

Recently I read some articles about web designers. This got me
thinking about the qualities I think you need to be a good designer
and about the different ways a design can be made.

# Skills

First of all a designer needs to be **creative**. After all, he is the
person that needs to capture the ideas of the client and visualize
them. However, it is also very important for the designer to
**understand the web**. Something that works in print, may completely
fail in a browser. One of the reasons is that print media is meant to
be seen/read, while websites need to be interacted with. Closely
related is **anticipating user generated content**. This means that a
design should also look great with less (or more) text than the
[lorem ipsum](http://en.wikipedia.org/wiki/Lorem_ipsum) in the design.

I think these skills are not disputed. But what about the **ability to
code?** I agree with Lukas Mathis that there are risks when designers
are also involved in implementation. In his essay
[Designers are not Programmers](http://ignorethecode.net/blog/2009/03/10/designers-are-not-programmers/)
he more or less says that designing and coding are two separate
worlds. To be able to be good at designing, you'll have to ignore
everything you know about coding. Otherwise the design is restricted
by technical limitations: you know what you can implement and you'll
design within those boundaries. Even worse: by already thinking ahead
about the way it's going to be coded, the focus will be on the code
instead of the user experience.

# Photoshop or HTML?

A related discussion is what the deliverable of a design should be. In
most of the projects I'm involved in, the design results in a
Photoshop file. This file is then cut to extract the needed graphics
and the HTML/CSS is coded. I guess you know the drill.

However, quite often the role of designer is combined with the role of
front-end developer, especially in smaller shops. In these cases it
can be easier to do the design in HTML directly, as described by
Meagan Fisher in
[Make Your Mockup in Markup](http://24ways.org/2009/make-your-mockup-in-markup). (The
Django package
[django.contrib.webdesign](http://docs.djangoproject.com/en/dev/ref/contrib/webdesign/)
even helps by generating sample text.) One advantage is that some
design **changes are easier to make in CSS** than in
Photoshop. Depending on your skills, the whole design process may even
be faster. Meagan also demonstrates that CSS3 gives you the ability to
create a lot of effects without having to resort to images, which
means you'll have to spend even less time in the graphics editor.

Another advantage of designing in HTML is that the client can **see
how the design works** in the browser. You have to be careful though:
since it's only a design, it's very likely that the code is not cross
browser compatible yet. If the client uses a wrong browser, the design
may not come across as intended. (To prevent this, you could export
the page as an image e.g. by using the Firefox add-on
[Screengrab](https://addons.mozilla.org/en-US/firefox/addon/1146).)

You'll also carefully have to manage client expectations. If the
design is done in HTML, the client may **incorrectly assume the
front-end work is done**. He may not appreciate the time that is still
required to make the site look good in all targeted browsers. Or the
time needed to make the static HTML more dynamic by integrating the
application or adding AJAX effects.

# However...

Perhaps the most important skill of a good designer is being able to
**communicate**. Not just because the design should communicate the
right things, but also because communication with the client and
development team is, in my opinion, the key to success.
