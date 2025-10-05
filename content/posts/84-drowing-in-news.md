title: Drowning in News
description: Moving from Feedly to FreshRSS and taking back control of my news feed.
date: 5th of October 2025
status: published
thumbnail: images/84/cover.png

The world moves fast, faster every day. For those who work with technology - and even those who don't - it's hard to keep up with the news. But I've always enjoyed staying up to date with what is happening, and my main tool to get it done hasn't changed in years: it's [RSS](https://en.wikipedia.org/wiki/RSS).

My morning routine has been the same for the past 10 years. Every morning I open up [Reeder](https://reederapp.com/classic/) on my Mac - or on my phone if I'm on the go - and ctrl+click the articles that interest me the most. The setup is not groundbreaking: a [Feedly](https://feedly.com/i) account for my feeds, and Reeder as the app to consume them. It's not complicated. But something was bothering me.

<img src="{static}/images/84/reeder.png" alt="reeder classic">

RSS lets me stay in control of what's happening. With RSS, I'm not a victim of someone else's algorithm. I decide what gets in front of me and how. But I didn't have that feeling anymore. Messy categories, more and more feeds, non-working feeds, just a firehose of articles everyday. Scanning 100+ titles every morning is not a great way to start the day. 

Like most people nowadays, I bluntly decided to 'throw AI'&reg; at the problem. I exported all my feeds from Feedly into `opml` format and created a [quick script](https://gist.github.com/duarteocarmo/4869cae3f8c5bd5c95a556cc3a70ece3) that uses LLMs to re-categorize all my feeds and reorganize them. That worked for a couple of weeks, but this was not a categorization problem. This was a *get back into control* problem. 

I took the plunge and decided to self-host my RSS server. A couple of clicks on [my Coolify instance](/blog/how-i-self-host-in-2024.html) and [FreshRSS](https://freshrss.org/index.html) was up and running at [news.duarteocarmo.com](https://news.duarteocarmo.com). 

My first impressions are great. First, it automatically detects dead or non-working RSS feeds. That led to a lot of 'Oh! I loved following this website' moments. So I spent half an hour cleaning those up. Also, managing the categories of different feeds is just much easier. There's a nice drag and drop view to put everything into place. But still, RSS is an uphill battle.

<img src="{static}/images/84/freshrss.png" alt="freshrss">

The world doesn't like RSS, they want you to go to the website and click those links. They'll ask for your email, they'll put up a paywall. Anything to get you to go to the website directly. But there's hope: here are some of my favorite tools to get everything back into your neatly organized RSS feed:

- **What about newsletters?** [Kill the Newsletter](https://kill-the-newsletter.com) is the solution. A great app from [Leandro](https://leafac.com/) that turns any newsletter into an RSS feed you can subscribe to. Better? It's free. I would pay for it.
- **What about Substack?** I know there's a lot of interesting content on [Substack](https://substack.com/), and many people I follow are pretty active there. Here's the good news: every Substack publication [also offers an RSS feed](http://support.substack.com/hc/en-us/articles/360038239391-Is-there-an-RSS-feed-for-my-publication).
- **What about Reddit?** That's a good question. For years, Reddit has been gradually phasing out the ability to follow subreddits via RSS. Throttling and failures have become the norm. [Feedly offers a solution for this](https://feedly.com/new-features/posts/follow-reddit-in-feedly), but it hasn't worked reliably for me. I want to follow *just the right amount* of Reddit content. Fortunately, there's an excellent open-source project called [Reddit Top RSS](https://github.com/johnwarne/reddit-top-rss). I self-hosted it on Coolify (again, just 2 clicks) and now I have a *limited* and *controlled* feed for every subreddit I'm interested in.

I haven't really scratched the surface of what [FreshRSS](https://freshrss.org/index.html) can do. Statistics, filtering feeds, extensions, labels, I haven't even begun exploring it all. And honestly? That's fine. My Reeder workflow remains unchanged, my morning routine intact. But underneath, something fundamental has shifted. Just like with my [finances](/blog/hacking-on-my-finances-part-2-beancount-on-beanstalk.html), self-hosting gives me something no third-party service can: control. 
