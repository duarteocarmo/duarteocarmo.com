"""Build the consulting page client banner from logos in content/clients/.

Add a client by dropping a PNG in that folder. Square icons and wide wordmarks are
interleaved, and rows alternate between COLUMNS and COLUMNS - 1 logos when possible.
"""

from pathlib import Path

import numpy
from pelican import signals
from PIL import Image

COLUMNS = 6
CELL_WIDTH = 536
CELL_HEIGHT = 320
BASE_LOGO_HEIGHT = 170
MAX_LOGO_WIDTH = 360
MAX_LOGO_HEIGHT = 170
LOGO_GRAY = 100
WORDMARK_ASPECT_RATIO = 1.8


def recolor(logo: Image.Image) -> Image.Image:
    pixels = numpy.asarray(logo.convert("RGBA")).astype(numpy.float32) / 255
    luminance = pixels[:, :, :3] @ numpy.array([0.299, 0.587, 0.114])
    ink = pixels[:, :, 3] * (1 - luminance)
    typical_ink = numpy.median(ink[ink > 0.05 * ink.max()])
    ink = numpy.clip(ink / typical_ink, 0, 1)
    output = numpy.full(pixels.shape, LOGO_GRAY, dtype=numpy.uint8)
    output[:, :, 3] = (ink * 255).astype(numpy.uint8)
    return Image.fromarray(output)


def resize_to_visual_weight(logo: Image.Image) -> Image.Image:
    aspect_ratio = logo.width / logo.height
    height = BASE_LOGO_HEIGHT * aspect_ratio**-0.4
    height = min(height, MAX_LOGO_HEIGHT, MAX_LOGO_WIDTH / aspect_ratio)
    return logo.resize(
        size=(round(height * aspect_ratio), round(height)), resample=Image.Resampling.LANCZOS
    )


def spread_evenly(groups: list[list]) -> list:
    positioned_items = [
        ((index + 0.5) / len(group), item) for group in groups for index, item in enumerate(group)
    ]
    return [item for _, item in sorted(positioned_items, key=lambda positioned: positioned[0])]


def interleave_icons_and_wordmarks(logos: list[Image.Image]) -> list[Image.Image]:
    wordmarks = [logo for logo in logos if logo.width / logo.height >= WORDMARK_ASPECT_RATIO]
    icons = [logo for logo in logos if logo.width / logo.height < WORDMARK_ASPECT_RATIO]
    return spread_evenly(groups=[wordmarks, icons])


def row_sizes_for(logo_count: int) -> list[int]:
    if logo_count % COLUMNS == 0:
        return [COLUMNS] * (logo_count // COLUMNS)
    for row_count in range(1, logo_count + 1):
        for first_row_size in (COLUMNS - 1, COLUMNS):
            row_sizes = [
                first_row_size if row_index % 2 == 0 else 2 * COLUMNS - 1 - first_row_size
                for row_index in range(row_count)
            ]
            if sum(row_sizes) == logo_count:
                return row_sizes
            if sum(row_sizes) > logo_count:
                break
    row_count = -(-logo_count // COLUMNS)
    small_row_size = logo_count // row_count
    large_row_count = logo_count % row_count
    return spread_evenly(
        groups=[
            [small_row_size + 1] * large_row_count,
            [small_row_size] * (row_count - large_row_count),
        ]
    )


def build_banner(pelican) -> None:
    logos_directory = Path(pelican.settings["PATH"]) / "clients"
    output_path = Path(pelican.output_path) / "images" / "clients.webp"
    logos = [
        resize_to_visual_weight(logo=recolor(logo=Image.open(logo_path)))
        for logo_path in sorted(logos_directory.glob("*.png"))
    ]
    logos = interleave_icons_and_wordmarks(logos=logos)
    row_sizes = row_sizes_for(logo_count=len(logos))
    banner = Image.new(
        mode="RGBA", size=(COLUMNS * CELL_WIDTH, len(row_sizes) * CELL_HEIGHT), color=(0, 0, 0, 0)
    )
    logo_index = 0
    for row_index, row_size in enumerate(row_sizes):
        row_offset = (COLUMNS - row_size) * CELL_WIDTH / 2
        for column_index in range(row_size):
            logo = logos[logo_index]
            logo_index += 1
            left = row_offset + column_index * CELL_WIDTH + (CELL_WIDTH - logo.width) / 2
            top = row_index * CELL_HEIGHT + (CELL_HEIGHT - logo.height) / 2
            banner.alpha_composite(logo, dest=(round(left), round(top)))

    output_path.parent.mkdir(parents=True, exist_ok=True)
    banner.save(output_path, format="WEBP", quality=90, alpha_quality=100, method=6)
    print(f"[clients] Wrote {len(logos)} logos to {output_path}")


def register():
    signals.finalized.connect(build_banner)
