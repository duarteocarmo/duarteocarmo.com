title:  Changelog neural search
date: 10-04-2023 13:00
description: Neural search .
status: draft
slug: changelog-neural-search-superduperdb
thumbnail: images/55/llama-small-cover.jpg

Search is one of the most important breakthroughs of the internet. Some say a list of blue links is not enough - and that AI will _overthrow_ search. I don't know if a revolution is about to happen; but as with most things - I don't really know until I've tried to build it myself. 

I like podcasts a lot. Hearing people talk about things I know nothing about, it's special. Some of my favorite podcasts are from the [Changelog](https://changelog.com/) network. More than once, I've had to use the [search feature](https://changelog.com/search?q=embedding) when researching something that was said in the past, or studying a particular topic.

One of the best things about the Changelog network is that the [whole thing is open source](https://github.com/thechangelog). From the podcast engine itself, to the [transcripts of every episode](https://github.com/thechangelog/transcripts). So why not take all of these transcripts and build an AI-powered™ search engine around them?

<center>
<a href="https://changelog.duarteocarmo.com">
<img src="{static}/images/56/search.png" alt="Neural search for the changelog" style="max-width:100%;">
</a>
</center>

## How it's built
Before I describe the stack, let's get the obvious out of the way: the whole thing is open source. Both the [back-end](https://github.com/duarteocarmo/thechangelogbot-backend) and the [front-end](https://github.com/duarteocarmo/thechangelogbot-frontend). So if you prefer to go and discover yourself, be my guest.

As previously mentioned, the entire transcript catalog [is open source](https://github.com/thechangelog/transcripts). So I built some logic into parsing and splitting all of the transcripts so I could then embed them. I also save some metadata about each one, in what I called a [snippet](https://github.com/duarteocarmo/thechangelogbot-backend/blob/master/src/thechangelogbot/index/snippet.py). 

I love the chunk-embed-search-retrieve dance as much as the next guy, but for this one, I wanted to keep things a bit simpler, by using something called [SuperDuperDB](https://www.superduperdb.com/). With SuperDuperDB, all I needed to do was add the BGE model to a MongoDB instance - and it handles the encoding and searching directly.

For the front-end, I decided to finally take [NextJS](https://nextjs.org/) for a spin. I love the productivity gains - but I'm a bit scared of the lock-in. Everything is seamless - but I wouldn't even know where to start if I wanted to stick this front-end into a docker container. A story for another time. 

TODO:

- how to seach with superduperdb
- fastapi and docker for the deployment
- Better closing hook



















