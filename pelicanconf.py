#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Chris Albon'
SITENAME = 'Machine Learning and Artificial Intelligence'
SITEURL = 'http://chrisalbon.com'
THEME = 'theme/'

PATH = 'content'

TIMEZONE = 'America/Tijuana'

DEFAULT_LANG = 'en'
DEFAULT_DATE = 'fs'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None
FEED_ALL_RSS = 'feeds/all.rss.xml'
CATEGORY_FEED_RSS = 'feeds/%s.rss.xml'

DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

STATIC_PATHS = ['extra/CNAME',
                'extra/favicon.ico',
                'pages',
                'blog',
                'statistics',
                'cloud-computing',
                'javascript',
                'sql',
                'scala',
                'deep-learning',
                'machine-learning',
                'python',
                'mathematics',
                'algorithms',
                'regex']

ARTICLE_URL = '{category}/{slug}.html'
ARTICLE_SAVE_AS = '{category}/{slug}.html'

FEED_MAX_ITEMS = 10

EXTRA_PATH_METADATA = {
    'extra/favicon.ico': {'path': 'favicon.ico'},
    'extra/CNAME': {'path': 'CNAME'},
}

ARTICLE_EXCLUDES = ['in_progress']

PLUGIN_PATHS = ['plugins']
PLUGINS = ['render_math', 'tipue_search', 'sitemap']

DIRECT_TEMPLATES = ['index', 'search']

CATEGORY_SAVE_AS = ''
AUTHOR_SAVE_AS = ''
TAG_SAVE_AS = ''
AUTHORS_SAVE_AS = ''
CATEGORIES_SAVE_AS = ''
TAGS_SAVE_AS = ''
ARCHIVES_SAVE_AS = ''

DELETE_OUTPUT_DIRECTORY = True

SITEMAP = {
    'format': 'xml',
    'priorities': {
        'articles': 0.5,
        'indexes': 0.5,
        'pages': 0.5
    },
    'changefreqs': {
        'articles': 'monthly',
        'indexes': 'daily',
        'pages': 'monthly'
    }
}

MD_EXTENSIONS = ['codehilite(guess_lang=False)', 'extra']
