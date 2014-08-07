---
title: Change the workflow of a content type to "(Default)"
slug: change-workflow-content-type-default
date: 2011-02-08 11:04
tags: [development, plone]
---

Today I wanted to set the workflow for the content type File to
`(Default)`.

I had some difficulty finding out how to do this. Especially since
exporting the workflow definition did not provide any clues. Here's a
quick note so I won't forget it again (thanks to Maciej Zięba from
[STX Next](http://www.stxnext.pl/)).

Add the following to `workflows.xml`:

    <bindings>
      <type type_id="File" remove="True" />
    </bindings>

After reinstalling the Generic Setup profile, the specified content
type (in my case File) will have the default workflow.
