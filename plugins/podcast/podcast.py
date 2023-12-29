from pelican import signals
from pelican.contents import Article
from pelican.generators import ArticlesGenerator
import feedparser
import logging
from diskcache import Cache

PODCAST_FEED = "https://r2.duarteocarmo.com/podcast.xml"
log = logging.getLogger(__name__)
cache = Cache(".cachedir/")


@cache.memoize(expire=3600)
def download_podcast_feed():
    feed = feedparser.parse(PODCAST_FEED)
    link_to_mp3_map = {}

    for feed in feed.entries:
        blog_link = feed.link.split("/")[-1]
        link_to_mp3_map[blog_link] = feed.guid

    return link_to_mp3_map


def add_podcast_link(instance, link_to_mp3_map):
    if type(instance) != Article:
        return

    if instance.metadata.get("category") != "blog":
        return

    blog_link = instance.url.split("/")[-1]
    mp3_link = link_to_mp3_map.get(blog_link)

    if mp3_link is None:
        return

    instance.metadata["mp3_link"] = mp3_link


def run_plugin(generators):
    link_to_mp3_map = download_podcast_feed()
    for generator in generators:
        if isinstance(generator, ArticlesGenerator):
            for article in generator.articles:
                add_podcast_link(article, link_to_mp3_map)


def register():
    try:
        signals.all_generators_finalized.connect(run_plugin)
    except AttributeError:
        # NOTE: This may result in #314 so shouldn't really be relied on
        # https://github.com/getpelican/pelican-plugins/issues/314
        signals.content_object_init.connect(add_podcast_link)
