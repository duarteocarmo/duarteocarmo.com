title: AMALIA vs. smaller reasoning models
date: 2026-09-14
status: draft
thumbnail: 

<!-- TODO: Add a thumbnail. -->

A few weeks ago there was a bit of a scandal back home. People were mad that the government had taken so long to grade this year's high school exams. At the time I saw a weird post on LinkedIn saying we should hav [AMALIA](https://huggingface.co/amalia-llm) grade all those exams, and it would be much faster.

Let's be serious. Using an LLM to grade high school exams is a _horrible_ idea. But it made me think for a bit. How good would AMALIA be at taking those exams? What the author might _not know_ is that the AMALIA also thought of this: [PT Exams](https://huggingface.co/datasets/amalia-llm/pt_exams) is one of the benchmarks that the team created that tests exactly that. 2000 questions taken from high school exams - formulated as multiple choice question. 

So the question stands, how good is Amalia really at doing this? I was not particularly interested in comparing with much bigger models. I was much more interested in seeing how much smaller models perform against Amalia. And the results are quite interesting. You can navigate them on this interactives chart below. You can select the benchmark you want and see how different models compare to Amalia. 
 
If you navigate to the PT exams benchmark, you'll notice that Quin 3.52B actually beats Somalia while being about a fourth of its total parameters. 

<figure style="width:100%;max-width:700px;margin:2rem auto">
  <object
    data="{static}/images/113/intelligence.svg"
    type="image/svg+xml"
    aria-label="Portuguese benchmark intelligence"
    style="display:block;width:100%;aspect-ratio:700/520;border-radius:2px"
  >
    <a href="{static}/images/113/intelligence.svg">Open interactive chart</a>
  </object>
</figure>

If you know a thing or two about LLMs, you'll probably call my bullshit right away. Even though the other models are smaller, they're also _reasoning_ models, while AMALIA is not. They use something called test-time scaling to improve their performance (which basically means that they let the LLM output more tokens when it's time to answer the question, leading to better performance).

It's a little unfair to compare AMALIA with these models. They come from big labs, from NVIDIA to Alibaba's Qwen team. AMALIA has a smaller team, a smaller budget, and admittedly a narrower goal. Still, it's interesting to see much smaller models outperform it even on Portuguese-focused tasks.

<figure style="width:100%;max-width:700px;margin:2rem auto">
  <object
    data="{static}/images/113/frontier.svg"
    type="image/svg+xml"
    aria-label="Portuguese benchmark intelligence compared with model size and output tokens"
    style="display:block;width:100%;aspect-ratio:700/520;border-radius:2px"
  >
    <a href="{static}/images/113/frontier.svg">Open interactive chart</a>
  </object>
</figure>

But strongest reasoning models pay for that performance in output tokens. AMALIA DPO averaged about 374 output tokens per question. [LFM2.5](https://huggingface.co/LiquidAI/LFM2.5-2.6B) used 1,733, about 4.6 times as many. Qwen3.5 2B used 6,954, nearly 19 times as many. But in cases like LFM2.5, it's pretty surprising how much punch a small model can pack. That likely comes down to extensive pretraining, together with test-time scaling.


<figure style="width:100%;max-width:700px;margin:2rem auto">
  <object
    data="{static}/images/113/tokens.svg"
    type="image/svg+xml"
    aria-label="Output tokens used for the Portuguese benchmarks"
    style="display:block;width:100%;aspect-ratio:700/520;border-radius:2px"
  >
    <a href="{static}/images/113/tokens.svg">Open interactive chart</a>
  </object>
</figure>

Now, what's the takeaway? Not much. We already knew that AMALIA was an okay model, and comparing it with models from big labs isn't really fair. But comparing it with much smaller models is still interesting. I think it says something about the power of reasoning. Test-time scaling can achieve surprisingly good results, although it's obviously not the most efficient technique when it spends so many more tokens.

Still, I think this tells us what would be cool for the future of AMALIA. Could we have a much smaller model that everyone could run on their own hardware, but that still performs well in Portuguese? For now, Qwen and LFM appear to be the models closest to that. It would be really nice to have an AMALIA model that packs the same punch. To get there, though, it probably needs to change how it is trained.


