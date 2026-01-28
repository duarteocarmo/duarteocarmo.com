title: Retrospectiva #2
description: A monthly newsletter about life.
date: 25th of November 2025
status: published
audio: true
thumbnail: images/90/cover.png

Big news in the state of Denmark. And no, [nothing's rotten](https://www.shakespeare-online.com/quickquotes/quickquotehamletdenmark.html). Allegra just came into the world.

As she takes a nap, I take the opportunity to write November's Retrospectiva update.

The most relevant thing this month is probably the release of my [recent book about DeepSeek](https://duarteocarmo.com/blog/book-release-deepseek-in-practice). It's nice to see it finally come to life. I've also been getting more regular in my running, hitting a nice weekly volume more consistently, it does get harder with cold weather. Given the recent events, I'm not sure it will last. In the midst of Vitamin D tablets and diapers, we'll do, as always, the best we can.

## Using

In preparation for the baby arriving, I hunted for a pair of headphones I could wear during calls. It needed to do two things: have a microphone that blocks out any surrounding noises (you know), but at the same time allow me to be aware of my surroundings. I regularly wear the [Open Run](https://shokz.com/pages/openrun) for running. I've enjoyed the bone conduction when I need to be aware of what's around me. I decided to take the plunge and get the [OpenMeet](https://shokz.com/products/openmeet)'s. After a month of use, I definitely recommend them. They are niche though: they do the *exact opposite* of cancelling the noise around you - so be aware of that.

For years, I've been a fan of [Jupyter Notebooks](https://jupyter.org/). If it's more than a script, and I need to know what's going on with the data, notebooks are the way I go. After reading so much about it, I decided to finally try [Marimo](https://marimo.io/) ([just acquired by Coreweave](https://www.coreweave.com/news/coreweave-acquires-marimo-to-unify-the-generative-ai-developer-workflow)). The visuals and [components](https://docs.marimo.io/examples/) are nice and extensive. The fact that any notebook is *just* a uv script makes things *very* reproducible. You can also transform notebooks into dashboards [and embed](https://docs.marimo.io/guides/deploying/programmatically/) them into your FastAPI app which is great. But most of my notebooks don't need an AI panel, MCP connectors, interactive cells, and other bells and whistles. They need to show cell outputs at the bottom, a running order I can understand, Copilot, and VIM bindings. That's it.

So for now, my go-to is still:

```bash
uv run --with jupyter --with jupyter_copilot --with jupyterlab-vim jupyter lab

```

On a final note, I got completely rid of [Dropbox](www.dropbox.com). For years, it's been the tool of choice for my *important* documents. They've been asking me to upgrade to a paid plan for years now to go beyond my 3GB limit(!). I've replaced it with self hosted [NextCloud](https://nextcloud.com/) on my [Coolify](https://duarteocarmo.com/blog/how-i-self-host-in-2024) instance. Now I have unlimited space, a lighter mac client, and exactly the same features. Without spending a single cent more.

## Reading

I finally took the plunge, and have gone back to reading some good old science fiction (the last thing I got seriously into was the [Red Rising ](https://www.goodreads.com/series/117100-red-rising-saga)series). I've been a John Scalzi fan for a long time, so I decided to pick up [Old Man's War](https://www.goodreads.com/book/show/36510196-old-man-s-war). I like Scalzi's straight, direct, and *no-bs* writing style. Great for when I don't have the lights on and have to rely on my [Palma](https://duarteocarmo.com/blog/goodbye-kindle-i-dont-think-ill-miss-you).

I'm also diving deep into LLM architectures and pre-training this month. [*"FineWeb: decanting the web for the finest text data at scale"*](https://huggingface.co/spaces/HuggingFaceFW/blogpost-fineweb-v1), was an insightful view into the world of creating datasets for pre-training. Full of gems. One of my favorites was the in-depth explanation of the [FineWeb-Edu classifier](https://huggingface.co/spaces/HuggingFaceFW/blogpost-fineweb-v1). The idea is simple: to train a classifier we can use to filter pre-training data in order to get the most "refined" pretraining dataset possible.

Highly related to that, I ordered *["The Ultra-Scale Playbook: Training LLMs on GPU Clusters"](https://www.lulu.com/shop/nouamane-tazi-and-ferdinand-mom-and-haojun-zhao-and-phuc-nguyen/the-ultra-scale-playbook/paperback/product-45yk9dj.html?page=1&pageSize=4)*. It’s the second book in this "trilogy" of blog posts (3rd one still being written). It starts off with some basic concepts like Data, Tensor, and Context Parallelism, but goes off to more advanced things like training configurations and GPU kernels. You can really feel the "war stories" some of the authors went through before writing it.

## Listening

I gave Apple Music a fair shot, but I had to go back to Spotify. Music is too important to have a search functionality that doesn't work. I don't want a single barrier between me and what I want to listen to.

There are a lot of things wrong with Apple Music. But one good thing is the live radio and shows hosted on there. Particularly [Classical Connections Radio](https://music.apple.com/us/curator/classical-connections-radio-with-alexis-ffrench/1653477785) which blends modern and classical music in a very original way. That show led me to the deep rabbit hole of [Duduk](https://en.wikipedia.org/wiki/Duduk) based music, which is particularly useful for soothing a sleeping baby.

Here's an amazing one by [Djivan Gasparyan](https://en.wikipedia.org/wiki/Djivan_Gasparyan):

<iframe data-testid="embed-iframe" style="border-radius:12px" src="https://open.spotify.com/embed/track/74EHZDVuASkFGH5BSy9KPp?utm_source=generator&theme=0" width="100%" height="152" frameBorder="0" allowfullscreen="" allow="autoplay; clipboard-write; encrypted-media; fullscreen; picture-in-picture" loading="lazy"></iframe>

## Watching

We found some time to pull the old projector out. Lately, the focus has been Spanish thrillers (or as Italians call the genre: *giallo* - i.e., yellow). The Netflix Spain originals based on [Javier Castillo's](https://www.goodreads.com/author/show/8339062.Javier_Castillo) writing have been the binge target. First up was the [Crystal Cuckoo](https://www.rottentomatoes.com/tv/the_crystal_cuckoo), which was definitely entertaining. That sparked our interest, so we started ["Chica de Nieve"](https://www.rottentomatoes.com/tv/the_snow_girl) (i.e., the Snow Girl), which has been even better so far.

<center>
<iframe width="100%" height="315" src="https://www.youtube.com/embed/SPcE8J2Xwjc?si=c54oLGgCNVrSveDq&amp;controls=0" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
</center>
