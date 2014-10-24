---
title: How we use Virtualenv, Buildout and Docker
date: 2014-09-28 21:53
tags: [development, devops, django, tools]
---

There are several technologies (in the Python world) to have isolated
environments for projects. In this article I will describe how we use
Virtualenv, Buildout and Docker for a project I'm working on at
[Fox-IT](https://www.fox-it.com).

# Virtualenv

The first tool I'll discuss here is
[Virtualenv](https://virtualenv.pypa.io/). According to its
documentation Virtualenv is <q>a tool to create isolated Python
environments.</q>

## What does it do?

It offers a way to install Python packages independent of the global
`site-packages` directory. This provides you with a way to install
packages even when you do not have permission to write in the global
`site-packages` directory *and* it will prevent conflicts with
packages installed there (or in other Virtualenv environments for that
matter).

For instance on my current Ubuntu 14.04 installation has the
[requests](https://pypi.python.org/pypi/requests/) package globally
installed. However, it is version 2.2.1. What if I need a newer
version? Or worse: what if my code is incompatible with a newer
version and the package is updated for some reason (perhaps with a
system upgrade)?

## How do we use it?

For the project I'm working on, we have a couple of small tools
written in Python that we need running in their own separate
environment (on different machines than the code of the main
application). For these tools, creating a virtualenv seems the best
solution. To make it easier to setup the virtualenv, we have a
`Makefile` sitting next to the `setup.py` file:

    lib/python2.7/site-packages/foo.bar.egg-link: bin/python
    	bin/python setup.py develop

    bin/python:
    	virtualenv --clear .
    	bin/pip install -r requirements.txt

    clean:
    	rm -rf bin include lib local dist

This way we can be certain that we have an isolated environment with
the packages we need for this tool (and with the right versions).


# Buildout

Another tool we use is [Buildout](http://www.buildout.org/). This is a
<q>Python-based build system for creating, assembling and deploying
applications from multiple parts, some of which may be
non-Python-based.</q>

## What does it do?

In contrast to Virtualenv, Buildout does not just create an isolated
environment for your project, but it is also a complete build
tool. Since there are many
[Buildout recipes](https://pypi.python.org/pypi?%3Aaction=search&term=buildout+recipe&submit=search)
available for all kinds of jobs---for instance to
[generate text files from a template](https://pypi.python.org/pypi/collective.recipe.template/),
[install Django](https://pypi.python.org/pypi/djangorecipe/),
[execute commands](https://pypi.python.org/pypi/collective.recipe.cmd/)
or to
[install user cronjobs](https://pypi.python.org/pypi/z3c.recipe.usercrontab/)---it
is as versatile as for instance a `Makefile` or a shell script. This
also makes the learning curve for Buildout a bit more steep than
for Virtualenv.

## How do we use it?

For the application I'm currently working on, we use Buildout to build
the components of the system. One of these components is Django, so
we've got this part in our Buildout configuration:

    [django]
    recipe = djangorecipe
    settings = production
    eggs =
        Django
        ${buildout:eggs}
        ${buildout:dev-eggs}
    extra-paths =
    project = my_project
    wsgi = true
    wsgi-script = ../my_project/wsgi.py

But we also generate the Nginx and
[Circus](https://pypi.python.org/pypi/circus/) configuration using
Buildout:

    [circus_ini]
    recipe = collective.recipe.template
    input = templates/circus.ini.in
    output = ${buildout:parts-directory}/conf/circus.ini

    [nginx_conf]
    recipe = collective.recipe.template
    input = templates/nginx.conf.in
    output = ${buildout:parts-directory}/conf/nginx.conf

This is convenient for us since, amongst other things, we need to
configure a port in both configurations. So the Circus template
contains this section:

    [socket:django]
    host = 127.0.0.1
    port = ${custom:webapp_port}

And the Nginx configuration template contains this section:

    upstream django {
        server 127.0.0.1:${custom:webapp_port};
    }

This port number set in our Buildout configuration file:

    [custom]
    webapp_port = 8080

Whenever we build the project, the Nginx and Circus configurations are
generated using that single variable. This makes it nice and
[DRY](http://en.wikipedia.org/wiki/Don't_repeat_yourself).


# Docker

[Docker](https://www.docker.com/) works on a whole different level to
isolate your environment. Docker is <q>an open platform for developers
and sysadmins to build, ship, and run distributed applications.</q>

## What does it do?

Docker allows you to launch containers to run your applications
in. These containers are based on images and these images can either
be existing images (e.g. from [Docker Hub](https://hub.docker.com/)) or
custom made images.

Using Docker is different from using a virtual machine because it does
not include a complete guest operating system. Instead it just runs
the application in an isolated process and shares the kernel with the
other containers. Or as they put it themselves: <q>it enjoys the
resource isolation and allocation benefits of VMs but is much more
portable and efficient.</q>

<figure>
  <img src="/images/vm-vs-docker.png" alt="VMs vs Docker containers" />
  <figcaption>
    How Docker, on the left, is different from virtual machines, on the right
    (images from the <a href="https://www.docker.com/whatisdocker/#compare-block">Docker documentation</a>)
  </figcaption>
</figure>

## How do we use it?

The application that is being built with Buildout, needs to be
deployed for multiple customers. To handle this deployment, we use
Docker. We create a custom image and make sure that Buildout does
its thing by having a line similar to this in our `Dockerfile`:

    RUN cd /var/application && python bootstrap.py && bin/buildout

Earlier in the `Dockerfile` we make sure that the application code is
extracted to the `/var/application` directory. The `Dockerfile` also
includes commands to install packages we need on the operating system
level, for instance Nginx.

This way we have an image that contains a version of our application
(and its dependencies) that is good to go. Now all we need to do is
run Docker using this image. By adding environment variables, we have
slightly different settings per customer.


# Conclusion

The tools discussed above (Virtualenv, Buildout and Docker) can all be
used to create an isolated environment for your project. In that
regard they are similar, but at the same time these tools are also
(completely) different.

They all have different features so which tool is the 'best' solution
absolutely depends on your situation. And as you can see in this article:
you don't have to chose just one.

The way I would personally 'categorise' them:

- If a project just needs a couple of Python packages, Virtualenv is
  probably a good fit.
- If the project is more complex, Buildout provides the tools to set
  up the environment.
- If the project needs to have a reproducible environment that also
  requires packages/configuration on the operating system level,
  Docker might be the way to go.
