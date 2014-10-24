# -*- encoding: utf-8 -*-
# This is your config file.  Please write in a valid python syntax!
# See http://acrylamid.readthedocs.org/en/latest/conf.py.html

# This is necessary since by default the encoding used by Python is
# ASCII. The deployment command updates the OS environment with the
# data from this file. But since the tagline contains a UTF-8
# character, we need to make sure the default encoding is also UTF-8.
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

SITENAME = 'Practicing web development'
TAGLINE = "Mark van Lent’s weblog"
WWW_ROOT = 'https://www.vlent.nl'

AUTHOR = 'Mark van Lent'
EMAIL = 'mark@vlent.nl'

FILTERS = ['markdown+headerid+delins+def_list', 'typography', 'h1']
DATE_FORMAT = '%Y-%m-%d %H:%M'
DISQUS_KEY = '2YTzu4nyYHHawjrkEMP8Vi8SL5wMH7p6AR77ad6pdMc59tODvp7eIC705ZvhR6rh'
DISQUS_SHORTNAME = 'vlent'
SUMMARIZE_LINK = '<span>&#8230; <a href="%s" class="continue">Continue reading</a></span>'

VIEWS = {
    # Article indexes
    '/': {'filters': 'intro', 'view': 'index',
          'pagination': '/page/:num/'},
    '/weblog/': {'filters': 'intro', 'view': 'index',
          'pagination': '/weblog/page/:num/'},

    # Articles
    '/weblog/:year/:month/:day/:slug/': {'views': ['entry', 'draft']},

    # Archive views
    '/weblog/:year/': {'view': 'archive'},
    '/weblog/:year/:month/': {'view': 'archive'},
    '/weblog/:year/:month/:day/': {'view': 'archive'},

    # Tag indexes
    '/weblog/tag/:name/': {'filters': 'intro', 'view': 'tag',
                    'pagination': '/weblog/tag/:name/:num/'},

    # Atom feeds
    '/feed.atom': {'filters': ['h2', ], 'view': 'atom',
                   'num_entries': 10},
    '/weblog/feed.atom': {'filters': ['h2', ], 'view': 'atom',
                          'num_entries': 10},
    '/weblog/tag/:name/feed.atom': {'filters': ['h2', ], 'view': 'atompertag',
                                    'num_entries': 10},

    # Sitemap
    '/sitemap.xml': {'view': 'sitemap'},

    # Pages
    '/:slug/': {'view': 'page'},
}

THEME = 'theme'
STATIC = ['assets', ]
FILTERS_DIR = 'filters/'

OUTPUT_IGNORE += ['/css/*', ]
CONTENT_IGNORE += ['.#*', '*/drafts/*', ]
THEME_IGNORE += ['.#*']
STATIC_IGNORE += ['.#*', 'vL.xcf']

DEPLOYMENT = {
    'bhosted': 'rsync -rtuvz --delete $OUTPUT_DIR bhosted:~/www/www.vlent.nl',
    'atlanta': 'rsync -rtuvz --delete $OUTPUT_DIR atlanta:/var/www/www.vlent.nl/html',
    'clean': 'rm -rf output/index.html output/sitemap.xml output/feed.atom output/weblog output/page',
}
