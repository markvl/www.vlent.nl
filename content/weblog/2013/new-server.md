---
title: New home for this site
date: 2013-05-15 13:33
tags: [blog, devops]
---

Since early April 2013 this blog has moved from a shared hosting environment
to a VPS.

# Puppet

Ever since the
[deployment knowledge sharing session](/weblog/2011/06/20/deployment-knowledge-sharing-session/)
I attended in 2011, I have fallen in love with
[Puppet](http://www.puppetlabs.com/). About three months later I
started to use it in my day job. Unfortunately the investment to
completely provision our server with Puppet would be too high compared
to what we would gain.

But nothing stopped me from doing just that with my own VPS... So the
box this site now runs on, is completely configured using Puppet. The
only thing that I have not handled (yet?) is the actual content of
this site. That is a separate process handled by an
[Acrylamid](http://posativ.org/acrylamid/) task which I have to run
after provisioning the server.

To accomplish this, I have a directory which contains the following:

    .
    ├── install.sh
    ├── manifests
    │   └── atlanta.pp
    └── modules
        ├── firewall
        ├── ...
        └── webserver

The `install.sh` script contains these lines:

    apt-get update && apt-get -y upgrade
    apt-get -y install puppet
    puppet apply --modulepath=./modules manifests/atlanta.pp

So all I need to do is `scp` this directory to the VPS and run the
`install.sh` script and the server is ready. A quick "`acrylamid dp
atlanta`" command later and I am done. The whole process takes only a
few minutes.

# The process

Most of the Puppet configuration was created and tested locally. To do
this I have a [Vagrant](http://www.vagrantup.com/) box (which uses
[Virtualbox](https://www.virtualbox.org/)) with almost the same setup
as the VPS. I am using Ubuntu 12.04 64-bit on both the VPS and the
Vagrant box, but after a reinstall (before I run Puppet) the VPS is
still configured a bit different than the Vagrant box. So I had to
make some tweaks to the Puppet configuration after trying it out on
the VPS.

Once I was satisfied with the result, I started with a fresh install
of the VPS, ran Puppet and copied the content of this site over. A
small DNS change later and I was up and running. (Since I have a
static site and use [Disqus](http://disqus.com/) for commenting I did
not even have to worry about the DNS change propagation time.)

# What does Google think?

My main reason to move from shared hosting to a VPS was to get more
control over the environment and get more freedom. Still, better
performance also would not hurt.

## Time to download

This is what I saw in the
[Google Webmaster Tools](https://www.google.com/webmasters/tools/home):

![Time to download a page: April is significantly lower](/images/gwt-2013-04-time-downloading.png)

As you can see, the time to download a page has about halved since
April. My initial thought was that this is probably related to the
location of the server: the shared hosting environment ran on a server
in The Netherlands while the VPS is running in a data centre in
Atlanta in the USA. That might make a huge difference if the pages are
crawled from the USA.

I did some quick measurements to get *some* data. To make a long story
short: the VPS is indeed a bit faster. There are too many differences
between the previous situation on the shared hosting environment and
the VPS to be able to tell what caused this difference. But I *am*
happy to see the previous graph none the less.

## Other statistics

Besides a change in time to download a page, I also saw that Google
crawls more pages a day:

![Number of pages crawled per day increased in April](/images/gwt-2013-04-pages-crawled.png)

But since there is also an increase in March that I cannot explain, it
might be a coincidence that more pages were crawled per day since
early April.

What is remarkable is that there is less data downloaded per day while
more pages were crawled:

![Less data downloaded per day](/images/gwt-2013-04-kb-downloaded.png)

This can---most likely---be explained by changes I made. In the old
shared environment I had no specific configuration to cache
content. On the VPS I have configured Nginx to send an expiry time (by
adding "`expires 7d;`" to the configuration which sets the appropriate
`Expires` and `Cache-Control` headers for the response).


# Result

I got what I wanted: my site is running on an environment I can
completely control (from the operating system level up that is). This
allows for experimentation and perhaps even small side projects.

I also really liked tinkering with Puppet to get everything setup the
way I wanted it to. Both the sysadmin side of deciding how I wanted
things configured and the 'developer' side of achieving that
configuration via Puppet were fun.
