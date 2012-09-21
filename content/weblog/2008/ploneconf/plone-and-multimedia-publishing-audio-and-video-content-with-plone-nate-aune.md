---
title: "Plone and multimedia: Publishing audio and video content with Plone (Nate Aune)"
slug: plone-and-multimedia-publishing-audio-and-video-content-with-plone-nate-aune
author: Jean-Paul Ladage
date: 2008-10-10 20:58
tags: [plone, ploneconf, ploneconf2008]
---

Plone4Artists Audio and Video.

**(Contribution by Jean-Paul Ladage)**

Plone4Artists consist of a collection of add-ons that provide rich
media in Plone.

# Audio

Audio is simply recognised by plone after uploading it as a regular
File type. It extracts the meta data to display. Audio containers can
be used to create listings of the audio files using the Collection
functionality.

# Video

Similar to the audio files, Plone recognizing Files that are video's
and showing the meta data and a player. Even a splash image will be
created to display initially. When clicking the image it will be
replaced by a player. It is still possible to create Video's that
contain a URL to one of the large video hosting providers.

Both types support Creative Commons licensing and Rating.

Plone.tv is a show case of what's possible with Plone4Artists.

# Extras

- PloneFlashUpload - allows for easy multiple file uploads at once.
- PloneJUpload - Older variant of the flash version based on Java,
  which is not well supported in all browsers.

# Large setups

Zope is not suited for handling large number of large file uploads, so
if you need to scale, you need to use one of the following solutions:

- Infrae's Tramline - This hands off the heavy lifting to Apache.
- S3 integration with Amazon
