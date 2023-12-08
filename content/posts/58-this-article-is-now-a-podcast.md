title: You can now listen to this blog
date: 12-08-2023 05:00
description: Cloning my voice and automatically generating transcripts for my blog
status: published
slug: you-can-now-listen-to-this-blog
thumbnail: images/58/podcaster.png

One of my favorite [Portuguese columnists](https://www.publico.pt/autor/joao-miguel-tavares) has this weird thing about his column. Maybe it's more common than I thought. For every piece he publishes, he also publishes a podcast version along with it. 

Now, either [Publico](https://www.publico.pt/) has 27th century text-to-speech (TTS) technology, or he's _actually_ reading them. I don't have a problem with that, but I'm _pretty_ sure we could automate that part of the process with today's tech. 

And yeah, I've heard all the rage about voice cloning services like [ElevenLabs](https://elevenlabs.io/pricing). But if you've been following this blog for a while, you probably guessed that we're not just gonna use an API. We're probably gonna build one from scratch. 

## An engine

The premise did not appear simple to build, but was easy to understand. Something that transcribes every new article of this blog using _my own_ voice. It needs to be cheap, seamless, and most importantly, not get in the way. Writing is _enough_ work as is. 

The result is [podcaster](https://github.com/duarteocarmo/podcaster/). It runs 100% on GitHub Actions, it scans every new blog post in my RSS feed and uses [XTTS-v2](https://huggingface.co/coqui/XTTS-v2) to transcribe it. The only thing it needs from me is a 1-min audio file. I tried [Bark](https://tts.readthedocs.io/en/latest/models/bark.html) and a couple of other models, but this was the only one that made Vittoria come into the room when I was testing things around. 

It's not that I hate infrastructure, I just wanted the whole thing to run on CI. All these TTS models are slow when running on the CPU. But instead of embarking on another painful journey through the world of GPU computing, I found [Modal](https://modal.com). I'm happy to report that I've regained faith in the future of serverless GPUs:

```python
# define the image
MODAL_IMAGE = (
    modal.Image.debian_slim()
    .pip_install_from_pyproject("pyproject.toml")
    .apt_install("ffmpeg")
)
stub = modal.Stub("modal-app", image=MODAL_IMAGE)

# create the function
@stub.function(gpu="any")
def transcribe(
    article: ParsedArticle,
    voice_file: str = VOICE_FILE,
    model_name: str = MODEL_NAME,
    language: str = LANGUAGE,
) -> bytes:
    # this part is executed in a GPU powered machine
    # ...
```

The engine stores all transcripts in S3, automatically generates a podcast feed from them (using [feedgen](https://feedgen.kiesow.be/)), and uses web hooks to trigger a new build of this blog. Again, pretty much for free. If you're curious or interested in taking it for a spin, [should be straightforward](https://github.com/duarteocarmo/podcaster#readme) to get started.

## Integrating with Pelican

As I said before: I really _don't_ like adding friction to my writing. It's already hard as is! The challenge then was to figure a way of automagically updating the blog with available transcripts after I publish, without me having to do anything at all. 

Fortunately, [Justin](https://justinmayer.com/about/) besides being great company at PyCon Italia every year, has also built a pretty [robust plugin system for Pelican](https://docs.getpelican.com/en/latest/plugins.html). All I had to do, was to add a [`podcaster` plugin](https://github.com/duarteocarmo/duarteocarmo.com/blob/master/plugins/podcast/podcast.py) to this website. The plugin automatically matches articles to corresponding episodes, and adds that short html snippet you're seeing above. Should be _build once_ and let run. Hopefully at least.


## Final thoughts

I had a lot of fun building this, and also learned a lot. First, it demystified the whole podcast hosting thing for me. Turns out, it's just a bunch of mp3 files in a bucket with [a rss feed](https://podcasts.apple.com/dk/podcast/duarte-o-carmos-articles/id1719493997). 

Often I've settled for running ML models on CPU just because deploying with a GPU was much more of a pain, and didn't add any happiness to the process. At least for now, GPUs are here to stay, hopefully so are services like [Modal](https://modal.com/). Pythonic, easy to use, and easy to isolate from the rest of the code base.

Finally, I was very impressed with the state of TTS and voice cloning technology. Is it perfect? No. Does it have some artifacts? Yes. Does it sound like a robot sometimes? Sure. But remember, I _only gave it a minute_ of my voice.

Open source never ceases to amaze me.
