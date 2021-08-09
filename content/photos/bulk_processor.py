import sys
from PIL import Image
import pathlib
import lzma
import json
import shutil
import re


def crop_center(pil_img, crop_width, crop_height):
    img_width, img_height = pil_img.size
    return pil_img.crop(
        (
            (img_width - crop_width) // 2,
            (img_height - crop_height) // 2,
            (img_width + crop_width) // 2,
            (img_height + crop_height) // 2,
        )
    )


def crop_max_square(pil_img):
    return crop_center(pil_img, min(pil_img.size), min(pil_img.size))


dump_folder = pathlib.Path("profile_dump")

"""
category: photos
title: 2020-11-24-02
date: 2020-11-24
location: Lisbon, Portugal
photo_url: https://duarteocarmo-photo-storage.s3.eu-west-1.amazonaws.com/2020-11-24_21-57-46_UTC_2.jpg
thumbnail_url: https://duarteocarmo-photo-storage.s3.eu-west-1.amazonaws.com/2020-11-24_21-57-46_UTC_2-thumbnail.jpg
"""

for file in dump_folder.glob("**/*.jpg"):
    # create compressed thumbnail
    # create markdown file
    if len(file.stem) >= 25:
        title = file.stem[0:10] + "-0" + file.stem[-1:]
        info_json = str(file).partition("UTC")[0] + "UTC.json.xz"
        info_caption = str(file).partition("UTC")[0] + "UTC.txt"
    else:
        title = file.stem[0:10] + "-00"
        info_json = str(file).replace("jpg", "json.xz")
        info_caption = str(file).replace("jpg", "txt")

    with lzma.open(info_json) as f:
        json_bytes = f.read()
        stri = json_bytes.decode("utf-8")
        data = json.loads(stri)
        try:
            location = data.get("node").get("location").get("name")
        except Exception as e:
            location = None

    if pathlib.Path(info_caption).is_file():
        caption = pathlib.Path(info_caption).read_text()
        print(f"Raw: {caption}")
        caption = re.sub("#[A-Za-z0-9_]+", "", caption)
        caption = caption.replace("\n.\n", "")
        caption = caption.replace("..", ".")
        caption = caption.replace("\n", " ")
        print(f"Raw: {caption}")

    else:
        caption = None

    date = file.stem[0:10]

    photo_url = f"https://d22fkxs2pw9y3y.cloudfront.net/{title}.jpg"
    thumbnail_url = (
        f"https://d22fkxs2pw9y3y.cloudfront.net/{title}-thumbnail.webp"
    )

    file_string = f"category: photos \ntitle: {title}\ndate: {date}\nlocation: {location}"
    file_string += f"\nphoto_url: {photo_url}\nthumbnail_url: {thumbnail_url}\n\n{caption}"

    clean_file_destination = pathlib.Path(f"processed_profile/{title}.jpg")

    shutil.copy(file, clean_file_destination)
    f = open(f"processed_profile/{title}.md", "w+")
    f.write(file_string)
    f.close()

    im = Image.open(file)
    im_new = crop_max_square(im)
    im_new.save(
        f"processed_profile/{title}-thumbnail.jpg", quality=50, optimize=True
    )

    im_new.save(
        f"processed_profile/{title}-thumbnail.webp", quality=50, optimize=True
    )

    print("-" * 50)
