---
title: All Day DevOps conference
date: 2018-10-17
tags: [devops]
---

[All Day DevOps](https://www.alldaydevops.com/) is a 24 hours long, online
conference about DevOps with 125 sessions in five tracks.

_Note: these are my notes. They are not necessarily representative or complete summaries of the talks._

_Note 2: The conference is still going on. I'll update this article when I have more notes._

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

- [SonarCube](https://www.sonarqube.org/): code analysis.
- [Quay Security Scanner](https://coreos.com/quay-enterprise/docs/latest/security-scanning.html) (using [Clair](https://github.com/coreos/clair))
- [Aqua Container Security Platform](https://www.aquasec.com/products/aqua-container-security-platform/)

Takeaways:

- Automation! Shift security to the left.
- Shared visibility
- Train first, enforce later
- Collaboration between dev, sec and ops teams, but also e.g. quality assurance
