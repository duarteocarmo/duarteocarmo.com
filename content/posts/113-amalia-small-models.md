title: AMALIA and smaller reasoning models
date: 2026-09-14
status: draft
thumbnail: 

<!-- TODO: Add a thumbnail. -->

A few weeks ago there was a bit of a scandal in Portugal. People were really mad that the government had taken so long to correct this year's high school exams. Once that happened, I saw a weird post on LinkedIn saying that we have AMÁLIA now, so we should just throw all the Portuguese exams at it and let it correct them, somehow arguing that this would be a good idea.

Let's be serious. Using an LLM to correct high school exams is a horrible idea, at least with where the technology stands today. But that piqued my interest. Is AMÁLIA actually the best model at Portuguese high school exams? What the author might not know is that the AMÁLIA team released not only the model, but also several benchmarks and evaluations that test how good models are in Portuguese. One of them is called PT Exams, and it tests exactly that: how well a model performs on questions from Portuguese high school exams.

So I decided to compare AMÁLIA with a bunch of smaller models. The results were a bit surprising. AMÁLIA isn't the best performer when compared with models that are much smaller. Some, like Qwen3.5 2B, have less than a quarter of AMÁLIA's 9 billion parameters and perform better.


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

If you know a thing or two about LLMs, you'll probably call my bullshit by now. Even though the models I compared AMÁLIA with are much smaller, they're reasoning models. They use something called test-time scaling to improve their performance. This basically means that we let the LLM babble and produce more text for longer, and eventually the scores improve. I also tested some non-reasoning variants, but the reasoning variants perform really well.

Of course, it's a little unfair to compare AMÁLIA with these models. They come from big labs, from NVIDIA to Alibaba's Qwen team. AMÁLIA has a smaller team, a smaller budget, and admittedly a narrower goal. Still, it's interesting to see much smaller models outperform it even on Portuguese-focused tasks.

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

The catch here is obvious. These models use many more tokens to achieve that performance. They think for a long while, so you have to wait much longer for the results. But in cases like the LFM model, it's pretty surprising how much punch a small model can pack. That likely comes down to extensive pretraining, together with test-time scaling.


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

Now, what's the takeaway? Not much. We already knew that AMÁLIA was an okay model, and comparing it with models from big labs isn't really fair. But comparing it with much smaller models is still interesting. I think it says something about the power of reasoning. Test-time scaling can achieve surprisingly good results, although it's obviously not the most efficient technique when it spends so many more tokens.

Still, I think this tells us what would be cool for the future of AMÁLIA. Could we have a much smaller model that everyone could run on their own hardware, but that still performs well in Portuguese? For now, Qwen and LFM appear to be the models closest to that. It would be really nice to have an AMÁLIA model that packs the same punch. To get there, though, it probably needs to change how it is trained.


