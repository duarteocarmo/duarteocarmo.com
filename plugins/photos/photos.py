from pelican import signals
from pelican.readers import BaseReader
import datetime
from pelican.contents import Article
import logging
import json
import boto3
import os
from concurrent.futures import ThreadPoolExecutor
from diskcache import Cache

PHOTO_BUCKET_URL = os.getenv("PHOTO_BUCKET_URL", "")
PHOTO_BUCKET_PUBLIC_URL = os.getenv("PHOTO_BUCKET_PUBLIC_URL", "")
AWS_ACCESS_KEY_ID = os.getenv("AWS_ACCESS_KEY_ID", "")
AWS_SECRET_ACCESS_KEY = os.getenv("AWS_SECRET_ACCESS_KEY", "")
PHOTO_BUCKET_NAME = os.getenv("PHOTO_BUCKET_NAME", "")


log = logging.getLogger(__name__)
cache = Cache(".cachedir/")


def addPhotos(articleGenerator):
    settings = articleGenerator.settings
    baseReader = BaseReader(settings)
    photos_data = load_photos_from(PHOTO_BUCKET_NAME)
    counter = 0

    for photo in photos_data:
        date = photo.get("date", "")

        if len(date) > 10:
            date = date[:10]

        date_object = datetime.datetime.strptime(date, "%Y-%m-%d")

        location = photo.get("location")
        caption = photo.get("caption", "")
        _id = photo.get("id")
        photo_url = f"{PHOTO_BUCKET_PUBLIC_URL}/{_id}.jpg"
        thumbnail_url = f"{PHOTO_BUCKET_PUBLIC_URL}/{_id}.webp"

        newArticle = Article(
            caption,
            {
                "title": date,
                "date": date_object,
                "location": location,
                "photo_url": photo_url,
                "thumbnail_url": thumbnail_url,
                "category": baseReader.process_metadata("category", "photos"),
                "url": f"photos/{_id}.html",
                "save_as": f"photos/{_id}.html",
            },
        )

        articleGenerator.articles.append(newArticle)
        counter += 1

    log.info(f"Added {counter} photos to the article list")


@cache.memoize(expire=3600)
def load_photos_from(bucket_name: str) -> list[dict]:
    s3 = boto3.client(
        "s3",
        aws_access_key_id=AWS_ACCESS_KEY_ID,
        aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
        endpoint_url=PHOTO_BUCKET_URL,
        region_name="auto",
    )
    objects = s3.list_objects_v2(Bucket=bucket_name)["Contents"]

    json_files = [obj["Key"] for obj in objects if obj["Key"].endswith(".json")]

    photos_data = []
    log.warning(f"Downloading photo metadata from : {PHOTO_BUCKET_URL}")
    with ThreadPoolExecutor(max_workers=10) as executor:
        futures = {
            executor.submit(
                get_photo_metadata, json_file, s3, PHOTO_BUCKET_NAME
            ): json_file
            for json_file in json_files
        }
        for future in futures:
            result = future.result()
            photos_data.append(result)

    log.warning("Finished downloading photo metadata")
    photos_data = [photo for photo in photos_data if photo is not None]
    return photos_data


def get_photo_metadata(json_file_key, s3, bucket_name):
    try:
        response = s3.get_object(Bucket=bucket_name, Key=json_file_key)
        content = response["Body"].read()
        return json.loads(content)
    except Exception as e:
        log.error(f"Failed to download {json_file_key}: {e}")
        return None


def register():
    signals.article_generator_finalized.connect(addPhotos)
