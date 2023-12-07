title: You can now listen to this blog
date: 12-07-2023 08:00
description:  # TODO 
status: published
slug: you-can-now-listen-to-this-blog
thumbnail: # TODO 

One of my favorite [Portuguese columnists](https://www.publico.pt/autor/joao-miguel-tavares) has this weird thing about his opinion column. Maybe it's more common than I thought. But for every piece he publishes, he also publishes a podcast version along with it. 

Now, either Publico.pt has 27th century text-to-speech (TTS) technology, or he's _actually_ reading them. I don't have a problem with that, but I'm _pretty_ sure we could automate that part of the deal on today's age. 

And sure, I've heard all the rage about voice cloning services like [ElevenLabs](https://elevenlabs.io/pricing). But if you've been following this blog for while, you probably guessed that we're not just going to use an API. We'll probably build one from scratch. 

## The engine

The premise was not simple, but pretty easy to understand. I wanted something that transcribed every new article of this blog, using _my own_ voice. It needed to be cheap, automatic, and not get in the way of my writing/publishing flow. 

[Podcaster](https://github.com/duarteocarmo/podcaster/) is the result. It runs 100% on github actions, scans every new blog post in my RSS feed, and uses [XTTS-v2](https://huggingface.co/coqui/XTTS-v2) to transcribe it with a clone of my voice. The only thing it needs is a 1 min snippet of my voice. I tried [Bark](https://tts.readthedocs.io/en/latest/models/bark.html), 
and a couple of other models, but this was the only one that made Vittoria come into the room when I was testing things around. 

I wanted the whole thing to run on [Github Actions](https://github.com/duarteocarmo/podcaster/actions). But these models are pretty slow when running on CPU. Fortunately, I finally took [Modal](https://modal.com) for a spin, and I'm happy to report that the future of serverless GPUs could not look brighter:

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

Podcaster also stores all the transcripts in S3, automatically generates a podcast feed from them, and triggers a new build of this blog. Again, pretty much for free. 

If you're interested in taking it for a spin, [should be straightforward](https://github.com/duarteocarmo/podcaster#readme) to get started.

## Integrating with Pelican

I really _don't_ like adding friction to my publishing flow. I mean, writing is already hard as is! So I needed to figure out a way of automatically updating it with transcripts once I publish. Without me having to do anything at all. 

Fortunately, [Justin](https://justinmayer.com/about/) is not only great company at PyCon Italia every year, but has also built a pretty easy and [robust plugin system for Pelican](https://docs.getpelican.com/en/latest/plugins.html). All I really had to do, was to add a [`podcaster` plugin](https://github.com/duarteocarmo/duarteocarmo.com/tree/master/plugins) to my website. Without me worrying, it will add the html to every article if there's a transcript available in the podcast feed. So it _should_ run without me having to do anything.

## Final thoughts

Not gonna lie, I had a lot of fun building this, and also learned a lot. First, it demystified the whole podcast hosting thing for me. Turns just a bunch of mp3 files in a bucket with a feed [will do it](https://podcasts.apple.com/dk/podcast/duarte-o-carmos-articles/id1719493997). 

Second, many times I've settled for running ML models on CPU. Using GPUs at runtime meant having to deal with infrastructure I didn't needed. I was really impressed at how easy [Modal](https://modal.com/) was to use, and can definitely think of other applications where it would be useful. 

Finally, I was super impressed with the state of TTS and voice cloning technology. Is it perfect? No. Does it have some artifacts? Yes. Does it sound like a robot sometimes? Yes. But remember, I _only_ gave it a minute of my voice. Open source never seizes to amaze me
