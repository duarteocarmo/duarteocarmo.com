title: An opinionated running dashboard
description: Some updates to my small and opinionated running dashboard: Tanda Runner
date: 25th of March 2026
status: published
thumbnail: images/99/cover.webp

<center>
<a href="https://tandarunner.duarteocarmo.com/">
<img src="{static}/images/99/calendar.webp" alt="Tanda Runner calendar view" style="max-width:100%;border-radius: 2px">
</a>
</center>

As you get older, life becomes complicated. Not in a bad way. There’s just more going on. We don’t all want to run marathons. Maybe you want to run a [parkrun](https://www.parkrun.com/). Maybe you want to gradually increase your volume. Maybe you don't want to run at all. Whatever your running goal is, you *should* be able to plan for it.

In the new version of [Tanda Runner](https://tandarunner.duarteocarmo.com/) you can plan for *whatever* your running goal is. I redesigned all the parts I wasn't a fan of. The result is a redesigned chat interface with an agent that knows about all your runs, and, my favourite: a fully automated - but personalized - running plan generator.

<center>
<a href="https://tandarunner.duarteocarmo.com/">
<img src="{static}/images/99/chat_interface.webp" alt="Tanda Runner chat interface" style="max-width:100%;border-radius: 2px">
</a>
</center>

The plan generator analyzes your past activity, understands your running habits, and builds a completely customized running plan just for you. You can take this and export it to your calendar app of choice.

The technology choices evolved a bit, but not too much. I’m still on my beloved [Django](https://www.djangoproject.com/) + [htmx](https://htmx.org/) stack. The LLM models are served through [OpenRouter](https://openrouter.ai/), and tracing is sent automatically to [W&B Weave](https://openrouter.ai/docs/guides/features/broadcast/weave). The agent itself is built with [PydanticAI](https://ai.pydantic.dev/), a framework I’ve enjoyed using more and more. 

There aren’t enough niche running tools out there. This one is mine.

See you out there, runner.
