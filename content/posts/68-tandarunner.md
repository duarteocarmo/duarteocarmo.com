title: Tanda Runner
date: 22-07-2024 17:00
description: Tanda Runner is a running dashboard and coach for your Strava data. 
status: draft
slug: tanda-runner
thumbnail: images/68/thumbnail.png

<center>
<a href="https://tandarunner.duarteocarmo.com">
<img src="{static}/images/68/app.png" alt="Tanda Runner Screenshot" 
style="max-width:100%;border-radius: 2px">
</a>
</center>

[Tanda Runner](https://tandarunner.duarteocarmo.com/) is an app that shows me the graphs I care most about when preparing my next marathon. It also features a small running coach/agent, designed to give me actionable feedback regarding my training. Some of that feedback is _probably_ hallucinatory - but we'll get to that part. 

It's built with Django - a framework I've gravitated to more and more when building these types of apps. It has all the batteries I need and a time-tested ecosystem. The front-end is a Frankenstein that uses Django channels, htmx, and some vanilla JavaScript. It’s not the most responsive PWA out there - but it's still a pretty usable experience.

The most interesting part is the small LLM coach that gives feedback and tips regarding my performance. It's an untested and unevaluated multi step LLM pipeline that extracts running-related insights from around the web, and analyses them given my Strava data.

To do this, I extract transcripts from marathon related Youtube videos (which I probably [shouldn't](https://www.youtube.com/watch?v=xiJMjTnlxg4)), and use those to generate a list of insights related to running and training. Once I have those insights, I use an LLM to translate those insights into Pandas code. With this in place, I can then feed an LLM the insight, the code, and the outcome of running such code on my own data. Sounds confusing? I know it does - but it works surprisingly well! This pipeline could probably be significantly improved by designing some evaluations and metrics. For now, I'll use it to prepare [Nice](https://www.marathon06.com/2024/AN/), and see where that gets me. 

The visualizations and graphs are built using [Altair](https://altair-viz.github.io/). They are a mix of my favorite graphs from [Christoph’s CR Plots](https://crplot.com/), Strava, and my own brain. The name (and most of the visualizations) come from [Giovanni Tanda](https://scholar.google.co.uk/citations?view_op=view_citation&hl=en&user=C__krSUAAAAJ&cstart=20&pagesize=80&citation_for_view=C__krSUAAAAJ:j3f4tGmQtD8C)'s work - which I encourage you to read through!

