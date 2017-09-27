---
title: Check if Ansible playbook is running on an EC2 instance
date: 2017-09-27 21:27
tags: [ansible, ec2]
---

In one of my Ansible playbooks I needed to only execute a couple of
tasks if they were running on an EC2 instance.

The way I solved this was by checking the `ansible_bios_version`
fact. For example:

    - debug:
        msg: "This is an EC2 instance"
      when: "'amazon' in ansible_bios_version"

This is probably not perfect, but at least it worked for me at the
moment.

Note that the day after I needed this, Jeff Geerling posted an
alternative way to
[check if you are in AWS](https://www.jeffgeerling.com/blog/2017/quick-way-check-if-youre-aws-ansible-playbook).
