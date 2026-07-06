title: Retrospectiva #9
description: A monthly newsletter about life.
date: 6th of July 2026
status: published
audio: true
thumbnail: images/107/cover.webp


This month's Retrospectiva comes a little later than usual. The whole house got sick battling the flu the past couple weeks. Mixed with a small heatwave here in Copenhagen, means summer hasn't blessed us like we expected. At least not yet.

Now that I'm feeling a bit better, I finally managed to get some writing in. Let's get to it.

## Using

**<a href="https://huggingface.co/zai-org/GLM-5.2" target="_blank">GLM-5.2</a>**: Finally. An open-weights model that competes with the big frontier models. For the past weeks I've been using GLM-5.2 extensively. Through [OpenCode Go](https://opencode.ai/go) it starts at 5 USD/month. It's different than using your GPT 5.5 or Fable, but it feels good in the open-source way. I urge you to take it for a spin. It costs about one-fourth of what Fable costs. And it deals with 99% of issues Fable does.

<center>
<a href="{static}/images/107/glm-52.webp" target="_blank">
<img src="{static}/images/107/glm-52.webp" alt="Artificial Analysis chart showing GLM-5.2 cost per intelligence index task" style="max-width:100%;border-radius: 2px">
</a>
<figcaption>
GLM-5.2 catching up - <a href="https://artificialanalysis.ai/" target="_blank">Artificial Analysis</a>
</figcaption>
</center>

