---
title: "Fabric: easy deployment"
slug: fabric-easy-deployment
date: 2010-09-27 09:27
tags: [development, devops, django, plone, tools]
---

Initially I was a bit sceptic about
[Fabric](http://docs.fabfile.org/). After all, I'm already using
[buildout](http://www.buildout.org/) to manage projects. "How much
better can it get?" After watching the video of the
[Django Deployment Workshop](http://blip.tv/file/3632436) (held by
Jacob Kaplan-Moss at PyCon 2010 Atlanta), I finally decided to see for
myself what Fabric is all about.

# Setup

Like I said, I'm using buildout. So the first thing I need to do is
include Fabric in my buildout. There's probably other ways to
accomplish that, but this is the way I do it:

    [buildout]
    parts =
       ...
       fabric

    [fabric]
    recipe = zc.recipe.egg

    [versions]
    fabric = 0.9.2
    paramiko = 1.7.6
    pycrypto = 2.0.1

After running the buildout there's a `fab` executable available in the
`bin` directory. Now it's time to start thinking about what you want
Fabric to do. My initial version is a reflection of the steps I used
to handle manually. This results in the following code in
`<buildout>/fabfile.py`:

    from fabric.api import cd, env, local, run, sudo

    env.hosts = ['example.com']
    env.code_root = '/path/to/buildout'

    def push():
        """Push code to the authorative repo."""
        local('git push')
        local('git push --tags')

    def fetch():
        """Fetch tags"""
        with cd(env.code_root):
            run('git fetch --tags')

    def checkout(version):
        """Checkout a specfic version."""
        with cd(env.code_root):
            run('git checkout -q %s' % version)

    def backup():
        """Make a fresh backup."""
        with cd(env.code_root):
            run('bin/backup')

    def stop_app():
        """Stop the application."""
        with cd(env.code_root):
            run('bin/supervisorctl shutdown')

    def update_app():
        """Run buildout."""
        with cd(env.code_root):
            run('bin/buildout -q')
            run('bin/django migrate --all')

    def start_app():
        """Restart the application process"""
        with cd(env.code_root):
            run('bin/supervisord')

    def reload_webserver():
        """Reload the webserver configuration if it's still okay."""
        sudo('nginx -t')
        sudo('invoke-rc.d nginx reload')

    def deploy(version):
        """Full deploy of a new version."""
        push()
        fetch()
        backup()
        stop_app()
        checkout(version)
        update_app()
        start_app()
        reload_webserver()

Note that I deliberately split retrieving the right version of the
code (in the `fetch` function) and actually switching that version
code (in `checkout`). This is because fetching the code might fail or
take a bit longer, expecially since the repository is on my own
computer at home. So I make sure I've retrieved the requested version
before stopping the website.

The Nginx configuration for my website is also in the buildout. I want
to prevent the Nginx reload to fail bacause I've made a
mistake. Especially since that will also take down other sites on the
same server. So I have Nginx explicitly check the configuration before
doing the reload.

# Related issues

There are a few other issues needed for an easy deployment
process. The first is setting up an ssh keypair to log in on the
server without having to type a password. The password for this key is
stored in OS X's Keychain so that's pretty safe.

But to fetch the requested tag from the Git repository I need another
ssh keypair to include in my
[Gitosis](http://eagain.net/gitweb/?p=gitosis.git) configuration. For
ease of use this will be a passwordless key which only has read only
access to the website repository. (Should the key be abused by
someone, the damage will be limited.)

Another hurdle is restarting Nginx when I the configuration is
changed. I'm in the fortunate position that the website is hosted on
one of the servers of [Zest Software](http://zestsoftware.nl/), my
employer. So getting sudo rights isn't a problem (unless you
[lock yourself out of the server](/weblog/2010/09/06/locked-myself-out-root-account-ec2-ubuntu-instance/)
while updating the sudoers file ;-) ). Because the machine hosts other
services and sites, I don't want a passwordless solution here. So I
have to type one password every time I deploy.

The last related issue was reducing the output. I want to see as
little output as possible so error messages stand out more. This means
switching from
[infrae.subversion](http://pypi.python.org/pypi/infrae.subversion) to
[iw.recipe.subversion](http://pypi.python.org/pypi/iw.recipe.subversion)
in my case because the latter is more quiet. And I submitted a
[small change](http://github.com/zerok/zerokspot.gitrecipe/commit/6018fcbdd9ad5f516ab93dab2b2e4a5c27d5e28f)
to
[zerokspot.recipe.git](http://pypi.python.org/pypi/zerokspot.recipe.git)
to make it less verbose.

# Result

The output is still a bit too verbose, but it's acceptable for now:

    $ bin/fab deploy:2.13.5
    [example.com] Executing task 'deploy'
    [localhost] run: git push
    [localhost] run: git push --tags
    [example.com] run: git fetch --tags
    [example.com] err: From ssh://repo/vlent
    [example.com] err:  * [new tag]         2.13.5     -> 2.13.5
    [example.com] run: bin/backup
    [example.com] out: Starting the backup...
    [example.com] out: Archived in /home/mark/backups/vlent.nl/2010-09-26-09-26.tar.gz
    [example.com] run: bin/supervisorctl shutdown
    [example.com] out: Shut down
    [example.com] run: git checkout -q 2.13.5
    [example.com] run: bin/buildout -q
    [example.com] run: bin/supervisord
    [example.com] sudo: nginx -t
    Password for mark@example.com:
    [example.com] err: the configuration file /etc/nginx/nginx.conf syntax is ok
    [example.com] err: configuration file /etc/nginx/nginx.conf test is successful
    [example.com] sudo: invoke-rc.d nginx reload
    [example.com] err: the configuration file /etc/nginx/nginx.conf syntax is ok
    [example.com] err: configuration file /etc/nginx/nginx.conf test is successful
    [example.com] out: Reloading nginx configuration: nginx.

    Done.
    Disconnecting from example.com... done.

The end result makes me very happy. The combination of
[zest.releaser](http://pypi.python.org/pypi/zest.releaser) and Fabric
means I can quickly release and deploy a new version of my
website. Which means it's even easier now to incrementally develop
stuff and push it out as soon as it's working.

# Next

I've currently got this setup for a couple of Django projects now, but
it will most likely also work great for Plone based sites. Although at
work we don't release new versions as often was I do for my own site,
automating it with Fabric not only makes things easier, it also makes
deployment more reliable in the sense that you cannot forget steps
(like making a backup or reloading the Nginx configuration).
