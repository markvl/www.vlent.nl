---
title: "Unit testing: useful?"
slug: unit-testing-useful
date: 2009-11-05 11:31
tags: [development, testing]
---

Today I read two articles about the usefulness of unit testing. Here
are my thoughts.

The first article I read is called
[It's OK Not to Write Unit Tests](http://blogs.msdn.com/cashto/archive/2009/03/31/it-s-ok-not-to-write-unit-tests.aspx)
(written by Chris "cashto" Ashton). Although Chris isn't saying that
all unit tests are worthless, he attributes less value to them than
they deserve, in my book at least. For the projects I've been working
on, unit tests can actually be very useful.

For example, I've frequently caught bugs after refactoring because a
unit test failed. Does this make me a bad programmer? Unit tests can
also be used to define the API of a certain piece of code. By writing
unit tests in the form of
[doctests](http://en.wikipedia.org/wiki/Doctest) you are forced to
think about the way something should work and at the same time
document it.

The other article I've read is
[The Problem with Unit Testing](http://andreyf.tumblr.com/post/224053080/the-problem-with-unit-testing). Although
I like
[test driven development](http://en.wikipedia.org/wiki/Test-driven_development),
I wholeheartedly agree to the view that 100% unit test coverage is
probably overkill in a project. You'll constantly have to evaluate
whether writing a unit test of a piece of code is worth it. For code
that is more or less isolated (only used in a tiny part of the
project), very straight forward and easy to debug (worst case
scenario), I'm likely to skip writing tests for instance.

Note that I'm only talking about unit tests here. There are many more
ways to make sure the quality of your code is what it should be.
