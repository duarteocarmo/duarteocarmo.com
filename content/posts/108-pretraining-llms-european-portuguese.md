title: Ginjinha: Pre-training LLMs on European Portuguese
description: TODO
date: TODO
status: published
audio: true
thumbnail: TODO

For the past year. I've been very curious on what training a Large Language Model on European Portuguese data. I built classifiers to filter European Portuguese, and datasets that gathered a large amount of European Portuguese data. 

Now, that's all fine and dandy. But the natural next step is obvious: Can we train a Large Language Model on these datasets? Is that model any good? 

It's time to get out of the rabbit whole and show some of the work I've done for the past weeks: project Ginjinha. 

## A hacker's harness: Nanochat

A couple of years ago, Andrej Karpathy released NanoChat: a small and hackable codebase to train GPT-2 style models. It's small, easy to understand, and very hackable. Exactly what I needed. 

The first step was to adapt NanoChat to my needs. Nanochat aims to mirror the full flow of trainign LLMs, and to do so, it includes all the steps we need to train a model from start to finish. These are: 

- Pre-training: Where we train a text completion model to predict the next token
- Supervised fine-tuning (SFT): Where we further train a model to follow instructions
- Reinforcement learning (RL): Where we "align" a model, via preference tunning or verifiable rewards (getting increseasingly popular) 

Now, we could do all of these stages. But Ginjinha focus only on the first one: Pre-training. By using our Bagaco v2 dataset, how good a portuguese text completion model can we get? The result of pre-training is what is know as a "base-model". This is not a model to chat with. This is a model that is really good at completing text, and that serves as a good "base" to go into SFT and RL.

In the pre-training phase, NanoChat focuses on something called the CORE metric. The CORE metric (insert original link). The CORE metric allows us to measure how "good" a base model is at completing text.


## From CORE to PTCORE

