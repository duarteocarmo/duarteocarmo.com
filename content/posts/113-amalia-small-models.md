title: AMALIA vs. smaller reasoning models
date: 2026-09-14
status: draft
thumbnail: images/113/pt-exams-thumbnail.webp


A few weeks ago there was a bit of a scandal back home. Everyone was mad that [the government had taken so long to grade this year's high school exams](https://www.publico.pt/2026/07/03/sociedade/noticia/ministerio-educacao-adia-tres-dias-afixacao-notas-exames-2180378). At the time, I saw a weird post on LinkedIn saying we should have [AMALIA](https://huggingface.co/amalia-llm) grade all those exams because that would be faster.

Let's be serious. Using an LLM to grade high school exams is a _horrible_ idea. But it made me think for a bit. How good is AMALIA at answering those questions? What the author might _not know_ is that the AMALIA team also thought of this. [PT Exams](https://huggingface.co/datasets/amalia-llm/pt_exams) is one of the benchmarks the team created to test exactly that. It contains 1,819 questions taken from high school exams, formatted as multiple-choice questions.

The question stands. How good is AMALIA at doing this? I was not particularly interested in comparing it with much bigger/closed models. I was more interested in understanding how smaller models perform vs. AMALIA. The results are interesting. In the following interactive chart, you can see how different models perform. 

If you navigate to the PT Exams benchmark, you'll notice that [Qwen3.5 2B](https://huggingface.co/Qwen/Qwen3.5-2B) actually beats AMALIA. This is surprising. That model has a fourth(!) of AMALIA's parameters/size.

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

If you know a thing or two about LLMs, you'll probably call bullshit on this right away. Yes, the other models are smaller, but they're also _reasoning_ models (most of them), while AMALIA is _not_. They use something called [test-time scaling](https://blogs.nvidia.com/blog/ai-scaling-laws/) to improve their performance. This basically means that they let the LLM output more tokens when it's time to answer the question, leading to better performance.

You'll say it's a little unfair to compare AMALIA with these. They come from big labs, from [NVIDIA](https://huggingface.co/nvidia) to [Alibaba's Qwen team](https://huggingface.co/Qwen). AMALIA has a smaller team, a smaller budget, and admittedly a narrower goal. I agree. Still, it's interesting to see much smaller models outperform it even on Portuguese-focused tasks.

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

But reasoning is not free. Models produce many more tokens before reaching an answer. AMALIA DPO averaged about 374 output tokens per question while [LFM2.5](https://huggingface.co/LiquidAI/LFM2.5-2.6B) used 1,733 (about 4.6x more). Qwen3.5 2B used 6,954 tokens per question, nearly 19x more(!). Nobody knows the exact recipe of models like LFM and Qwen (they are open-weight, not open source). But it will likely come down to extensive pretraining (almost overtraining) and some advanced post-training recipe. We can only speculate.


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

What's the takeaway? In practice, if you work at a law office and are interested in a small model that can help you respond to legal questions, you might be better off starting with [Qwen3.5 4B](https://huggingface.co/Qwen/Qwen3.5-4B) than AMALIA (select [LegalBench PT](https://huggingface.co/datasets/BeatrizCanaverde/LegalBench.PT) above). It's thanks to the AMALIA team and their great work that we now have something to judge these models against. 

Still, I think this tells us something else that is interesting for the future of AMALIA. Could we have a much smaller model that everyone could run on their own hardware easily, but that still outperforms smaller models? Should the next AMALIA be a reasoning model? 

---

Note: All the evaluations and code are open in [this repo](https://github.com/duarteocarmo/amelia). I adapted some of the evaluations from [AMALIA-LM-eval](https://github.com/AMALIA-LLM/amalia-lm-eval).

Acknowledgement: Thanks to [Gonçalo](https://x.com/goncalossilva) for providing compute to make this happen!
