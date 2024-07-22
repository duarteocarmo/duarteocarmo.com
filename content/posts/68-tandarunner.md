title: Tanda Runner: A personalized running dashboard
date: 22-07-2024 17:55
description: A dashboard for visualizing your Strava running data and getting personalized recommendations for your next big race.
status: published
slug: tanda-runner
thumbnail: images/68/thumbnail.png

<center>
<a href="https://tandarunner.duarteocarmo.com">
<img src="{static}/images/68/app.png" alt="Tanda Runner Screenshot" 
style="max-width:100%;border-radius: 2px">
</a>
</center>

[Tanda Runner](https://tandarunner.duarteocarmo.com/) is a web app that shows me the things I care most about when preparing my next marathon. I've also added a running coach/agent designed to give me actionable feedback about my training. Some of that feedback is _probably_ hallucinatory - I'll get to it in a bit.

It's built with [Django](https://www.djangoproject.com/) - a framework I've gravitated to more and more when building these types of apps. It has all the batteries I need and a time-tested [ecosystem](https://djangopackages.org/grids/g/for-comparison/). The front-end is a Frankenstein that uses Django [channels](https://channels.readthedocs.io/en/latest/), [htmx](https://htmx.org/), and some vanilla JavaScript. It’s not the most responsive PWA out there - but it's still a pretty usable experience. The chat interface is adapted from [LLaMA.cpp](https://github.com/ggerganov/llama.cpp/blob/master/examples/server/README.md).

The most interesting part is the small LLM coach/agent that gives feedback and tips regarding my performance. It's an _untested_ and _non-evaluated_ multi step LLM pipeline that extracts running-related insights from around the web, and uses them to give me personalized feedback using my [Strava](https://www.strava.com) data.

To do this, I extract transcripts from marathon related YouTube videos (which I probably [shouldn't](https://www.youtube.com/watch?v=xiJMjTnlxg4)), and use those to generate a list of insights related to running and training. Once I have those insights, I use an LLM to translate those them into Pandas code. Once that's done I can feed an LLM the insight, the code, and the outcome of running such code on my own data. Sounds confusing? I know it does - but it works surprisingly well! 

This pipeline could probably be significantly improved by designing some evaluations, some metrics, and continuously improving it. But for now, I'll use it to prepare [Nice](https://www.marathon06.com/2024/AN/), and make any adjustments I see fit. 

The visualizations and graphs are built using [Altair](https://altair-viz.github.io/). They are a mix of my favorite graphs from [Christoph’s CR Plots](https://crplot.com/), Strava, and my own brain. The name (and most of the visualizations) come from [Giovanni Tanda](https://scholar.google.co.uk/citations?view_op=view_citation&hl=en&user=C__krSUAAAAJ&cstart=20&pagesize=80&citation_for_view=C__krSUAAAAJ:j3f4tGmQtD8C)'s work - which I encourage you to read through!

