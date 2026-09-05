import importlib.util
from pathlib import Path
from urllib.parse import urljoin


def load_variable_from(*, filename: str, variable_name: str):
    module_path = Path(__file__).resolve().parent / filename
    spec = importlib.util.spec_from_file_location(name=module_path.stem, location=module_path)
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return getattr(module, variable_name)


AUTHOR = "Duarte O.Carmo"
SITENAME = "Duarte O.Carmo"
SITEURL: str = ""
SITE_DESCRIPTION = (
    "The personal website of Duarte O.Carmo. A technologist/consultant "
    "from Lisbon, now based in Copenhagen."
)
INTRO_TEXT = [
    "Hi, I'm Duarte <i><code>du-art</code></i>. I'm a technologist from Lisbon, now based in Copenhagen. I work across machine learning, data, software, and people.",
    "I've worked in consumer electronics, public institutions, management consulting, and YC-backed startups. The common thread is solving hard problems end to end.",
]
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
    "extra/ard.json",
    "extra/openapi.json",
    "extra/mcp-server-card.json",
    "pdfs/cv.pdf",
    "html",
    "extra/favicons",
]


EXTRA_PATH_METADATA = {
    "extra/robots.txt": {"path": "robots.txt"},
    "extra/ard.json": {"path": ".well-known/ard.json"},
    "extra/openapi.json": {"path": "openapi.json"},
    "extra/mcp-server-card.json": {"path": ".well-known/mcp/server-card.json"},
    "pdfs/cv.pdf": {"path": "cv.pdf"},
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

JINJA_FILTERS = {"urljoin": urljoin}

# MARKDOWN
MARKDOWN = {
    "extensions": [
        "markdown.extensions.toc",
        "markdown.extensions.fenced_code",
        "markdown.extensions.codehilite",
        "markdown.extensions.tables",
    ]
}

# PLUGINS
PLUGIN_PATHS = ["plugins"]
PLUGINS = [
    "pelican.plugins.feed_filter",
    "plugins.podcast",
    "plugins.photos",
    "plugins.api",
    "plugins.llms",
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
BOOKS = load_variable_from(filename="books.py", variable_name="BOOKS")
TALKS = load_variable_from(filename="talks.py", variable_name="TALKS")
