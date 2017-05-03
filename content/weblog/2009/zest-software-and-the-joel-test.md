---
title: Zest Software and The Joel Test
date: 2009-07-10 10:00
tags: [development, opinion, zest software]
---

A couple of years ago, Joel Spolsky wrote "The Joel Test". Let's see
how Zest Software scores...

[The Joel Test](http://www.joelonsoftware.com/articles/fog0000000043.html)
was devised to rate the quality of a software team. In contrast to
other methods, it is designed to quickly provide some basic insight in
how a team is doing. And although Joel used the words "highly
irresponsible" and "sloppy", I though it was fun to see how we at
[Zest](http://zestsoftware.nl) rate.

We mainly use agile development to create
[buildout](http://www.buildout.org/) based
[Plone](http://plone.org) applications. In answering the questions,
I'll focus on those type of projects.

(Disclaimer: obviously this represents my own view on the matter and
is not necessily the opinion of Zest or any of my co-workers.)

# 1. Do you use source control?

Yes! I cannot even imagine working without it. We mainly use
[Subversion](http://subversion.tigris.org/) but some of us are (or
have been) experimenting with other source control software, like
[Bazaar](http://bazaar-vcs.org/) , [Git](http://git-scm.com/) and
[Mercurial](https://www.mercurial-scm.org/).

# 2. Can you make a build in one step?

Hmmm... tough one. We don't really "build" in the traditional
way. Since [Python](http://www.python.org) is an interpreted language,
we don't need to explicitly compile. For instance: restarting
[Zope](http://www.zope.org/) is enough to use the latest code (and
with [plone.reload](http://pypi.python.org/pypi/plone.reload)
restarting isn't even necessary in many cases).

But okay sometimes you'll have to rerun the buildout to get/update all
the dependencies. Rerunning buildout is a single step so I'll count
this as a yes.

# 3. Do you make daily builds?

In the way Joel describes this, it basically translates for us to
doing a clean checkout, running the buildout and then running the
tests. (Assuming the tests include integration tests which need the
whole Plone/Zope stack.)

But no, we don't do this. We did have
[buildbot](http://buildbot.net/trac) running for a couple of projects
to run the tests after every commit, but I have to admit we are not
doing this often enough.

# 4. Do you have a bug database?

Yes we do. If we encounter a bug, we store it either in a
[(user) story](http://www.extremeprogramming.org/rules/userstories.html)
or we put it in the issue tracker associated with the project.

# 5. Do you fix bugs before writing new code?

This depends on the project. Most of the time we try to estimate the
time needed to solve the problem and report back to the customer if we
expect that the fix will take a significant amount of time. Since in
agile development the customer sets the priorities, he can decide that
the bug is less important than getting a new feature in the next
release.

For our own projects or community projects we do want to make sure we
ship code as bug free as possible and in general we give bugs a high
priority.

# 6. Do you have an up-to-date schedule?

For each project we maintain a list of features in our
[project management tool](http://plone.org/products/extreme-management-tool). Each
feature (or story in XP terminology) has an estimate of how much time
it will take to implement. So we can determine when the project will
be done.

However, at each
[iteration meeting](http://www.extremeprogramming.org/rules/iterationplanning.html)
the customer could decide to add new feature, change the priorities,
etcetera. So the schedule is in no way set in stone.

# 7. Do you have a spec?

Each story in the project represents a single feature. Since the set
of features for a project isn't static (new ones can be added, others
can be dropped), we don't write a thick document specifying every
detail of a project. We tend to describe the feature in a couple of
sentences in the story. By splitting it up in tasks when we start
working on it, more details are added.

(By the way, don't writing specifications and justifying that by
saying "XP doesn't need specs" is wrong in my opinion. You do need to
have other practices in place to compensate the lack of written
specs.)

Another characteristic of agile development: we only build what is
requested. That is: we don't try to accommodate for every possible
future use case of a feature. We try to find a balance between
iterative design and thinking things though enough to limit the
refactoring needed when more use cases have to be implemented.

And since we have iteration meetings every (other) week where we demo
and discuss the work done in the previous iteration, the customer has
the opportunity to refine his ideas.

# 8. Do programmers have quiet working conditions?

No we don't. Which is a good thing when sprinting on a project: by
having all developers in the same room it is incredibly easy to
exchange knowledge. Pair programming also helps here. In my experience
if one of the partners gets distracted by the discussion (e.g. to
answer a question) the other half of the pair can quickly get him
focussed again.

When we are not sprinting though, it can be a bit hard to focus on
your task. Especially if co-workers are discussing a project on which
you aren't working right now, but you are familiar with. (Perhaps I'm
overly curious and therefore more easily distracted...) However, at
the office we do have a place where you are isolated from the other
developers and it is also possible to work from home.

# 9. Do you use the best tools money can buy?

If we need tools and our demands are reasonable, sure. It just happens
that many of the tools we think are the best, are open source
tools. (Although it also depends on the platform that is being
used. I've got the feeling that the Mac users at Zest use more
proprietary software than the Linux users.)

# 10. Do you have testers?

No we don't. This doesn't mean our software is deployed at random
though. First of all we try to write automated tests (unit, functional
and integration tests), although I do have to admit that this heavily
depends on the quality level the customer asks for. But this is a
different discussion.

Furthermore: usually the project manager tests the application to see
whether it meets the requirements. Then we demo it to the
customer. And finally: most of the times we first deploy the code to a
preview server where the customer can play around test it.

# 11. Do new candidates write code during their interview?

No, as far as I know we don't require candidates to write code. (I
certainly didn't have to do it. :) ) But at the same time we also
haven't yet hired developers that didn't meet up to our
expectations. Perhaps we don't have as high standards as e.g. Joel
does, perhaps it has to do with the fact that we are a small
company. I don't know.

# 12. Do you do hallway usability testing?

It's no excuse, but this is hard to do this if you're in a small
company. I think most co-workers are too "technology infected" by now
to give a completely objective opinion. If you've been working with a
system long enough (e.g. Plone) you get used to it's quirks.

However, we do frequently request co-workers to give a second opinion
about the (user) interface. And since we work in short iterations, the
end-user also gets to work with the software shortly after writing
it. So any strange behaviour should be detected quickly.

# Conclusion

Perhaps I'm not being objective, but I think that some of the
questions from the Joel Test don't fit in our development process. I
therefore don't want to calculate a score but let you draw your own
conclusions. I did certainly find a couple of areas where we can
improve...
