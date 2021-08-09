import sys
from PIL import Image


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


file = sys.argv[1]
filename = file.split(".")[0]
im = Image.open(file)
im_new = crop_max_square(im)
im_new.save(
    f"{filename}-thumbnail.webp", quality=50, optimize=True
)
print("Done.")
