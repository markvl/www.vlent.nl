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
    # Article indexes
    '/': {'filters': 'summarize+16', 'view': 'index',
          'pagination': '/page/:num'},
    '/weblog/': {'filters': 'summarize+16', 'view': 'index',
          'pagination': '/weblog/page/:num'},

    # Articles
    '/weblog/:year/:month/:day/:slug/': {'view': 'entry'},

    # Tag indexes
    '/weblog/tag/:name/': {'filters': 'summarize+16', 'view': 'tag',
                    'pagination': '/weblog/tag/:name/:num'},

    # Atom feeds
    '/atom.xml': {'filters': ['h2', ], 'view': 'atom'},
    '/weblog/atom.xml': {'filters': ['h2', ], 'view': 'atom'},
    '/weblog/tag/:name/atom.xml': {'filters': ['h2', ], 'view': 'atompertag'},

    # Sitemap
    '/sitemap.xml': {'view': 'sitemap'},

    # Pages
    '/:slug/': {'view': 'page'},
}

PERMALINK_FORMAT = '/weblog/:year/:month/:day/:slug/index.html'
DATE_FORMAT = '%Y-%m-%d %H:%M'
OUTPUT_IGNORE = ['/css/*', '/js/*', '/fonts/*', '/images/*', 'favicon.ico',
                 'robots.txt', 'humans.txt']
ENTRIES_IGNORE = ["drafts/*", ]
DISQUS_SHORTNAME = 'vlent'
SUMMARIZE_LINK = '<span>&#8230; <a href="%s" class="continue">Continue reading</a></span>'
