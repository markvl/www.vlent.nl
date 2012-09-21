---
title: A simple Plone setup on Amazon EC2 and S3 (David Bain)
slug: a-simple-plone-setup-on-amazon-ec2-and-s3-david-bain
date: 2008-10-09 16:18
tags: [plone, ploneconf, ploneconf2008]
---

Taking advantage of Amazon's Elastic Compute Cloud (EC2) and Simple
Storage Service (S3).

EC2 is a system that connect lots of computers that act as a single
parellel one. You can get a virtual machine which can be scaled in
time (say only during working hours), quantity (more or less servers)
and power (you can choose between different types). EC2 is targeted at
developers and one can manage it programatically via the API. The
problem was that when you were not using it, your data was gone. Using
the Elastic Block Store (EBS) you can solve this. EBS can be seen as a
thumbdrive in the cloud. (Note that S3 differs from EBS: they have a
different API. You can for instance download stuff from your S3
directly, but the EBS is connected to your instance.)

Summarised in layman terms: you run a virtual machine, Amazon meters
your usage and you only pay for what you use.

The process in short:

- You get a certificate from Amazon Web Services
- Choose and install an Amazon Machine Image (AMI), e.g. Ubuntu, and
  Amazon starts measuring
- Use the virtual machine
- Stop the machine and Amazon stops the meter.

SPLEC is an initiative to have an easy persistent Plone solution for
EC2. The shell scripts use java to connect to EC2. ElasticFox is a
Firefox extension to interface with the API tools.

To get up-and-running:

- You need to generate a keypair.
- Launch your instance (see [alestic.com](http://alestic.com/) for
  information about different types of AMIs, you can also create your
  own AMI if you want to.)
- Log in with the generated keypair.
- Setup EBS. (Otherwise when stopping the instance, you need to make
  sure the data is stored on another instance that isn't going down.)
  Once this is done, you can mount and unmount the EBS.
- Deploy Plone (David created shell scripts for deployment.)

Notes:

- Amazon's Elastic IP can give you a static IP address which can be
  used for the DNS
- You can switch IP addresses between images (e.g. to have a stable
  machine running while getting another one ready to go live with an
  update).
