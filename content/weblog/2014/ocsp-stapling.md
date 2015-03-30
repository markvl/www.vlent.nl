---
title: OCSP Stapling in Nginx
date: 2014-04-19 23:39:00
tags: [devops, https, nginx, ocsp]
---

The Heartbleed bug triggered a review of the configuration of my own
web server. As a result I discovered that I had my Online Certificate
Status Protocol (OCSP) stapling configured wrong. In this article I
will briefly explain OCSP and OCSP stapling, what I had done wrong and
what is a---as far as I now know---right way to implement OCSP stapling
in Nginx.

# What are OCSP and OCSP stapling?

## Certificates

First things first: if you are reading pages on this website, your
connection will be secure because my web server is configured to only
use [HTTPS](http://en.wikipedia.org/wiki/HTTP_Secure). To secure this
connection,
[certificates](http://en.wikipedia.org/wiki/X.509#Certificates) are
used. These certificates prove that your browser is actually talking
to *this* site and not another site pretending to be vlent.nl.

## Certificate revocation

Certificates can become invalid. One reason is that they expire: when
you get a certificate from a
[certification authority](http://en.wikipedia.org/wiki/Certification_authority),
the certificate has a start and end date. For example, my current
certificate is valid from April 10th, 2014 and valid until April 10th
2015. Outside these dates, clients (like your browser) should not
accept this certificate.

Another way a certificate can become invalid is when it is
revoked. This means that your client should no longer trust the
certificate even though it may not be expired yet. One reason to
revoke a certificate is when (you believe) the
[private key](http://en.wikipedia.org/wiki/Public_key_infrastructure)
associated with the certificate is compromised. And that is exactly
what could have happened due to the [Heartbleed bug](http://heartbleed.com/).

## OCSP

Revoked certificates are listed in so called
[certificate revocation lists](http://en.wikipedia.org/wiki/Certificate_Revocation_List). A
more efficient alternative is the
[Online Certificate Status Protocol (OCSP)](http://en.wikipedia.org/wiki/Online_Certificate_Status_Protocol). How
the latter basically works is that the client asks the certificate
authority (CA) that issued the certificate, whether the received
certificate is still valid.

## OCSP stapling

The downside of OCSP is that the client must contact the CA to
discover whether the certificate is valid. This both creates a privacy
issue (the CA knows which IPs were interested in a certain
certificate), and a scaling issue: a CA might have to respond to a
large number of requests when a site using 'their' certificate is for
instance a high traffic web site.

OCSP stapling resolves this problem by having the certificate holder
itself query the OCSP server of the CA at regular intervals. The
response from the CA, which is signed and time stamped, is then added
("stapled") to the response to the client visiting the web site.

So for example, when your browser connects to
[www.vlent.nl](https://www.vlent.nl), my web server does not only
return the usual certificate information, but the OCSP response is
also included. This saves your browser a round trip to my CA.


# What did I do wrong?

Originally I had included the OCSP stapling mainly to tick another box
on
[Qualys SSL Labs test report](https://www.ssllabs.com/ssltest/analyze.html?d=vlent.nl)
without really understanding how it worked. To accomplish this, I used
the
[`ssl_stapling_file` directive](http://nginx.org/en/docs/http/ngx_http_ssl_module.html#ssl_stapling_file)
in my Nginx setup:

    ssl_stapling on;
    ssl_stapling_file path/to/file_with_ocsp_response;

This---in itself---is not a problem. However, what I did not realise
was that the file with the OCSP response needed to be *updated*
frequently. Since I did not do that, the result was something like
this:

    $ openssl s_client -connect www.vlent.nl:443 -tls1  -tlsextdebug  -status
    ...
    OCSP response:
    ======================================
    OCSP Response Data:
        ...
        Produced At: Oct  9 14:31:12 2013 GMT
        ...
        Cert Status: good
        This Update: Oct  9 14:31:12 2013 GMT
        Next Update: Oct 11 14:31:12 2013 GMT

Although I ran the command last week (April 2014), the OCSP response
data was still only valid until October 11th, 2013. Basically the OCSP
stapling I used was just a waste of bits since it had only been valid
for two days and clients still had to query the OCSP server
themselves.


# A good OCSP stapling configuration

Luckily, there is an easy solution: have Nginx itself handle the OCSP
stapling, for example with this configuration:

    ssl_stapling on;
    ssl_stapling_verify on;
    ssl_trusted_certificate /path/to/cert_chain.pem;
    resolver 8.8.8.8 8.8.4.4 valid=300s;
    resolver_timeout 5s;

When I now check the response, I get:

    $ openssl s_client -connect www.vlent.nl:443 -tls1  -tlsextdebug  -status
    OCSP response:
    ======================================
    OCSP Response Data:
        ...
        Produced At: Apr 19 07:33:29 2014 GMT
        ...
        Cert Status: good
        This Update: Apr 19 07:33:29 2014 GMT
        Next Update: Apr 21 07:33:29 2014 GMT

Note that the OCSP response is valid while I only updated the Nginx
configuration a week ago and have not touched it since.


# Two warnings

When you have updated your configuration and restarted Nginx, you may
not get an OCSP response when you want to test. Instead, the result of
the `openssl` command might contain this line instead of the OCSP
response data block:

    OCSP response: no response sent

In that case, don't immediately tweak your configuration. Just try
again first.

And finally this: not all clients check whether a certificate is
revoked or not. For instance in Chrome the
[online revocation check is disabled by default](https://www.imperialviolet.org/2012/02/05/crlsets.html). But
that is a completely different side of this story. There's only so
much humble web server can do.
