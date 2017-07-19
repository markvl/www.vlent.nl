---
title: Bash set builtin
date: 2017-07-19
tags: [tools]
---

Shell scripts I come across sometimes have for instance "`#!/bin/bash
-eux`" on the first line. Because I've Googled for this too many times
now, I'll record the meaning of these options here for my own sanity.

The options (`-e`, `-u` and `-x`) are part of the `set` builtin. They
have the following meaning:

`-e`
:   Exit immediately if a pipeline ... returns a non-zero status.

`-u`
:   Treat unset variables and parameters ... as an error when performing
    parameter expansion.

`-x`
:   Print a trace of [...] commands and their arguments or associated
    word lists after they are expanded and before they are executed.

For more details and other options,
[read the manual](https://www.gnu.org/software/bash/manual/bashref.html#The-Set-Builtin).
