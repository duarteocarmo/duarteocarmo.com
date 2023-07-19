title: aicoverlettercreator.com
date: 07-19-2023 13:00
description: aicoverlettercreator.com is a Django app that allows you create personalized cover letters using AI.
status: published
slug: ai-cover-letter-creator-django-ai
thumbnail: images/54/aicoverlettercreator.png

<center>
<a href="https://aicoverlettercreator.com?ref=blog_post" target="_blank">
<img src="{static}/images/54/cover.png" alt="aicoverlettercreator.com" style="max-width:100%;border-radius: 2px">
</a>
</center>

_Get rid of all applications that don't have a cover letter_

I remember it like it was yesterday. As I was leaving one of the first companies I've ever worked for, my manager asked me to hire my replacement. Drowning in hundreds of applications for the position, I still recall his exact words.

I don't want to start a debate on if you should include a cover letter in your job application or not. I've heard good arguments on both sides. There's one thing I'd like to point out though: in the days of ChatGPT, it's hard to get a good excuse *not* to write one. 

Enter: <a href="https://aicoverlettercreator.com?ref=blog_post" target="_blank">aicoverlettercreator.com</a>

## Why I built it

The short answer: _Why not?_ 

The long answer, for a couple of reasons. 

I like mentoring/helping people that are just entering the industry (or just getting out of University) regarding their careers. Most people, when applying for positions, don't really pay close attention to the cover letter. I believe it can be a really big differentiator. Even though I hope they are aware of just how much ChatGPT can help them, I integrated in this version a little bit of _secret juice_. I think that secret juice will make those cover letters even better. And that's the first reason, to help people.

The second one is a bit more selfish. I've built a handful of LLM powered applications, but never anything completely end-to-end. They say the best way to learn about something is to build it yourself right? I certainly [think so](/blog/nftuga-nft-experimentation.html). So I wanted to build something where I made all the choices. Or something where I felt all the pain.

## The stack

I'm not the biggest fan of falling in-love with a stack. "What stack would you use?" Well, tell me about the problem first.

For this app, I went with [Django](https://www.djangoproject.com/) and [htmx](https://htmx.org/) ([again](/blog/infrequent.html)). Django is probably overkill for most _simple_ web applications, but when users, databases, and settings start becoming a thing, it includes almost all the batteries I need. As for htmx, it's not that I don't like React, it's that I love keeping things simple. That [_does not_](https://htmx.org/essays/when-to-use-hypermedia/#hypermedia-not-a-good-fit-if) mean it's always a great fit. But for this small project, it sure was.

One of the biggest hurdles when building this, was the implementation of streaming from OpenAI's API. There's nothing I hate more than clicking a button and having to wait 10 seconds for something to appear on screen. Turns out, integrating [server-sent events](https://developer.mozilla.org/en-US/docs/Web/API/Server-sent_events/Using_server-sent_events) with Django is not so straightforward. And even though Django supports [streaming responses](https://docs.djangoproject.com/en/4.2/ref/request-response/#streaminghttpresponse-objects). At the end of the day, you can't really escape some good old Javascript. And I'm ok with that.

Still sticking to my premise of keeping things as simple as possible. Every component I add to an app during development is a component I'll have to maintain during its lifetime. And I'm not the biggest fan of maintenance work. Because of this, [aicoverlettercreator.com](https://aicoverlettercreator.com) is both simple to use _and_ to operate. It's a simple Django app with no [queues](https://docs.celeryq.dev/en/stable/django/first-steps-with-django.html) and no self hosted PostgreSQL containers. It's a Dockerfile that connects to a [PlanetScale](https://planetscale.com/) database. That's it, every git commit automatically updates the app. 

Nothing like keeping things simple. 
