title: You also hate SQL? Let the LLM handle it
date: 9th March 2025
status: published
thumbnail: images/77/pycon-wroclaw-llm-text-to-sql_page-0001.webp
popular: true

Last year I made an effort to speak less and learn more. However, I still had the opportunity to present at a couple of conferences. One of them was [PyCon Wroclaw](https://www.pyconwroclaw.com/). The main goal was to talk about a couple of interesting paradigms I've come across while using LLMs to help me solve some Text-to-SQL problems.

Unfortunately the recording came out a bit broken. So I decided to copy a typical post from [Simon's blog](https://simonwillison.net/2025/Mar/8/nicar-llms/), and do a small slide walk through here. I won't promise I'll do this for the rest of my [talks](/talks). But I think it could be a pretty interesting read.

I started with my typical introduction:

<img src="{static}/images/77/pycon-wroclaw-llm-text-to-sql_page-0001.webp" class="shadow"/>

<img src="{static}/images/77/pycon-wroclaw-llm-text-to-sql_page-0002.webp" class="shadow"/>

The goal of the talk was to walk through a 'grab bag' of client cases I've come across recently and five different lessons I've learned.

<img src="{static}/images/77/pycon-wroclaw-llm-text-to-sql_page-0004.webp" class="shadow"/>

The first chapter was all about setting expectations right. When clients come with a problem nowadays, they always expect a "ChatGPT" style of product.

<img src="{static}/images/77/pycon-wroclaw-llm-text-to-sql_page-0005.webp" class="shadow"/>

<img src="{static}/images/77/pycon-wroclaw-llm-text-to-sql_page-0006.webp" class="shadow"/>

But ChatGPT isn't a simple product. It's actually a fairly complex piece of software.

<img src="{static}/images/77/pycon-wroclaw-llm-text-to-sql_page-0007.webp" class="shadow"/>

<img src="{static}/images/77/pycon-wroclaw-llm-text-to-sql_page-0008.webp" class="shadow"/>

Here I introduced what I call the *no regrets move*. I.e., what is the minimum thing that you can solve for a certain problem that will always be valuable? In the case of text-to-sql, it's *not* the interface. It's just answering questions based on your data.

<img src="{static}/images/77/pycon-wroclaw-llm-text-to-sql_page-0009.webp" class="shadow"/>

The second chapter was all about getting *something out*. Quick. I'm convinced that at least 50% of engineering problems are due to someone developing something in the basement instead of failing fast.

<img src="{static}/images/77/pycon-wroclaw-llm-text-to-sql_page-0010.webp" class="shadow"/>

<img src="{static}/images/77/pycon-wroclaw-llm-text-to-sql_page-0011.webp" class="shadow"/>

Here I mentioned some tools to get a ChatGPT interface relatively fast. So you can focus on what matters. [Here's](https://gist.github.com/duarteocarmo/85435ce9209d1824f68e11b6126ab5c9) the code for a ChatGPT-like interface using Streamlit that already includes tools like plotting.

<img src="{static}/images/77/pycon-wroclaw-llm-text-to-sql_page-0012.webp" class="shadow"/>

This is my favorite advice for any sort of engineering:

<img src="{static}/images/77/pycon-wroclaw-llm-text-to-sql_page-0013.webp" class="shadow"/>

In the 3rd chapter I finally start focusing on the task at hand. Text-to-SQL.

<img src="{static}/images/77/pycon-wroclaw-llm-text-to-sql_page-0014.webp" class="shadow"/>

I took some time to present the [BIRD-SQL](https://bird-bench.github.io/) benchmark. One of the most popular benchmarks for text-to-sql.

<img src="{static}/images/77/pycon-wroclaw-llm-text-to-sql_page-0015.webp" class="shadow"/>

When looking at the rankings, we can see that the best performing text-to-sql system has an accuracy ~75%. So in your best case scenario. Whatever you build. You can already expect your LLM to get *at least* 1/4 questions wrong.

<img src="{static}/images/77/pycon-wroclaw-llm-text-to-sql_page-0016.webp" class="shadow"/>

<img src="{static}/images/77/pycon-wroclaw-llm-text-to-sql_page-0017.webp" class="shadow"/>

I cover two 'typical' approaches to text-to-sql. And how these approaches can go from something very simple in the right - just by stuffing information into the prompt. To something a bit more [complex](https://arxiv.org/abs/2405.16755) in the left.

<img src="{static}/images/77/pycon-wroclaw-llm-text-to-sql_page-0018.webp" class="shadow"/>

But in general. Stuffing information into the prompt is what most people are doing.

<img src="{static}/images/77/pycon-wroclaw-llm-text-to-sql_page-0019.webp" class="shadow"/>

In the fourth chapter, I go into a good baseline to generate SQL to answer questions about a particular database.

<img src="{static}/images/77/pycon-wroclaw-llm-text-to-sql_page-0020.webp" class="shadow"/>

I start by talking about the funny 'please give me json' prompts. And show this small bit straight from one of Apple's prompts (Probably Apple Intelligence), where they beg the LLM to return json.

<img src="{static}/images/77/pycon-wroclaw-llm-text-to-sql_page-0021.webp" class="shadow"/>

But for me, structured outputs are critical for a maintainable and well-built LLM application. So I also take some time to talk about that.

<img src="{static}/images/77/pycon-wroclaw-llm-text-to-sql_page-0022.webp" class="shadow"/>

I start by introducing [instructor](https://python.useinstructor.com/), one of my favorite LLM libraries.

<img src="{static}/images/77/pycon-wroclaw-llm-text-to-sql_page-0023.webp" class="shadow"/>

Of course, you don't need to use instructor. You can go with [Structured Outputs](https://platform.openai.com/docs/guides/structured-outputs) as well.

<img src="{static}/images/77/pycon-wroclaw-llm-text-to-sql_page-0024.webp" class="shadow"/>

But in general - I absolutely hate 'OpenAI code'. E.g., code that is completely locked into OpenAI or any other AI provider. So I present [LiteLLM](https://docs.litellm.ai/#litellm-python-sdk). A great tool to keep your code provider agnostic.

<img src="{static}/images/77/pycon-wroclaw-llm-text-to-sql_page-0025.webp" class="shadow"/>

Here's where [LiteLLM](https://docs.litellm.ai/#litellm-python-sdk) really shines. When you can switch out *any* model from *any* provider, just by switching the prompt.

<img src="{static}/images/77/pycon-wroclaw-llm-text-to-sql_page-0026.webp" class="shadow"/>

As an example I use a simple SQLite database of my running data from Strava.

<img src="{static}/images/77/pycon-wroclaw-llm-text-to-sql_page-0027.webp" class="shadow"/>

Here's the code to load the Strava data and a small preview of the data.

<img src="{static}/images/77/pycon-wroclaw-llm-text-to-sql_page-0029.webp" class="shadow"/>

Time to build a basic text-to-sql prompt.

<img src="{static}/images/77/pycon-wroclaw-llm-text-to-sql_page-0030.webp" class="shadow"/>

My prompt structure. It includes a Preamble, the CREATE TABLE statement so that the LLM knows the structure, some response guidelines, and the user question.

<img src="{static}/images/77/pycon-wroclaw-llm-text-to-sql_page-0031.webp" class="shadow"/>

The issue with most of these systems is that we have no way to ensure a certain query is actually valid..

<img src="{static}/images/77/pycon-wroclaw-llm-text-to-sql_page-0032.webp" class="shadow"/>

Here's a particularly nasty piece of code. I use [Instructor](https://python.useinstructor.com/) to generate the SQL from a question, but also include a custom validator. This will ensure that whatever the LLM generates can actually be run against the database. This is of course, very dangerous. So one should not put this code in production, since you'll be opening yourself to all sorts of problems. But it's a nice way to ensure *validity*.

Here's the Frankenstein class:

<img src="{static}/images/77/pycon-wroclaw-llm-text-to-sql_page-0033.webp" class="shadow"/>

And the function we use to call it.

<img src="{static}/images/77/pycon-wroclaw-llm-text-to-sql_page-0034.webp" class="shadow"/>

Here are some examples of running this system. With two questions. For one, it responds well. For the other, it completely fails the answer. But both answers are smooth and valid from the SQL perspective. But that doesn't mean they are correct.

<img src="{static}/images/77/pycon-wroclaw-llm-text-to-sql_page-0035.webp" class="shadow"/>

So now that we are getting valid answers, how can we ensure that they are actually good?

<img src="{static}/images/77/pycon-wroclaw-llm-text-to-sql_page-0036.webp" class="shadow"/>

Once we've started with a baseline. I take Chapter 5 to talk about how to make things better once you have this baseline done.

<img src="{static}/images/77/pycon-wroclaw-llm-text-to-sql_page-0037.webp" class="shadow"/>

Mandatory meme about testing and performance. If you never test, your tests never fail. If you never evaluate, your LLM system is perfect.

<img src="{static}/images/77/pycon-wroclaw-llm-text-to-sql_page-0038.webp" class="shadow"/>

To improve your text-to-sql system, you actually need to measure it.

<img src="{static}/images/77/pycon-wroclaw-llm-text-to-sql_page-0039.webp" class="shadow"/>

This is just like traditional Machine Learning. We can go back to one of the most well-known metrics: Accuracy.

<img src="{static}/images/77/pycon-wroclaw-llm-text-to-sql_page-0040.webp" class="shadow"/>

To measure accuracy, we can create some questions based on the data from our Database. Use our LLM system to respond to those same questions, and compare both answers. That's it!

<img src="{static}/images/77/pycon-wroclaw-llm-text-to-sql_page-0042.webp" class="shadow"/>

We can use instructor/structured outputs again here, to understand if our LLM answer matches the information in our baseline answer.

<img src="{static}/images/77/pycon-wroclaw-llm-text-to-sql_page-0043.webp" class="shadow"/>

I really like looking at data, and evaluating where things go wrong. But I'm skeptical of the myriad of tools coming out to evaluate LLMs. And I'm a big fan of Google Sheets. Mainly because when I look at the data, I probably also look at it with some sort of subject matter expert. So the fewer 'things' between us and the data, the better. And Google Sheets are fine.

<img src="{static}/images/77/pycon-wroclaw-llm-text-to-sql_page-0044.webp" class="shadow"/>

Here's an example of how I use Google Sheets to look at the performance of this text-to-sql system. You can see the question we want answered. The SQL and answer from our ground truth, the SQL and answer from the LLM system, and its evaluation. We also include a reason why a certain case was FAIL/PARTIAL.

<img src="{static}/images/77/pycon-wroclaw-llm-text-to-sql_page-0045.webp" class="shadow"/>

This is all nice and dandy. But we should never forget the big picture. So what?

<img src="{static}/images/77/pycon-wroclaw-llm-text-to-sql_page-0046.webp" class="shadow"/>

In the final slide, I come back to the three most important lessons: Iterate quickly, make the SQL generation robust and explainable, and iterate from a baseline.

<img src="{static}/images/77/pycon-wroclaw-llm-text-to-sql_page-0047.webp" class="shadow"/>

I then took some questions and wrapped things up!