**<a href="https://github.com/phun333/pi-infobar" target="_blank">Pi Stats</a>**: You probably know by now that I'm a big fan of the [Pi](https://pi.dev/) harness. If you like Claude Code better, that's fine - enjoy yourself. One issue with Pi is that it's hard to know exactly how much you're spending. I discovered this little application called [Pi Stats](https://github.com/phun333/pi-infobar), which gives me a widget in my menu bar that shows me exactly how much I've spent and on what. Even though I still pay for a fixed plan every month, it's still important to know (in terms of real value) what's going where.

<figure style="margin: 0;">
<div style="display:flex;gap:1rem;justify-content:center;align-items:flex-start;flex-wrap:wrap;">
<a href="{static}/images/107/pistats-overview.webp" target="_blank" style="flex:1 1 260px;max-width:45%;text-decoration:none;">
<img src="{static}/images/107/pistats-overview.webp" alt="Pi Stats overview screen" style="width:100%;max-width:100%;border-radius: 2px">
</a>
<a href="{static}/images/107/pistats-languages.webp" target="_blank" style="flex:1 1 260px;max-width:45%;text-decoration:none;">
<img src="{static}/images/107/pistats-languages.webp" alt="Pi Stats languages screen" style="width:100%;max-width:100%;border-radius: 2px">
</a>
</div>
<figcaption>
Pi Stats in action (not my usage)
</figcaption>
</figure>

**<a href="https://github.com/jesseduffield/lazygit" target="_blank">Lazygit</a>**: We write less code, but we are accountable for more. Some of it is not worth looking at — but the important bits are. For the past few months I've experimented with a lot of "code diff viewers". I need somewhere I can review the changes the agent has made, and direct it in case anything goes wrong or weird. I've tried [Hunk](https://github.com/modem-dev/hunk) (and even contributed a couple of PRs: [#310](https://github.com/modem-dev/hunk/pull/310), [#347](https://github.com/modem-dev/hunk/pull/347)), and [codediff.nvim](https://github.com/esmuellert/codediff.nvim) in Neovim, which is what my `<space>d+d` mapping calls. But lazygit paired with [difftastic](https://github.com/Wilfred/difftastic) has been hard to beat. Fast to iterate and great diff highlighting.

**<a href="https://www.sofascore.com/" target="_blank">Sofascore</a>**: I like watching sports. Not all sports, not all the time. But when I do (surprise), I like looking at the data. Sofascore is the app that gives me all of this - in a way I love. Who plays where? Who used to play where? When you're not 15 and playing FIFA extensively - it's hard to keep up. This team out of Croatia has built an incredible app!


## Reading

**<a href="https://www.oreilly.com/library/view/deep-learning-for/9781098168025/" target="_blank">Deep Learning for Biology</a>**: I finished this one over 2-3 weeks. I recommend it. A great read in an area where there's much left to do!

**<a href="https://medarc-ai.github.io/mindeye/" target="_blank">Reconstructing the Mind's Eye</a>**: Some wild research out of Princeton that shows how they reconstruct images from brain activity. Yes. You heard that right. 

**<a href="https://lilianweng.github.io/posts/2026-06-24-scaling-laws/" target="_blank">Scaling Laws, Carefully - Lilian Weng</a>**: What is the ideal amount of data given a certain model size? Given a certain compute budget? And vice versa? These are just some of the questions researchers have been asking themselves. Lilian writes about them beautifully.

<center>
<a href="{static}/images/107/chinchilla-2.webp" target="_blank">
<img src="{static}/images/107/chinchilla-2.webp" alt="Chinchilla scaling laws comparison" style="max-width:100%;border-radius: 2px">
</a>
<figcaption>
Image source: <a href="https://arxiv.org/abs/2203.15556" target="_blank">Hoffmann et al. 2022</a>, as shown in Lilian Weng's <a href="https://lilianweng.github.io/posts/2026-06-24-scaling-laws/" target="_blank">Scaling Laws, Carefully</a>.
</figcaption>
</center>

**<a href="https://injuly.in/blog/napkin-inference-cost/index.html" target="_blank">Inference cost at scale with napkin math</a>**: A fast and short reference on how to think about serving models on GPUs. If you wanted to serve GLM-5.2 to multiple users, what would that cost?

**<a href="https://lonriesberg.com/posts/investing-with-agents/" target="_blank">Investing with Agents - Lon Riesberg</a>**: A very fun read from Lon Riesberg (creator of the awesome [Data Elixir newsletter](https://dataelixir.com/)) about using LLMs to make investments in the stock market. 


## Listening

Not the most inspiring month musically. Being sick means less running, which means less listening.

**<a href="https://www.mlst.ai/" target="_blank">Machine Learning Street Talk</a>**: One of my favourite podcasts about Machine Learning/Deep Learning/AI. You should give it a listen.

<iframe data-testid="embed-iframe" style="border-radius:12px" src="https://open.spotify.com/embed/show/02e6PZeIOdpmBGT9THuzwR?utm_source=generator&theme=0" width="100%" height="152" frameBorder="0" allowfullscreen="" allow="autoplay; clipboard-write; encrypted-media; fullscreen; picture-in-picture" loading="lazy"></iframe>

**<a href="https://soundcloud.com/worldwide-fm/skate-muzik-listen-to-sade-14" target="_blank">Skate Muzik: Listen to SADE - Worldwide FM</a>**: I mean - Sade. Do I need to expand?

<iframe width="100%" height="166" scrolling="no" frameborder="no" allow="autoplay; encrypted-media" src="https://w.soundcloud.com/player/?visual=false&url=https%3A%2F%2Fapi.soundcloud.com%2Ftracks%2F2323007471&show_artwork=true"></iframe>

## Watching

**<a href="https://www.sofascore.com/football/tournament/world/world-championship/16#id:58210" target="_blank">World Cup 2026</a>**: Norway just eliminated Brazil. Morocco eliminated Canada. Portugal drew with Congo and is playing Spain today. I'm not a sports fanatic, but I come from a place where football is very close to religion. 

**<a href="https://www.wser.org/" target="_blank">Western States</a>**: When I can't run, I watch other people run. This year's Western States 100 miler was an exciting one to watch. Even though I was rooting for [Hans Troyer](https://utmb.world/runner/5883300.hans.troyer) to win this one, [Vincent Bouillard](https://www.wser.org/2026/06/29/2026-race-recap/) made an amazing run! Record broken, again! 



