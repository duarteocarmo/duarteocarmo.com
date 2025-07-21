title: A Benchmark for language models on European Portuguese
description: Creating European Portuguese benchmarks for EuroEval. Because European Portuguese evaluation needs European Portuguese data
date: 21st of July 2025
status: published
thumbnail: images/82/cover.png


<div class="iframe-container">
  <iframe
    scrolling="no"
    id="euroeval-frame"
    src="{static}/html/pt-euroeval.html"
    title="EuroEval European Portuguese Benchmarks"
    loading="lazy">
  </iframe>
</div>

<style>
  .iframe-container {
    width: 100%;
    max-width: 800px;
    margin: 2rem auto;
    text-align: center;
  }
  
  #euroeval-frame {
    width: 100%;
    height: 500px;
    border: none;
    display: block;
    box-sizing: border-box;
  }
  
  @media (max-width: 768px) {
    #euroeval-frame {
      height: 450px;
    }
  }
  
  @media (max-width: 480px) {
    #euroeval-frame {
      height: 350px;
    }
  }
</style>






A couple of weeks ago in Lisbon, I went to a friend's birthday dinner. In front of me sat someone that recently started working for the Portuguese government where they focus on modernization and technology. It's not everyday that I talk to someone that works for the Portuguese government in an area similar to mine, so I was very curious. I asked about the [AMÁLIA](https://www.it.pt/News/NewsPost/5065) project. The 5.5 Million Euro project about creating a new LLM *specifically* designed for Portuguese. 

The first beta release of AMÁLIA is scheduled for the [first trimester of 2025](https://www.portugal.gov.pt/pt/gc24/comunicacao/noticia?i=modelo-de-linguagem-em-grande-escala-para-a-lingua-portuguesa), but I've heard little news about it. Still I asked: "Are you pre-training it? Or are you fine-tuning something that is already out there?". "No, we're training from scratch." the person told me. "Really, what's the point of that?" I asked, but did not get a clear reply. But the question stuck in my mind. What's the goal? To show Portugal is capable of pre-training a model from scratch? To build a model that is *specifically* really good at Portuguese? [ref]Other countries like Italy have done this - [See Minerva](https://minerva-ai.org/). They also spend 5M, [but from EU funds](https://eurohpc-ju.europa.eu/advancing-ai-eurohpc-minerva-project-2025-02-13_en) afaik[/ref]

## The problem: Shooting in the dark

Let's assume the goal is to build a model that is *really good* at Portuguese, and that the Portuguese state is really not interested in "showing we are capable of training models" (we have [bigger problems](https://www.theguardian.com/commentisfree/2025/jun/25/lisbon-europe-portugal-golden-visa-capital-investors-short-term-rentals)). If we assume that, the first thing I would do would actually be to **measure how good language models are at speaking Portuguese**. 

Portuguese is a popular language, it's the **8th** most spoken language in the world. But it comes in [flavors](https://en.wikipedia.org/wiki/Portuguese-speaking_world). Portuguese spoken in Brazil (82% of native speakers) is quite different from Portuguese from Portugal (4% of speakers). A common complaint from people in Portugal is that the models often reply in "Brazilian" Portuguese. The difference is not only about the pronunciation: a lot of the vocabulary, verbs, and conjugations are different.

Let's take Llama 3. It [was trained](https://scontent-cph2-1.xx.fbcdn.net/v/t39.2365-6/468347782_9231729823505907_4580471254289036098_n.pdf?_nc_cat=110&ccb=1-7&_nc_sid=3c67a6&_nc_ohc=MN9Qsqv_WlwQ7kNvwFzR-jm&_nc_oc=Adl-itXHUl8EqL_TJpicf2-H5wTmlDZO7zwWJkSwPs1eFM7cXlQzA1ddUZSIonQnPxI&_nc_zt=14&_nc_ht=scontent-cph2-1.xx&_nc_gid=r6Z1jsaqV629vM4DSY2Iag&oh=00_AfQPdfe0Ubcu4_kec6ttGpTvvtA2MNJeEJZ7_xzT3SJMFg&oe=6882A3C0) on 8% multilingual data. If we assume 2% of that was Portuguese, and if we assume 5% of that is European Portuguese, then only **0.008%** of the data Llama saw was European Portuguese. That's not a lot. But under representation is a common issue.

## European Portuguese on EuroEval

Denmark has a similar problem, and I knew Dan Nielsen at [The Alexandra Institute](https://alexandra.dk/) worked on something called [ScandEval](https://arxiv.org/pdf/2304.00906) where he evaluated the performance of language models across different Scandinavian languages. I was surprised to see the project evolved into something more general: [EuroEval](https://euroeval.com/). 

EuroEval, is similar to ScandEval - but for all European languages. And you want to guess the one that *was* missing? Yes, Portuguese.

Over a couple of weeks, [we put together](https://github.com/EuroEval/EuroEval/issues/1040)[ref]Thanks [Dan](https://www.saattrupdan.com/) for all the help in making this happen![/ref] a collection of datasets to evaluate the performance of language models in in European Portuguese. We also did some extra work to ensure that the data is *exclusively* Portuguese from Portugal. 

Here are the datasets we put together:

- **Sentiment Classification** ([SST2-PT](https://huggingface.co/datasets/duarteocarmo/sst2-pt-mini)): Part of the work from the [ExtraGLUE](https://arxiv.org/abs/2404.05333) project. A sentiment analysis dataset built using machine translation (DeepL). 
- **Named Entity Recognition** ([HAREM](https://huggingface.co/datasets/duarteocarmo/harem)): Part of the work from the [HAREM project](https://www.linguateca.pt/harem/). We filter by entries where the origin is PT - to create an NER dataset.
- **Linguistic Acceptability** ([ScaLA-pt](https://huggingface.co/datasets/duarteocarmo/scala-pt)): Based on [Portuguese-Bosque treebank](https://universaldependencies.org/treebanks/pt_bosque/index.html), filtered by entries from [CETEMPúblico](https://www.linguateca.pt/cetempublico/). Created by corrupting grammatically correct sentences.
- **Reading Comprehension** ([BoolQ-PT](https://huggingface.co/datasets/duarteocarmo/boolq-pt)): Also part of the [ExtraGlue](https://arxiv.org/abs/2404.05333) work. Adapted by taking the original passage, question, and yes/no options, and turning it into a Q/A style question where the model can answer yes or no.
- **Knowledge** ([MMLU-pt](https://huggingface.co/datasets/duarteocarmo/mmlu-pt-mini)): Based on [this paper](https://arxiv.org/abs/2410.08928). Already included entries specifically for Portuguese from Portugal. 
- **Common-sense Reasoning** ([GoldenSwag-pt](https://huggingface.co/datasets/duarteocarmo/goldenswag-pt-mini)): High quality filtered samples from the [HellaSwag dataset](https://aclanthology.org/P19-1472/). Also machine translated with DeepL for European Portuguese.
- **Summarization** ([Publico](https://huggingface.co/datasets/duarteocarmo/publico-mini)): Filtered the [CCNews corpus](https://commoncrawl.org/blog/news-dataset-available) for entries where the url matched [Público](https://www.publico.pt/). Transformed into summarization dataset by extracting the first two sentences as the summary (a common trick).

I you want to look at some samples, [I published the datasets on HuggingFace](https://huggingface.co/duarteocarmo). You can also read the extensive descriptions on the [EuroEval docs](https://euroeval.com/datasets/portuguese/).

## Running benchmarks for European Portuguese

While Dan is working on the general leaderboard, I ran some benchmarks on my own which you saw on top of this blog post or [in this link](/html/pt-euroeval.html). I selected some models I was curious about within 3 "categories": Large, Small, and things I can run on my laptop without the fan coming on. 

If you're curious about how a particular model performs that I (or Dan) didn't benchmark, you can also run them yourself (assuming you have [uv](https://docs.astral.sh/uv/getting-started/installation/) installed):

```bash
$ uvx --with euroeval euroeval \
    --model ollama_chat/smollm2:135m \
    --task sentiment-classification \
    --language pt
```

Set the `--model` flag to any model that [LiteLLM](https://docs.litellm.ai/docs/providers) supports.

The reality of building these benchmarks is a clear realization: European Portuguese is an unpopular language. Brazilian Portuguese is simply a much more popular version of the language. Still, there is value in building benchmarks focused on the European variant. And it was a lot of fun tracking/building these datasets. I expect to do some more work in this area. 

And I *don't* know if investing 5.5M Euro in developing a Portuguese Language Model is a good idea. But there's one thing I do know: Whenever that model comes out, we are now in a *much* better position to say if it hit the mark. Or if it didn't.


----

*Note: The benchmarks above are preliminary. For the official ones keep an eye on [EuroEval Leaderboards](https://euroeval.com/leaderboards/)*




