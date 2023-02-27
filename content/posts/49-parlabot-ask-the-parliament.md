title: parlabot - ask the Portuguese parliament
date: 27-02-2023 18:55
description: A contextual LLM question/answering system
status: published
slug: parlabot
thumbnail: images/49/parlabot-screenshot.png

Large language models (LLM) are really [dumb](https://www.theverge.com/2023/2/8/23590864/google-ai-chatbot-bard-mistake-error-exoplanet-demo). I mean, how can you fail when the question is as simple as "_What is 23 times 18_"? Even though they're making most headlines, at the end of the day, these models are, predicting the next token based on the previous ones. If we ask a super simple question without any context to an LLM, the performance will only depend on [how much the model has seen that example](https://arxiv.org/pdf/2202.07206.pdf).

But LLMs are also amazing. Have you used [GitHub copilot](https://github.com/features/copilot) lately? I don't trust it to write my functions for me, but damn it writes a good boilerplate. It's like auto-complete, but _better_. It doesn't only know your imports. It knows where you are in the code base, and can suggest based on that. 

The difference? _Context_. When using copilot, your code _is_ the context, and that's why copilot knows exactly what to suggest. So how can I give the right context to one of these models? To answer this, I built [parlabot](https://parlabot.duarteocarmo.com/). Parlabot ([parlamento](https://www.collinsdictionary.com/dictionary/portuguese-english/parlamento) + bot) uses all transcripts from the Portuguese parliament to answer any question you might have about Portuguese politics. It also (tries) to do so in the most truthful way it can, with the information it has.

<a target="_blank" href="https://parlabot.duarteocarmo.com">
<img src="{static}/images/49/parlabot-screenshot.png" alt="Parlabot website" style="max-width:100%;">
</a>

There are two things at play when you ask a question to parlabot. Below is a sketch that might make things easier to follow.

The first part is the search engine. To make this work, I scrapped all transcripts from the Portuguese parliament and used a multilingual embedding model to transform them into vectors. Whenever you type in a question, I embed it using the same exact model, transforming it into another vector. I then find the top k most similar reference vectors to the query vector. This is the same as finding the top K most relevant speech segments for that question.  

Once I have the most relevant speech segments, it's time to build the _prompt_. The prompt, has two parts, the _context_, and the _direction_. The context, is simply the most relevant speech segments, the corresponding speakers, and the political parties. In the direction part of the prompt, I ask GPT3 to answer a given question using the segments from the context.

<a target="_blank" href="https://parlabot.duarteocarmo.com">
<img src="{static}/images/49/LLM-sketch.png" alt="LLM Question/Answer system" style="max-width:100%;border-radius: 2px">
</a>

The results are pretty good! The bot is very capable of using the context given to answer most questions. Of course, the context is not always relevant to a question. For example, if you ask "How to bake a cake?", it's unlikely we'll find the answer in the data set of parliament transcriptions. With good prompt design, we can make the bot answer "_I don't know_" when this is the case. 

The mix of LLMs, politics, and poorly written code is a great recipe for disaster. Although disaster does sound pretty fun,  I don't expect this bot to answer _truthfully_ any of the questions Portuguese tax-payers have about elected parties. These answers should be taken with a massive grain of salt and skepticism. LLMs are stochastic beasts that might predict two different outputs with the exact same set of inputs. 

Still, this system might be interesting to solve problems where the cost of failure is not catastrophic. Without forgetting, that a bit of skepticism is a great foundation for any ML system. 

