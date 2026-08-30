title: How I use Pi
description: My setup for the Pi coding agent, why I use it, and the tools I've built around it.
date: 30th August 2026
status: draft   

Today, I'd like to talk about Pi. Pi - is a minimal coding agent originally built by Mario Zechner. It's one of the key tools I use to get things done. Brainstorming, writing code, testing, debugging, navigating, research, you name it. The idea of Pi is simple: ship the minimum amount of tools and let the agent evolve with its user. 

I've used most agent harnesses out there. And regularly test what's out there. Claude code, Codex, OpenCode - you name it. None really stuck for me. Some are closed source (even though their code got leaked), others tend to change under my feet. Pi is simple, predictable, and doesn't do anything I'm not expecting. For something I drive everyday - reliability is important. 

Importantly - Pi is also model agnostic. It's not tied to a Frontier lab or model provider. Working for every model out there is increasingly challenging (link blog post from earandil), but Pi does a great job. I can use my Codex sub for some work, DeepSeek Flash V4 through the API for other work, and my local llama cpp models when I don't need *frontier intelligence*. 

My everyday workflow revolves largely around the terminal. My Mac as my main machine, a Hetzner server for Hermes and agents I want to run in the Cloud. Everything is connected to the same Tailscale network. Ghostty makes everything pretty seamless. Together with Tmux, Neovim, and LazyGit.

Tmux maps well to my mental model of work. Every project gets its own session, every task gets its own window. Nowadays - most of the time, I'll be running 2-3 agents in parallel on smaller things - while I put my focus on a single one.

Some weeks ago I mentioned (link retrospectiva) I stopped using Tmux in favour of Herdr. But I switched back. In Herdr, you get "pinged" when an agent is done. You are constantly looking at the status of all your agents. That makes me tired. I want to check on my agents - but at my own rythm. I don't want to be pinged. I like Do Not Disturb mode too much. The cognitive load as a bit too much - I needed another solution. 

I ended up building Pi-tools.

Pi-tools is a set of tools I use as part of my Pi workflow. The centerpiece (and probably the only *really* original tool) is `pi-jumper`. 

Pi-jumper is my own take on to the whole "multiple agents running, Herdr, Commander, your agent pings you when done, parallel work bullshit". It has two widgets: a sticky one below your input field that shows you how many other Pi sessions you have running (which you can turn off). The second allows you to quickly jump to other Pi sessions running on tmux.

But pi-tools has a couple of other goodies.

Pi-helicopter, is something I completely ripped off from phun333's pi-infobar app (add link). This one is Mac only. Pi-infobar was consuming 1GB of RAM on my Mac (https://github.com/phun333/pi-infobar/pull/10). Pi-helicopter is a bit more lightweight and performant - for now at least.

The rest of the pi-tool extensions are small things I've built that make my life a bit more pleasant. pi-no-sleep prevents my Mac from sleeping while Pi is running. pi-preview allows me to read longer clanker messages in a nice web page. Pi-subagents is a very minimal implementation of subagents for pi I stole from Armin, and pi-modus themes is a port of my favourite themes for pi. 

All of these extensions tend to evolve with my taste. I believe they all stick to pi's philosophy of being minimal instead of overwhelming. 

And that's the idea of pi no? Minimal, extensible, but still predictable.

Note: If you're interested in the rest of my setup (skills, extensions, etc), everything is in my dotfiles.  https://github.com/duarteocarmo/dotfiles

