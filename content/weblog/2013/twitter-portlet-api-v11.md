---
title: Collective.twitterportlet and Twitter API version 1.1
date: 2013-06-13 12:46:00
tags: [development, plone]
---

This week, on June 11th, Twitter retired version 1 of their API. As a
result, the Twitter portlets of some of our customers stopped
working. They are all using collective.twitterportlet so we created a
quick (and slightly dirty?) fix to get them up and running again:
[edition1.twitterportletfix](https://pypi.python.org/pypi/edition1.twitterportletfix).

# The problem

The obvious symptom we were confronted with, was that there were no
tweets shown in the portlet. Instead, it contained the following text:

<blockquote><p>There was an error while rendering the portlet.</p></blockquote>

And the error log included entries like this:

    AttributeError: 'unicode' object has no attribute 'get'

After vaguely recalling something about a Twitter API change, we
started looking around and found the Twitter blog entry where they
stated that the
[API v1 is retired](https://dev.twitter.com/blog/api-v1-is-retired)
and we should use
[API v1.1](https://dev.twitter.com/docs/api/1.1/overview). But API
version 1.1 requires you to use
[OAuth](https://dev.twitter.com/docs/auth/oauth/faq).

The good news is that
[collective.twitterportlet](https://pypi.python.org/pypi/collective.twitterportlet/)
uses
[python-twitter](https://pypi.python.org/pypi/python-twitter/). And
that package is compatible with version 1.1 of the Twitter API. So
upgrading to version (at least) version 1.0 of that package should at
least make the Twitter API wrapper compatible.

The bad news is that just upgrading python-twitter is not enough. You
still need to give it some keys (consumer key, consumer secret,
et cetera) to get data from Twitter. Otherwise, you'll see these kind
of messages in you logs:

    TwitterError: [{u'message': u'Bad Authentication data', u'code': 215}]

# The optimal solution

In my humble opinion the optimal solution would be to do something
similar as the combination of
[collective.facebook.portlets](https://pypi.python.org/pypi/collective.facebook.portlets)
and
[collective.facebook.accounts](https://pypi.python.org/pypi/collective.facebook.accounts)
provides. That is: allow the user to configure accounts (and perhaps
even applications?) and let the user choose which account to use *per
portlet*.

Unfortunately this involves more work and time than we could spend at
the moment with customers waiting for their home page to look good
again.

**Update (2013-06-14):
[collective.twitter.accounts](https://pypi.python.org/pypi/collective.twitter.accounts)
probably provides everything we'd need. Thanks for the tip Héctor!**

# The quick workaround

So instead of doing it the proper way, we decided to create a small
package,
[edition1.twitterportletfix](https://pypi.python.org/pypi/edition1.twitterportletfix),
that would solve our immediate need. What this package does is it
allows the user to configure the required keys/tokens. It also
customises the `Renderer` class of the portlet to use those keys to
call the Twitter API.

Obviously this package will not fulfil all needs (and I'm not really
proud of it) but for our use cases it should be enough for now. At
least until there is a better solution available.

## Why I chose this solution

*(This section was added on 2013-06-14 after the question why it was
easier to create this package than contribute to
collective.twitterportlet. A very fair question.)*

As I already stated, this is not an optimal solution and I'm not
really proud of it. So why did I still go ahead with it? There are
several reasons.

First of all, even if I would have liked to contribute, the
[PyPI page of collective.twitterportlet](https://pypi.python.org/pypi/collective.twitterportlet/)
does not list a publicly available repository. Looking around on the
[collective repo on GitHub](https://github.com/collective) also did
not turn up anything. I did find a
[repo with the same name](https://github.com/muellert/collective.twitterportlet)
but saw no relation between the owner of the repo and the owner of the
package.

Furthermore, even if I had found a repository, contributing to the
original package would have delayed this fix. My current solution does
not provide a fix for every use case of the package. For instance, you
cannot have two portlets showing different accounts. But building that
proper solution (and effectively replicating the functionality of
[collective.twitter.accounts](https://pypi.python.org/pypi/collective.twitter.accounts))
would have taken more time and I needed a fix for our customers sooner
rather than later.

(My focus was on fixing collective.twitterportlet rather than
replacing it. As a result I failed to look around more and did not
know about collective.twitter.accounts until Héctor commented on this
article. Otherwise I would have tried to have
collective.twitterportlet use collective.twitter.accounts, instead of
reinventing the wheel.)

So I was fully aware that edition1.twitterportletfix is not a
permanent solution. That is why I tried to make sure that you can
cleanly uninstall the package. Once there is a better solution
available---or you decide to replace collective.twitterportlet
completely---you should be able to uninstall the fix and not leave a
trace.
