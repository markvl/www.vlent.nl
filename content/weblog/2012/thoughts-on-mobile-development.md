---
title: Thoughts on mobile development
slug: thoughts-mobile-development
date: 2012-01-11 08:54
tags: [css, design, development, html, opinion, plone]
---

For years web development was quite predictable. The resolution of the
average screen slowly but steadily increased, bandwidth became less of
an issue and everything was good. Then smartphones became
mainstream. Suddenly we have to make sure our websites are also
accessible on small screens. And bandwidth may also be limited to a
few kilobytes per second. In other words: new challenges. But how are
we responding to them?

An approach that is quite popular these days is to create a separate
mobile site. In most cases visitors of the 'desktop' site of
`example.com` are redirected to the mobile version on `m.example.com`
as soon as the site detects (or thinks) that the client is a mobile
device.


# What is a mobile device?

And there we already see the first problem with this approach. What
exactly is a "mobile device"? We can probably agree on a
smartphone. But what about tablets? An iPad, for example, has a
resolution of 1024 x 768 pixels. Isn't that the same resolution a lot of
designs are made for?

So is an iPad a mobile device? If your answer is no, what about an
iPhone 4? With a resolution of 960 x 640 it gets awfully close. So *is*
every smartphone a mobile device? Perhaps we should focus on the size
of the screen. But where to draw the line? 10 inch, 7, smaller?

Perhaps the term "mobile" should not be defined just by the
specifications of the device, but by how the device is used. For
instance, you would probably use your smartphone while waiting in a
queue, but not your laptop. However, using that definition will open
another can of worms.


# Bandwidth

The life of a modern web developer is even more complex. We may want
to optimize the content of the mobile site or application for low
bandwidth conditions of 3G or EDGE networks. But user agent sniffing
doesn't help here. Smartphones can also be on Wi-Fi. And the other way
around, laptops can be tethered and thus have to suck your heavy
desktop version through a straw.

In other words, the user agent or even the type of device your are
working on, has nothing to do with how much bits per second can be
consumed. As a result you should probably try to keep the size of your
site to a minimum either way.


# Other issues

There are bad implementations of mobile websites out there. A simple
example: you see a link to an interesting article on Twitter. You
click on the link and you are directed to the *homepage* of the mobile
site. Good luck finding that interesting article on the mobile
version...

Or the other way around: you are reading a nice article on your phone
and want to send the link to a friend. Now he's stuck with the mobile
version of the article on his 22 inch monitor.

Another complaint I have is that the mobile sites are often dumbed
down. For example a restaurant that only shows the menu and contact
information on the mobile site. Perhaps I want to get a feel for the
place and like to view the photo gallery. But now I have to switch to
the full version. If that option is even available!


# Alternative

Instead of having a separate mobile site, you can use
[responsive web design](http://www.alistapart.com/articles/responsive-web-design/). With
this approach you use
[css media queries](https://css-tricks.com/css-media-queries/) to
change the layout of the page, while serving the same HTML and the
same content. In other words: you don't necessarily care about the
type of device your visitor is using, you set the rules on how things
should be displayed on certain widths and let the browser handle the
rest.

With this approach you do not design separate sites for distinct
devices, instead you design for a range of resolutions. So if next
month a new device comes on the market, your site will probably be
ready for it. (The obvious exception is when the new device does not
fall in the ranges you had anticipated, e.g. a television with a
really high resolution.)

Other people, like Ethan Marcotte in his
[responsive web design article](http://www.alistapart.com/articles/responsive-web-design/),
describe the concept a lot better. Mikko Ohtamaa also just started
[a series of blog posts](http://opensourcehacker.com/2012/01/09/mobilizing-websites-with-responsive-design-and-html5-tutorial/)
that promises to be very interesting.


# So is a mobile site always a bad thing?

Don't get me wrong, having a (separate) site specifically for mobile
devices certainly does have its benefits and can be a good
solution. But in my opinion it should not be the first option when
building a website or web application that should be "mobile aware".


# Conclusion

Actually, I do not have a conclusion... Although I think responsive web
design provides a good solution, it is not the holy grail. As I said
at the start of this article, we live in exciting times. There is a
lot we still have to discover!
