import os
import sys

sys.path.append(os.curdir)
from pelicanconf import *

# If your site is available via HTTPS, make sure SITEURL begins with https://
SITEURL = "https://duarteocarmo.com"
RELATIVE_URLS = False
FEED_ALL_ATOM = "feed.xml"
DELETE_OUTPUT_DIRECTORY = True
GOOGLE_ANALYTICS = False
GOAT_COUNTER = False
PLAUSIBLE = True
