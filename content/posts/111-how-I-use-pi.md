title: How I use Pi
description: My setup for the Pi coding agent, why I use it, and the tools I've built around it.
date: 30th August 2026
status: published

Today, I'd like to talk about [Pi](https://pi.dev/). Pi is a minimal coding agent originally built by [Mario Zechner](https://mariozechner.at/). It's one of the key tools I use to get things done. Brainstorming, writing code, testing, debugging, navigating, research, you name it. The idea of Pi is simple: ship the minimum amount of tools and let the agent evolve with its user.

I've used most agent harnesses out there and regularly test what's out there. [Claude Code](https://www.anthropic.com/claude-code), [Codex](https://openai.com/codex/), [OpenCode](https://opencode.ai/), you name it. None really stuck for me. Some are closed source (even [though their code got leaked](https://www.infoq.com/news/2026/04/claude-code-source-leak/)); others tend to change under my feet. Pi is simple, predictable, and doesn't do anything I'm not expecting. For something I drive every day, reliability is important.

Importantly, Pi is also model agnostic. It's not tied to a Frontier lab or model provider. [Working for every model out there is increasingly challenging](https://earendil.com/posts/session-portability/), but Pi does a great job. I can use my Codex sub for some work, DeepSeek Flash V4 through the API for other work, and my local [llama.cpp](https://github.com/huggingface/pi-llama) models when I don't need *frontier intelligence*.

My everyday workflow revolves largely around the terminal. My Mac is my main machine, with a [Hetzner server]({filename}/posts/66-how-I-host-my-projects.md) for [Hermes]({filename}/posts/106-how-I-hermes.md) and agents I want to run in the Cloud. Everything is connected to the same [Tailscale](https://tailscale.com/) network. [Ghostty](https://ghostty.org/) makes everything pretty seamless, together with [Tmux](https://github.com/tmux/tmux/wiki), [Neovim](https://neovim.io/), and [LazyGit](https://github.com/jesseduffield/lazygit).

Tmux maps well to my mental model of work. Every project gets its own session, every task gets its own window. Nowadays, most of the time, I'll be running 2-3 agents in parallel on smaller things while I put my focus on a single one.

Some weeks ago I [mentioned I stopped using Tmux in favour of Herdr]({filename}/posts/109-retrospectiva-#10.md). But I switched back. In [Herdr](https://herdr.dev/), you get "pinged" when an agent is done. You are constantly looking at the status of all your agents. That makes me tired. I want to check on my agents, but at my own rhythm. I don't want to be pinged. I like Do Not Disturb mode too much. The cognitive load was a bit too much. I needed another solution.

I ended up building [pi-tools](https://github.com/duarteocarmo/pi-tools/).

pi-tools is a set of tools I use as part of my Pi workflow. The centerpiece (and probably the only *really* original tool) is [`Pi-jumper`](https://github.com/duarteocarmo/pi-tools/tree/master/packages/pi-jumper).

Pi-jumper is my own take on the whole "multiple agents running, Herdr, Commander, your agent pings you when done, parallel work bullshit". It has two widgets: a sticky one below your input field that shows you how many other Pi sessions you have running (which you can turn off). The second allows you to quickly jump to other Pi sessions running on Tmux.

But pi-tools has a couple of other goodies.

[Pi-helicopter](https://github.com/duarteocarmo/pi-tools/tree/master/packages/pi-helicopter) is something I completely ripped off from [phun333's Pi-infobar app](https://github.com/phun333/pi-infobar). This one is Mac only. Pi-infobar was [consuming 1GB of RAM on my Mac](https://github.com/phun333/pi-infobar/pull/10). Pi-helicopter is a bit more lightweight and performant, for now at least.

The rest of the pi-tools extensions are small things I've built that make my life a bit more pleasant. [Pi-no-sleep](https://github.com/duarteocarmo/pi-tools/tree/master/packages/pi-no-sleep) prevents my Mac from sleeping while Pi is running. [Pi-preview](https://github.com/duarteocarmo/pi-tools/tree/master/packages/pi-preview) allows me to read longer clanker messages in a nice web page. [Pi-subagents](https://github.com/duarteocarmo/pi-tools/tree/master/packages/pi-subagents) is a very minimal implementation of subagents for Pi I stole from [Armin](https://github.com/mitsuhiko/agent-stuff/blob/main/extensions/subagent.ts), and [Pi-modus themes](https://github.com/duarteocarmo/pi-tools/tree/master/packages/pi-modus-themes) is a port of my favourite themes for Pi.

All of these extensions tend to evolve with my taste. I believe they all stick to Pi's philosophy of being minimal instead of overwhelming.

And that's the idea of Pi, no? Minimal, extensible, but still predictable.

Note: If you're interested in the rest of my setup (skills, extensions, etc), everything is in [my dotfiles](https://github.com/duarteocarmo/dotfiles).

