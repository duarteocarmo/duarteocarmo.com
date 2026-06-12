title: How I Hermes
description: 
date: 
status: draft
audio: true
thumbnail: 

January this year, OpenClaw went viral. You probably heard about it. My guess it that some of you that read this blog even used it, or at least experimented with it. I certainly did. 

I remember it like yesterday. I installed it, and very quickly realised I was debugging my own AI-agent on why certain reminders/cron jobs didn't fire like they were supposed to. I got frustrated, and deleted it from pretty much everywhere. What is this bug-filled vibe-coded excuse for a product? 

A couple of months later I decided to download Hermes Agent. And I have to admit, that I have been using it pretty much every day since then. I'm hooked. Let's talk about it. 

## What the Hermes Agent is, and isn't

Nous Research is a popular research lab that first got popularized by building uncensored models. After the boom of OpenAI, they decided to launch their own take on it. At its core, it's very similar to OpenAI. It's an always-on agent that runs in a computer and that can act as your own personal assistant/agent. It's a bit like a ChatGPT that lives in your computer, can read/edit files, can browse the web, can write code, etc. You can talk to it via the terminal, via a web interface, via messaging apps (Telegram, WhatsApp), or even a recently released desktop app. 

The Hermes Agent is a mix of a coding agent and an automation machine that lives in a computer of its own. You configure the agent by creating (or installing skills). I'll talk about some use cases below. 

Let's get it out of the way. Hermes is not plug-and-play. Do not expect to just install it and be amazed instantly. You need to spend a considerable amount of time making it your own. It's a bit like tweaking an editor like VIM or installing apps on your phone. It takes time to make it your own.


## My agent setup: Saramago

You probably know about the meme of programmers leaving their laptops open with agents running inside. It's a fun meme. But I don't like to keep my computer open in random places. I'm also not particularly fond of having an agent freely running inside my main machine. 

Fortunately, for the past 5 years, I've been running most of my web applications and deployments on a refurbished Hetzner server. For a fixed and predictable monthly price, I have my own little Debian machine that runs in the Cloud and is available 24/7. Thiis is exactly where Saramago (Yes, I gave him a name) runs. 

All of these harnesses have the notion of messaging gateway. A process that is always on that you can use to talk to the agent in your machine. To keep things simple and reliable - I talk to Saramago via Telegram. 

Right now, Saramago runs primarly on three models. Deepseek V4 (flash or pro depending on task complexity) - through the official DeepSeek API which is dirt cheap - and pretty reliable. For the most important things - I also run GPT 5.5 via my Codex subscription. I'm not particulary tied to any - and tend to experiment every now and then with new models. I would love to tell you the sstory of how I use a fully local and private open source model. Unfortuntely - we're not there yet. 

My setup keeps changing, but I can already say it's very useful for my day-to-day work & life. 

### Use case 1: Coding on the go

The first use case is the most obvious one. Having Hermes is a bit like having a [insert your favourite coding agent here] but available 24/7. I don't use when I need to do especially *deep* work. But I use it for small annoyances while I am on the go. To interact with most projects, it has access to the GitHub cli and a Github CLI skill. I've also directed it to clone any new repos under a specific folder. So whenever I want to fix a broken pipeline, a typo on this blog, a small fix - it just creates a PR and sends me a likn for review. 

### Use case 2: Reminders

I've used TickTick for at least 5 years. It's my go-to todo's app. It runs my life. But there is a certain type of reminder that TickTick is just not able to do. That's because the reminder depends on a condition. Other types of reminders would just be too hard to program into TickTick. 

Some examples: 

- "Remind me to pack up my rain jacket if it rains outside tomorrow"
- "Remind me which type of trash to bring outside to pick up tomorrow" - This is complicated, especially in Italy. 

Another interesting thing is that Hermes knows when to stay silent. If it doesn't rain tomorrow it just won't text me, instead of texting me - "Hey - no rain tomorrow". Which is just annoying. 

### Use case 3: Monitor long running jobs

