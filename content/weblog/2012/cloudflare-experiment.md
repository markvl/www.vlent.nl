---
title: CloudFlare experiment
date: 2012-12-27 22:04
tags: [blog, development]
---

For about a month I have served this website using the CloudFlare free
plan. This article describes what I observed.

# Why

Let me first explain why I started using
[CloudFlare](https://www.cloudflare.com/). Earlier this year I
[migrated this blog](/weblog/2012/10/01/migrating-to-acrylamid/) from
Django to a static site.  At the same time I also switched from
hosting at [Zest Software](http://zestsoftware.nl/) back to my hosting
provider, [bHosted.nl](http://www.bhosted.nl/). Still, I expected to
see a drop in the time required to download a page and thus in the
related graph in the
[Google Webmaster Tools](https://www.google.com/webmasters/tools/home). This
is what I saw:

![Time to download a page: September vs October](/images/webtoolsstats-october.png)

As of October 1st---when I made the switch---the time needed to
download a page didn't necessarily drop; instead it became more
erratic and often higher than it was before.

I guessed that the expected speed improvement of having a static site
was negated by hosting the site on another server. Because at Zest my
site was dynamic but ran on a server that had a very light load and
was only hosting a couple of sites. And at bHosted.nl the site is
running on a shared server with a load of 2--4 (based on a few
samples) and several hundred other sites.

I then by chance stumbled upon the content delivery network provided
by CloudFlare. And they even have a
[free plan](https://www.cloudflare.com/plans).

# Setup and first experience

First of all, the video on the CloudFlare homepage is absolutely right
about how easy it is to setup. Sure, I know a bit about DNS but
basically they do not require you to do very hard stuff. In fact, the
most complicated I had to do was to change the name servers so they
pointed to CloudFlare. (Actually: I found out that I could not change
them myself so I had to ask my hosting provider to do so form me.)

Unfortunately I lost the screenshots I made of my CloudFlare
statistics. But according to those statistics, CloudFlare handled
about half of the requests and traffic. And, on the side, also blocked
quite a few, supposedly, malicious requests.

I made the switch around the 1st of November. I expected that the
time to download a page would be more stable but also that is would be
lower. (That's one of the benefits of a content distribution network,
right?) Well, I was partially right...

![Time to download a page: October vs November](/images/webtoolsstats-december.png)

As you can see, the time to download a page indeed did not fluctuate
as much anymore. But the download time increased dramatically! (That's
the reason why I switched back to bHosted.nl at the end of November,
as you can see in the graph.)

Google also assigned "special crawl rate settings" in the period I was
using CloudFlare. I am not sure what this means and if it's positive
or not. Either way, within a week after taking CloudFlare out of the
loop, it was back to normal.

![Google assigned special crawl rate settings](/images/crawlratesetting.png)


# Measurements

Before I decided to switch back to just bHosted.nl, I tried to do some
experiments to see if I could reproduce the differences measured by
Google. I gathered circa 30 URLs (the home page, the ten most recent
articles, a number of popular articles and a (more or less) random
selection) and told [Siege](http://www.joedog.org/siege-home/) to have
a crack at it. More specifically I used the options ``benchmark`` (to
run the requests without a delay), ``internet`` (which randomly hits
the URLs I selected) and ``concurrent`` to experiment with different
number of concurrent users. These tests ran for 60 seconds each.

Since the bHosted.nl servers are located in The Netherlands, I decided
to make the measurements a bit more fair. So I did not run the test
from my home (also in The Netherlands), but a
[RamNode](http://ramnode.com/) VPS, which is hosted in Atlanta,
Georgia.

## Results

The shortest transaction for both servers was stable: for bHosted.nl
it was 0.21 seconds and for CloudFlare it was 0.14 seconds. The
average response time is also comparable (the lower lines in the graph
below). The longest transactions however, differed a bit more.

<script src="/js/dygraph-combined.js"></script>
<div id="avg-max-transaction-time" class="graph"></div>
<script type="text/javascript">
  g = new Dygraph(
    document.getElementById("avg-max-transaction-time"),
    "/cloudflare_csv/avg_max_transaction.csv",
    {
        title: 'Transaction time',
        xlabel: 'Concurrency',
        ylabel: 'Seconds',
        colors: ['#1F77B4', '#FE7F0E', '#1F77B4', '#FE7F0E'],
        strokeWidth: 3
    }
  );
</script>

The transaction rate of bHosted.nl and CloudFlare seem to be comparable.
(Except for a spike in the bHosted.nl setup at 50 concurrent simulated
users. But this could just be a happy accident...)

<div id="transaction-rate" class="graph"></div>
<script type="text/javascript">
  g = new Dygraph(
    document.getElementById("transaction-rate"),
    "/cloudflare_csv/transaction_rate.csv",
    {
        title: 'Transaction rate',
        xlabel: 'Concurrency',
        ylabel: 'Transactions/sec',
        colors: ['#1F77B4', '#FE7F0E', '#1F77B4', '#FE7F0E'],
        strokeWidth: 3
    }
  );
</script>

## Summary

As you may have guessed, I am absolutely not an expert on the
matter. But what I conclude from this data is that there is not *that*
much difference between bHosted.nl and CloudFlare.

Sure, the longest transaction time in the CloudFlare setup is larger
in *some* situations. But for my blog 100 concurrent users are
unlikely. (As a matter of fact in December an average of about 150
pages are requested per day. And Google only indexes an average of 80
pages per day at the moment of writing.) More importantly: the
*average* transaction time for bHosted.nl and CloudFlare is
practically the same.


# Conclusion?

I am sure you should **not** draw the conclusion that using CloudFlare
is a bad thing. Nor do I want to complain about their service---after
all I did not pay them a dime. Having said that, my **personal**
conclusion was that since Google is
[using site speed in web search ranking](http://googlewebmastercentral.blogspot.nl/2010/04/using-site-speed-in-web-search-ranking.html)
**this site** is better off by not using CloudFlare. Your mileage may
vary.
