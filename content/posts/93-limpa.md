title: Limpa: Ad-Free podcasts powered by LLMs
description: Limpa is a small web application that removes ads from podcast feeds. Powered by NVIDIA's Parakeet and LLMs.
date: 5th of January 2026
status: published
audio: true


I get up feeling sleepy. I lace up my running shoes and head out the door. I fire up my favourite podcast. "This show is brought to you by..." I *hate* ads.

I understand the attention economy. Companies are capitalizing more and more on everyone's time. I have nothing against it. But I'm also a big fan of protecting my time. A [Pi-hole](https://pi-hole.net/) under my desk, [uBlock Origin](https://ublockorigin.com/), [SponsorBlock](https://sponsor.ajay.app/), I run them all. My time is mine, unless I tell you otherwise. 

And I spend a lot of time listening to Podcasts. And what are podcasts at the end of the day? Just mp3 files. Once you download them from the server, they're yours. 

So I built [Limpa](https://github.com/duarteocarmo/limpa)[ref]It means "clean" in Portuguese[/ref]

<a href="https://github.com/duarteocarmo/limpa" target="_blank">
<center>
<img src="{static}/images/93/limpa_screenshot.png" alt="Limpa screenshot"  style="max-width: 100%; border-radius: 2px">
</center>
</a>


Limpa is a simple yet powerful web app. You paste in the [RSS feed](https://rss.com/tools/find-my-feed/) of your favourite podcast, and it will give you back an ad-free feed that you can plug into your favourite Podcast app. 

It's a simple [Django](https://www.djangoproject.com/) app with [htmx](https://htmx.org/) on the front-end. A stack I love since it has few moving pieces. Every time a podcast gets added, I transcribe the latest episode using [NVIDIA's Parakeet v3](https://huggingface.co/nvidia/parakeet-tdt-0.6b-v3) running on [Modal](https://modal.com/). Once I extract the [transcript with timestamps](https://github.com/duarteocarmo/limpa/blob/master/limpa/services/modal_transcription.py#L72), I can [prompt an LLM](https://github.com/duarteocarmo/limpa/blob/master/limpa/services/extract.py#L48) to get the exact timestamps of the ads that should be cut out. I then pass those to [ffmpeg](https://www.ffmpeg.org/) and voilà: ad-free podcasts.

Django's new [Tasks framework](https://docs.djangoproject.com/en/6.0/topics/tasks/) has also been a joy to use. No more [Celery](https://docs.celeryq.dev/en/v5.5.3/django/first-steps-with-django.html), no more [Flower](https://flower.readthedocs.io/en/latest/), just a simple database to run background tasks. The fewer moving pieces, the fewer mistakes [my agents](https://opencode.ai/) are prone to making.

If you're wondering - no - I'm not planning on hosting this service to others. I'm not interested in discussing the nuances and implications of providing this as a service to others.[ref]That might be illegal, and you probably shouldn't do it[/ref]. The project's simple and [well documented](https://github.com/duarteocarmo/limpa), and so it should be easy for you to run it for yourself. 

Feel free to fork, and build on top of it!