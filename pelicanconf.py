AUTHOR = "Duarte O.Carmo"
SITENAME = "Duarte O.Carmo"
SITEURL = ""
SITE_DESCRIPTION = (
    "The personal website of Duarte O.Carmo. A technologist/consultant "
    "from Lisbon, now based in Copenhagen."
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
        "markdown.extensions.tables",
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
TALKS = [
    {
        "text": "Panel: The Dashboard That Grew - A Scaling Saga",
        "links": [
            {"text": "PyData Global 2024", "url": "https://pydata.org/global2024"},
            {
                "text": "Slides",
                "url": "/pdfs/pydata-global-panel-the-dashboard-that-grew.pdf",
            },
        ],
    },
    {
        "text": "You also hate SQL? Let the LLM handle it",
        "links": [
            {"text": "PyCon Wroclaw", "url": "https://pyconwroclaw.com/"},
            {"text": "Slides", "url": "/pdfs/pycon-wroclaw-llm-text-to-sql.pdf"},
        ],
    },
    {
        "text": "Go Time",
        "links": [{"text": "Podcast", "url": "https://changelog.com/gotime/308"}],
    },
    {
        "text": "The A.I. and Digital Transformation Podcast",
        "links": [
            {
                "text": "Podcast",
                "url": "https://www.gmscconsulting.com/ai-and-digital-transformation-podcast/episode-12",
            },
            {
                "text": "Video",
                "url": "https://youtu.be/9l0BTZipArQ?si=uSpvwFWcIjYwu7Xn",
            },
        ],
    },
    {
        "text": "Verbos AI Podcast",
        "links": [
            {
                "text": "Podcast",
                "url": "https://open.spotify.com/episode/0Ja8xzuiOAYZeD4WSP8TxL?si=0JFkY1fWRwCf0_BkiUUfvA&nd=1",
            },
            {
                "text": "Video",
                "url": "https://youtu.be/7nT4NrdjUF4?si=oLVzEF_iRE4qz_Qy",
            },
        ],
    },
    {
        "text": "ML in the wild 2nd Edition",
        "links": [
            {"text": "DIS", "url": "https://disabroad.org/copenhagen/"},
            {"text": "Slides", "url": "/pdfs/ml-in-the-wild-v2.pdf"},
        ],
    },
    {
        "text": "An introduction to Google Earth Engine",
        "links": [
            {"text": "EuroSciPy", "url": "https://www.euroscipy.org/2023/"},
            {"text": "Slides", "url": "/pdfs/euroscipy-gee-intro.pdf"},
            {
                "text": "Video",
                "url": "https://youtu.be/GXBPOlSxfoY?si=79ZSKAFu8vdW8J8W",
            },
        ],
    },
    {
        "text": "On Scaling Machine Learning Microservices",
        "links": [
            {"text": "PyCon Italia", "url": "https://pycon.it/en"},
            {"text": "Slides", "url": "/pdfs/pycon-italia-scalable-ml.pdf"},
            {"text": "Video", "url": "https://www.youtube.com/watch?v=T1Je3UHkxVk"},
        ],
    },
    {
        "text": "Real Python Podcast",
        "links": [
            {"text": "Podcast", "url": "https://realpython.com/podcasts/rpp/150/"}
        ],
    },
    {
        "text": "ML in the wild",
        "links": [
            {"text": "DIS", "url": "https://disabroad.org/copenhagen/"},
            {"text": "Slides", "url": "/pdfs/ml-in-the-wild.pdf"},
            {"text": "Feedback", "url": "/pdfs/dis_feedback.pdf"},
        ],
    },
    {
        "text": "MLOps for the rest of us",
        "links": [
            {
                "text": "PyData Copenhagen",
                "url": "https://www.meetup.com/pydata-copenhagen/",
            },
            {"text": "Slides", "url": "/pdfs/pydata-cph-mlops-for-the-rest-of-us.pdf"},
        ],
    },
    {
        "text": "Bag of tricks to scale ML Apps",
        "links": [
            {
                "text": "DTU MLOps Course",
                "url": "https://skaftenicki.github.io/dtu_mlops/",
            },
            {"text": "Slides", "url": "/pdfs/bag-of-tricks-scalable-api.pdf"},
        ],
    },
    {
        "text": "Taming the black box",
        "links": [
            {
                "text": "DTU MLOps Course",
                "url": "https://skaftenicki.github.io/dtu_mlops/",
            },
            {"text": "Slides", "url": "/pdfs/mlops-monitoring-sanitized.pdf"},
        ],
    },
    {
        "text": "MLOps for the rest of us",
        "links": [
            {"text": "PyData Global", "url": "https://pydata.org/global2022/"},
            {"text": "Slides", "url": "/pdfs/mlops-for-the-rest-of-us.pdf"},
            {"text": "Video", "url": "https://www.youtube.com/watch?v=R6lPb9Meqoc"},
        ],
    },
    {
        "text": "MLOps Live Podcast",
        "links": [
            {
                "text": "Podcast",
                "url": "https://podcasts.bcast.fm/e/r8k1qky8-early-stage-startups-small-teams-mlops-duarte-carmo",
            },
            {"text": "Video", "url": "https://youtu.be/sqv1ydViDgA"},
        ],
    },
    {
        "text": "Machine learning! (But in the real world)",
        "links": [
            {"text": "LIP Coimbra", "url": "https://pages.lip.pt/data-science/"},
            {"text": "Slides", "url": "/pdfs/lip-2022-sanitized.pdf"},
        ],
    },
    {
        "text": "Four years of Python",
        "links": [
            {"text": "PyCon Italia", "url": "https://pycon.it/en"},
            {"text": "Slides", "url": "/pdfs/four-years-of-python-pycon.pdf"},
            {"text": "Video", "url": "https://www.youtube.com/watch?v=zB_Hr-05Stc"},
        ],
    },
    {
        "text": "Four years of Python",
        "links": [
            {
                "text": "PyData Copenhagen",
                "url": "https://www.meetup.com/pydata-copenhagen/",
            },
            {"text": "Slides", "url": "/pdfs/four-years-of-python-pydata.pdf"},
        ],
    },
    {
        "text": "Measuring the uniqueness of technological capabilities",
        "links": [
            {"text": "DTU", "url": "https://www.dtu.dk/english"},
            {
                "text": "Slides",
                "url": "https://dl.dropboxusercontent.com/s/8h2kvhu6detyo82/Presentation%20Public.pdf",
            },
        ],
    },
]
