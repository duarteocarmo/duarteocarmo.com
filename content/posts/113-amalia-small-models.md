title: AMALIA vs. smaller reasoning models
date: 2026-09-14
status: draft
thumbnail: 

<!-- TODO: Add a thumbnail. -->

A few weeks ago there was a bit of a scandal back home. People were mad that [the government had taken so long to grade this year's high school exams](https://www.publico.pt/2026/07/03/sociedade/noticia/ministerio-educacao-adia-tres-dias-afixacao-notas-exames-2180378). At the time, I saw a weird post on LinkedIn saying we should have [AMALIA](https://huggingface.co/amalia-llm) grade all those exams, and it would be much faster.

Let's be serious. Using an LLM to grade high school exams is a _horrible_ idea. But it made me think for a bit. How good would AMALIA be at responding to those questions? What the author might _not know_ is that the AMALIA team also thought of this. [PT Exams](https://huggingface.co/datasets/amalia-llm/pt_exams) is one of the benchmarks the team created to test exactly that. It contains 1819 questions taken from high school exams and formatted as multiple-choice questions.

So the question stands. How good is AMALIA really at doing this? I was not particularly interested in comparing it with much bigger models. I was much more interested in seeing how smaller models perform against AMALIA. And the results are quite interesting. You can explore them in the interactive chart below. You can select the benchmark you want and see how different models compare to AMALIA.

If you navigate to the PT Exams benchmark, you'll notice that [Qwen3.5 2B](https://huggingface.co/Qwen/Qwen3.5-2B) actually beats AMALIA while having about a fourth of its total parameters.

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

If you know a thing or two about LLMs, you'll probably call my bullshit right away. Even though the other models are smaller, they're also _reasoning_ models (most - not all), while AMALIA is not. They use something called test-time scaling to improve their performance (which basically means that they let the LLM output more tokens when it's time to answer the question, leading to better performance).

It's a little unfair to compare AMALIA with these models. They come from big labs, from [NVIDIA](https://huggingface.co/nvidia) to [Alibaba's Qwen team](https://huggingface.co/Qwen). AMALIA has a smaller team, a smaller budget, and admittedly a narrower goal. Still, it's interesting to see much smaller models outperform it even on Portuguese-focused tasks.

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

But reasoning is not free. Models produce many more tokens before reaching an answer. AMALIA DPO averaged about 374 output tokens per question while [LFM2.5](https://huggingface.co/LiquidAI/LFM2.5-2.6B) used 1,733 (about 4.6x more). Qwen3.5 2B used 6,954 tokens per question, nearly 19x more. Nobody knows the complete secret of how models like LFM and Qwen achieve this performance. They are open-weight and not open source. But it will likely come down to extensive pretraining and an advanced post-training recipe. We can only speculate.


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

Now, what's the takeaway? For practical purposes, this is good news. If you're a law office and interested in a small model that can help you respond to legal questions, you might be better off starting with [Qwen3.5 4B](https://huggingface.co/Qwen/Qwen3.5-4B) than AMALIA (check [LegalBench PT](https://huggingface.co/datasets/BeatrizCanaverde/LegalBench.PT) above). It is thanks to the AMALIA team and their work that we now have something to judge these models against. 

Still, I think this tells us something interesting for the future of AMALIA. Could we have a much smaller model that everyone could run on their own hardware, but that still outperforms other smaller models? Should the next AMALIA be a reasoning model? It certainly looks like it.

---

Note: All the evaluations and code are open in [this repo](https://github.com/duarteocarmo/amelia). I adapted some of the evaluations from [AMALIA-Bench](https://github.com/AMALIA-LLM/amalia-lm-eval).

Acknowledgement: Thanks [Gonçalo](https://x.com/goncalossilva) for providing compute to make this happen!
