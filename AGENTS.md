# Project instructions

- Use `cwebp` to convert images to WebP before adding them to posts.
- Link to other blog posts with Pelican-style links, for example: `[text]({filename}/posts/88-tts-still-sucks.md)`.
- Put post-specific assets in `content/images/<post-number>/`, and reference them with `{static}/images/<post-number>/<filename>`.
- Preferred image style: center the image, make it clickable to the full-size asset, use `style="max-width:100%;border-radius: 2px"`, and put the caption in a `<figcaption>` block below it.
- The consulting page client banner is built by `plugins/clients` from the PNG logos in `content/clients/`. To add a client, add a PNG there; layout and ordering are automatic.
- Do not run `make build` while `make run` is active: both write to `output/`.
