#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
import pelican

AUTHOR = "Duarte O.Carmo"
SITENAME = "Duarte O.Carmo"
SITEURL = ""
SITE_DESCRIPTION = (
    "My personal website. Here, you can read my blog posts, and learn about my"
    " projects. I write about data science, AI, programming, business, and"
    " other topics. "
)
# TODO
SITELOGO = "images/logo.png"
PATH = "content"
TIMEZONE = "Europe/Copenhagen"
DEFAULT_LANG = "en"

PAGE_URL = "{slug}/"
PAGE_SAVE_AS = "{slug}.html"
ARTICLE_URL = "blog/{slug}.html"
ARTICLE_SAVE_AS = "blog/{slug}.html"
ARTICLE_EXCLUDES = ["html"]

# SEO
PELICAN_VERSION = pelican.__version__

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None
FEED_ALL_ATOM = "feed.xml"

# NO EXTRAS
TAGS_SAVE_AS = None
ARCHIVES_SAVE_AS = None
CATEGORIES_SAVE_AS = None
AUTHORS_SAVE_AS = None

# Social widget
SOCIAL = (
    ("You can add links in your config file", "#"),
    ("Another social link", "#"),
)

# pagination
DEFAULT_PAGINATION = False

# extra paths
STATIC_PATHS = [
    "images",
    "pdfs",
    "extra/favicon.ico",
    "pdfs/cv.pdf",
    "extra/CNAME",
    "html",
]
EXTRA_PATH_METADATA = {
    "extra/favicon.ico": {"path": "favicon.ico"},
    "pdfs/cv.pdf": {"path": "cv.pdf"},
    "extra/CNAME": {"extra/CNAME": {"path": "CNAME"}},
    "html/StateOfVim.html": {"path": "StateOfVim.html"},
}

# SOCIAL
TWITTER_HANDLE = "duarteocarmo"

# MARKDOWN
MARKDOWN = {
    "extensions": ["markdown.extensions.toc", "markdown.extensions.fenced_code",]
}

# PLUGINS
PLUGIN_PATHS = ["plugins"]
PLUGINS = ["pelican.plugins.sitemap", "pelican.plugins.simple_footnotes"]
SITEMAP = {
    "exclude": ["archives.html", "author/", "category/"],
    "format": "xml",
    "priorities": {"articles": 0.9, "indexes": 0.5, "pages": 0.9},
    "changefreqs": {"articles": "hourly", "indexes": "hourly", "pages": "hourly",},
}