More often that not, I run long running jobs on remote computers. Either it's a large GPU training run. Can be a long running data parsing or enrichment job. Can be anything really. It can also be a particularly annoying CI pipeline. I use to have to click a browser, ssh into a server, leave tmux open, etc. Now - Saramago can do it for me. "SSH into the machine X and give me an update on the running job every 15 mins - turn off the machine when done". By giving access to CLIs/SDKs this can be made even more powerful. 


### Use case 4: Manage my calendar 

I'm not particularly proud of it. But most of my emails run on GMail. And Saramago has access to the Google Workspace CLI. That means it can read my email, check my calendar - and iteract with both of these. This unlocks yet another space for convenient automations. "Check email for the last train trip and add it to my calendar". "Everytime a new email comes in - if it mentions a work location - add an all-day event to my calendar". Most of the useful (and not dangerous) things here come from the agent connecting (better than Google does) your email to your calendar. 


### Use case 5: Choosing flights 

"An agent that books flights for you" is the dream that has been sold to us for many years now. And that stops when you have an agent taking pictures and trying to click around the google flights interface. Not anymore. Saramago has access to the google flights CLI. And that means I can search flights in my own terms. And it can adapt to my peculiar travelling choices. And plot them just the way I like. I'll do the booking and decision making. But it will help me much more than a Momondo interface. 


### Use case 6: Writing and brainstorming

With a kid now. I have less and less time in front of the actual computer. Thankfully, we have agents now. That means that I can do a lot of the prep-work on-the-go, and once I sit down - I can do the stuff that matters. Creating the structure for my blog post, adding the images and figcaptions, the boilerplate, etc. The agent can do that. And I can focus solely on the writing. Once I get down to write, the headers are already there, the markdown file is already there. I just need to sit and write. Massive productivity booster. I can write to Saramago, or I can also speak, and Telegram will transcribe automatically. 


### Use case 7: Fitness coaching

I like running. I have a Garmin, and an Oura ring. I've tried to make Saramago act as my running coach. Giving me feedback after a run. Preparing my next run. Managing my running volume. Adapting my training plan to my tiredness levels. You know where I'm getting at. I think there's something interesting here - in connecting all the different sources of data and acting like my personal training coach. The best success I've had was using a custom skill + the strava-cli. But I'm still not satisfied. I think there's a very good use case here. I'm just not sure which yet. 


## The big boys are noticing 

I don't know about the future of work and all. But after a lot of grooming and tweaking - I can confidently say that Saramago is very useful in my day-to-day life. Work or not. It's by no means and out of the box experience. You need to make it yourself. 

And the big boys are noticing. Wehter is ChatGPT pulse, or Gemini Spark, or even OpenClaw - they now there is a use case here. There certainly is. But I would also argue that you need some level of technical sviness and will to hack on your own agent - I'm not sure everyone wants to spend the time. The most similar parallel in my head is when I used to spend hours tweaking my VIM config, but now I tweak my Hermes Agent instead. 

So this is how I use Hermes - I hope that was useful. 







Links to add: 
https://nousresearch.com/
https://hermes-agent.nousresearch.com/
https://hermes-agent.nousresearch.com/desktop
https://hermes-agent.nousresearch.com/docs/skills/


Tutorial  https://www.youtube.com/watch?v=1ve4Atbqmoo
https://www.businessinsider.com/coders-keep-laptops-open-in-public-ai-agent-2026-5
https://hermes-agent.nousresearch.com/docs/user-guide/messaging/
https://api-docs.deepseek.com/quick_start/pricing
github cli link
Ticktick link
https://www.atarifiuti.an.it/comuni.php?idcomune=36&pag=calendario
https://vast.ai/developers/cli
https://github.com/googleworkspace/cli
https://github.com/punitarani/fli
telegram transcribe autoamtically - do we have a link to this? 
https://github.com/duarteocarmo/skills/tree/main/skills
https://gemini.google/overview/agent/spark/ (big boys noticing)
