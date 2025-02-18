title: Simple AI tools
date: 18th Feb 2025
description: An opinionated guide on my favorite LLM-based tools. Turns out you don't need all the tools - just a couple of good ones.
status: published
thumbnail: images/76/cover.png

Last week over lunch, [Pedro](https://www.parraguezr.net/) was telling me how he uses [Perplexity](https://www.perplexity.ai/) to improve the way he searches around the web. He mentioned we're entering a phase where we have at least 20 'AI' tools to boost our productivity - and the tough thing now is choosing which ones to use.

With so much buzz around AI - it's easy to feel overwhelmed and think "I don't use that, maybe I should?". Now - I don't know which tools are the best for your particular use case. But for the past 6-10 months, I've settled on a nice group of tools I think more people would benefit from.

## For everything else

I recently upgraded my MacBook to an M3 Max with 64GB of RAM. One of the main reasons I got it was so that I could run a nice suite of Large Language Models (LLMs) locally. [Ollama](https://ollama.com/) has been at the center of that workflow - ([don't forget](https://www.reddit.com/r/ollama/comments/1idqxto/comment/ma19shz/?utm_source=share&utm_medium=web3x&utm_name=web3xcss&utm_term=1&utm_content=share_button)). Whenever a new [model](https://ollama.com/library/deepseek-r1) comes out, it's just an `ollama pull` away - and you're up and running.

Models are great - but just like ChatGPT showed everyone, the interface really makes the difference. Since I'm a Mac user, I wanted a unified way to interact with all the models I'm interested in - in a nice interface. [BoltAI](https://boltai.com?aff=2OOJDR) does just that.

There are a lot of things I like about BoltAI. But my favorite one is that I can use a single interface for just about any model under the sun (and running on my laptop). I've also setup [OpenRouter](https://openrouter.ai/), so I can try out any tropical model/provider combo with just a few clicks. It's a one time purchase - and [Daniel](https://danielnguyen.me/) is [super responsive](https://boltai.canny.io/).

![BoltAI LLM application]({static}/images/76/boltai.png)

There are two things that are currently missing from my workflow for everyday tools and I haven't solved yet. The first is some sort of canvas interface, [artifacts](https://support.anthropic.com/en/articles/9487310-what-are-artifacts-and-how-do-i-use-them) are my favorite for this. The second thing I'm missing is some sort of LLM + web search integration. I've been experimenting with [Perplexity](https://www.perplexity.ai/), [Phind](https://www.phind.com/), and some [plugins](https://docs.boltai.com/docs/chat-ui/ai-plugins) for BoltAI - but I'm still skeptical of LLM's interpretation of search results.

Great, what about engineering?

## For code

My first purchase of any AI service at all was (and still is) GitHub's [copilot](https://github.com/features/copilot). I've tried everything under the sun - [Codeium](https://codeium.com/), [SuperMaven](https://codeium.com/), but none comes quite close to GitHub. I consider it a commodity now, just like my LSP's completion.

I'm still, largely a [NeoVim](https://github.com/duarteocarmo/dotfiles/tree/master/.config/nvim) user. And the one of the most useful LLM tools/plugins I've used with it is [Gp.nvim](https://github.com/Robitx/gp.nvim).

It's an amazing plugin. It allows me to generate new code, re-write portions of the code base, or even create a floating chat window to chat with a particular part of the codebase I want to understand better. Oh, and it also support Ollama models - so that the magic doesn't stop - even when I'm on an airplane.

![Gif of GpNvim in action]({static}/images/76/gpnvim.gif)

Even if I like NeoVim, I'll admit that for certain projects - it doesn't quite cut it. For larger codebases, using notebooks, or when I _feel like it_, [Cursor](https://www.cursor.com/) has also been a booster. Particularly when you're creating something new, rather tweaking something that exists already. A small static page - some css styling on a template - it can handle most of that.

A tool I've been exploring more lately is [Aider](https://aider.chat/). Think of it as Cursor, but terminal based - with a git integration. Aider gives me a bit more control over the changes I want it to make. It allows me to only select certain files where it operates, it can also run commands - and examine their output. It's a super nice tool - especially if you prefer a terminal + git workflow. As an added bonus, Aider also supports [local](https://aider.chat/docs/llms/ollama.html) models. To be completely honest - I think I've barely even [scratched](https://aider.chat/docs/usage/commands.html) what's possible with Aider.

![Aider LLM tool in action]({static}/images/76/aider.gif)

## Final thoughts

**On tools.** I agree with Pedro - there's no shortage of tools out there. Everyone will tell you to use X, use Y, or charge you 20 USD for it. Like most things, tools are only as good as you're productive with them - and very person specific. The best tool for me is probably not the best tool for you.

**Exploration is key.** I believe one of the most important things is to keep exploring what's out there. Don't dismiss something just because it's new. A great new [model](https://www.deepseek.com/)? Take it for a spin.. A transformative [IDE](https://www.all-hands.dev/)? Give it a shot and see what it's capable of. You might just find something you like - and _a lot_ of things you don't.

**Local first.** If there's something we learned in the last few months, is that we probably don't need so much compute like we thought we did. Local models are getting really good, really fast. You might have noticed that almost all tools shared here also support local models that I'm running on my own machine? Are they as good as the big ones? No. Well, at least _not yet_.

Keep exploring.
