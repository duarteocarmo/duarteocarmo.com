title: Book release: DeepSeek in Practice
description: Thoughts on my new book, DeepSeek in Practice, now available for pre-order through Packt
date: 17th of November 2025
status: published
audio: true
thumbnail: images/89/cover_image.jpeg

<br>
<a href="https://www.packtpub.com/en-us/product/deepseek-in-practice-9781806020850" target="_blank">
<center>
<img src="{static}/images/89/cover_image.webp" alt="DeepSeek in Practice book Packt" class="shadow" style="max-width: 40%">
</center>
</a>
<br>
Back in May this year, my longtime friend [Alex](https://mlops.systems/about.html) reached out and asked me if I wanted to collaborate with him on a book about DeepSeek. I would love to tell you the story of how I thought long and hard before getting back to him. I didn't. I just said yes.

Now, 6 months later, I'm excited to announce that [*DeepSeek in Practice*](https://www.packtpub.com/en-us/product/deepseek-in-practice-9781806020850) is out and available for pre-order! The book is published by [Packt](https://en.wikipedia.org/wiki/Packt) and is a collaboration between [Andy Peng](https://pengandy.com/), [Alex Strick van Linschoten](https://mlops.systems/about.html), and me.

As the title suggests, this book focuses on DeepSeek models, which [famously took the world by storm earlier this year](https://www.nytimes.com/2025/01/27/technology/what-is-deepseek-china-ai.html). It's organized into three parts: "Understanding and Exploring DeepSeek" examines their role in the wider LLM world. "Using DeepSeek" is entirely dedicated to applying DeepSeek models to real-world problems. Finally, "Distilling and Deploying DeepSeek," covers distillation and deployment.

Even though the book was a joint effort, my main focus was on Part 2, and how to use DeepSeek models to tackle real-world problems. In particular two chapters:

**Chapter 5, *Building with DeepSeek*,** walks through creating an alternative to Garmin's daily summary notifications. We go through building a prototype using DeepSeek's API, how to leverage local models, frameworks like [XGrammars](https://github.com/mlc-ai/xgrammar) and [vLLM](https://docs.vllm.ai/en/latest/), all the way to deploying your own model using [AWS Large Model Inference](https://docs.djl.ai/master/docs/serving/serving/docs/lmi/index.html) (LMI).

**Chapter 6, *Agents with DeepSeek*,** is all about agents. We start with a short intro to agents, tools, and the inner workings of the [MCP protocol](https://modelcontextprotocol.io/docs/getting-started/intro). After that, we build (from scratch) three different agents powered by DeepSeek models: an evaluator-optimizer that summarizes Arxiv papers, an orchestrator-worker that generates research reports, and a tool-calling agent that can search the web and answer complex questions.

Overall, I'm really excited that this book finally gets to see the light of day. Contributing to a book is no small feat. The process is rough: lots of discussion and lots of drafts thrown in the trash. It was hard work, but also a lot of fun.

I hope you enjoy it!

Links:

- [Packt](https://www.packtpub.com/en-us/product/deepseek-in-practice-9781806020850)
- [Amazon](https://a.co/d/8I139tG)
- [GitHub Repository](https://github.com/PacktPublishing/DeepSeek-in-Practice)

