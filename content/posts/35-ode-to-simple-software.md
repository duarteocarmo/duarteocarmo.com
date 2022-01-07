title: Simple software
date: 01-06-2022
description: Keep it simple, stupid 
status: published
slug: simple-software
lang: en

In the summer of 2017 I wrote one of my very first programs: an algorithm that ranked leads. It would help our sales team to target the best potential customers in Boston and surrounding areas. 

We (me and my manager at the time) were making a short trip to the local [Dunkin' Donuts](https://goo.gl/maps/8nRDzKo9VUaBxXe56), and I remember talking to him about what I was building. In the midst of talking about all the edge cases I had in mind, he cut me off, and said: "Duarte, *first* make it work. *then* make it pretty". He became one of my mentors.

At the time I didn't really get it. But this was one of *the* best pieces of advice I was ever given. 

Don't make a "robust" plan for that weird edge case. That edge case will probably never happen. Which means you will be writing code for something that will most likely not happen (i.e. useless code). Why should you write useless code? You shouldn't. Handle that edge case when it happens, and only *if* it happens.  

Even though words like Agile, SAFe, and LEAN have become nothing  short of *buzzwords*, there's one lesson from the Agile Manifesto that I try to keep in mind: "Responding to change over following a plan". Iterate quickly, and then change your software only when required. 

Writing complex code is not a way of demonstrating technical ability. It has the exact opposite effect. Startups and large Businesses value programs that solve problems. Of course they also value reliability and speed, but do they prefer something slow that works, or something fast that doesn't exist? 

Scheduler, State Machine, Abstract, Controller, Operator. These words always make my complexity alarm go off. Yes, under certain circumstances they're needed, but when you have a technical discussion and these come up, it's time to take a step back and make sure that you know what you're getting into. By the time you do, it might be too late to make things simple again. 

Some people think great software is complicated. [Instagram](https://instagram-engineering.com/types-for-python-http-apis-an-instagram-story-d3c3a207fdb7) is a Python monolith with a few thousand Django endpoints. And even if [I don't use it anymore](/photos), it's great software. What makes software great is the ability to provide high value to users in a [reliable](https://www.gkogan.co/blog/simple-systems/) and upgradable way. 

I think of great software like I think about great architecture.  There is a way of adding complexity without adding rigidity, maintaining flexibility, and breathability. And I don't think I've mastered that yet. Because great is simple, but it's also [hard](https://bigseventravel.com/how-long-to-build-the-pyramids/). 
