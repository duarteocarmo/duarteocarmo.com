title: How I use Pi, the coding agent
description: How I use Pi with tmux, the coding workflow around it, and the small tools I built to fill the gaps.
date: 30th August 2026
status: draft   

Today, I'd like to talk about Pi. Pi - is the minimal coding agent that I use to get things done. Writting code, testing, navigating, research - a large chunk of my workflow nowadays revolves around Pi. Pi is actually made in Europe, and it's idea is simple: a minimal and extensible agent that grows and extends with you. (Oh - and it's Open Source, that's important). 

## Why I use it 

I've used most agent harnesses out there. Claude code, Codex, OpenCode, even some obscure Pi variations like Oh-my-pi. None really stuck for me. Some changed under my feet, some tended to hide a bit too much, and other were just plain slop/garbarge. Pi is simple, predictable - and doesn't change things when I'm not expecting. For something I drive everyday - knowing what to expect is important. 

Pi is also model agnostic. It's not tied to a Frontier lab, so it doesn't try to consume more tokens than it should. I tries to work well for all - and that's a challenge today. But that also means that I can start a conversation with GPT Sol, and switch to DeepSeek flash in the middle of the session, without too much hassle. I like that. I don't need frontier intelligence to run some tests. 

## My workflow 

My workflow still revolves largely around the terminal. I use my main Mac, and a remote machine with Hermes when I'm on the go. On my main machine I use Ghostty, tmux, Neovim, and LazyGit. 

My work maps well to Tmux. Every project gets its own tmux session, and tasks for a project will usually get different windows inside that session. At anytime, I might be running 2-3 agents in parallel working on different things - while I focus on a single main one with my bbrain. 

## Tmux, to herdr, and back to Tmux

Some weeks ago I mentioned I stopped using Tmux and now was using Herdr more and more. I stopped. There was too much going on. With the cognitive load of doing more things in parallel, I didn't need some constant noise about what was ready or not. I wanted to check on my other agents - but I wanted to do it CALMLY. 

And so, to solve the problem, I used Pi. And I ended up building Pi-tools. 

## Introducing pi-tools 

Pi-tools is a set of tools I use as part of my pi workflow. The centerpiece (and probably the only *really* original tool) is called `pi-jumper`. 

Pi-jumper is my solution to the whole multiple agents running, herdr, commander, your agent pings you when done, parallel work bullshit. It has two components: a sticky widget below your input prompt that shows you how many other pi sessions you have running on different tmux sessions - which you can turn off. And the other - more important - is a widget that allows you to quickly jump between other pi sessions running on other tmux sessions. 

Pi-helicopter, is something I completely ripped off from phun333's pi-infobar app. Mine is mac only, and is a bit more tailored to what I need. Pi-infobar was also using 1GB of RAM on my mac (https://github.com/phun333/pi-infobar/pull/10). Pi-helicopter is much more lightweight and performant - afaik. 

The rest of pi-tools are other small utilities I've built that make my life just a bit more pleasant with pi. pi-no-sleep keeps my MacOS display on while pi is running. pi-preview allows me to read longer messages in a nice browser view. Pi-subagents is a very minimal implementation of subagents for pi that I stole from multiple other extensions, and pi-modus themes is an adaptation of my favourite themes for pi. 

I've used LLMs to build these, and iterate on them, and so they evolve with my taste. If they have something in common - is that they stick to pi's philosophy of being minimal instead of overwhelming. 


And that's the idea of pi no? Minimal, predictable, and extensible. 



Note: If you're interested in the rest of my setup (skills, extensions, etc), everything is in my dotfiles.  https://github.com/duarteocarmo/dotfiles

