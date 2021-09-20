title: Self-hosting my Instagram profile
date: 20-09-2021
description: Moving my Instagram profile to /photos
status: published
slug: self-hosting-instagram-python

After more than 5 years using Instagram, I decided it's time to move out. This "turning" point for me, is when I start loosing control and influence over the platform I'm using. This happens in a multitude of ways: Loosing control of what we consume/see (a) by means of a completely algorithmic feed, being served a multitude of ads (b), and being pushed to consume, rather then share (c).

So I created [/photos](https://duarteocarmo.com/photos)

Bulk downloading them was quite straightforward. Using Python and [Instaloader](https://instaloader.github.com), I was able to retrieve all of my +300 posts from Instagram, including albums. Since I'm using [Pelican](https://docs.getpelican.com/en/latest/) for this static blog, I had to create a "page" for every one of these photos. Which is, albeit, a bit of a hack. But hey, Python is great to automate this type of thing.

The actual photos are now stored in a (probably insecure) S3 bucket, which I sync to a local folder. To keep things fast, I have both Cloudfront (for the photos) and Cloudflare (for the actual blog) sitting on top of them. I'm also using [Pillow](https://pillow.readthedocs.io/en/stable/) to generate thumbnails in `.webp` format, just to ensure the [/photos](https://duarteocarmo.com/photos) page loads relatively fast.

Uploading is by no means as simple as opening an app and snapping a picture. But I've created a small python script that processes a photo, generates a thumbnail, asks some questions about it, and uploads it to S3 and my blog. And that's good enough. 

For those wondering, I still have my [Instagram profile](https://www.instagram.com/duarteoc/) up, which now just serves to redirect people back to my website via a [landing page](https://tinyurl.com/duarteintheinterwebs/). Instagram blocked my url a long time ago - reasons unknown. 

Vittoria suggested I should also email my close friends and family automatically when I upload a photo, I think that's a great idea - but probably a story for another day. 
