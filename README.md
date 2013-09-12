# www.vlent.nl

This repository contains the code and content of my personal website:
[www.vlent.nl](http://www.vlent.nl). This incarnation of the site is
built with [Acrylamid](https://github.com/posativ/acrylamid/) and
[Compass](http://compass-style.org/).


## Setup

The project consists of two parts: on the one hand we have the HTML
and XML which are generated by Acrylamid and on the other hand there
is the CSS which is handled by Compass.

### Acrylamid

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

### Compass

To generate the CSS, you need to install Compass (and Sass)
first. Then you need to compile the Sass code to CSS.

To accomplish this, you need to install Compass and Sass. A nice way
to do this is by using
[virtualenvwrapper.gem](http://pypi.python.org/pypi/virtualenvwrapper.gem). Once
this is installed you can use ``gem install`` and the Gems will be
installed in your virtualenv library directory.

    $ gem install sass --version="3.2.10"
    $ gem install compass --version="0.13.alpha.4"

(Note that these are the minimal versions this site needs at the
moment. It is also assumed you already cloned the repository, as
described in the Acrylamid section.)

Using this version of compass means that you'll get the warning to
install the gem `rb-inotify`, which has a dependency on the `ffi`
gem. To install these gems you'll need to have the `ruby-dev` package
installed if you are running Ubuntu. When that is the case, you can
install the `rb-inotify` gem:

    $ gem install rb-inotify

If you now reload the site, the CSS should be in place and the site
should look pretty. :)


## Development

If you want to develop on this site, you don't want to manually
compile the HTML and CSS by hand every time you change something...

To have Acrylamid automatically refresh the HTML:

    $ acrylamid autocompile

And to have Compass compile your CSS when needed:

    $ compass watch
