title: Changelog neural search
date: 10-06-2023 05:00
description: A vector database backed search and chat portal for podcasts on the Changelog network
status: published
slug: changelog-neural-search-superduperdb
thumbnail: images/56/changelog-cover.png

Search is one of the most important breakthroughs of the internet. Some are saying a list of blue links is not enough - and that AI _will_ overthrow search. I don't know if we're about to witness a revolution. But as with most things - there's only one way to know - to build and use it _myself_. 

I like podcasts a lot. There's really nothing like hearing people talk about things I know _nothing_ about. Some of my favorite podcasts are produced by the [Changelog](https://changelog.com/) network. More than once, I've had to use their [search engine](https://changelog.com/search?q=embedding) when researching something that was said during an episode.

One of the best things about the Changelog is that the [whole thing is open source](https://github.com/thechangelog). From the podcast engine itself, to the [transcripts of every episode](https://github.com/thechangelog/transcripts). Why not take all of these transcripts and build an AI-powered™ search engine around them?

<center>
<a href="https://changelog.duarteocarmo.com">
<img src="{static}/images/56/search.png" alt="Neural search for the changelog" style="max-width:100%;margin-bottom:-1em;">
</a>
<figcaption><a target="_blank" href="https://changelog.duarteocarmo.com">changelog.duarteocarmo.com</a></figcaption>
</center>

## How it's built
Before I describe the stack, let's get the obvious out of the way: the whole thing is open source. Both the [back-end](https://github.com/duarteocarmo/thechangelogbot-backend) and the [front-end](https://github.com/duarteocarmo/thechangelogbot-frontend). If you prefer to go and poke around the code yourself, be my guest.

I love the chunk-embed-search-retrieve dance as much as the next guy, but for this one, I wanted to keep things a bit simpler, so I'm letting [SuperDuperDB](https://www.superduperdb.com/) do most of the heavy lifting for me. With it, all I really need to do is add the embedding model to my serverless MongoDB instance, and it handles the rest for me:

```python
# add model to DB
model = SentenceTransformer(...)
db.add(
    VectorIndex(
        identifier=index_id,
        indexing_listener=Listener(
            model=model,
            key=key,
            select=collection.find(),
        ),
    )
)
# search the DB
cur = db.execute(
    collection.find({"$regex": {"podcast": "practicalai"}}).like(
        {"text": "What are embeddings"}, n=limit, vector_index=index_id
    )
)

```

For the front-end, I finally took [NextJS](https://nextjs.org/) for a spin. Love the productivity gains - especially when we're talking about developer experience. [Vercel](https://vercel.com/) is absolutely killing the developer experience side of things. On the other side, I have no clue how most of the magic is working - and I'm not sure that's a good thing.

