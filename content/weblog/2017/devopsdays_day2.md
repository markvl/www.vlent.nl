---
title: DevOpsDays Amsterdam 2017: day two
date: 2017-06-30
tags: [devops, humanops]
---

These are the notes I took on the second conference day of DevOpsDays
Amsterdam 2017.


# Adapt or Die: how DevOps can (and should!) save the world --- Jody Wolfborn (Chef Software)

By practising DevOps principles, you can save the world (and not just our
own sanity).

Jody has her own definition of DevOps which includes that it is an
ideology, it focuses on how we build and how we operate and it is
about diversity of skills, knowledge and experience. In a DevOps
context, diversity can be defined as "a rainbow array of skills,
ideas, tools, experiences, backgrounds, and knowledge."

DevOps centres around four main ideas:

  - Scaleability
  - Flexibility
  - Responsibility
  - Portability

DevOps is about adding value to a system so that the system generates
value back.

Symptoms of systems gone wrong:

  - Uncontrollable growth
  - Brittle rigidity
  - Blame-shifting
  - Heavy, static and esoteric

What does this have to do with the world? The above symptoms can be
mapped to real world problems.

![Jody Wolfborn showing examples of systems gone wrong in the real world](/images/devopsdays2017_jody_wolfborn.jpg)

How to apply the DevOps main ideas in real world:

  - Scaleability:
    - Contribute back, e.g. ideas, or cutting back on your waste
      production.
    - Build empathic relationships.
    - Use tools that accelerate collaboration and affinity.
  - Flexibility:
    - Integrate opposing viewpoints into the approval process.
    - Connect the solutions to the problems.
    - Continuously iterate on and reevaluate priorities, assumptions
      and practices. Be flexible to change with your system.
  - Responsibility:
    - Don't assume anything (not even positive intent), ask!
    - No finger-pointing, rather decide on action to resolve issues.
    - Accept responsibility and seek feedback.
    - Enable the system to implement the changes it needs.
  - Portability:
    - Shadowing: view the full spectrum of the system.
    - Pairing: two people, one system.
    - Mentoring: distribute expertise.
    - Documentation and enablement share: make information stupid-easy
      to obtain.

You can implement DevOps practices without the business or system
knowing what DevOps is. Feed your knowledge and experience back into
the system and help others by doing so.


# Practical tips for defending web applications in the age of agile/DevOps --- Zane Lackey (Signal Sciences)

This talk is a collection of lessons Zane learned when working as
head of security at Etsy.

![Zane Lackey giving the TL;DR version of his talk](/images/devopsdays2017_zane_lackey.jpg)

Realities in the modern DevSecOps world:

  - Changes happen multiple of orders of magnitude faster than before
    (e.g. deployments _x_ times a day, instead of once per _y_
    months.)
  - Decentralised ownership of deployment. (It is no longer just ops
    doing the deployment after long journey via QA and security.)

Security can not be "outsourced" to the security team, it has to be
baked into the development/DevOps process.

SDLC components:

- Training
- Threat modelling
- Static analysis
- Pentesting
- etc.

This talk focused on a couple of them and compared the 'legacy'
approach with the modern take on them.

**Static analysis** has traditionally (in a waterfall model) been done
as heavyweight, top-down process. The resulted in massive reports with
mostly false positives and spending a long time on
tuning and configuration.

We can adapt this by going bottom-up:

  1. What vulnerability do we care about?
  1. Eliminate false positives.
  1. Include a check for this vulnerability in the process to prevent
     regression (which could be as simple as a `grep` over the code
     base by the way).

Pro tip: start with the easiest thing to implement and go from there.

Do not block changes, but for instance let developers know that a
certain change will notify these 4 senior persons in the
organisation. In a crisis situation that may be okay (because those
persons will also be in the same room to solve the crisis) but it
might also result in the developer thinking about it some more an
deciding to go with a different solution. Either way: security does
not get in the way.

**Dynamic scanning** was used to meet the baseline of discovering
vulnerabilities. Too little bang for the buck when used with modern
applications. However, you can modify it to ensure that security
policies are enforced (e.g check that the TLS configuration only
supporting strong ciphers, check for CSP or X-Frame-Options
headers). It can also function as an additional control on regression
test, for instance by having a scanner hit the search box with a known
XSS payload.

The legacy approach for **Security visibility**: collect logs, service
and outage reports and keep each source of information isolated
between groups. Modern approach: break down silos to give everyone
access to security relevant information in real time.

Example: if you get a lot of HTTP 500 errors, you might want to
investigate what change in you code could have caused them.
But if you can combine those error logs with metrics about SQL
injection logs, you might discover that the errors are related to
attacks, not a change in the code.

**Feedback** is typically done as annual pentests. That only tells you
if you have bugs. This used to be real-time enough with 1 or 2 release
per year.

