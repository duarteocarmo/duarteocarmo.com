title: Rebuilding /photos
date: 01-02-2024 22:35
description: Rebuilding the /photos part of my blog 
status: published
slug: rebuilding-photos
thumbnail: images/59/ambrosio_preview.png

A couple of years ago, I decided to remove all my photos from Instagram. I wanted something for myself. Something that suited what I needed. The result was [/photos](/photos.html). I wrote about it when I built it [too]({filename}/posts/31-self-hosting-my-instagram-profile.md). Here's a snippet from that post:

_[...] Uploading is by no means as simple as opening an app and snapping a picture. But I've created a small Python script that processes a photo, generates a thumbnail, asks some questions about it, and uploads it to S3 and my blog. And that's good enough [...]_

It wasn't good enough. I guess some [principles](https://course.ccs.neu.edu/cs5500f14/Notes/Prototyping1/planToThrowOneAway.html) are just timeless. It needed to be thrown away.

## One to throw away

Quickly after making it, it was pretty obvious it was a solution to throw into the trash. In 2 years, I published a little over 10 photos. It's not that I want to publish thousands of photos, but I've always enjoyed taking and sharing them. But that whole run a script thing was just not working for me.

In a way, it's a lot like writing. Add a little bit of friction to the process, and nobody will use it at all. The script I originally built quickly got lost and stopped working. Whenever I wanted to share a photo, my laptop wasn't around. When the laptop was around, I wasn't thinking of sharing photos. So no, not good enough. 

Whatever I was going to build to replace the old system, needed to do one thing really well: get out of the way. 

I thought about it a bunch. An API? Should I interact with that API via shortcuts? Should I just build an entire front-end? What if I give [leptos](https://leptos.dev/) a shot? Should I rclone a google photos album? It can't be that hard. I needed something that got out of the way.

<center>
<img src="{static}/images/59/ambrosio.png" alt="Ambrosio create photo" style="max-width:95%;border-radius: 2px">
<figcaption></figcaption>
</center>


## Ambrosio

I needed something that was already part of my routine. The result is [Ambrosio](https://github.com/duarteocarmo/ambrosio). Some will recognize the [name](https://youtu.be/oSKi309VnG8?si=92t2m6KNgsX092FX&t=9). Ambrosio is a Telegram bot that was designed to be my personal assistant. 

I designed Ambrosio to be able to have different [_modes_](https://github.com/duarteocarmo/ambrosio/tree/master/modes). The first one is the `photo` mode. It's responsible for performing [CRUD](https://www.crowdstrike.com/cybersecurity-101/observability/crud/) operations on an [R2 bucket](https://www.cloudflare.com/developer-platform/r2/). To maintain the speed of /photos, it also generates a `webp` thumbnail with reduced quality. If needed, it triggers a rebuild of my website using a [deploy hook](https://developers.cloudflare.com/pages/configuration/deploy-hooks/).

Instead of having to create a markdown page for every new photo, I've built another small pelican [plugin](https://github.com/duarteocarmo/duarteocarmo.com/blob/master/plugins/photos/photos.py). Before building the website, it downloads all the metadata for each photo, and generates the pages that it needs to. So that website builds remain fast on my local machine, I also added disk caching. Remember: get out of the way!

## On Go

I decided to build Ambrosio using something I've never used before: Go. I've tinkered with a couple of code bases but never really used it to build something from scratch. The idea of something not as strict as Rust, but also not as flexible as Python really sparked my curiosity. 

Go gives me mixed feelings, but Go gives me hope. It is strict, but not _too_ strict. It gives me the confidence when writing code that Python has never given me. And gives me guarantees that if the compiler does not complain, things will mostly work fine. There are some things I still don't understand about Go. The first is error handling. Having a bunch if `if err == nil` throughout the code base is not particularly nice to look at. Also hesitant about the whole one letter variable names thing. Things tend to become cryptic. 

It's fun how programming languages all start looking like the same the more you use them. For now, I'm curious to see how my opinion about Go evolves with time. 

One thing is clear though: Whatever technology you use, whatever framework you go with, technology is beautiful when it _gets out of the way_. 



