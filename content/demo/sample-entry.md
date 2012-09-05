---
title: Example
date: 2012-06-02 12:00
tags: [example, acrylamid, development]
---

This is an example where features can be tested.

Here's an example where I want the dashes to be replaced:
1--2. And---as is to be expected---here as well.

This doesn't work because I don't want them replaced: decrement-- and --parameter.

But if I use a code block, they won't be replaced: `decrement--` and `--parameter`

Or like this:

    def foo():
        decrement--
        --parameter

But the "kbd" element also works: <kbd>decrement--</kbd> and <kbd>--parameter</kbd>
