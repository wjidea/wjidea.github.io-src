#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'JW'
SITENAME = u'bitBio'
# SITEURL = 'http://wjidea.github.io'
THEME = '/Users/wjidea/OneDrive/ghpages/theme/pelican-cait'
PATH = 'content'
STATIC_PATHS = ['posts', 'files'] # what is this PATH for???
ARTICLE_PATHS = ['posts']
ARTICLE_SAVE_AS = '{date:%Y}/{slug}.html'
ARTICLE_URL = '{date:%Y}/{slug}.html'
PAGE_PATH = ['content/pages','content']

# TIME and DATYE
TIMEZONE = 'America/Detroit'
DEFAULT_DATE = 'fs'
DATE_FORMAT = { 'en': '%m %d %Y'}
# DEFAULT_DATE_FORMAT = '%m %d %Y'
DEFAULT_LANG = u'en'
SUMMARY_MAX_LENGTH = 150


USE_CUSTOM_MENU = True
CUSTOM_MENUITEMS = [
			  ('Home', '#'),
			  ('Blog', 'category/article.html'),
              ('Contact', 'pages/contact.html')]
              #('Research','files/researchStatement.pdf'),
              #('CV','files/CV-Wang_noRef.pdf')]

# CONTACT
CONTACT_EMAIL = "wjidea@gmail.com"
CONTACTS = (('twitter', 'https://twitter.com/wjidea'),
			('github', 'https://github.com/wjidea'),
			('facebook', 'https://facebook.com/wjidea'),
			('linkedin','https://www.linkedin.com/in/wjidea'))


# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'))
# Social widget
SOCIAL = (('twitter', 'https://twitter.com/wjidea'),
          ('github-alt', 'https://github.com/wjidea'),
          ('facebook', 'https://facebook.com/wjidea'),
          ('weibo', 'https://weibo.com/u/1733966500'),
          ('linkedin','https://www.linkedin.com/in/wjidea'))

DISQUS_SITENAME='bitbio.disqus.com'

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
USE_FOLDER_AS_CATEGORY = True
DISPLAY_PAGES_ON_MENU = False
LOAD_CONTENT_CACHE = False

