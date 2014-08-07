---
title: "Travis CI: easy and fun CI for your Plone packages (Nejc Zupan)"
slug: travis-ci-easy-and-fun-ci-for-your-plone-packages-nejc-zupan
date: 2012-10-12 09:45
tags: [plone, ploneconf, testing]
---

A talk about Travis CI: hosted continuous integration for the open
source community.

Ideally you run the tests often (on every commit) in a clean
environment. This way you can make sure that not only the product
works properly, but also that the buildout of the product works on a
clean system. That last part is really helpful during sprints: if
someone cannot get the buildout running, it's most likely the problem
of the machine of the developer, not the product itself.

If you haven't seen the
[tutorial.todoapp](https://github.com/collective/tutorial.todoapp) then
definitely check it out. It shows some great best practises, including
tests and CI.

Travis is free for any public GitHub repository. You can also have paid
subscriptions for private builds. Travis already ran 757k tests for +10k open source projects. They are
crowd funded: +120k USD from +700 people.  They support a lot of programming
languages and preinstalled DBs (you only have to enable them).

Travis is very easy to setup. To get started you:

   - Sign in to [travis-ci.org](https://travis-ci.org/) with your GitHub account.
   - Enable a repository.
   - Add a `.travis.yml` file.
   - Push the `.travis.yml` file.

Example of a very simple `.travis.yml` file:

    language: python
    python:
      - 2.7
    install:
      - python bootstrap.py
      - bin/buildout
    script:
      - bin/test

(Note that because the tests are run from a clean Ubuntu install, you
have to have a buildout configured for you project.)

With [Jenkins](http://jenkins-ci.org/) it is harder to get
started. With Travis the minimal configuration is quite simple. But
you can get more complex if you want to. The drawback is that you only
get the console output. With Jenkins you can get more information
(e.g. coverage reports).

There are a number services on the default Ubuntu image that is
used. You just have to enable them. For instance, the X Virtual Frame
Buffer.

You can whitelist or blacklist branches of your repository. This
prevents errors when you are just trying things out. If you want to
skip a specific build from being tested, you can add `[ci skip]` to
the commit message.

Build notifications can be sent. Mail and IRC are the most common
ones, but many more options are available.

There is are
[Travis browser extensions](http://about.travis-ci.org/docs/user/browser-extensions/)
that will show you the Travis status of a project when you go to the
page. If you want to, you can also create a status image
(`https://travis-ci.org/[YOUR_GITHUB_USERNAME]/[YOUR_PROJECT_NAME].png`),
e.g for on your PyPI page.

You can also have pull request testing. If someone issues a pull
request from a branch, Travis merges the code and you get a
notification whether the pull request is good to merge because the
tests succeed (or not). You can even see the status per commit (if
there is some back-and-forth on an issue for example).

Limitations of Travis: there's a 15 minute build runtime limit. The
limit is for the entire build: from start to the end of the test. And
since the build starts from scratch every time, this may be an
issue. And again, the reporting is still limited.

Tips to speed up the build:

   * Use a non-ancient zc.buildout version (1.6+)
   * Proper configuration (add "`socket-timeout = 3`" and
     "`allow-hosts = ...`" to the `[buildout]` section)
   * Use Asko Soukka's trick to
     [speed up your Plone add-on tests on Travis CI](http://datakurre.pandala.org/2012/09/speed-up-your-plone-add-on-tests-on.html):
     download the unified installer and extract that to your buildout
     cache.


Nejc would like to see Travis and Jenkins go hand in hand in Plone.

Advantages of Travis CI:

   - New developers with broken builds.
   - Can also be used for non-plone packages (simple Python libraries).
   - It's cool to do public CI for company owned public packages. This
     way others can contribute and see if their build succeeds

[View the slides](http://www.slideshare.net/zupo/travis-ci-fun-and-easy-ci-for-your-plone-packages)
or [watch the video](http://www.youtube.com/watch?v=HsGLLGeXFOU).
