title: Running evaluations from AI systems: Lessons and tools
date: 2026-11-23
status: draft
slug: lessons-from-running-model-evaluations
description: TODO
thumbnail: images/116/cover.webp

Last week, Anders invited me to give a talk at [PyData Copenhagen](https://www.meetup.com/pydata-copenhagen/) meetup. He asked me to talk about [European Portuguese LLMs]({filename}/posts/113-amalia-small-models.md) (even though I had already done so at [Lisbon AI](https://www.youtube.com/watch?v=e7VYjMgMv2U)). I decided to expand the talk with a series of lessons I've learned recently by running evaluations for AI systems (LLMs, VLMs, Audio models). 

Here we go. 

<center>
<a href="{static}/images/116/cover.webp" target="_blank">
<img class="slide" src="{static}/images/116/cover.webp" alt="The Hitchhiker’s Guide to European Portuguese LLMs (and how to ensure your models and applications run well) Duarte O.Carmo AI/ML/Data Consultant &amp; Researcher @ DOC Tech." style="max-width:100%;border-radius: 2px">
</a>
</center>

## Inspect

[Inspect](https://inspect.aisi.org.uk/) has become my hammer for almost any scenario. AI Product evals, coding traces, audio models, you name it - I use Inspect. It's open source, stable, and supports a bunch of [off-the-shelf evaluations](https://ukgovernmentbeis.github.io/inspect_evals/)(think MMLU, GPQA, HumanEval, etc).  (There's also [Inspect SWE](https://meridianlabs-ai.github.io/inspect_swe/) to run evaluations for coding agents. Stil waiting for [Pi support](https://github.com/meridianlabs-ai/inspect_swe/pull/152). Yes - I have my own fork for that). 

<center>
<a href="{static}/images/116/inspect.webp" target="_blank">
<img class="slide" src="{static}/images/116/inspect.webp" alt="My evaluation superpower: Inspect Inspect docs ↗" style="max-width:100%;border-radius: 2px">
</a>
</center>

Now that LLMs write most of the code, I care that a coding agent can easily expand and act on my eval suite. I have started to gravitate towards the layout below. Models, Tasks, VLLM arguments, GPU clusters, everything is config. It's very easy for an agent to add things without me loosing understanding of what is happening. 

<center>
<a href="{static}/images/116/evals-layout.webp" target="_blank">
<img class="slide" src="{static}/images/116/evals-layout.webp" alt="LLMs write the code, but I like my things organized evals/ ├── Makefile ├── configs/ │ ├── tasks.yaml │ └── models.yaml ├── clusters/ │ └── gb10.mk ├── src/evals/tasks/ ├── logs/ └── experiments.md # make help # what to run # how to run it # where to run it # custom tasks # .eval files # every run, appended Config, not code: task × model × cluster Pin everything: dataset + model revision, seed, lab sampling One make target per action: submit, rescore, sync, view Logs are the source of truth: rescore without regenerating Experiments log: every run appends model, task, score  # configs/tasks.yaml # Zero-shot, like the model report. gsm8k_0shot: task: inspect_evals/gsm8k args: fewshot: 0 # configs/models.yaml qwen3-4b: path: Qwen/Qwen3-4B generation: temperature: 0.7 # Qwen recommendation top_p: 0.8 seed: 42 # clusters/gb10.mk MODELS_ROOT := /data/models VLLM_IMAGE := images/vllm.sif $ make submit MODEL=qwen3-4b TASK=gsm8k_0shot CLUSTER=gb10 $ make sync # logs → hf://buckets/&lt;you&gt;/evals $ make view # Inspect viewer on the tailnet" style="max-width:100%;border-radius: 2px">
</a>
</center>

One of the nicest things about Inspect is that it allows you to very easily LOOK AT WHAT IS GOING ON. Everything is powered by the [Inspect Viewer](https://inspect.aisi.org.uk/log-viewer.html). You can add anything to a trace to get more context: PNGs, Audio files, extra scorers, you name it! 
<center>
<a href="{static}/images/116/audio-sample.webp" target="_blank">
<img class="slide" src="{static}/images/116/audio-sample.webp" alt="It works for anything you might be working on" style="max-width:100%;border-radius: 2px">
</a>
</center>

Inspect also has great support for LLM as a Judge. You can run an evaluation and "re-score" it - with an LLM as a Judge. That allows you to keep both things in the same place - so you can see when things go wrong. (more on that below). 
<center>
<a href="{static}/images/116/llm-judge.webp" target="_blank">
<img class="slide" src="{static}/images/116/llm-judge.webp" alt="LLM as a judge: the judge is in the log too" style="max-width:100%;border-radius: 2px">
</a>
</center>

## Lessons

**Lesson 1: Not everything is what it appears to be.** In a recent project I was tasked with running evaluations for an LLM that is still in the works. My first goal: Reproduce scores from popular open weight models. My first reaction? Oh my god this is a shit show. Next time you look at an evaluation benchmark table - beware - you have no clue of what is going on. 

<center>
<a href="{static}/images/116/lesson-1.webp" target="_blank">
<img class="slide" src="{static}/images/116/lesson-1.webp" alt="Lesson 1: Not everything is what it appears to be Expectation • All models use the same configuration for tasks • All models use the same configuration for generation • We compare apples to apples Reality “For each question, we sample 64 times and take the average accuracy as the final score.” Qwen3 technical report, p. 13  • We ran this 64 times and took the best or average • We turned off thinking because it was looping, and removed it from the report • We use the lab’s preferred settings for generation, otherwise greedy • When we can’t parse an answer, we give the model a random letter • Our parsing assigns the first matching letter as the choice • …and the list goes on" style="max-width:100%;border-radius: 2px">
</a>
</center>

**Lesson 2: Look at your fucking traces.** It's easy to take a task and use an LLM as a judge to 2x check its score. What's harder is making an LLM as a judge that is *actually* good. I invite curious readers to read the slide below. And you quickly realise why this lesson is named so aggressively. 

<center>
<a href="{static}/images/116/lesson-2.webp" target="_blank">
<img class="slide" src="{static}/images/116/lesson-2.webp" alt="Lesson 2: Look at your f*cking traces" style="max-width:100%;border-radius: 2px">
</a>
</center>

**Lesson 3: Start small.** I've seen this hundreds of times: I ask about performance, I get answers with the words "groundedness" and "fidelity". You know - all those bullshit metrics made by open source frameworks just so you can feel good abour yourself of having a number to look at. Even if you have no idea what that number means. 

My advice is very simple: start with 10 cases. Not 100, not 50. 10! 10 cases where you think your system might fail. Build those, measure how well your system does, and read some traces. You'll learn much more than by throwing off-the-shelf bullshit metrics at your problem.

<center>
<a href="{static}/images/116/lesson-3.webp" target="_blank">
<img class="slide" src="{static}/images/116/lesson-3.webp" alt="Lesson 3: Start small, don’t complicate • If your problem is challenging enough, you can start with 10 cases • Look at where things failed • Expand from that: it will help you make decisions • Don’t throw generic benchmarks or generic metrics at it • Have an internal Inspect task where you can test new models, prompts, etc." style="max-width:100%;border-radius: 2px">
</a>
</center>

[Thanks Hamel for the meme](https://hamel.dev/notes/llm/evals/memes/#meme-images). 

If you're interested in the full slide deck, [here it is]({static}/pdfs/pydata_copenhagen_european_portuguese_llms.pdf).
