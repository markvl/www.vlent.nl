---
title: DockerCon EU 2017: day two
#date: 2017-10-18
#tags: [devops, docker, security, tools]
---

These are my notes of my second day at DockerCon.

Just as with
[yesterday's notes](/weblog/2017/10/17/dockercon-eu-2017-day-one/),
these are just notes and not summaries.


# General session

The general session was mostly devoted to modernizing traditional
applications, saving costs and customer success stories.

![DockerCon Europe 2017 General Session day 2](/images/dockerconeu17_gs2.jpg)


# Tips and Tricks of the Docker Captains --- Adrian Mouat (Container Solutions)

Several small tips and tricks.

## Daily development

You can configure the output of the "`docker ps`" or "`docker
container ls`" commands with the "`--format`" argument. You can also
put your preference for the formatting in your `~/.docker/config.json`
file under the `psFormat` property (see the documentation on
[configuration files](https://docs.docker.com/engine/reference/commandline/cli/#configuration-files). Warning,
this file also contains your passwords to Docker registries so **do not**
put it online.

Cleaning up:

  - Remove dangling images: `docker image prune`
  - Remove stopped containers: `docker container prune`
  - Remove unused volumes: `docker volume prune`
  - Remove unused networks: `docker network prune`
  - Remove all of the above: `docker system prune`

## Building images

The "`.`" at the end of a Docker `build` command means that the target
(the current directory in this case) is sent to the Docker Daemon as a
tarball. Use the `.dockerignore` file to exclude large directories.

Alpine is pretty small (5MB). Couple of gotchas though, like:

  - uses `musl` instead of `glibc`
  - uses its own package manager

If you are looking for an alternative, have a look at the Debian Slim
images like `debian:stretch-slim`. They are (at the moment) 30MB or
smaller.

If you build static binaries, you can put the binary in the scratch
image. Since there is no operating system on top of the kernel, you
cannot use user names. You can use IDs, `USER 65534` maps to the the
"nobody" user.

![Adrian Mouat showing a minimal image Dockerfile](/images/./dockerconeu17_adrian_mouat_1.jpg)


## Container lifecycle

Do not require containers to start in sequence. Instead have a
container wait for a service it depends on (including backoff) and
include this in the application itself or in a startup script.

When Docker stops a container, it sends a `SIGTERM` signal, waits for
10 seconds and then hard kills the container with a `SIGKILL`. If the
latter happens, you cannot tidy up properly (e.g. close network
connections, write a final log entry, etc). So try to prevent this.

[Tini](https://github.com/krallin/tini), used for signal forwarding,
is integrated in Docker now.

A benefit of healthchecks is that Swarm will only route to healthy
containers. Note that healthchecks are run _inside_ the container
itself, not on the host. This might mean you will have to install more
software in your image (e.g. `curl`).

## Security

To improve security, use a read-only file system by adding
`--read-only` to the `run` command. Use a
[tmpfs mount](https://docs.docker.com/engine/admin/volumes/tmpfs/) to
create writable locations where applications can write e.g. pid
files. The data written to the tmpfs mounts is kept in memory and not
stored persistently on the host.

![Adrian Mouat showing how to start a read-only Nginx container](/images/./dockerconeu17_adrian_mouat_2.jpg)


Users are not namespaced (by default). If an attacker breaks out of
the container via service running as root, the attacker is also root
on the host. So do not run as root! Create and set a `USER` in your
`Dockerfile` or use the `nobody` user.


To prevent using `sudo`, use [gosu](https://github.com/tianon/gosu)
instead.

It's nearly always a bad idea to run Docker in Docker (issues with
file systems and caching, image stores). Instead, mount the Docker
socket with "`-v /var/run/docker.sock:/var/run/docker.sock`". Be
aware: this is a security problem because there is less isolation
between the container and the host.


# Alpine Linux under the microscope --- Natanael Copa (Docker)

[Alpine Linux](https://alpinelinux.org/) uses the MIT licensed musl
libc which has a clean, modern codebase and is lightweight. It's
small, so what is missing?

  - Some GNU extensions
  - Lots of localization data
  - GNU bloat
  - Name Service Switch (NSS)
  - Network Services Library (libnsl)
  - 80+ CVEs ;-)

<figure>
  <img src="/images/dockerconeu17_natanael_copa.jpg" alt="Natanael Copa comparing the sizes of CentOS, Ubuntu and Alpine Linux Docker images" />
  <figcaption>
    Natanael Copa comparing the sizes of CentOS, Ubuntu and Alpine Linux Docker images
  </figcaption>
</figure>

Busybox is also part of Alpine Linux. It includes most of POSIX's
shells and utilities. It's pretty impressive how many tools are
squeezed into ~800KB.

Alpine created apk-tools because the traditional package managers were
not fast enough. It is faster than other package managers because it
is designed to read once and write once (compared to minimal 3 reads and 2
writes).

The `--no-cache` option was added to the package manager specifically
for Docker. It does not store cache information on disk. If you use
this flag, you do not need a cleanup step (in contrast to when you are
using `apt`).

With regards to security:

  - Alpine uses secure defaults,
  - has a smaller attack surface,
  - uses more secure components (musl, libressl), and
  - has a hardened kernel (unofficial fork of grsecurity).

When not to use Alpine? If you:

  - depend on precompiled (closed source) binaries
  - need good localization
  - want commercial support
  - need glibc/GNU specific behaviour


# Practical design patterns in Docker networking --- Dan Finneran (Docker)

Several types of network drivers:

  - **Null**: you can use this to blackhole your container.
  - **Host**: simplest, come out of the box (use
    `--net=host`). The container will connect its ports to the host.
  - **Bridge**: no flags needed (the default), connect to the
    internal bridge network. Containers can speak with each other, but
    nothing can speak with them or the other way around. <br />
    Using the `-p` flag you can expose ports. Only expose services
    that need to be exposed.
  - Swarm **overlay** networking: using VXLAN to create overlay network over
    the underlying network. The network is encrypted by default.

![Dan Finneran](/images/dockerconeu17_dan_finneran.jpg)

A relatively new addition is the **macvlan** driver. It provides a
hardware address to each container. You'll want this if you need to
connect to a VLAN network or have to deal with IPAM. It requires
promiscuous mode.

> The macvlan driver essentially makes a Docker container a first
> class citizen on the network.

You can have a separate data and control plane in your network on
hosts with multiple NICs. This provides physical and logical
separation of traffic.
