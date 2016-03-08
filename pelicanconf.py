#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'JW'
SITENAME = u'JW\'s Site'
# SITEURL = 'http://wjidea.github.io'
THEME = 'pelican-cait'
PATH = 'content'
PAGE_PATH = '/content/pages'
DISPLAY_PAGES_ON_MENU = True
TIMEZONE = 'America/Detroit'
DATE_FORMAT = { 'en': '%d %m %Y'}
DEFAULT_DATE_FORMAT = '%d %m %Y'
DEFAULT_LANG = u'en'

ARTICLE_PATHS = ['posts']

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
USE_FOLDER_AS_CATEGORY = True
DISPLAY_PAGES_ON_MENU = True
LOAD_CONTENT_CACHE = False

