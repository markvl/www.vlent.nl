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
etcetera) to get data from Twitter. Otherwise, you'll see these kind
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
