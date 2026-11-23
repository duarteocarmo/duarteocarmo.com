title: Lessons from running model evaluations
date: 2026-11-23
status: draft
slug: lessons-from-running-model-evaluations
description: TODO
thumbnail: images/116/cover.webp

Last week, Anders invited me to give a talk at the local Pieda Copenhagen meetup. He wanted me to talk about European Portuguese LMs, but I had already talked about that theme, had already talked about that topic at Lisbon AI at the Lisbon AI conference recently so I decided to expand the presentation with a bunch of things I've learned recently by running evaluations for AI systems new paragraph. For systems I mean anything that can be like something like a large language model, maybe it's a vision language model, maybe it's like a voice model that we're developing, basically anything surrounding that. 

So I covered a couple of extra topics that I think might be relevant to my audience, mainly focus on evaluation. 






TODO intro. [Full slides]({static}/pdfs/pydata_copenhagen_european_portuguese_llms.pdf). Related: [AMALIA vs. smaller reasoning models]({filename}/posts/113-amalia-small-models.md).

<center>
<a href="{static}/images/116/cover.webp" target="_blank">
<img class="slide" src="{static}/images/116/cover.webp" alt="The Hitchhiker’s Guide to European Portuguese LLMs (and how to ensure your models and applications run well) Duarte O.Carmo AI/ML/Data Consultant &amp; Researcher @ DOC Tech. |" style="max-width:100%;border-radius: 2px">
</a>
</center>

The first thing I talked about was the fact that I use Inspect for almost all of my evaluation work. Either it's an LLM, even if it's a coding agent or some trace, Inspect has become like the de facto tool I use to run evaluations for most of the AI systems I run across. It's great, it's open source, it's pretty stable, it supports a bunch of off-the-back evaluations, and it supports a very simple system to add more evaluations on it. And here we should probably link the Inspect framework website. We should also link like there's they have like a separate website with a bunch of the evaluations with like default configs and commands and stuff like that. And we should also link that website and there's also the inspect suite thing that tries to like where we can run evaluations for coding agents. So add that link as well and mention that there's this thing that I made a PR and they didn't really accept it. Something in fact, it's so stable that even the PRs that I added to it don't even get merged. So normally I think that's a good indicator

<center>
<a href="{static}/images/116/inspect.webp" target="_blank">
<img class="slide" src="{static}/images/116/inspect.webp" alt="My evaluation superpower: Inspect Inspect docs ↗" style="max-width:100%;border-radius: 2px">
</a>
</center>

Inspect is a great framework, and now that LLMs write most of the code, I don't really care about the nitty-gritty of the code, but I actually care about the format of any evaluation project I start and I've gravitated towards this single format that I've described in the previous in the next slide where actually whenever I need the LM to do anything it's it's going to mostly add config by models or new config with a new task or new cluster support so it's a really really nice and easy way to just expand on your evaluation framework and just let the LLM add stuff on top and on top of it Without losing the control of what's actually going on

<center>
<a href="{static}/images/116/evals-layout.webp" target="_blank">
<img class="slide" src="{static}/images/116/evals-layout.webp" alt="LLMs write the code, but I like my things organized evals/ ├── Makefile ├── configs/ │ ├── tasks.yaml │ └── models.yaml ├── clusters/ │ └── gb10.mk ├── src/evals/tasks/ ├── logs/ └── experiments.md # make help # what to run # how to run it # where to run it # custom tasks # .eval files # every run, appended Config, not code: task × model × cluster Pin everything: dataset + model revision, seed, lab sampling One make target per action: submit, rescore, sync, view Logs are the source of truth: rescore without regenerating Experiments log: every run appends model, task, score  # configs/tasks.yaml # Zero-shot, like the model report. gsm8k_0shot: task: inspect_evals/gsm8k args: fewshot: 0 # configs/models.yaml qwen3-4b: path: Qwen/Qwen3-4B generation: temperature: 0.7 # Qwen recommendation top_p: 0.8 seed: 42 # clusters/gb10.mk MODELS_ROOT := /data/models VLLM_IMAGE := images/vllm.sif $ make submit MODEL=qwen3-4b TASK=gsm8k_0shot CLUSTER=gb10 $ make sync # logs → hf://buckets/&lt;you&gt;/evals $ make view # Inspect viewer on the tailnet" style="max-width:100%;border-radius: 2px">
</a>
</center>

