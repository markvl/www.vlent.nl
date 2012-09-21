---
title: Locked myself out of root account on EC2 Ubuntu instance
slug: locked-myself-out-root-account-ec2-ubuntu-instance
date: 2010-09-06 10:27
tags: [devops, ubuntu]
---

This is a short recap of how I managed to lock myself out of the root
account of an Amazon EC2 Ubuntu instance and how I gained control
again.

Let's first start with what happened. My goal was to add user "mark"
to the `/etc/sudoers` file so I could restart the web server (running
on port 80) from that account. It was going to be the last thing I
would do for that day.

I logged in as user "ubuntu" on the machine, sudoed to root and edited
the `/etc/sudoers` file with visudo. I logged out again, and logged in
as mark and tried to sudo something. That didn't work: "`mark is not
in the sudoers file.`" My first thought was that I must have made a
typo while editing the `/etc/sudoers` file. So all I needed to do was
to log in as user ubuntu, become root again and fix the file. Just
five more minutes and then off to bed.

When I had typed "`sudo su`" as ubuntu and was prompted for the
password, I started to sweat. "What do you mean, password?" First of
all it had never been necessary to give my password to sudo anything
and secondly I never had to set the password for the user ubuntu. To
make matters even worse: I also didn't have to set a password for root
either, so a simple "`su`" command would also not help me. Sure, the
server was still running normally. But since I would not be able to
administer the machine, it was going to be a problem sooner or
later. Especially since there are a couple of production sites running
on the server, including a web shop.

# Recovering from the mistake

After some searching and pondering I decided to take advantage of the
fact that it is an
[Amazon Elastic Compute Cloud](http://aws.amazon.com/ec2/) (EC2)
instance with an [Elastic Block Store](http://aws.amazon.com/ebs/)
(EBS) volume. These are the steps I took to access the box as root
again:

1.  Create a new, temporary instance.
2.  Stop the old instance.
3.  Detach the EBS volume from the old instance.
4.  Attach the volume to new instance on `/dev/sdb1`.
5.  Mount the device in new instance.
6.  Edit the `sudoers` file.
7.  Unmount the device.
8.  Detach the volume.
9.  Attach the volume to old instance on `/dev/sdba1`.
10. Boot old instance.
11. Link the old instance back to the elastic IP address.
12. Start breathing again.
13. Delete the temporary instance.

For most of the juggling with the storages I could use the
[Elasticfox add-on](http://developer.amazonwebservices.com/connect/entry.jspa?externalID=609)
for Firefox. I only needed to use the
[API command line tools](http://developer.amazonwebservices.com/connect/entry.jspa?externalID=351&categoryID=88)
to create the instance and attach the storage back to the old
instance. All in all the instance was down for less than 15
minutes. And that includes the stress of not being able to attach the
storage back to the instance with Elasticfox, wondering whether it was
even possible to attach an EBS volume to a stopped instance, and
having to figure out how to do it with the command line (hint: use
`ec2-attach-volume` and don't forget to add the `--region` parameter
if you are in the EU region).

# Where it all went wrong


You might be curious about the mistake I made to lock myself
out. Let's first show you the last couple of lines of the /etc/sudoers
file before I touched it:

    # ubuntu user is default user in ec2-images.
    # It needs passwordless sudo functionality.
    ubuntu  ALL=(ALL) NOPASSWD:ALL

Now the version I had created:

    # ubuntu user is default user in ec2-images.
    # It needs passwordless sudo functionality.
    ubuntu  ALL=(ALL) NOPASSWD:ALL
    ubuntu  ALL=(ALL) ALL

Yes, I copied and pasted the last line and was so focussed on removing
the `NOPASSWD` part, that I forgot to change the user name.

# Lessons learned

Besides gaining more insight in EC2, I also learned a couple of
lessons the hard way:

-   Don't try to "quickly" change potentially dangerous stuff.
-   When doing something like this triple check things.
-   Don't log out until you've confirmed you can log in again.
-   Don't get lazy when copying and pasting.
