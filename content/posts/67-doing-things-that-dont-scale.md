title: Do things that don't scale
date: 06-06-2024 10:00
description: Thoughts on doing things that don't scale, and getting stuck in the ether.
status: published
slug: do-things-that-dont-scale
thumbnail: images/67/cover.png

I'm lucky enough to work with some pretty talented folks. During a recent offsite, one of them gave a completely improvised talk. He had just gotten back home from holidays - so naturally, they didn't really have time to prepare anything. But what they said resonated. 

It was about _improvisation_. How a lot of things we do every day are - to some extent, made up! From how we greet each other, to how we respond to an unexpected phone call. None of it is planned. We don't create some sort of crazy scalable distributed architecture to deal with these things: They're _[licks](https://en.wikipedia.org/wiki/Lick_(music))_. 

For some, this felt counter-intuitive. For me, it really hit home.

But I understand how it might feel counter-intuitive. Experienced engineers think _hard_ before solving problems - they're expected to. "Hey - we've seen this before..." -  They'll research. They'll anticipate problems. Even when the problem is not well-defined, they'll work hard on defining it! It doesn't even cross our minds that a badly defined problem is probably not a problem to begin with. With all this thinking, they enter _the ether_. The ether is that stale anticipation, that hesitation. It takes many forms - but in the engineering world it's normally in the form of endless research, stalling, no decisions being made. The ether is this "pre-problem" hesitation.

The talk also argued about how perfect is [the ENEMY](https://www.youtube.com/watch?v=CZ8fTfpyqpQ&t=211s) of good enough. While we're thinking of the perfect solution, the original problem is _still_ there. Users don't see your research, users don't see the architecture meetings, users don't see _the ether_. The only thing they see is the problem. And guess what? The problem is still there. 

And yeah, good enough is likely pretty bad. The first solution, will probably suck. It was fast, we were in a rush. We just wanted to put something out there to solve a problem! And obviously, we didn't think of all the ways it would/could break. 

It's a privilege to build something that doesn't scale. We might argue that if you get stuck in the ether in the first place, you won't even get to scale being problem. Scale is a great problem to have. It means your solution _started_ solving a problem - and people want more of it. This is a good thing. 

And yes, now we have _double the trouble_. Now we need to scale AND handle users at the same time. But what's the alternative? Getting stuck in the ether and potentially building something we don't even know if people will use? 

I like to think that doing things that don't scale will likely save time in the long run. Lots of things we build don't get used. And so if you spend a lot of time in the ether - you risk that time being completely wasted. And there are no guarantees you'll likely be able to anticipate all the ways you won't scale. But getting something out there, in front of people, takes you from 0 to 1. And the faster we realize what we've built doesn't solve anyone's problem, the better. 

And solving problems is what we're here for.