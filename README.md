www.vlent.nl
============

This repository contains the code and content of my personal website:
[www.vlent.nl](http://www.vlent.nl). This incarnation of the site is
built with [Acrylamid](https://github.com/posativ/acrylamid/).

Setup
-----

To get it up and running, do the following:

    $ mkvirtualenv www.vlent.nl
    $ git clone https://github.com/markvl/www.vlent.nl.git
    $ cd www.vlent.nl
    $ pip install -r requirements.txt
    $ acrylamid compile
    $ acrylamid view

Now you can surf to [http://localhost:8000](http://localhost:8000) to
view the site.

Note that this assumes you have
[virtualenvwrapper](http://pypi.python.org/pypi/virtualenvwrapper)
installed. If you don't, your best options are to:

 - install it now, or
 - use [virtualenv](http://pypi.python.org/pypi/virtualenv)
   directly (and don't forget to activate the new virtualenv after you
   create it).
