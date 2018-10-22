---
title: All Day DevOps conference
date: 2018-10-17
tags: [conference, devops, security]
---

[All Day DevOps](https://www.alldaydevops.com/) is a 24 hours long, online
conference about DevOps with 125 sessions in five tracks.

_Note: these are my notes. They are not necessarily representative or complete summaries of the talks._

# Container security monitoring using open source --- Madhu Akula (AppSecCo)

Why is container security monitoring  (CSM) important? An attacker could gain
access to one of your containers. Or you may be using an image from the Docker
Hub with malicious code. CSM can help you to take actions based on the
monitoring alerts.

For CSM it is important to collect your logs on a central location. Then you can
analyse them to find suspicious patterns. Based on the patterns we identified,
we can set thresholds and create pattern to trigger alerts.

How to look at logs? E.g. using commands like "`docker events`" or "`docker logs`."
Using "`docker diff <container>`" you can check which files have changed in your
container. Although not security specific, for system level monitoring you can
use [cAdvisor](https://github.com/google/cadvisor).

For security specific monitoring you can have a look at AppArmor, Auditd,
Elastic Beats (e.g. the
[auditd module](https://www.elastic.co/guide/en/beats/filebeat/current/filebeat-module-auditd.html))
and [Sysdig Falco](https://sysdig.com/opensource/falco/).

Sysdig Falco is not an enforcement tool, but an auditing and monitoring tool.
With Falco you can load rules that trigger on events, e.g. when a shell was
spawned or a sensitive file has been opened. Falco comes with rules, but you can
also customize rules yourself.

You can even create an automated defence to e.g. deploy new versions when an
alert triggers (as was shown in a demo).

# 7 Container design patterns you need to know --- Christian Melendez (Equinix)

Most of your problems are not unique, both in software development and container
usage. Having patterns makes it easier to communicate: they provide a shared
language to known problems. Having patterns also allows you to reuse shared
components (solutions).

## Patterns for a single container

### Single-container pattern

A base for other patterns.

- Establish resource boundaries
- Isolate resources from others
- Separate concerns --- the container only has one responsibility

### Sidecar pattern

Extend an application container with extra tools.

- Co-schedule the sidecar in the same node (same pod in the case of Kubernetes)
- Shared resources (volumes)

### Ambassador pattern

The ambassador is a broker or proxy between an application and consumers.

- Modular
- Reusable in other applications

### Adapter pattern

An application container to modify the interface of the application to e.g.
provide a consistent interface.

- Helps to set a communication standard
- Can translate between protocols
- Reusable modules, perhaps environment variables to configure behavior
- Examples: collect metrics, parse and store logs, custom health checks

## Multi-node patterns

Used to scale at the node level for loosely coupled applications. Communication
is via network calls. They are the base for microservices.

### Scatter/Gather pattern

Split a big task to into smaller tasks that can run simultaneous and combine the
results afterwards.

- Partial processing
- Multiple threads for requests and process
- Response time is the sum of all requests

### Leader election pattern

How to select a new leader when the old leader fails.

- Reuse, don't invent your own wheel
- Container implementations like etcd, Zookeeper and consul

### Work Queue

One manager container with multiple worker containers. The manger concurrently
distributes the tasks to the workers.

# How To Build An Effective Container-Based Local Development Environment --- Martino Fornasa (Kiratech)

Having a local development workflow is important:

- Easier onboarding
- Consistent software dependency management
- Environment similar to production
- Local testing (faster than waiting for CI tool)
- You build knowledge

Creating a local environment is _hard_. Lots of variables to take into account
like languages, preferences of developers, you need to keep allow a certain
flexibility.

A first attempt led to issues:

- Speed
- Sync issues
- Cleanup
- Resources (CPU/memory)

And people hated it.

Goals for a proper solution:

- Tune for performance and reusability.
- Allow people to use their preferred tools
- Make it easy to do the right thing.

When your target is Kubernetes, your development workflow should also take this
into account. Benefits of a Kubernetes workflow:

- Easier to setup complex environments
- Same/similar tools for development and deployment
- Each developer is able to run the full system (perhaps using external systems)

Three approaches:

- Auto rebuild the image on each code change, push to registry and deploy in the
  cluster. Related tools: [draft](https://draft.sh/) and
  [skaffold](https://github.com/GoogleContainerTools/skaffold). Skaffold is
  probably more convenient for interpreted languages.
- Run on cluster + sync the filesystem between the local system and the cluster.
  Higher risk of drift between local image and image built by your CI system.
  Tools: [skaffold](https://github.com/GoogleContainerTools/skaffold) and
  [ksync](https://github.com/vapor-ware/ksync).
- Run locally + develop against remote resources. Tool: [telepresence](https://www.telepresence.io/).

# DevSecOps Toolchain: Blocking Dangerous Containers --- Siamak Sadeghianfar (Red Hat) & Georgios Kryparos (Tink)

DevSecOps is a shift in both mindset (everyone is responsible for security) and
security work (security as code).

We've gone from running applications on hardware to running them in a VM using
a hypervisor. Then we started running applications in containers (which may or may not run in
a VM). Now the world is even more complex with container orchestrators. In
summary: many layers to take into account. And then we haven't even touched on
the registry for images...

Containers have brought good things (consistency from dev to production, faster
deployments), but they have also brought security concerns:

- isolation breakouts
- outdated apps and dependencies
- secret management is an additional headache
- auditing and monitoring are still issues we need to deal with

You need vulnerability scanners, configuration auditors, secret scanners and
traffic monitors on all levels: host, container engines, orchestrator and
registry.

Tools you can use to help you:

- [SonarQube](https://www.sonarqube.org/): code analysis.
- [Quay Security Scanner](https://coreos.com/quay-enterprise/docs/latest/security-scanning.html) (using [Clair](https://github.com/coreos/clair))
- [Aqua Container Security Platform](https://www.aquasec.com/products/aqua-container-security-platform/)

Takeaways:

- Automation! Shift security to the left.
- Shared visibility
- Train first, enforce later
- Collaboration between dev, sec and ops teams, but also e.g. quality assurance

# Zero Gain vs. Zero Loss: Practical Tales of Enterprise Decision-Making --- Amélie Koran (HHS)

Leadership would like to see as little loss as possible. Selling the value of
what you do on a day-to-day basis to others in the organization is important.

A "play" is an action you can take to a affect a certain outcome.
Examples: skills development and applicability of what you do to the mission of
the business.

## Play one: metaphors

Metaphors allow you to connect on a common touchstone. E.g. use physical
security measures as a metaphor for "cyber" security measures; executives can
conceptualize the former, but perhaps not the latter.

Don't talk tech, talk about something they are familiar with. Examples: risk,
saving money, spend a little to prevent a greater loss.

## Play two: participation

Having a seat at the table is valuable. Think about design sprints, strategy
sessions, budget planning sessions. This leads to deeper connections, reduces
communication barriers, creates more empathy and enables awareness.

## Play three: conceptualization

Defining stuff is important. Having a shared lexicon helps communication. The
terms and definitions enable knowledge sharing.

Clear communication has all kinds of benefits like reducing questions, stress
and anxiety.

## Story time

Why do people want dashboards? They would love to have a single number to give
them insight in how things are going. But what is the question that is to be
answered? What decision should the dashboard support? Is what is being presented
actionable?

Tips:

- Aim to reduce user errors (via good UX/UI)
- Automate tests
- Don't deploy to production, invest in development and test environments
- Perform root cause analysis for major issues
- Include the proper team members (for instance: include security people)

# Monitoring the easy way --- Daniel Barker (National Association of Insurance Commissioners)

Some definitions:

Observability
:   Based on the output the system state should be deterministic.

Controllability
:  Based on the input the system state should be deterministic.

Observability tools (in implementation order):

- Metrics aggregation
- Log aggregation
- Alerting and visualizations
- Distributed tracing (harder than the others to implement, not all systems need it)

Let's have a look at each of those tools.

## Metrics

Metrics aggregation tools:

- Prometheus, used a lot with Kubernetes
- Graphite
- InfluxDB
- OpenTSDB

The two last ones are great for long term storage for Prometheus.

OpenMetrics is a metrics exposition format. Implement your metrics once and
different products can understand them. Datadog is currently the only commercial
product that support this standard; it is still early days though.

## Logs

Log aggregation tools:

- Splunk (commercial)
- ELK stack
- Graylog
- FluentD (not log aggregation, but you can use it to replace Logstash in your
  ELK stack because it is a bit more efficient)

Tips:

- Assume your logs arrive in a random order in your log aggregation service so
  include a timestamp
- Use UTC for your timestamps
- Format logs in JSON
- Log _all_ application errors, don't eat them without logging them, otherwise
  you don't find out about them until your users start complaining
- Turn logging on
- Make the log messages human readable because they are meant to be read by humans
- Do not log informational/debug data in production
- Do not log anything a human cannot read or react on
- Only log significant events
- Do not print personally identifiable information (PII)

## Alerting and visualization

Only send alerts when action can be taken. Information is never an alert.

> You would not go running around the town square yelling the weather.

Visualization: you should be able to look at it and understand the system better.

Tools:

- Prometheus AlertManager
- Bosun
- Cabot
- StatsAgg (does a lot more than just alerting)
- Grafana
- Vizceral
- Flame graphs

## Distributed tracing

Track requests throughout the system

Tools:

- Zipkin
- Jaeger
- AppDash

More information on [monitoring.danbarker.codes](http://monitoring.danbarker.codes).

# Getting started with chaos engineering --- Ana Medina (Gremlin)

Definition of chaos engineering: thoughtful, planned experiments designed to
reveal the weakness in our systems.

Chaos engineering is **not** about unexpected or unmonitored experiments. It is
also **not** about creating outages.

> Like a vaccine, we inject harm to build immunity.

Use cases: outage reproduction, on-call training, strengthen products and battle
test infrastructure.

Prerequisites for chaos engineering:

- Monitoring and observability in place
- On-call and incident management (a good SRE practice in general)
- Know the cost of downtime per hour

You can inject chaos on all layers. Nice places to do it are e.g. elasticsearch,
cassandra, etc.

To get started with chaos engineering, pick one of the top 5 most critical
systems. Whiteboard the system and determine what experiment you want to run
(e.g. maximize CPU, kill processes, packet loss) and determine the blast radius
(for example only impact 1% of your traffic).

Chaos day is a dedicated day where the whole company focuses on resilience
There's a [tutorial on the Gremlin
site](https://www.gremlin.com/community/tutorials/planning-your-own-chaos-day/)
if you want help to plan your own chaos day.

Examples of experiments:

- Reproduce actual outage
- Datacenter failure
- Large traffic spikes
- Maxing out CPU and disk

Tools:

- [Chaos Monkey](https://github.com/Netflix/chaosmonkey)
- [Simian Army](https://github.com/Netflix/SimianArmy)
- [Kube Monkey](https://github.com/asobti/kube-monkey)
- [Litmus](https://github.com/openebs/litmus)
- [Powerfulseal](https://github.com/bloomberg/powerfulseal)
- [Gremlin](https://www.gremlin.com): failure as a service

# What is SRE and why every DevOps professional should care --- Dave Rensin (Google)

How do we choose between DevOps and SRE?

DevOps principles:

- Reduce organizational silos
- Accept failure as normal
- Implement gradual changes
- Leverage tooling and automation
- Measure everything (otherwise you run your business by luck)

SRE principles:

- Reliability is the most important feature of a system (_every_ system, not just software).
- The only measure that actually matters is the reliability experienced by your users.
- 100% is always the wrong goal all the time. (Your users also don't need 100%
  reliability, they won't even notice it.)

The space between 100% and your availability target (e.g. 99.99%) is called the
"error budget." If you achieve higher reliability than you targeted for, you
are wasting budget.

Terms:

SLI
:   A service level indicator tells us how our user is experiencing our system.

SLO
:   A service level objective is an SLI plus a goal.

SLA
:   A service level agreement, in contrast to SLI and SLO, points outward.
    SLA = SLO + margin + consequences. Purely a business discussion; there is no
    engineering involved.

SRE practices:

- Metrics & monitoring (are we measuring and alerting on the right thing?)
- Capacity planning
- Change management (consistency is important because you want to automate this)
- Emergency response
- Culture (toil management, engineering alignment, blamelessness)

Why choose between SRE and Devops? It is not one or the other. SRE is a
concrete, highly opinionated implementation of DevOps! (Also see the video
[class SRE implements
DevOps](https://www.youtube.com/watch?v=uTEL8Ff1Zvk&list=PLIivdWyY5sqJrKl7D2u-gmis8h9K66qoj).)
It provides a consistent and optimized way of implementing DevOps principles.

Some nice quotes:

> The closer to zero you can drive the blast radius of a mistake, the closer to
> infinity you can drive your risk.

(And SRE manages risk.)

> SRE is what happens when you ask a software engineer to design operations.

Take the SLO and calculate your error budget. Then apply risk analysis and
calculate how many bad minutes/year something cost (or could cost). Then you
start working on the items that are > 25% of your error budget. Tool to play
with this: [CRE Risk Analysis Template](https://docs.google.com/spreadsheets/d/1XTsPG79XCCiaOEMj8K4mgPg39ZWB1l5fzDc1aDjLW2Y/view)

How to start with SRE? The most important thing is willingness to do SRE. You
cannot adopt SRE unless you have executive buy-in. (Note that you 'only' need
buy-in, it does not work if executives enforce implementation.)

The next important thing is to pick **one** application (defined as a "discrete
failure domain") first. This will reduce the number of people you need buy-in
from. But it has to be a **meaningful** application, otherwise the lessons you
learn won't be internalized. Once the reliability and velocity are increasing
and the frustration between dev and ops is decreasing, others will want to do it
too!

When you have the willingness and know which application to work on, you start
with defining your SLIs, SLOs and error budgets. Answer the question "what do my
customers care about?" Pick the smallest number of things that answer that
question. So not "CPU utilization" but e.g. "latency of the application." Then
determine the first set of objectives. Also determine a policy, for instance: feature
freezes until you go below the error budget.

Note that the SLOs don't have to be perfect. You can re-evaluate them
periodically (monthly, quarterly for instance).

Now, before you do any engineering, get your alerting and monitoring in order.
Make sure you monitor the things that are relevant for your SLOs. Usually you
can turn off half of your alerts without impacting the experience of your user.
More alerting is almost never better. More logging and measurements _are_
(probably) better. Simple test: only alert on something _your customer_ would
want to be alerted on.

An important prerequisite for doing SRE is having a blameless culture! The
highest return on investment of a mistake is if you learn as much as possible
from it. You can only do that in a blameless culture.

Take one step at a time:

1. Define SLO, SLOs and error budgets
1. Audit and adjust monitoring and alerting
1. Model and reward blameless postmortems

If you do this, you will improve things!

More information: [google.com/sre](https://landing.google.com/sre/)

# DevSecOps - securing a great developer experience --- Stefan Streichsbier (GuardRails)

Some stats: 51% of the world's population has internet access (June 2017) and
there are 31 million developers on GitHub (October 2018).

> In the future every company will become a software company --- Marc Andreessen

Having a website used to be simple: you uploaded the needed files to your
hosting provider via FTP. There was no to little collaboration (just one "web
master"), no build steps (PHP, ASP, etc) and you tested by checking if there
were parse errors.

Now there is a whole bunch of additional (and different) steps required. There
are code repositories, build pipelines, several environments (test,
production). Deployment on e.g. a Kubernetes cluster is much more complex
than putting some files somewhere. And then there's the complexity of all the
development tools and all the products that the cloud providers offer.

So how does security fit in?

Michael Wittig wrote an [AWS security
primer](https://cloudonaut.io/aws-security-primer/) in which he has a mind map
of all security related tasks and activities there are in AWS. On [Hacker
News](https://news.ycombinator.com/item?id=14628108) someone posted a comment on
it:

> I've worked extensively with AWS over the last 4 years, and I can barely wrap
> my head around the scope of managing security in AWS. We have an entire
> department dedicated to security in our company, and none of them are remotely
> close to being experts in AWS security either. <br />
> I'm starting to get curious if there even is an expert who could set up and
> maintain a bulletproof AWS Account.

Steps in the evolution of security:

- Penetration testing
- Secure software development life cycle
- DevSecOps

Going to DevSecOps is not easy for typical security teams. They have to get into
the mindset of software development. Security tools are typically also not made
with developers in mind.

Tools are not everything. We need to have a proper workflow around it. We should
not "automate the nagging" by building in security tools in the development
pipeline.

Only a fraction of the 31 million developers on GitHub have access to
(enterprise grade) security tools and penetration testing.

Quality had to face some of the challenges security is currently facing. Quality
is now more and more a first class citizen.

Some definitions:

- Usability: can the user accomplish his/her goal very effectively when they
  interface with a product?
- User experience: everything around using a certain product
- Developer experience: user experience where your audience is exclusively developers.

To increase the developer experience with regards to security we have to keep
some things in mind:

- Signal vs noise
    - Security tools should not add more noise.
    - Instead it should focus on high impact issues.
    - Make sure that issues are reported with a high level of accuracy.
- Lost in translation
    - Security has to speak the same language as developers. Otherwise
      developers have to become security experts as well to understand what the
      security team is talking about.
    - Use the right communication channel. So not a PDF report or Excel sheet
      per email, but notifications in the workflow (e.g. in a pull request,
      issue, chat application).
    - Describe the issues clear so that developer know how to solve them.
- Make it easy
    - Make it simple to get started and try out (not: "schedule an appointment
      with our sales rep)
    - Tight integration with the workflow
    - Provide all functionality in one tool.

How to make security a part of DevOps?

- Acknowledge that developers are key. Tools should bring them joy using it and
  provide value.
- Respect that security is a complex topic but provide clear focus and make it easy
  to consume for developers.
- Security has to become a commodity, not just for big enterprises.
