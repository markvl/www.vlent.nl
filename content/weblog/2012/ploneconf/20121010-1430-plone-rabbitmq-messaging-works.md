---
title: Plone, RabbitMQ and messaging that just works (Asko Soukka and Jukka Ojaniemi)
slug: plone-rabbitmq-messaging-just-works-asko-soukka-jukka-ojaniemi
date: 2012-10-10 14:30
tags: [plone, ploneconf]
---

Performing asynchronous tasks with Plone using message queues.

The speakers had to connect to difference services, some using
XML-RPC, others HTTP and yet others via SQL. They needed a reliable,
effective and scalable solution. The best solution was using
[RabbitMQ](http://www.rabbitmq.com/) as an external message
broker. RabbitMQ implements the Advanced Message Queue Protocol (AMQP)
open standard and is written in Erlang. It is industry tested and
reliable.

You can compare AMQP with a mailbox: stuff gets put in and something
else picks up the messages some unknown time later.

Some definitions:

   - A *Message* consists of label and payload.
   - A *Producer* is a program which sends messages to exchange
   - A *Consumer* is a program which mostly waits to receive messages.
   - An *Exchange* receives the messages from producers and pushes them to queues.
   - A *Bindings* are how the messages get routed from the exchange to a queue.
   - A *Queue* is a buffer that stores messages.

To make this easier in Plone, you can use
[collective.zamqp](http://pypi.python.org/pypi/collective.zamqp/). The
package is currently available via a
[personal GitHub repository](https://github.com/datakurre/collective.zamqp),
but it will be moved to the Collective in the future. It does not
require a lot of code to make use of a message queue.

Example code:
[collective.zamqpdemo](https://github.com/datakurre/collective.zamqpdemo),
[chatbehavior](https://github.com/datakurre/chatbehavior)

The [slides of this talk](http://goo.gl/RDYZc) are available.