A modern way to do this is to combine a bug bounty with a pentest. A
bug bounty is not a replacement, but an augmentation though! Bounties
are good for broad, continuous feedback. As a result your pentest can
be focused and deep.

When you have bug bounty projects: collect information on what is going
on. What are persons trying? What vulnerabilities get found but never
reported?

A success story of this approach: someone found an issue at Etsy but
didn't get around reporting it. When he wanted to make a write-up he
discovered that Etsy had already fixed the problem. (See
[Etsy has been one of the best companies I've reported holes to](https://www.reddit.com/r/netsec/comments/vbrzg/etsy_has_been_one_of_the_best_companies_ive/)
for more information.)

Modern security approach is a combination of continuous feedback and
visibility.

> You have to be able to answer the question "how do I know when my
> attackers are being successful?"

Pillars of effective visibility + continuous feedback:

  - ability to detect attackers as soon as possible in the attack chain.
  - ability to continuously test + refine vulnerability triage/response.
  - ability to continuously test and refine your incident response
    process.

Treat every benign bug report/outage as if it was an incident. Learn
from these exercises.


Modern application security is about shifting from having a (heavy)
process to guard bugs from ever reaching production (which is an
impossible goal) to having a focus on continuous visibility and
feedback, and providing capabilities to make developers/DevOps teams
security self sufficient.


# Data-driven incident reviews --- Jason Yee (Datadog)

The words "post mortem" have a negative connotation. Jason removed it
from the title and replaced it with "incident reviews", which is more
neutral.

![Jason Yee quoting Henry Ford: the only real mistake is the one from which we learn nothing](/images/devopsdays2017_jason_yee.jpg)

> Collecting data is cheap; not having it when you need can be expensive.

Four qualities of good metrics:

  - Must be well understood.
  - Sufficient granularity.
  - Tagged and filterable.
  - Long-lived.

Three types of data you should collect:

  - Work metrics (e.g. throughput, performance); this is what you _should_ get paged on.
  - Resource metrics (e.g. utilisation, saturation, availability);
    this is what most of us _currently_ page on, but this leads to alert
    fatigue. You want alerts on business metrics.
  - Events.

Tips:

  - Technical issues can have non-technical causes.
  - Don't do a post mortem until the incident is over.

Who are collecting data?

  - Responders (engineers)
  - Identifiers (people that witnessed the event and have an outside perspective)
  - Affected users

What data do you collect?

  - What they did.
  - What they thought.
  - Why they though/did it.

When writing things down, don't forget to include pictures. Don't just
write "we saw a spike in latency" but include a screenshot of the
graph.

When do you collect data?

  - As soon as possible, because:
    - Memory drops sharply within 20 minutes.
    - Susceptibility to "false memories" increases on an inverse
      curve: the longer you wait, the less reliable your memory.
    - Get your project managers involved!

Causes for data skew/corruption: fatigue, blame culture, biases.

Datadog emails the post mortems company wide (which means that for instance
marketing/sales may be able to use it when they contact
(potential) customers.) At Datadog they also schedule a monthly
recurring post mortem meeting (time to learn from each other plus sets
the expectation that they care about improving).

The Datadog post mortem template consists of the following items:

  1. Summary (What happened? What was the impact and severity? Which components? Etc.)
  1. How was the outage detected? (To speed up the time to detect the
     next outage. Did we have a metric to show the outage and was there a
     monitor for the metric?)
  1. How did we respond? (Who was involved? Slack archive links +
     timeline of events. What went well? What did not go so well?)
  1. Why did it happen?
  1. How do we prevent it in the future? (Include link to
     tickets. Think about what we need now, next sprint and later. Add
     follow up notes.)

Talking in a war room is great, but there is no archive. Being able to
use a chat archive after an outage can be useful for the
post mortem. You can also use it to create reminders for yourself to
address later.

Resources:

  - [Slides](https://drive.google.com/file/d/0B1IHl71JwnxFeF81cUFTRzJqN1U/view)
  - [Postmortem template](https://docs.google.com/document/d/1A8paeWbiPJBSVjj3yXhtygxtZk7r76H8g5DzFCzwZgE/edit)
  - [The Infinite Hows (or, the Dangers Of The Five Whys)](http://www.kitchensoap.com/2014/11/14/the-infinite-hows-or-the-dangers-of-the-five-whys/)


# Ignites

The concept of ignites: the speaker provides twenty slides and a new
slide is shown automatically every 15 seconds.

## Pipelines: breaking the wall between Dev and Ops --- Joep Weijers (TOPdesk)

A customer wanted a SaaS version of TOPdesk. The initial though: we
just deploy the on premise solution. However, this wasn't as easy as
thought. As a result, they put a developer next to an ops person to
improve the situation.

To get to continuous deployment, you have to cross three chasms:

- People (culture)
- Processes
- Tooling

At TOPdesk they created tooling to influence people + culture. They
visualised the pipeline to make it clear for developers that stuff
ends up on the production environment. As a result, development
realised that they have to talk to operations. This (largely) took
down the wall between the teams. Joep hopes that in the future it
will completely crumble down.


## In-line code documentation --- Arnab Sinha (TATA Consultancy Services)

Modern IT systems are complex and moving quite fast. Code bases look
like organised chaos. It is hard to find out what went wrong and hard
to find the right level of documentation

- How much to document?
- Where do we store it?
- How do we organise the documentation?

How can we reduce response time by improving documentation?

Arnab created a shell script to test the code vs documentation
ratio. This fails the build if there is not enough documentation. See
his GitHub repo at
[arnabsinha4u/in-line-code-documentation-demo](https://github.com/arnabsinha4u/in-line-code-documentation-demo)

## Business = IT --- Pavel Chunyayev (Levi9)

There is a separation between the business and IT. Devs want specs and
don't want/need the reason the business wants a feature. Business are
too busy to work with the team and explain the "why".

Developers need to learn the "why" of the company, because this is
needed to keep the company alive.

DevOps is about breaking the wall between Dev and Ops. However, there
is still a wall between the business and IT. We need to remove that
wall, because business **is** IT.


# Secret Management in the world of Infrastructure as Code --- Peter Souter (Puppet)

![Peter Souter](/images/devopsdays2017_peter_souter.jpg)

What defines secrets in infrastructure as code?

  - Small: only a few kb (with big files you are in the realm of protected data).
  - Radioactive: it's bad if they are leaked.
  - Required: your infrastructure won't work without them.

Worst case scenario: organisational catastrophe (ransom, data theft,
loss of customers, bad PR).

It is important to remove plain text secrets from your code (this
include tests in build pipelines).

Tools mentioned to search for secrets in your code:

  - [Truffle Hog](https://github.com/dxa4481/truffleHog): this tool
    will look for 'complex' strings and assume those are IDs or
    passwords. Probably lots of false positives.
  - [gittyleaks](https://github.com/kootenpv/gittyleaks): Basically
    the same idea as Truffle Hog.
  - [GitRob](http://michenriksen.com/blog/gitrob-putting-the-open-source-in-osint/):
    sort of a pentesting tool for GitHub organisations.
  - `grep`: Super simple, search for strings like "password", "email", etc.
  - [Danger.systems](http://danger.systems/ruby/)
  - [Hiera](https://docs.puppet.com/hiera/) / [Hiera-eyaml](https://github.com/voxpupuli/hiera-eyaml)

Note that it's not just the code that can leak secrets, commit
messages can also reveal information!

Once you have found all secrets, you will have to replace the
plain text versions with encrypted versions. Tools you can use:

  - Command line tools, for instance:
    - [GPG](https://www.gnupg.org/)
    - [SOPS](https://github.com/mozilla/sops)
    - [ejson](https://github.com/Shopify/ejson)
  - Secret servers, like:
    - [Vault](https://www.vaultproject.io/)
    - [Conjur](https://www.conjur.com/)
    - [Keywhiz](https://square.github.io/keywhiz/)
    - [Confidant](https://lyft.github.io/confidant/)
    - [CyberArk](https://www.cyberark.com/)
  - Cloud native secret services:
    - Amazon: [KMS](https://aws.amazon.com/kms/)
    - Google Cloud Platform: [Cloud KMS](https://cloud.google.com/kms/)
    - Azure: [Key Vault](https://azure.microsoft.com/nl-nl/services/key-vault/)
    - Openstack: [Barbican](https://wiki.openstack.org/wiki/Barbican)
  - VCS based encryption

Good summary: [Turtles All The Way Down: Storing Secrets in the Cloud and in the Data Center](https://danielsomerfield.github.io/turtles/).

Have a procedure for when secrets are leaked. There is no silver
bullet to detect leaked secrets! Tips:

  - [Scumblr](https://github.com/Netflix/Scumblr) can help you find
    leaked secrets.
  - Look for anomalies and outliers (logins from unexpected countries
    or at atypical times.
  - Use a host based intrusion system (HIDS).

Book tips:

  - <cite>The Secret History of Cyber War</cite>
  - <cite>Threat Modelling</cite>

Examples for security game days:

  - Give access to a server.
  - Laptop theft: give someone a standard workstation.

The idea is that you see how much damage the 'attacker' can do. And
how long it takes before it is detected? (**Is** it detected?)

Summary:

  - Leaking things is bad.
  - Remove plain text secrets.
  - Make sure data is kept secret.
  - Ensure secrets are kept secret.
  - Know what to do when things go wrong.
  - Move security left (part of the process, not afterthought).

The slides contain a bunch of interesting links on the last page.
