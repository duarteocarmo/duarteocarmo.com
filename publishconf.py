#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

# This file is only used if you use `make publish` or
# explicitly specify it as your config file.

import os
import sys

sys.path.append(os.curdir)
from pelicanconf import *

# If your site is available via HTTPS, make sure SITEURL begins with https://
SITEURL = "https://duarteocarmo.com"
RELATIVE_URLS = False

FEED_ALL_ATOM = "feed.xml"

DELETE_OUTPUT_DIRECTORY = True

GOOGLE_ANALYTICS = "G-B1G7KP3ZF4"