When evaluating a base model, NanoChat uses something called the "CORE" metric. The CORE metric, is a set of evaluations designed to measure the capability of the model on downstream tasks. Currently, it's a total of 22 tasks (like ARC, HellaSwag, Big-bench, etc). For each one of these, we measure how often the model gets it right. 

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
Correct answer: B o a 
```

The CORE metric is a great way of evaluating a model - if you are building a general-purpose ChatGPT like model. But for our use case, since we are training on European Portuguese data, we are much more interested in capabilities that measure knowledge and capability around Portugal and the European Portuguese language: enter PTCORE. 

PTCORE (https://huggingface.co/datasets/duarteocarmo/ptcore-eval) is a collection of 6 tasks that look to measure the capability of base models on everything Portugal (culture + language). It leverages a lot of the recent work from the AMALIA team and a couple of other datasets I curated. Here's the full list:  

| Task | What it measures | N |
|---|---|---:|
| [SST2-PT](https://huggingface.co/datasets/duarteocarmo/ptcore-eval/viewer/sst2_pt_mini/validation) | Sentiment classification in Portuguese | 2,048 |
| [ALBA-MCQ](https://huggingface.co/datasets/duarteocarmo/ptcore-eval/viewer/alba_mcq/validation) | European Portuguese linguistics, language variety, and wordplay | 240 |
| [CulturaVivaPT](https://huggingface.co/datasets/duarteocarmo/ptcore-eval/viewer/cultura_viva_pt_mcq/validation) | Portuguese culture, places, history, and personalities | 1,000 |
| [PT Exams](https://huggingface.co/datasets/duarteocarmo/ptcore-eval/viewer/pt_exams_history_geography/validation) | History and Geography questions from Portuguese national exams | 544 |
| [SAUDADE](https://huggingface.co/datasets/duarteocarmo/ptcore-eval/viewer/saudade_pt/validation) | Temporal reasoning about Portuguese events | 8,573 |
| [OpenBookQA-PT](https://huggingface.co/datasets/duarteocarmo/ptcore-eval/viewer/openbookqa_mt_pt/validation) | Commonsense and elementary science questions translated into Portuguese | 500 |

Just like Nanochat, for each of these, we can measure two scores: The accuracy, and the centered score. The centered score is actually pretty cool: From 0-1. 0 being the same performance as random (example: 33% accuracy if mutiple choice with 3 options, gives a 0 centered score), and 1 being a perfect score. We can then also aggregate all these scores into a single PTCORE centered metric tthat goes from 0 to 1. Giving us a single number for how good a base model is on our evaluation. 

## Educational ablations

Now that we have a way of measuring how good a model is in European Portuguese, the next step was to run some ablations/experiments. How good is the Bagaco V2 dataset to pre-train language models? If we filter data by educational score (include link to another blog post) - do we see a change in the capability of the base model? 

Now - I don't work for big lab, and don't really have an H100 GPU sitting under my desk, so I neded something small. For this experiment I trained 12 small language models, each with ~75 Million paramters. Each model was trained on ~928 Million training tokens of Bagaco. For each model, I filtered the Bagaco v2 dataset at different educational scores. 

About 50 USD and 5 hours later here are the results. Task scores are centered and shown on a 0–100 scale. Values are the mean ± standard deviation across three seeds; validation BPB is not centered and lower is better:

| Filter | Seeds | SST2-PT | ALBA | Cultura Viva | History / Geo | SAUDADE | OpenBookQA-PT | PTCORE ↑ | Final val BPB ↓ |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| All scores | 3 | **24.2 ± 5.1** | 18.3 ± 3.1 | 3.3 ± 2.3 | 11.7 ± 1.1 | −2.7 ± 0.7 | 7.3 ± 1.2 | 10.4 ± 0.9 | **1.0166 ± 0.0016** |
| Score ≥1 | 3 | 21.0 ± 2.4 | 18.1 ± 0.0 | 4.0 ± 1.1 | 14.1 ± 1.6 | −1.7 ± 0.6 | 7.0 ± 0.9 | 10.4 ± 0.3 | 1.0562 ± 0.0009 |
| Score ≥2 | 3 | 23.1 ± 5.8 | **23.3 ± 1.8** | 4.9 ± 0.1 | 14.4 ± 1.8 | 2.6 ± 0.7 | **8.5 ± 0.9** | **12.8 ± 1.3** | 1.0849 ± 0.0012 |
| Score ≥3 | 3 | 16.8 ± 5.5 | 20.4 ± 1.9 | **5.8 ± 1.2** | **14.6 ± 0.8** | **4.6 ± 0.3** | 8.0 ± 0.8 | 11.7 ± 1.2 | 1.1059 ± 0.0008 |

There's a couple of interesting things about this table: 

1. Filtering the pre-training with documents with highest educational score improved the performance of the base model. But not within a certain threshold. Filtering by educational score of >= 2 performed better than filtering by >= 3. 
2. The base models that did not filter any of the data (the first row), produced the model that models language the best. This is seen by the validation BPB (validation bits per byte ~ lower is better) lower is better). Probably because it generalizes better.

Now, higher quality pre-training data creating better Language Models is not breakthrough research. This is the idea in a lot of research work like FineWeb, FineWebEDU, and even Langauge Models like Phi from Microsoft. But still, it's very interesting to see it in practice! 

## Training larger, and for longer horizons. 

During this work I tested a lot (trust me) of small language models in the bagaco dataset. More than I should have honestly. I took some time to get to experimenting in a nice and structured way.  

The two best performing models were: 
- `ginjinha_d8_ratio80_ptcore5_education_score_gte2` - PTCORE ~ 0.163 (125M params) 
- `ginjinha_d11_ratio130_ptcore5_education_score_gte1` - PTCORE ~ 0.162 (280M params)

Its interesting to see how a model that is half the size performs so well, just because we filtered the data to be higher in quality. 

These models can complete European Portuguese text to a pretty nice extent!

[Include two examples in a code block of running uv run python -m scripts.chat_pretrain \
                                             --temperature 0.8 \
                                             --top-k 40 \
                                             "O bairro de Alvalade"

With a couple of nice examples
]

Not AGI, but you can definetly see how these can actually become quite capable after some SFT and RL on top. Still, PTCORE gives us an idea of where we can go. 


## Lessons learned and Next steps

This was a fun exercise. Again - not breakthrough research. Many people already knew that better quality data results in better pre-trained models - or at least more capable ones. But doing these experiments on a limited budget really thought me how structure for experimentation matters so much. I started off with running a lot of Yolo runs - until I really thought about what I wanted to proove.Define the research goal first.

The Ginjinha project also makes me realize what an enourmous advantage labs with access to compute have. Even if I had a single H100, there are a lot of interesting things you could do with one, and you could do them much faster. Increasingly - with the rise of local AI, I'm seriously considering investing on my own compute. 

Bagaco v2 has a problem: the data quality. ~50% of the data in Bagaco v2 has an educational score of 0. Yes, you read that right. That data might be useful for some diversity in pre-training, but we need more high quality educational data. Be that synthetic, or original. 

And yes - I'm working on it. 




TODOS: 
https://huggingface.co/datasets/duarteocarmo/fineweb2-bagaco2#statistics--counts
- also - add misc session wth some other tries
- completion examples as well 
- sft and rl thoughts












































- [TABLE] The controlled D6 experiment setup
- [IMAGE] PTCORE by educational-score filter and seed
- [IMAGE] Validation BPB by educational-score filter
- [TABLE] Aggregate D6 results
- [IMAGE] The longer runs in W&B
- [TABLE] D11 model sizes, training tokens, and results

### What the Bagaço2 educational scores mean

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

