title: LLMs in production: lessons learned
date: 26-03-2023 20:35
description: Lessons learned from deploying a Large Language Model to production. 
status: published
slug: llms-lessons-learned
thumbnail: images/50/openai_2.png

<center>
<img src="{static}/images/50/openai_3.png" alt="OpenAI image 1" style="max-width:100%;border-radius: 2px">
</center>

A couple of months ago nobody asked me about my work. _Something_ related to computers and AI. Fast forward to today, even my uncle asks me about ChatGPT. The [_hype_](https://www.urbandictionary.com/define.php?term=hype) is real. Only time will tell if the hype will materialize. But while the world wonders, work goes on. 

In the last couple of months, I've helped develop a product that leverages this tech at its core. It was - to say the least - a learning experience. Full of lessons learned, full of little traumas and things I would've done better. In the hopes of helping someone out there, here are some lessons I've learned along the way. 

### Know your use case

With so much hype surrounding LLMs, it's easy to think they'll solve all problems in Machine Learning. Or at least the ones related to NLP. From what I've seen, this is hardly the case. Let's split Machine Learning tasks into two types. (1) Predictive tasks, such as classifying the sentiment of a tweet, and (2) generative tasks, such as summarizing the content of an article.

GPT is _great_ at generative tasks. Writing an email with context, writing a summary of a web page, and creating an article given some ideas. These are a very specific subset of Machine Learning. Most of the problems we face are predictive problems: what is the sentiment of this tweet? What is the class of this image? It's hard to tell exactly how good these models will become for the predictive use case. But before throwing GPT at whatever you're facing, think about the use case. This leads me to my next point.

### Deterministic vs. stochastic

Do you know the classic "_I cannot reproduce this issue_" we've said oh so many times? Well, welcome to a whole other level of that. "_The AI said something wrong_" is a very common issue I've faced with these models. At the core, LLMs are stochastic, and not deterministic. Before LLMs, whatever model we were building, given an input, would always produce the same output. With LLMs, given the same input, the output is _rarely_ the same.

This is amazing for generative tasks but can become a real problem for predictive tasks. The problem of reproducibility. To avoid this issue, you can play around with some of the parameters of this model such as the [temperature](https://lukesalamone.github.io/posts/what-is-temperature/) or the presence penalty. This further reinforces the idea that these models are great for generating text - where the cost of failure is low. If you're predicting something with a high cost of failure - best beware.

### Prepare for the future 

This tech is moving incredibly fast. Yes, even for _us_, the group of people that _loves_ to move fast. OpenAI, is releasing models and updates at an astronomical pace. By the time you finished developing that shiny new product, there will probably be a new one. This happened to us actually. We started developing a system based on GPT-3 (e.g., `text-davinci-003`).  Shortly after, OpenAI released the ChatGPT model (e.g., `gpt-3.5-turbo`). Two days before we went to production - GPT-4 (e.g., `gpt-4`) was here. 

These models use different APIs, structures, and behaviors. Thankfully, I'd spent a Friday afternoon implementing the [Strategy Pattern](https://refactoring.guru/design-patterns/strategy/python/example), so that we could support both [Text Completion](https://platform.openai.com/docs/guides/completion) and [Chat Completion](https://platform.openai.com/docs/guides/chat) for our system. Turned out to be time well spent, and adopting GPT-4 was a moderate one-line code change. Whenever a new model comes out, expect to be rate limited, and expect timeouts. Especially with these technologies, it's worth preparing for the future, and anticipating what _might_ be released. Without [exaggerating](/blog/simple-software.html), of course. 

<center>
<img src="{static}/images/50/openai_2.png" alt="OpenAI image 2" style="max-width:100%;border-radius: 2px">
</center>

### Streaming vs. Batching

Yes, it comes down to that, a single API call to OpenAI. (Well, at least while we don't have a solid open-source alternative). Given a large enough prompt, these models can take quite a while to return a result. There's nothing worse than making a user wait for 20-30 seconds before showing some action on the screen - especially when that request ends up failing sometimes. After some days of frustration, a co-worker sent me [this](https://github.com/openai/openai-cookbook/blob/main/examples/How_to_stream_completions.ipynb) link. 

Instead of waiting for the whole completion to be finished, consider streaming the response. In short, it allows you to start receiving completion tokens as soon as they're generated. Together with FastAPI's excellent implementation of [`StreamingResponse`](https://fastapi.tiangolo.com/advanced/custom-response/#streamingresponse), it allows you to show the completion happening in real-time to users. This pattern is widely used by implementations such as [Notion's](https://www.notion.so/product/ai). Now that all we have is an API, customer experience is even more differentiating. 

### Prompt engineering is hard

We have prompt engineers now. No wonder. I prefer the term prompt _artists_. As soon as we had to put a system in place we struggled. We are used to fancy tools to track every parameter of an experiment. Now that we're designing prompts for a stochastic system the game has changed. How can know the impact of every little change in the prompt? How can I know how one instruction affects another instruction? What really defines a _good_ prompt? You see where I'm getting at. For now, it's an art - more than engineering. 

Very soon, our prompt was a list of 10-15 instructions giving very specific directions on what we needed to generate. To battle this, we created a set of scripts that would allow us to quickly compare the impact of small changes in the prompt. This is a costly exercise - given a stochastic system - since we have to call a paid API 2/3x to compare the effect of prompt changes. This allowed us to at least get a decent direction on how good the prompt is. Still, I feel like prompt engineering is still a lot of shooting in the dark. 


### Conclusion: Not the hammer you were looking for

LLMs are incredibly powerful tools. From generating text to now even supporting images - it's hard to tell where the field will lead us. For creative and generative tasks they shine like nothing before in our field. Being able to have access to such a powerful system will be groundbreaking in a lot of fields of machine learning. But with great power comes great responsibility - or _baggage_. 

Putting an LLM into production is a challenging problem with a lot of unknowns. From depending on a simple API call, to not being able to reproduce results - it can get complicated. 

If the task is simple enough (e.g., classification) it's still hard to justify a more expensive, less explainable, and albeit slower system than _traditional_ methods. I don't think this is the hammer for all our problems. At least not _yet_. 
