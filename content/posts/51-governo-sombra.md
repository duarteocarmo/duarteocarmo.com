title: Governo Sombra transcripts
date: 19-04-2023 16:30
description: A website will all the transcripts for one of my favorite podcasts
status: published
slug: governo-sombra-transcripts
thumbnail: images/51/website.png

<center>
<a href="https://governosombra.duarteocarmo.com" target="_blank">
<img src="{static}/images/51/website.png" alt="governosombra.duarteocarmo.com" style="max-width:100%;border-radius: 2px">
</a>
</center>

7 years. That's how long I've lived in Denmark for. I love it, but Portugal is still close to my heart. As an emigrant, it's always hard to stay connected to what's going on in Portugal. What are people talking about? What's in the news? What worries people? What is everyone arguing about over morning coffee? 

One of the ways I like to stay in touch is by listening to _Governo Sombra_ (now cleverly called  _Program whose name we are legally prevented from saying_, after changing networks). It's a weekly show where the 3 guests (+1 host) comment on Portuguese and World news. Besides being funny, I also love the fact that the 3 guests represent different parts of the political spectrum, so I can get a good idea about how most of the people are feeling. 

Inspired by [Lexicap](https://karpathy.ai/lexicap/), I decided to build a [website](https://governosombra.duarteocarmo.com) with the transcripts for all of the episodes of the show. More than once I've listened to a particular part of an episode and wanted to share it with a friend. Now, [I can do it](https://governosombra.duarteocarmo.com/episodes/171#170). 

For the transcription, I used OpenAI's Open Source [Whisper](https://github.com/openai/whisper) model. With a  _small_ caveat: the whole thing (serving + transcribing) needed to run in my 20 EUR/month [VM](/blog/down-from-the-cloud-self-hosting.html). So it needed to be small _and_ efficient. 

I like Python, but Rust was the obvious choice. For the transcription part, I used [whisper.rs](https://github.com/tazz4843/whisper-rs) (Rust bindings for [whisper.cpp](https://github.com/ggerganov/whisper.cpp/)). For serving the app, I went with [Actix Web](https://actix.rs/) - it's small, efficient, and reminds me a lot of Flask. Incredible how a small Linux box can handle transcribing 60min+ episodes without hiccuping much. 

The quality of the transcription is something like a 6/10. I did use the [base](https://github.com/openai/whisper#available-models-and-languages) model so there is _clearly_ space for improvement. Maybe when I get a dedicated box. 

The entire thing is up on [GitHub](https://github.com/duarteocarmo/governosombra). 

