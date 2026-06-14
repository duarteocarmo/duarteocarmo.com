import os
import sys

sys.path.append(os.curdir)
from pelicanconf import *

# If your site is available via HTTPS, make sure SITEURL begins with https://
SITEURL = "https://duarteocarmo.com"
RELATIVE_URLS = False
FEED_ALL_ATOM = "feed.xml"
UMAMI= True
DELETE_OUTPUT_DIRECTORY = True
PLAUSIBLE = True