One of the nicest things about Inspect is that it allows you to look at what's going on really easily. And that's powered by this Inspect Viewer, which is pretty much a website that allows you to look at traces. One of the nicest things about the Inspect Viewer and the Inspect Traces is that you can add pretty much anything to your trace. You can add PNGs, you can add audio files if you're evaluating like a language model, you can add pretty much anything. And that's a really, really powerful paradigm so that you can actually do the most important thing of all, which is looking at your data. 

<center>
<a href="{static}/images/116/audio-sample.webp" target="_blank">
<img class="slide" src="{static}/images/116/audio-sample.webp" alt="It works for anything you might be working on" style="max-width:100%;border-radius: 2px">
</a>
</center>

Finally, my final favorite thing about Inspect is that you can actually add to the same trace the original trace and also the LLM as a judge trace. So you can actually see the initial scoring and also after an LLM is a judge scored that trace, what exactly happens? And so it allows you to have this full traceability that is really, really useful. 

<center>
<a href="{static}/images/116/llm-judge.webp" target="_blank">
<img class="slide" src="{static}/images/116/llm-judge.webp" alt="LLM as a judge: the judge is in the log too" style="max-width:100%;border-radius: 2px">
</a>
</center>

Now, let's talk about lessons from running evaluations. We probably want a header here. 

The first lesson about evaluation is that not everything is what it appears to be. 
One of the recent projects I've worked on was running large language model evaluations for a model that was currently and is still currently in the works. One of the main things I tried to do is to reproduce a bunch of evaluations from open source models out there. And that's quickly, and that's the first time I realized that this is a massive shit show. And that most of the times when you look at evaluation benchmark tables, you actually have absolutely no clue what you're looking at. 

<center>
<a href="{static}/images/116/lesson-1.webp" target="_blank">
<img class="slide" src="{static}/images/116/lesson-1.webp" alt="Lesson 1: Not everything is what it appears to be Expectation • All models use the same configuration for tasks • All models use the same configuration for generation • We compare apples to apples Reality “For each question, we sample 64 times and take the average accuracy as the final score.” Qwen3 technical report, p. 13  • We ran this 64 times and took the best or average • We turned off thinking because it was looping, and removed it from the report • We use the lab’s preferred settings for generation, otherwise greedy • When we can’t parse an answer, we give the model a random letter • Our parsing assigns the first matching letter as the choice • …and the list goes on" style="max-width:100%;border-radius: 2px">
</a>
</center>

The second lesson is to look at your fucking traces. 
It's really easy to take any task and just use an LLM as a judge to evaluate that task. But what's a little bit harder than that is to actually design an LLM as judge that is actually good. I encourage you to take a second and just read this slide below and you'll understand very quickly why. 

<center>
<a href="{static}/images/116/lesson-2.webp" target="_blank">
<img class="slide" src="{static}/images/116/lesson-2.webp" alt="Lesson 2: Look at your f*cking traces" style="max-width:100%;border-radius: 2px">
</a>
</center>

The final lesson is to start small. 
I've seen this thousands of times where a team starts adding groundness, fidelity, and all of these bullshit benchmark metrics made to evaluate LLM systems and rack systems and God knows what. The problem with that is that it's very quickly overwhelming by one side because you're adding these thousands of metrics and it's completely useless because you have absolutely no clue what you're measuring. And so my advice most of the times is very simple. Start with 10 cases. 10 cases where you think your AI system might fail and measure those and then look at your choices. You'll realize that you've learned much more than throwing off-the-shelf bullshit metrics at your problem. 

<center>
<a href="{static}/images/116/lesson-3.webp" target="_blank">
<img class="slide" src="{static}/images/116/lesson-3.webp" alt="Lesson 3: Start small, don’t complicate • If your problem is challenging enough, you can start with 10 cases • Look at where things failed • Expand from that: it will help you make decisions • Don’t throw generic benchmarks or generic metrics at it • Have an internal Inspect task where you can test new models, prompts, etc." style="max-width:100%;border-radius: 2px">
</a>
</center>


If you're interested in the full slide deck, I've linked it here. 