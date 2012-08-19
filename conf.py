# -*- encoding: utf-8 -*-
# This is your config file.  Please write in a valid python syntax!
# See http://acrylamid.readthedocs.org/en/latest/conf.py.html

SITENAME = 'vLent.nl'
TAGLINE = 'Practicing software development'
WWW_ROOT = 'http://www.vlent.nl'

AUTHOR = 'Mark van Lent'
EMAIL = 'mark@vlent.nl'

FILTERS = ['markdown', 'typography', 'h1']
VIEWS = {
    '/': {'filters': 'summarize+16', 'view': 'index',
          'pagination': '/page/:num'},

    '/:slug/': {'view': 'page'},

    '/weblog/:year/:zmonth/:zday/:slug/': {'view': 'entry'},


    '/tag/:name/': {'filters': 'summarize+16', 'view': 'tag',
                    'pagination': '/tag/:name/:num'},

    '/weblog/atom.xml': {'filters': ['h2', ], 'view': 'atom'},

    '/sitemap.xml': {'view': 'sitemap'},

    # Here are some more examples

    # # '/atom/full/' will give you a _complete_ feed of all your entries
    # '/atom/full/': {'filters': 'h2', 'view': 'atom', 'num_entries': 1000},

    # # a feed containing all entries tagged with 'python'
    # '/rss/python/': {'filters': 'h2', 'view': 'rss',
    #                  'if': lambda e: 'python' in e.tags}

}

PERMALINK_FORMAT = '/weblog/:year/:zmonth/:zday/:slug/index.html'
DATE_FORMAT = '%Y-%m-%d %H:%M'
OUTPUT_IGNORE = ['/css/*', '/js/*', '/fonts/*', '/images/*', 'favicon.ico']
ENTRIES_IGNORE = ["drafts/*", ]
DISQUS_SHORTNAME = 'vlent'
SUMMARIZE_LINK='<span>&#8230; <a href="%s" class="continue">Continue</a></span>'
