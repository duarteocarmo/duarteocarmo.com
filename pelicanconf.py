from typing import List, Dict, Any

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
PAGE_PATHS = ["pages"]
DEFAULT_CATEGORY = "blog"
ARTICLE_URL = "{category}/{slug}.html"
ARTICLE_SAVE_AS = "{category}/{slug}.html"
ARTICLE_EXCLUDES = ["html"]
ARTICLE_PATHS = ["posts"]
CATEGORY_URL = "category/{slug}.html"
CATEGORY_SAVE_AS = "category/{slug}.html"
USE_FOLDER_AS_CATEGORY = False
DRAFT_URL = "drafts/{slug}.html"


# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None
FEED_ALL_ATOM = "feed.xml"
FEED_FILTER = {
    "feed.xml": {
        "exclude.categories": ["photos"],
    }
}

# NO EXTRAS
TAGS_SAVE_AS = None
ARCHIVES_SAVE_AS = None
CATEGORIES_SAVE_AS = None
AUTHORS_SAVE_AS = None

# pagination
DEFAULT_PAGINATION = False

# extra paths
STATIC_PATHS = [
    "images",
    "pdfs",
    "extra/robots.txt",
    "pdfs/cv.pdf",
    "extra/CNAME",
    "html",
    "extra/favicons",
]


EXTRA_PATH_METADATA = {
    "extra/robots.txt": {"path": "robots.txt"},
    "pdfs/cv.pdf": {"path": "cv.pdf"},
    "extra/CNAME": {"extra/CNAME": {"path": "CNAME"}},
    "html/StateOfVim.html": {"path": "StateOfVim.html"},
}

FAVICONS_LIST = [
    "android-chrome-192x192.png",
    "android-chrome-512x512.png",
    "apple-touch-icon.png",
    "favicon-16x16.png",
    "favicon-32x32.png",
    "favicon.ico",
    "site.webmanifest",
]

for favicon in FAVICONS_LIST:
    EXTRA_PATH_METADATA[f"extra/favicons/{favicon}"] = {"path": f"favicons/{favicon}"}

# MARKDOWN
MARKDOWN = {
    "extensions": [
        "markdown.extensions.toc",
        "markdown.extensions.fenced_code",
        "markdown.extensions.codehilite",
        "markdown.extensions.tables"
    ]
}

# PLUGINS
PLUGIN_PATHS = ["plugins"]
PLUGINS = [
    "pelican.plugins.feed_filter",
    "plugins.podcast",
    "plugins.photos",
    "sitemap",
    "simple_footnotes",
]
SITEMAP = {
    "exclude": ["archives.html", "author/", "category/", "photos/"],
    "format": "xml",
    "priorities": {"articles": 0.9, "indexes": 0.5, "pages": 0.9},
    "changefreqs": {
        "articles": "hourly",
        "indexes": "hourly",
        "pages": "hourly",
    },
}

# Define a TALKS variable accessible in your templates
TALKS: List[Dict[str, Any]] = [
    {
        "title": "Panel: The Dashboard That Grew - A Scaling Saga",
        "url": "https://pydata.org/global2024",
        "resources": [
            {"text": "slides", "url": "/pdfs/pydata-global-panel-the-dashboard-that-grew.pdf"}
        ],
    },
    {
        "title": "You also hate SQL? Let the LLM handle it",
        "url": "https://pyconwroclaw.com/",
        "resources": [
            {"text": "slides", "url": "/pdfs/pycon-wroclaw-llm-text-to-sql.pdf"}
        ],
    },
    {
        "title": "Go Time",
        "url": "https://changelog.com/gotime/308",
        "resources": []
    },
    {
        "title": "The A.I. and Digital Transformation Podcast",
        "url": "https://www.gmscconsulting.com/ai-and-digital-transformation-podcast/episode-12",
        "resources": [
            {"text": "video", "url": "https://youtu.be/9l0BTZipArQ?si=uSpvwFWcIjYwu7Xn"}
        ],
    },
    # Add more talk entries as needed
]
