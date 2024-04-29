title: How I self-host in 2024
date: 28-04-2024 19:00
description: From scattered Docker files to Coolify. 
status: published
slug: how-i-self-host-in-2024
thumbnail: images/66/cover.png

I'm a sucker for side projects. There's nothing quite like building something to learn about it.

Over the last 5+ years I've accumulated a little over 15 small web apps and websites. Almost all of them are hosted on a small Hetzner server and deployed using [a mix of ssh, docker-compose, and Caddy]({filename}/posts/41-down-from-the-cloud.md). 

Some months ago my small server started giving me some problems. The 4 vCPUs and 16 GB RAM weren't enough, and hiccups became more frequent. I also want to run more and more small LLMs on it, which turned out to be _[challenging](https://github.com/duarteocarmo/lusiaidas/blob/master/app.py#L1)_. The whole ["ssh with root using github actions"](https://github.com/duarteocarmo/governosombra/blob/master/.github/workflows/workflow.yml) started to look like more of a limitation than a feature. 

It was time for an upgrade.

<center>
<img src="{static}/images/66/coolify-apps.png" alt="Coolify apps" 
style="max-width:100%;border-radius: 2px">
</center>

First, I needed to upgrade my hardware. Not sure if [Hetzner](https://www.hetzner.com/) is the cheapest out there, but after using them for 5+ years I can definitely say they're reliable. I went with their [server auction](https://www.hetzner.com/sb), which is a great (and sustainable) way of getting a nice refurbished server for a fair price. For about 30 EUR/month, I upgraded to a nice Intel i7 with 64GB RAM(!). Should be more than enough.

With better hardware, I needed to decide whether I would keep my [old setup]({filename}/posts/41-down-from-the-cloud.md), or upgrade to something a bit more _streamlined_ (god I _hate_ that word). Turns out, there are quite some open source PaaS alternatives. From [Dokku](https://dokku.com/), [CapRover](https://caprover.com/), to DHH's [Kamal](https://kamal-deploy.org/). The one who caught my eye the most was [Coolify](https://coolify.io/). Without much due diligence, it seemed fit most of what I needed: [Open source](https://github.com/coollabsio/coolify), [easy to install](https://coolify.io/docs/installation), [active project](https://github.com/coollabsio/coolify/commits/main/), [with a polished interface](https://coolify.io/docs/screenshots), [integrates](https://coolify.io/docs/knowledge-base/git/github/integration) with GitHub, and supports docker-based deployments. That's not an easy list to check-off.

The migration was pretty smooth, except for [a](https://aicoverlettercreator.com/) [couple](https://infrequent.app/) of more complicated Django applications with databases on docker volumes. Since everything was already running on containers, it was pretty much plug-and-play. In a couple of days everything was migrated. 

<center>
<img src="{static}/images/66/kuma-screenshot.png" alt="Kuma screenshot" 
style="max-width:100%;border-radius: 2px">
</center>

There are a lot of things I love about Coolify. It scans my GitHub repos and redeploys when needed via webhooks. It also sends me Telegram notifications when something gets updated to a new version. Finally, it also provides a wide range of other applications you can deploy (Databases, S3-compatible storages, and a [wide range](https://coolify.io/docs/resources/services/index) of other services). 

Don't get me wrong - I love the Cloud. But essentially, the Cloud is just someone else’s computer. So why shouldn’t it be my computer? Self-hosting everything means I can pay a fixed price for my hardware, and _not_ for the number of applications that run on it. And even though I did like my little _hacked-together_ setup, I love being able to use, AND [contribute](https://github.com/coollabsio/coolify/pull/2028) to a promising open source project!

There's something incredible about what a [1-man team](https://github.com/andrasbacsai) can accomplish with the support of the open source community.
