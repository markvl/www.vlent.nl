---
title: Open tabs — March 2019
date: 2019-03-14
tags: [aws, blog, devops, go, observability, monitoring, sre, tabs]
---

Last May I [published the list of tabs](/weblog/2018/05/12/open-tabs/) I had
open on my phone at that moment in time. This another one of those posts.

I have switched phones but there were about 50 tabs open in the browser on my
old phone. This article is a selection of the pages I want to (re)read in the
future.

# Go
I want to learn [Go](https://golang.org/). This is a list of resources that seem
useful:

[Containerization of Golang applications](https://elsesiy.com/blog/containerization-of-golang-applications)
: An example by Jonas-Taha El Sesiy (including a Dockerfile and Makefile) of how
you can deploy a Go application in a Docker image.

[Effective Go](https://golang.org/doc/effective_go.html)
: I've heard positive things about this document.

[Go for Python Programmers](https://golang-for-python-programmers.readthedocs.io/en/latest/about.html)
: Well... I'm a Python programmer and I want to learn Go. Nuff said. ;-)

[Go by Example](https://gobyexample.com/)
: Again practical examples to teach the concepts in Go. The examples are, as far
as I've seen, relatively short. This is positive because it highlights the
concept at hand, but on the other hand it can be useful to have more complex
examples to get a better understanding of how concepts work together to create a
larger application.

[Let's Go! Learn to Build Professional Web Applications With Golang](https://lets-go.alexedwards.net)
: This book promises to teach Go while building an application. I find having
practical examples helps me when learning a new programming language.

[Programming Talks](https://github.com/hellerve/programming-talks)
: A (community maintained) list of talks on programming language specifics.

[The Go Programming Language Specification](https://golang.org/ref/spec)
: It's always good to have the specs nearby.


# Observability and monitoring
[Observability and Monitoring Best Practices](https://www.integralist.co.uk/posts/monitoring-best-practices/)
: Terminology and a set of best practices by Mark McDonnell.


[Lessons from Building Observability Tools at Netflix](https://medium.com/netflix-techblog/lessons-from-building-observability-tools-at-netflix-7cfafed6ab17)
: Lessons learned from big companies usually make an interesting read. Even
though things might not apply to your situation.

[Monitoring for Distributed and Microservices Deployments](https://www.digitalocean.com/community/tutorials/monitoring-for-distributed-and-microservices-deployments)
: An article about the challenges of distributed architectures and adjustments
needed to be able to respond to incidents in this changed environment.

[Observability+](https://medium.com/observability)
: A blog with a number of interesting articles about observability.

[Stack Overflow: How We Do Monitoring - 2018 Edition](https://nickcraver.com/blog/2018/11/29/stack-overflow-how-we-do-monitoring/)
: This article (and Nick Craver's previous posts by the way) makes for
fascinating reading.

[Why Your Server Monitoring (Still) Sucks](https://www.linuxjournal.com/content/why-your-server-monitoring-still-sucks)
: Five reasons why your current monitoring sucks and what to do about it.

[10 monitoring talks that every developer should watch](https://techbeacon.com/10-monitoring-talks-every-developer-should-watch)
: Enough material in here to learn from.


# Cloud services
[How many AWS accounts do I need?](https://nodramadevops.com/2019/01/how-many-aws-accounts-do-i-need/)
[How should I organize my AWS accounts?](https://nodramadevops.com/2019/01/how-should-i-organize-my-aws-accounts/)
: Two articles published on the \#NoDrama DevOps blog about organizing your AWS account(s).

[Serverless: From Azure to AWS](https://www.awsadvent.com/2018/12/19/serverless-from-azure-to-aws/)
: Comparing Azure and AWS serverless offerings.


# Other devops related articles
[Advanced multi-stage build patterns](https://medium.com/@tonistiigi/advanced-multi-stage-build-patterns-6f741b852fae)
: Tõnis Tiigi has a number of examples of multi-stage Docker image build
patterns.

[How To Use Git Hooks To Automate Development and Deployment Tasks](https://www.digitalocean.com/community/tutorials/how-to-use-git-hooks-to-automate-development-and-deployment-tasks)
: A list of available Git hooks and a demonstration on how to use hooks to
automate tasks.

[Open sourcing Terratest: a swiss army knife for testing infrastructure code](https://blog.gruntwork.io/open-sourcing-terratest-a-swiss-army-knife-for-testing-infrastructure-code-5d883336fcd5)
: I am using tools like [Terraform](https://www.terraform.io/) and
[Packer](https://packer.io/) quite a bit these days, but testing the code is
still something I'm doing manually. Perhaps [Terratest](https://github.com/gruntwork-io/terratest) is a nice solution?

[SRE University](https://github.com/andrealmar/sre-university)
: A list of resources related to Site Reliability Engineering.

[What Does a Site Reliability Engineer Do? ](https://www.scalyr.com/blog/site-reliability-engineer)
: Activities an Site Reliability Engineer is participating in, according to Erik
Dietrich.


# Blog improvements
Once I get around to working on this site again, there are a few things I want
to have a look at.

[Bye, Bye Disqus - Say Hello to Isso](https://matthiasadler.info/blog/isso-comment-integration/)
: I am thinking about replacing the [Disqus](https://disqus.com/) comments with
something else. [Isso](https://posativ.org/isso/) is a contestant.

[On Switching from HEX & RGB to HSL](https://www.sarasoueidan.com/blog/hex-rgb-to-hsl/)
: Sara Soueidan convinced me in this article that expressing colors in HSL (Hue,
Saturation and Lightness) can be an intuitive way to choose colors. I'll want to
keep this in mind if I overhaul the colors used on this site.

[security.txt](https://securitytxt.org/)
: A (proposed) standard to provide information on how to report security issues.

[The Font Loading Checklist](https://www.zachleat.com/web/font-checklist/)
: I like having pretty (IMHO) fonts for this site. This resource might help me
improve the use of them.

[The headers we don't want](https://www.fastly.com/blog/headers-we-dont-want)
: Time to review the response headers this site is returning.


# Miscellaneous
[CyberChef](https://gchq.github.io/CyberChef/)
: <q>CyberChef is a simple, intuitive web app for carrying out all manner of
"cyber" operations within a web browser.</q>

[Engineering Management: The Pendulum Or The Ladder](https://charity.wtf/2019/01/04/engineering-management-the-pendulum-or-the-ladder/)
: Another great article by Charity Majors. This time she writes about becoming
an engineering manager and career options.

[Hashicorp at Home](https://www.mockingbirdconsulting.co.uk/blog/2019-01-05-hashicorp-at-home/)
[Hashicorp at Home - Part 2](https://www.mockingbirdconsulting.co.uk/blog/2019-01-08-hashicorp-at-home-part-2/)
: Matt Wallace improved his home network with [Vault](https://vaultproject.io/)
(managing secret), [Consul](https://consul.io/) (managing DNS and service
discovery), [Nomad](https://nomadproject.io/) (managing containers),
[Traefik](https://traefik.io/) (dynamic reverse proxy/load balancing) and
[DataDog](https://www.datadoghq.com/) (monitoring).

[Howto: 433mhz verzenden en ontvangen op raspberry pi](https://shoarma.000webhostapp.com/index.php/howto-433mhz-verzenden-en-ontvangen-op-raspberry-pi/)
: Dutch article on using a Raspberry Pi to send radio signals to turn your
lights on and off.

[How To Use SSHFS to Mount Remote File Systems Over SSH | DigitalOcean](https://www.digitalocean.com/community/tutorials/how-to-use-sshfs-to-mount-remote-file-systems-over-ssh)
: Basically what the title says: instructions on how to mount a file system of a
remote machine, using SSH.

[Time Management for System Administrators](http://shop.oreilly.com/product/9780596007836.do)
: Something I could get better at: time management. Now to make the time to
actually read this book...
