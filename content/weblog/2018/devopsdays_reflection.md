---
title: Devopsdays Amsterdam 2018: reflection
date: 2018-07-04
tags: [devops, docker, elastic, go, kubernetes]
---

About a week has past since devopsdays Amsterdam. Time to write down
some of my thoughts.


# The conference

This has been the third time I went to devopsdays Amsterdam. And I
love this conference!

Some of the reasons:

- The organizers manage to get great speakers with interesting talks
  on stage each year.
- [Pakhuis de Zwijger](https://dezwijger.nl/) is a great location.
- Excellent Wi-Fi.
- Great atmosphere.
- Good food.


# The workshops

## Go

I had heard about [Go](https://golang.org/), some of my co-workers
have some experience with it, but I never wrote anything in the
language. I was curious about it though.

The [workshop from Michael
Hausenblas](/weblog/2018/06/27/devopsdays-amsterdam-2018-workshops/#go-for-ops-michael-hausenblas-red-hat)
was a nice intro. Based on what he told and showed us I cannot say
that I expect that Go will replace Bash and Python for me. However, I
will make some time to actually write some code myself to get a better
feel for it.

## Monitoring with Elastic

We are already using the [Elastic
Stack](https://www.elastic.co/products) in some places, but I have not
used if for monitoring purposes. (I gravitate towards
[Prometheus](https://prometheus.io/) combined with
[Alertmanager](https://github.com/prometheus/alertmanager) for
alerting and [Grafana](https://grafana.com/) for dashboards with
graphs.) However, [Philipp Krenn showed
us](/weblog/2018/06/27/devopsdays-amsterdam-2018-workshops/#monitor-your-microservices-logs-metrics-pings-and-traces-philipp-krenn-elastic)
that you can also do very interesting things with
[Kibana](https://www.elastic.co/products/kibana) in the monitoring and
debugging realm. Especially since you can correlate metrics with logs
in the same tool.

## Kubernetes

I could say that [Bridget Kromhout's Kubernetes
workshop](/weblog/2018/06/27/devopsdays-amsterdam-2018-workshops/#kubernetes-101-bridget-kromhout-microsoft)
was a nice refresher of what I had learned in the [Kubernetes workshop
last
year](/weblog/2017/06/28/devopsdays-amsterdam-2017-day-zero-workshops/#introduction-to-kubernetes-andy-repton-schuberg-philis)
but, to be honest, that would be a lie. I am glad I took this
workshop.

It was a good workshop with lots of hands-on tasks. But it went a bit
too fast to make it stick. I would have to spend more time on a
Kubernetes cluster to really understand everything and get fluent with
it. Luckily there is lots of information on
[container.training](https://container.training/) (including the
sheets of this workshop) and there are plenty of cloud providers where
you can get a Kubernetes cluster without having to create or maintain
it yourself.


# The talks

The talk that resonated most with me this year was the one from [Waldo
Grunenwald about product
teams](/weblog/2018/06/29/devopsdays-amsterdam-2018-day-two/#that-product-team-really-brought-that-room-together-harold-waldo-grunenwald-datadog).
Perhaps because (in my opinion) this is something that could be better
in my job. Product management, development and operations are three
different teams with different managers. Then again, I currently try
to be the "ops guy" in our team so that's also DevOps, right? :)

The other most memorable talks for me were:

- [Bridget Kromhout's keynote: Cloud, containers, k8s ](/weblog/2018/06/28/devopsdays-amsterdam-2018-day-one/#cloud-containers-kubernetes-bridget-kromhout-microsoft)
- [Armon Dadgar on service meshes](/weblog/2018/06/28/devopsdays-amsterdam-2018-day-one/#service-mesh-for-microservices-armon-dadgar-hashicorp)
- [Jason Yee relating Dutch peculiarities to DevOps](/weblog/2018/06/28/devopsdays-amsterdam-2018-day-one/#going-dutch-observaties-over-nederlandse-cultuur-devops-jason-yee-datadog)
- [Lee Atchison about monitoring in a dynamic (cloud) environment](/weblog/2018/06/29/devopsdays-amsterdam-2018-day-two/#monitoring-the-dynamic-nature-of-cloud-computing-lee-atchison-new-relic)


# Miscellaneous

I have been using [Emacs](https://www.gnu.org/software/emacs/) for
quite a while. I was a [Vim](https://www.vim.org/) user in the past,
but switched somewhere between 2007 and 2009. (The first time I wrote
about Emacs here was in
[2009](/weblog/2009/05/03/using-git-when-developing-plone-applications/).)

I have tried [PyCharm](https://www.jetbrains.com/pycharm/) a couple of
times and it is a really nice editor with very useful features. It
just never stuck with me and I always went back to Emacs after a
while.

During the conference I used [Visual Studio
Code](https://code.visualstudio.com/) to write my notes. And I have to
say I quite liked it. I intend to also give it a go at work. Who
knows, I might even switch...
