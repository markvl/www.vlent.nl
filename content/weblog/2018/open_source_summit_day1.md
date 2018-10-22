---
title: Open Source Summit Europe: day one
date: 2018-10-22
tags: [conference, devops, logging, monitoring, tools]
---

The first day of the Open Source Summit Europe 2018.

_These are just notes. They are not proper summaries of the talks._

# A Day in the Life of a Log Message: Navigating a Modern Distributed System --- Kyle Liberti & Josef Karasek (Red Hat)

Abstracted tools help us to make systems manageable. We layer abstractions on
top of each other.

Kafka is a publish/subscribe messaging system. It decouples the source of the
messages from the system where they are needed.

![Integrate distributed logging with Kafka](/images/osse18_kyle_liberti_and_josef_karasek.jpg)

Origin aggregated logging is a part of [OKD](https://www.okd.io/). It is based
on Elasticsearch, Fluentd and Kibana (EKF).

Taking a look at the journey of a log message, it first encounters a log
collector. This component can tag and enrich log messages. The message then goes
to a Kafka source connector, which imports data from external systems into Kafka
brokers. (There are many types of connectors.) These brokers are like post
boxes: messages are delivered there and other systems can pull them out.
Messages written to topics. Finally a Kafka sink connector is used to export
broker data to external systems, for instance Elasticsearch.

Kafka is not a cloud native application. Strimzi Operators integrate Kubernetes,
OKD and Kafka; it manages the Kafka deployment. The most important operator is
the cluster operator which manages Kafka, Kafka Connect, Zookeeper and
MirrorMaker.

([Slides](https://events.linuxfoundation.org/wp-content/uploads/2017/12/A-Day-in-the-Life-of-a-Log-Message-Navigating-a-Modern-Distributed-System-Kyle-Liberti-Josef-Karasek-Red-Hat-1.pdf))

# AIOps: Anomaly Detection with Prometheus --- Marcel Hild (Red Hat)

A quick intro to [Prometheus](https://prometheus.io/): Prometheus can pull
metrics from targets and store them in a time series database. It will push
alerts to the AlertManager, based on rules you specify.

For machine learning we need data. Prometheus is not configured to keep your
data for a long term. [Thanos](https://github.com/improbable-eng/thanos) is a
project for reliable historical data storage. Until it is production ready, you
can use [Influxdb](https://www.influxdata.com/time-series-platform/influxdb/).
Unfortunately it eats RAM for breakfast. You could instead store your metrics
using [Ceph](https://ceph.com/). This is also a future proof solution as it
provides a path to Thanos.

![Marcel Hild about experimenting with collected data](/images/osse18_marcel_hild.jpg)

[Prophet](https://facebook.github.io/prophet/) is a Python library to predict
future data and dynamic thresholds.

Interesting links:

- [Data Science on Prometheus Metrics](https://github.com/AICoE/DataScience-on-Prometheus-Metrics)
- [Prometheus Anomaly Detector](https://github.com/AICoE/prometheus-anomaly-detector)

([Slides](https://events.linuxfoundation.org/wp-content/uploads/2017/12/AIOps-Anomaly-Detection-with-Prometheus-Marcel-Hild-Red-Hat.pdf))

# Lifecycles, Versions, and System Administration, Oh My! --- Adam Samalik (Red Hat)

Packaging makes software integrated, tested, updated and easily installable.
Linux distributions pick versions of packages and put them in the same
lifecycle.

![Adam Samalik about packaging](/images/osse18_adam_samalik.jpg)

Containers are great, but they are not the solution for this problem. [Fedora
Modularity](https://docs.fedoraproject.org/en-US/modularity/) tries to provide a
solution. Its core concepts are:

- Packages: the core building blocks of Linux distributions
- Modules: logical groups of packages on independent lifecycles
- Defaults: you can use a specific version only when you want to
- Updates: respect your choice and won't automatically upgrade to a different stream.

The true benefits of containers are that you can run them (almost) anywhere and
build and test the images upfront. With apps in containers, the OS can be
immutable (see [CoreOS](https://coreos.com/),
[Silverblue](https://silverblue.fedoraproject.org/)).

# Introducing OpenFaaS Cloud, a Developer-Friendly CI/CD Pipeline for Serverless --- Alex Ellis (OpenFaaS project / VMware)

[OpenFaaS](https://www.openfaas.com/), functions as a service; serverless on
your terms. Used by dozens of companies.

Serverless is an architectural pattern. How do you arrange your compute and how
do you use it?

![Alex Ellis about application evolution](/images/osse18_alex_ellis.jpg)

Functions:

- are short lived
- have a single purpose
- have no state

These properties allow them to auto-scale.

Core values of OpenFaaS:

- Focus on developers first
- Operator friendly; simple as possible to get it up and running, no magic
  inside
- Community centric

([Slides](https://events.linuxfoundation.org/wp-content/uploads/2017/12/Introducing-OpenFaaS-Cloud-a-Developer-Friendly-CICD-Pipeline-for-Serverless-Alex-Ellis-OpenFaaS-project-VMware.pdf))

# Automated Testing for Infrastructure-as-a-code --- Florian Winkler (B1 Systems GmbH)

What (kind of) tools doe we use? A lot!

- Source control (Git, SVN)
- Predefined installation (Kickstart / autoYAST / preseed)
- Software and images (Koji, open build service, Kiwi)
- Installation tools (e.g. Cobbler, the Foreman)
- Configuration management (Puppet, Chef, Ansible)
- Enterprise tools (Red Had Satellite, SUSE Manager, Spacewalk)
- Containers (LXC, Docker, etc)
- IaaC tools (docker-compose, Docker swarm, Kubernetes, Vagrant, Terraform)
- CI/CD (Jenkins, GitLab CI)

Don't just use a tool and let it define your work. Define a goal, determine how
to achieve the goal and pick the tools that match what you actually need so they
work for you.

> Make use of automation, as much as you can.

![Florian Winkler about DevOps](/images/osse18_florian_winkler.jpg)

You can use a number of workflows:

- SCM polling: check if there is a commit and then start the build.
- Web hook: the SCM server hook triggers the build.
- External trigger: calling a URL which triggers the build.
- Ticket based workflow: updating a ticket triggers a new build.

([Slides](https://events.linuxfoundation.org/wp-content/uploads/2017/12/Automated-Testing-for-Infrastructure-as-a-code-Florian-Winkler-B1-Systems-GmbH.pdf))