---
title: DockerCon EU 2017: day one
date: 2017-10-17
tags: [conference, devops, docker, security, tools]
---

These are my notes of my first day at DockerCon.

Where I usually try to make summaries of conference talks I attend,
I've only made notes for this conference. Most, if not all, talks have
been recorded as far as I know, so you should be able to watch them to
place the notes into context.

# General session

In the context of "MTA" (modernize traditional applications) we saw a
demo of how easy it is to convert legacy applications with the Docker
application converter (dac). In the demo they showed how the tool can
generate a `Dockerfile` from a tarball of a Java application.

Not everyone is using Swarm. Unfortunately, using a different
orchestration tool means that you do not have the seamless integration
that Swarm has. However, the next version of Docker will have native
integration for both Swarm and Kubernetes.

![Kubernetes will have native support in Docker](/images/dockerconeu17_native_kubernetes.jpg)

This way you can still use the same tools and workflow while being
able to choose between Swarm and Kubernetes. It also means you can
still use your `docker-compose.yml` files.

**Update 2017-10-19:** I now understand that Docker CE will only
include Kubernetes in Docker for Windows and Docker for Mac because
those platforms use LinuxKit. Docker is not clear on how/when
Kubernetes will supported on Linux.

![Kubernetes supported in Docker CE for Windows and Mac](/images/dockerconeu17_kubernetes_win_mac.jpg)


# Hacked! Run time security for containers --- Gianluca Borello (Sysdig)

A container is ephemeral and you don't need to protect it. You want
to protect the application/service instead.

SELinux is very powerful, but difficult to master. And thus people
often turn it off. To avoid users turning off or circumventing
security measures, one should reduce friction.

Forensics on containers is difficult, for instance because containers
may only live for a few minutes.

To build a security framework, you need to:

  - observe, e.g. using Sysdig
  - understand the services, e.g. using Sysdig ServiceVision
  - detect bad behaviour, e.g. using [Sysdig Falco](https://www.sysdig.org/falco/)

![Gianluca explaining what you need to build a security framework](/images/dockerconeu17_gianluca_borello.jpg)

Gianluca demonstrated that Falco can detect e.g. network activity
performed by known binaries that are not supposed to send or receive
data over the network.


Sysdig maintains a ruleset for Falco. They update it weekly.  They are
also experimenting with automatic ruleset creation based on normal
behaviour of a container.

[Sysdig Secure](https://sysdig.com/product/secure/): A new product to
provide run-time security for containers. You can define policies when
to trigger an event. You can also store Sysdig captures so that you
can see what happened _before_ the event triggered.

[Sysdig Inspect](https://sysdig.com/blog/sysdig-inspect/) is a UI
around open source Sysdig tool to analyse Sysdig captures.


Sysdig has a low overhead (different from strace). It is meant to run
24/7 on production systems.


# Docker?!?! But I'm a SysAdmin --- Mike Coleman (Docker)

There was a contest to create the smallest Docker container that
printed out "Hello world". The result was an image of only 64
kilobyte.

Security is about more than just isolation. For instance: where did
the images come from, are they up to date, how do you deal with
sensitive data and/or passwords?

Docker for AWS and Docker for Azure have integration for those
platforms. They offer more than installing standard Docker on an
EC2 instance.

![Mike Coleman about some of the considerations you have to make](/images/dockerconeu17_mike_coleman.jpg)

When you start integrating Docker into your environment, don't forget
to change your processes. Think about our backup and recovery
strategies, etcetera.

Mike encourages us to share our knowledge, and our missteps.


# Creating effective images --- Abby Fuller (AWS)

This is a talk about disk space.

Smaller images mean faster builds and deploys, but also a smaller
attack surface.

Some tips:

  - Use shared base image where possible.
  - Limit the data written to the container layer.
  - Chain `RUN` statements.
  - Prevent cache misses at build for as long a possible.

To prevent cache misses, put all static stuff first (labels, etc). You
really want to make sure that you use the cache as much as possible.

Read the documentation about the [build cache](https://docs.docker.com/engine/userguide/eng-image/dockerfile_best-practices/#build-cache).

Pick your base images wisely. You can go for a minimal OS, but there
are also reasons for wanting a full base OS:

  - Security (with a minimal image, you have to roll your own)
  - Compliance
  - Ease of deployment (a minimal image can mean extra work)

(Note to self: have a look at the
[ONBUILD](https://docs.docker.com/engine/reference/builder/#onbuild)
command.)

Some random notes:

  - MSI installations (for Windows images) are not space efficient.
  - Coming up soon: run Linux containers "as-is" on Windows.
  - Switching users also adds another layer.
  - Where possible use two images: one to build an artefact, one to build an image.
  - `scratch` is a special, empty Docker image. Use this to build your own base images.
  - Use a [.dockerignore](https://docs.docker.com/engine/reference/builder/#dockerignore-file) file.

![Abby Fuller with tips for creating Docker images](/images/dockerconeu17_abby_fuller.jpg)

Cleaning up:

  - `docker image prune -a`: Remove danging images
  - `docker system prune -a`: Also remove untagged volumes, etc.
  - Make sure your orchestration platform is garbage collecting.

Recap:

  - Less layers is more
  - Choose or build your base wisely
  - Not all languages should build the same
  - Keep it simple, avoid extras (e.g. use `apt install --no-install-recommends`)
  - Tools are here to help


# Docker 500: Going fast while protecting data -- Diogo Mónica (Docker)

Security means "a state of being free from danger or threat". But as
soon as we connect something to a network, we are exposing it to
threats. So it would be better to talk about "safety" since that is
about "being protected from or unlikely to cause danger, risk or
injury."

![Diogo Mónica about going as fast as possible, safely](/images/dockerconeu17_diogo_monica.jpg)

The "Docker 500" from the title is a play on the [Indy 500](https://en.wikipedia.org/wiki/Indianapolis_500)

While there can be horrible accidents in the Indy 500, the drivers
often can just walk away from their car. We must architect our systems
to protect our data, just like the drivers are protected in the Indy
500.

In racing, two categories of measures are taken: before the crash and
after/during the crash.

If we translate the pre-crash measures to our world, we'd get
something like this:

  - Test: create a trusted, repeatable and **adversarial** CI/CD
    pipeline. Unless you have adversarial tests, you are effectively
    testing in production.
  - Design applications to segment portions of their infrastructure
    (microsegmentation).
  - Practice worst case scenarios. For example: if a secret (key) is
    leaked, can you revoke trust of that secret in under X time?
  - Reverse uptime! Have a maximum uptime for a server. Note that this
    is also good for operations because the machines don't get a
    chance to drift.

Measures after/during a crash:

  - Freeze the container (disk and memory state), solve the problem
    and inspect the frozen container later.
  - Automatic scaling.
  - Sandbox by default (by putting it in Docker).  Make sure that data
    cannot be operated outside your data center by so called
    "crypto-anchors" (a term coined by Diogo) via e.g. a hardware
    security module.
  - Role based access control + visibility
  - Have data about the crash. This is where the Docker security
    ecosystem shines.

Access to the data should not just be secure, but also safe. With careful
engineering you can be fast and safe at the same time.

Note that containerd can freeze memory and push to a registry. For
freezing the disk you can use `commit` and then push to a registry.
