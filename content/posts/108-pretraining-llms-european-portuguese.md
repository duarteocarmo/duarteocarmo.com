title: Ginjinha: Pretraining LLMs on European Portuguese
description: TODO
date: TODO
status: published
audio: true
thumbnail: TODO

For the past year, I've been very curious about training a Large Language Model on European Portuguese data. I built [classifiers to filter European Portuguese]({filename}/posts/98-fasttext-vs-bert-portuguese.md) and [datasets that gathered a large amount of European Portuguese data]({filename}/posts/103-bagacov2-dataset.md).

Now, that's all fine and dandy. But the natural next step is obvious: Can we train a Large Language Model on these datasets? Is that model any good?

It's time to get out of the rabbit hole and show some of the work I've done over the past few weeks: project Ginjinha.

## A hacker's harness: NanoChat

In 2025, Andrej Karpathy released [NanoChat](https://github.com/karpathy/nanochat): a small and hackable codebase to train GPT-2-style models. It's small, easy to understand, and very hackable. Exactly what I needed.

The first step was to adapt [NanoChat](https://github.com/duarteocarmo/nanochat) to my needs. NanoChat aims to mirror the full flow of training LLMs and includes all the steps we need to train a model from start to finish. These are:

- **Pretraining:** Where we train a text-completion model to predict the next token.
- **Supervised fine-tuning (SFT):** Where we further train a model to follow instructions.
- **Reinforcement learning (RL):** Where we "align" a model via preference tuning or verifiable rewards (which are getting increasingly popular).

Now, we could do all of these stages. But Ginjinha focuses only on the first one: pretraining. Using our [Bagaço v2 dataset](https://huggingface.co/datasets/duarteocarmo/fineweb2-bagaco2), how good a Portuguese text-completion model can we get? The result of pretraining is what is known as a "base model". This is not a model to chat with. This is a model that is really good at completing text and serves as a good "base" for SFT and RL.

In the pretraining phase, NanoChat focuses on something called the [CORE metric](https://arxiv.org/abs/2406.11794). The CORE metric allows us to measure how "good" a base model is at completing text.


## From CORE to PTCORE

When evaluating a base model, NanoChat uses the [CORE metric](https://arxiv.org/abs/2406.11794), a set of evaluations designed to measure the capability of the model on downstream tasks. Currently, there are 22 tasks, like [ARC](https://arxiv.org/abs/1803.05457), [HellaSwag](https://arxiv.org/abs/1905.07830), and [BIG-bench](https://arxiv.org/abs/2206.04615). For each one, we measure how often the model gets it right.

For example:

```text
Question:
Qual dos dois acontecimentos sobre Fortios ocorreu primeiro?

Candidate completions:
A. Registo populacional de 1785 habitantes em Fortios
   → average loss: 1.76
B. Fortios foi desanexada da freguesia de São Lourenço
   → average loss: 1.12

Prediction: B (lowest loss)
Correct answer: B ✓
```

The CORE metric is a great way of evaluating a model—if you are building a general-purpose ChatGPT-like model. But for our use case, since we are training on European Portuguese data, we are much more interested in capabilities that measure knowledge about Portugal and the European Portuguese language: enter PTCORE.

[PTCORE](https://huggingface.co/datasets/duarteocarmo/ptcore-eval) is a collection of six tasks that aim to measure the capability of base models on everything related to Portugal (culture + language). It leverages a lot of the recent work from the [AMÁLIA team]({filename}/posts/101-AMALIA-portuguese-llm.md) and a couple of other datasets I curated. Here's the full list:

| Task | What it measures | N |
|---|---|---:|
| [SST2-PT](https://huggingface.co/datasets/duarteocarmo/ptcore-eval/viewer/sst2_pt_mini/validation) | Sentiment classification in Portuguese | 2,048 |
| [ALBA-MCQ](https://huggingface.co/datasets/duarteocarmo/ptcore-eval/viewer/alba_mcq/validation) | European Portuguese linguistics, language variety, and wordplay | 240 |
| [CulturaVivaPT](https://huggingface.co/datasets/duarteocarmo/ptcore-eval/viewer/cultura_viva_pt_mcq/validation) | Portuguese culture, places, history, and personalities | 1,000 |
| [PT Exams](https://huggingface.co/datasets/duarteocarmo/ptcore-eval/viewer/pt_exams_history_geography/validation) | History and Geography questions from Portuguese national exams | 544 |
| [SAUDADE](https://huggingface.co/datasets/duarteocarmo/ptcore-eval/viewer/saudade_pt/validation) | Temporal reasoning about Portuguese events | 8,573 |
| [OpenBookQA-PT](https://huggingface.co/datasets/duarteocarmo/ptcore-eval/viewer/openbookqa_mt_pt/validation) | Commonsense and elementary science questions translated into Portuguese | 500 |

Just like CORE, for each of these, we can measure two scores: accuracy and the centered score. The centered score is actually pretty cool: it goes from 0 to 1, with 0 being the same performance as random (for example, 33% accuracy on a multiple-choice question with three options gives a centered score of 0) and 1 being a perfect score. We can then aggregate all these scores into a single [PTCORE centered metric](https://github.com/duarteocarmo/nanochat/blob/master/nanochat/ptcore_eval.py) that goes from 0 to 1, giving us a single number for how good a base model is on our evaluation.

## Educational ablations

Now that we have a way of measuring how good a model is in European Portuguese, the next step was to run some ablations and experiments. How good is the Bagaço v2 dataset for pretraining language models? If we filter data by [educational score]({filename}/posts/96-bagaco-dataset.md), do we see a change in the capability of the base model?

Now, I don't work for a big lab and don't really have an H100 GPU sitting under my desk, so I needed something small. For this experiment, I trained 12 small language models, each with approximately 75 million parameters and approximately 928 million Bagaço v2 training tokens. I trained four groups of models, using a different educational-score threshold for each group.

About $50 and five hours later, here are the results. Task scores are centered and shown on a 0–100 scale. Values are the mean ± standard deviation across three seeds; validation BPB is not centered, and lower is better:

| Filter | Seeds | SST2-PT | ALBA | Cultura Viva | History / Geo | SAUDADE | OpenBookQA-PT | PTCORE ↑ | Final val BPB ↓ |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| All scores | 3 | **24.2 ± 5.1** | 18.3 ± 3.1 | 3.3 ± 2.3 | 11.7 ± 1.1 | −2.7 ± 0.7 | 7.3 ± 1.2 | 10.4 ± 0.9 | **1.0166 ± 0.0016** |
| Score ≥1 | 3 | 21.0 ± 2.4 | 18.1 ± 0.0 | 4.0 ± 1.1 | 14.1 ± 1.6 | −1.7 ± 0.6 | 7.0 ± 0.9 | 10.4 ± 0.3 | 1.0562 ± 0.0009 |
| Score ≥2 | 3 | 23.1 ± 5.8 | **23.3 ± 1.8** | 4.9 ± 0.1 | 14.4 ± 1.8 | 2.6 ± 0.7 | **8.5 ± 0.9** | **12.8 ± 1.3** | 1.0849 ± 0.0012 |
| Score ≥3 | 3 | 16.8 ± 5.5 | 20.4 ± 1.9 | **5.8 ± 1.2** | **14.6 ± 0.8** | **4.6 ± 0.3** | 8.0 ± 0.8 | 11.7 ± 1.2 | 1.1059 ± 0.0008 |

There are a couple of interesting things about this table:

1. Filtering the pretraining data to documents with higher educational scores improved the performance of the base model, but only up to a certain threshold. Filtering by an educational score of ≥2 performed better than filtering by ≥3.
2. The base models trained without filtering any of the data (the first row) modeled language best. We can see this in the validation BPB (validation bits per byte—lower is better). This is probably because they generalize better.

Now, the fact that higher-quality pretraining data creates better language models is not breakthrough research. This is the idea behind a lot of research work, such as [FineWeb and FineWeb-Edu](https://arxiv.org/abs/2406.17557), and even language models such as Microsoft's [Phi](https://arxiv.org/abs/2306.11644). Still, it's very interesting to see it in practice!

## Training larger and for longer

During this work, I tested a lot (trust me) of small language models on the Bagaço v2 dataset. More than I should have, honestly. It took me some time to start experimenting in a nice, structured way.

The two best-performing models were:

- [`ginjinha_d8_ratio80_ptcore5_education_score_gte2`](https://huggingface.co/duarteocarmo/ginjinha/tree/main/ginjinha_d8_ratio80_ptcore5_education_score_gte2) — PTCORE ≈ 0.163 (125M parameters)
- [`ginjinha_d11_ratio130_ptcore5_education_score_gte1`](https://huggingface.co/duarteocarmo/ginjinha/tree/main/ginjinha_d11_ratio130_ptcore5_education_score_gte1) — PTCORE ≈ 0.162 (280M parameters)

It's interesting to see how a model that is half the size performs so well, just because we filtered the data to be higher quality. You can find the models and evaluation results in the [Ginjinha repository](https://huggingface.co/duarteocarmo/ginjinha).

These models can complete European Portuguese text pretty well!

[TODO: Include two completion examples generated with:

```bash
uv run python -m scripts.chat_pretrain \
    --temperature 0.8 \
    --top-k 40 \
    "O bairro de Alvalade"
```
]

Not AGI, but you can definitely see how these can actually become quite capable after some SFT and RL on top. Still, PTCORE gives us an idea of where we can go.


## Lessons learned and next steps

This was a fun exercise. Again—not breakthrough research. Many people already knew that better-quality data results in better pretrained models—or at least more capable ones. But doing these experiments on a limited budget really taught me how much a structured approach to experimentation matters. I started off with a lot of YOLO runs—until I really thought about what I wanted to prove. Define the research goal first.

The Ginjinha project also made me realize what an enormous advantage labs with access to compute have. If I had even a single H100, there are a lot of interesting things I could do with it, and I could do them much faster. With the rise of local AI, I'm increasingly considering investing in my own compute.

Bagaço v2 has a problem: data quality. Approximately [50% of the data in Bagaço v2 has an educational score of 0](https://huggingface.co/datasets/duarteocarmo/fineweb2-bagaco2#statistics--counts). Yes, you read that right. That data might be useful for some diversity in pretraining, but we need more high-quality educational data, whether synthetic or original.

And yes—I'm working on it.




TODO:
- Add a miscellaneous section with other experiments.
- Add completion examples.
- Add thoughts on SFT and RL.












































- [TABLE] The controlled D6 experiment setup
- [IMAGE] PTCORE by educational-score filter and seed
- [IMAGE] Validation BPB by educational-score filter
- [TABLE] Aggregate D6 results
- [IMAGE] The longer runs in W&B
- [TABLE] D11 model sizes, training tokens, and results

### What the Bagaço v2 educational scores mean

The labels use the additive rubric documented in the original Bagaço dataset and adapted from FineWeb-Edu: a document receives another point each time it satisfies a stricter educational-quality criterion.

| Score | Meaning |
|---:|---|
| 0 | No meaningful educational information |
| 1 | Some basic educational information, but mostly promotional, irrelevant, or poorly suited to teaching |
| 2 | Potentially useful educational material, but superficial, disorganized, or mixed with non-educational content |
| 3 | Coherent and appropriate for education, introducing curriculum-relevant concepts, but incomplete or containing some irrelevant material |
| 4 | Highly relevant, clear, focused, and substantial educational content suitable for structured learning |
| 5 | Outstanding educational material, perfectly suited to teaching, with detailed reasoning and thorough explanations |

In practice, none of the 30,000 reference annotations received a 5, so the trained classifier effectively produces scores from 0 to 4.

*Source: [Bagaço educational-score rubric](https://huggingface.co/datasets/duarteocarmo/fineweb2-bagaco#educational-score).*

