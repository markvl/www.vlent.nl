---
title: "Deployment knowledge sharing session: release management + buildout + puppet"
slug: deployment-knowledge-sharing-session
date: 2011-06-20 11:31
tags: [devops, django, plone]
---

On June 16th Jan-Jaap Driessen from
[The Health Agency](http://www.thehealthagency.com/) (THA) organised a
meeting to share knowledge about using Puppet, zc.buildout, release
management and how those are related. For the most part, Jan-Jaap
showed us his setup. My impression in one word: wow! They are running
a tight ship at THA!

# Puppet

Edd Dumbill wrote the article
[We're all ops people now](http://times.usefulinc.com/2008/06/16-ops-now)
in June 2008. Although Jan-Jaap didn't refer to this article, he did
expressed a similar opinion: the days where developers toss code over
the wall and expect the system administrator to deploy it, are
over. At THA they took it one step further: the developers are
managing the server themselves now.

A configuration management system like
[Puppet](http://www.puppetlabs.com/) "comes in handy." Amongst the
benefits are documentation of your configuration and the fact that all
systems are configured the same (you cannot forget to e.g. update that
one file on that one server).

Jan-Jaap described their setup. They manage everything with Puppet:
which packages to install, backup configuration, network devices,
users, bash profile settings, vim configuration and a whole lot
more. THA even configures which applications are deployed on which
server in Puppet.

Although it is possible to push updates of packages to servers with
Puppet (see a discussion about
[ensuring a packages is newer than version X](http://www.mailinglistarchive.com/html/puppet-users@googlegroups.com/2011-05/msg00374.html)),
THA isn't using it right now.

Tips for Puppet:

- [Pro Puppet](http://www.apress.com/9781430230571), by James Turnbull
  and Jeffrey McCune, is a good read.
- Check out [Puppet Forge](http://forge.puppetlabs.com/) for Puppet
  modules.
- Use [Vagrant](http://vagrantup.com/) to setup
  [VirtualBox](http://www.virtualbox.org/) instances to experiment
  with Puppet. Check out [Vagrantbox.es](http://www.vagrantbox.es/)
  for base boxes.
- Put a header in the files that you control with Puppet. Otherwise
  you might make a change in a file without knowing that Puppet will
  change the file somewhere in the future.
- If you need to experiment with a change in a file managed by Puppet,
  make sure that Puppet is temporarily disabled.

# zc.buildout

The applications at THA are deployed with
[zc.buildout](http://www.buildout.org/). With buildout you can create
isolated environments for your applications. I won't go into details
about why buildout is such a great piece of software. Reinout van Rees
wrote a series about
[software release managment](http://reinout.vanrees.org/weblog/tags/softwarereleasesseries.html)
and he quite nicely describes buildout in his article
[Isolation and repeatability with buildout](http://reinout.vanrees.org/weblog/2010/04/14/buildout.html).

Jan-Jaap mentioned a couple of useful packages:

- [z3c.checkversions](http://pypi.python.org/pypi/z3c.checkversions/0.4.1)
  to check if there are updates for the packages you have pinned in
  your buildout configuration.
- [mr.developer](http://pypi.python.org/pypi/mr.developer) to work on
  your own packages.
- [pywatch](http://pypi.python.org/pypi/pywatch) to run a command if a
  file changes.

# Release management

To properly deploy your applications, you should at least tag the
software you deploy. To help with releasing your software, check out
these packages:

- [zest.releaser](http://pypi.python.org/pypi/zest.releaser) to
  release your packages.
- [gocept.zestreleaser.customupload](http://pypi.python.org/pypi/gocept.zestreleaser.customupload)
  to upload (scp) your packages to a configurable destination.

Don't forget that you should also tag your buildout so you can deploy
a specific version of your application.

# Tying it together

The release management and buildout parts are geared towards the
application (user), while the Puppet configuration is more related to
the underlying system (root). Tying those two together also happens in
Puppet.

By having e.g. the Apache configuration files also in your buildout
(using
[collective.recipe.template](http://pypi.python.org/pypi/collective.recipe.template))
you only have to define the ports on which the application is running
in one place: your buildout configuration. And using Puppet to symlink
the generated configuration to the right locations, connects the
application to the system.

So Puppet makes sure that the right applications are on the right
machines (doing the checkout, running buildout, etcetera). And it also
makes sure everything is connected to the right system configuration.

# Monitoring

Jan-Jaap described a couple of standard tools to monitor the setup:
[Nagios](http://www.nagios.org/),
[Munin](http://munin-monitoring.org/), and
[Puppet dashboard](http://projects.puppetlabs.com/projects/dashboard)

THA also uses a custom made application to give them insight in their
applications. It tells them on which server an application is running,
which port number(s) it uses, which version of the application is
deployed and (really cool!) an overview of which versions of which
Python packages are in use. With the last is't really easy to see that
only application A is still using version x.y.z of package P. This
data is gathered on-the-fly (that is, once an hour if I recall
correctly) from the actual applications that are running on the
servers. Jan-Jaap will try to make this application publicly
available.

# Now it's my turn

Jan-Jaap really inspired me with his presentation! I would really like
to optimize things at my company,
[Edition1](http://www.edition1.nl/). Things are going fine, but
processes can always be optimized.

For instance, we do have proper release management for
[SwordFish](http://www.swordfish.nl/) in place. But for our older
customers we haven't made releases (or tags) of their custom products
or buildouts.

I'd also like to start using Puppet to manage our servers. Although
we've put configuration files in our version control system, we still
have to update our servers manually. I'm note sure yet if I'll want to
configure the deployment of our applications in Puppet though. I also
like [Fabric](http://fabfile.org/) to automate deployment.

On the monitoring department I would like to add Munin to our
setup. And definitely some application (preferably (re)using the one
from THA) to generate an overview of applications, ports, etcetera
running on our servers. We are now manually maintaining such a list
and it's real easy to make a mistake or forget to update it...

Finally I'd like to thank Jan-Jaap for taking the initiative of
organising the meeting and being so open and detailed about the
process and setup of THA!

**Update (2012-04-27)**: I am now using
[Whiskers](http://pypi.python.org/pypi/whiskers/) and
[buildout.sendpickedversions](http://pypi.python.org/pypi/buildout.sendpickedversions)
to generate an overview of which packages (and versions) are used by
which buildouts. See the blog entry
[Whiskers and buildout.sendpickedversions](/weblog/2012/04/27/whiskers-and-buildoutsendpickedversions/)
for more information.
