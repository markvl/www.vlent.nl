---
title: Change of editor
date: 2018-08-14
tags: [tools]
---

As I [mentioned last
month](/weblog/2018/07/04/devopsdays-amsterdam-2018-reflection/#miscellaneous),
I enjoyed working with Visual Studio Code when I used it to create my
devopsdays notes. I even started using it for my day-to-day work four weeks
ago. And I still like it!

I wanted to write a short article about this change, but then I read the
articles by [Chris Coyier](https://css-tricks.com/on-switching-code-editors/)
and [Lucas
Oliveira](https://dev.to/lucasprag/my-editor-journey-sublime-vim-emacs-vscode-19k0)
about their switch.  They (also) described what editors they have used _before_
VS Code and I thought it would be fun to do a similar article about my 'path to
VS Code,' so to speak.


## Early years

The first coding environments I can remember using, are the IDEs that came with
[QBasic](https://en.wikipedia.org/wiki/Pico_(text_editor)) and [Turbo
Pascal](https://en.wikipedia.org/wiki/Turbo_Pascal). And yes, I realise I am
showing my age by confessing this. ;-)

<figure>
  <img src="/images/pascal.png" width="640" height="400" alt="Turbo Pascal Hello World example" />
  <figcaption>Source: <a href="http://borlandpascal.wikia.com/wiki/Borland_Pascal">borlandpascal.wikia.com</a></figcaption>
</figure>


## University

When I went to university I came in contact with Linux for the first time. My
first emails were sent with the [Pine email
client](https://en.wikipedia.org/wiki/Pine_(email_client)) and as a result I
also used [Pico](https://en.wikipedia.org/wiki/Pico_(text_editor)) to edit
files. When I was working on a Windows system, my preferred editor was
[Notepad++](https://notepad-plus-plus.org).

Once I really started doing more things on the (Linux) command line, I switched
to [Vim](https://www.vim.org/). Over the years I invested time in configuring
it the way I liked it and put my `vimrc` file on my website. Thanks to the
[Wayback Machine](https://web.archive.org) you can still retrieve [the 2003
version of
it](https://web.archive.org/web/20040608105137/http://panic.et.tudelft.nl:80/~mark/config/vimrc).
(Apparently by then I had switched to [Mutt](http://www.mutt.org/) for my
emails and was using a versioning system---I think it was
[CVS](https://en.wikipedia.org/wiki/Concurrent_Versions_System).)


## Co-worker influence

Fast forward a couple of years to 2007 when I started working as a developer at
[Zest](https://zestsoftware.nl/). I was still using Vim as my editor when I was
pair programming with a co-worker and saw him debugging some Python code with
[Emacs](https://www.gnu.org/software/emacs/). He was running the debugger in one
window and was shown the code (with the active line highlighted) in the other
window. Once I had seen this I wanted to switch to Emacs! The fact that
a couple of other co-workers were also using Emacs helped a bunch. There were
enough people to help me make the switch and figure out configuration issues
when I ran into them. This must have been somewhere in 2007 or 2008.

In the years that followed I kept using Emacs. I did try other editors/IDEs
(like [TextMate](https://macromates.com/), [Sublime
Text](https://www.sublimetext.com/) and
[PyCharm](https://www.jetbrains.com/pycharm/)) usually because I saw co-workers
using and recommending them. But sooner or later I always came back to Emacs.
I think it is safe to say I have effectively been using Emacs the past ten years.


## A new era: VS Code

I was reconsidering my use of Emacs for a while because I was jealous of a
co-worker whenever I saw him navigate through our code base with PyCharm.
Opening files and going to the definition of classes (with `CTRL`+click) was
way easier than in my setup. I was even considering to give PyCharm another
shot when I heard good things about [Visual Studio
Code](https://code.visualstudio.com/).

The main reasons that motivated me to try it:

- The [code navigation](https://code.visualstudio.com/docs/editor/editingevolved)
  options.
- I seemed like a nice editor out of the box.
- Lots of extensions available in the
  [marketplace](https://marketplace.visualstudio.com/).
- [IntelliSense](https://code.visualstudio.com/docs/editor/intellisense)
- Colleagues can actually use my editor if needed. (No more explaining they need
  to use `CTRL`+`X` `CTRL`+`S` to save for instance.)

To give VS Code a fair chance, I decided to use it for at least a week
full time. To make sure I did not cheat, I switched over completely: I
updated my settings (e.g. the `EDITOR` environment variable and
aliases) to use VS Code instead of Emacs. And I haven't looked back
since.

Sure, there are some things that I probably want to add, improve or
change on my current setup, but in general the experience has been
great.

Some of the things I like and have not yet mentioned:

- It is really easy to use in presentations/demonstrations. Without having to
  look up key bindings I can easily enlarge the font size (`CTRL`+`=`, just like
  e.g. in a browser) or change the theme to a light version (black on white) for
  better legibility.
- So far I have been able to find extensions for all the types of files I want
  to edit, like Ansible, Terraform or Vagrant files.
- VS Code has global and workspace setting. I have not used it extensively, but
  I can see its use and will probably customize settings for certain projects in
  the future.

Things that I do not like as much:

- I contrast to Emacs I cannot use VS Code on the command line. This means I
  still have to have working knowledge of another editor to edit files on
  other machines. (To be fair: most servers do not have Emacs installed anyway
  so in practice I already had to use another editor (Vim) in most cases
  already.)
- My current laptop does not have separate `Home` and `End` keys. This was no
  issue with Emacs because I used `CTRL`+`A` and `CTRL`+`E` to navigate to the
  beginning and ending of lines. But since I
  want to keep the key bindings in VS Code as default as possible, I will have 
  to learn to use `FN`+`←` and `FN`+`→` or disable Num Lock and use the `1` and 
  `7` on the keypad.

<figure>
  <img src="/images/dell_precision_keyboard.jpg" alt="Dell Precision keyboard layout" />
  <figcaption>Source: <a
href="https://www.dell.com/support/article/nl/nl/nlbsdt1/sln308143/dell-precision-7520-mobile-workstation-keyboard-guide?lang=en">Dell site</a></figcaption>
</figure>

I found the following resources useful to make the transition:

- The [documentation](https://code.visualstudio.com/docs), where I
  often end up after searching for something VS Code related.
- The [keyboard shortcut reference](https://code.visualstudio.com/docs/getstarted/keybindings#_keyboard-shortcuts-reference).
- The video [VS Code Can Do That?! VS Code Tips and Tricks](https://www.youtube.com/watch?v=x5GzCohd4eo).


## The future

The experiment with VS Code has been a success. I have made the switch and have
no intention of returning to Emacs.  VS Code has the ingredients I was looking
for and then some. 

Does this mean that I use VS Code for the next decade? Only time will tell...

