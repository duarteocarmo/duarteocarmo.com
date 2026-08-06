title: Ginjinha: Pretraining LLMs on European Portuguese
description: Training small European Portuguese base models with NanoChat, Bagaço v2, and PTCORE.
date: 6th August 2026
status: published
audio: true
thumbnail: images/108/wandb-pt-exams-evolution.webp
toc: true

<center>
<a href="{static}/images/108/wandb-pt-exams-evolution.webp" target="_blank">
<img src="{static}/images/108/wandb-pt-exams-evolution.webp" alt="Portuguese History and Geography exam accuracy during pretraining for three Ginjinha runs" style="max-width:100%;border-radius: 2px">
</a>
</center>

For the past year, I've been very curious about the intersection of Large Language Models (LLMs) and the European Portuguese language. I've built [evaluations]({filename}/posts/82-benchmark-llms-european-portuguese.md), [classifiers]({filename}/posts/98-fasttext-vs-bert-portuguese.md), and eventually [the largest pretraining dataset in European Portuguese]({filename}/posts/103-bagacov2-dataset.md).

Now, that's all fine and dandy, but it raises the obvious question: Can we pretrain an LLM fully in European Portuguese? And is it any good?

Welcome to project Ginjinha.

But before we start training models, we need a harness.

## A pretraining harness: NanoChat

In 2025, Andrej Karpathy released [NanoChat](https://github.com/karpathy/nanochat): a small, hackable codebase for training GPT-2-style language models. It's easy to understand and modify. Exactly what I needed.

The first step was to adapt it to Ginjinha ([code](https://github.com/duarteocarmo/nanochat)). NanoChat includes the three key stages of training LLMs:

- **Pretraining:** We train a text-completion model to predict the next token.
- **Supervised fine-tuning (SFT):** We further train the model to follow instructions (i.e., chat).
- **Reinforcement learning (RL):** We "align" the model through preference tuning or verifiable rewards (very hyped nowadays).

We could do all of these, provided we had the data. But Bagaço v2 is a pretraining dataset, so we are only interested in the first stage here. If we use Bagaço to pretrain an LLM, how good a model can we get?

To measure how good a base model is, NanoChat uses something called the CORE metric.

## From CORE to PTCORE

The CORE metric is an evaluation suite designed to measure the capability of a language model on downstream tasks. For CORE, there are 22 tasks. These tasks are things like [ARC](https://arxiv.org/abs/1803.05457), [HellaSwag](https://arxiv.org/abs/1905.07830), and [BIG-bench](https://arxiv.org/abs/2206.04615). Each one is made up of questions (usually multiple choice). We take each answer and measure the loss that the model assigns to it. If the correct answer gets the lowest loss, we consider the model answered correctly.

A trivial example:

```text
Question:
What is the capital of Le Marche?

Candidate completions:
A. Camerano
   → average loss: 1.76
B. Ancona
   → average loss: 1.12

Prediction: B (lowest loss)
Correct answer: B ✓
```

The CORE metric is a great way to evaluate a model if you are building a general-purpose LLM (think ChatGPT).

For our use case, since we're training on European Portuguese data, we're interested in capabilities that measure knowledge of Portugal and the Portuguese language: enter **PTCORE**.

<center>
<a href="{static}/images/108/ptcore-vs-training-tokens.webp" target="_blank">
<img src="{static}/images/108/ptcore-vs-training-tokens.webp" alt="PTCORE compared with training tokens across all Ginjinha runs" style="max-width:100%;border-radius: 2px">
</a>
<figcaption>PTCORE across training budgets. Bubble size represents the model's total number of parameters.</figcaption>
</center>

[PTCORE](https://huggingface.co/datasets/duarteocarmo/ptcore-eval) is a collection of six tasks that measure the capabilities of base models across Portuguese language and culture (e.g., think CORE for Portuguese). It draws on recent work from the [AMÁLIA team]({filename}/posts/101-AMALIA-portuguese-llm.md) and a couple of other datasets I curated. Here's the full list:


| Task | What it measures | Examples |
|---|---|---:|
| [SST2-PT](https://huggingface.co/datasets/duarteocarmo/ptcore-eval/viewer/sst2_pt_mini/validation) | Sentiment classification in Portuguese | 2,048 |
| [ALBA-MCQ](https://huggingface.co/datasets/duarteocarmo/ptcore-eval/viewer/alba_mcq/validation) | European Portuguese linguistics, language variety, and wordplay | 240 |
| [CulturaVivaPT](https://huggingface.co/datasets/duarteocarmo/ptcore-eval/viewer/cultura_viva_pt_mcq/validation) | Portuguese culture, places, history, and personalities | 1,000 |
| [PT Exams](https://huggingface.co/datasets/duarteocarmo/ptcore-eval/viewer/pt_exams_history_geography/validation) | History and Geography questions from Portuguese national exams | 544 |
| [SAUDADE](https://huggingface.co/datasets/duarteocarmo/ptcore-eval/viewer/saudade_pt/validation) | Temporal reasoning about Portuguese events | 8,573 |
| [OpenBookQA-PT](https://huggingface.co/datasets/duarteocarmo/ptcore-eval/viewer/openbookqa_mt_pt/validation) | Commonsense and elementary science questions translated into Portuguese | 500 |


And here's an example question from the `SAUDADE` task:

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

For each task, we can measure two scores: accuracy and a centered score. Accuracy is self-explanatory: how many questions the model got right. The centered score is a bit more interesting: 0 means random performance (for example, 33% accuracy on a multiple-choice question with three options gives 0), while 1 is a perfect score. Scores below 0 indicate worse-than-random performance. We can then aggregate the centered scores for each task, giving us a single number—the PTCORE score—for a base model.

## Educational ablations

Now that we have a way of measuring how good a model is at European Portuguese, the next step was to run some experiments: How good is the Bagaço v2 dataset for pretraining language models? If we filter data by [educational score]({filename}/posts/96-bagaco-dataset.md), do we see a change in the capability of the base model?

If you remember, every document in the Bagaço v2 dataset has an educational score associated with it:

<details style="margin:1rem 0">
  <summary style="cursor:pointer;font-weight:600">Expand the educational-score rubric</summary>
  <div class="table-scroll">
    <table>
      <thead><tr><th>Score</th><th>Meaning</th></tr></thead>
      <tbody>
        <tr><td>0</td><td>No meaningful educational information</td></tr>
        <tr><td>1</td><td>Some basic educational information, but mostly promotional, irrelevant, or poorly suited to teaching</td></tr>
        <tr><td>2</td><td>Potentially useful educational material, but superficial, disorganized, or mixed with non-educational content</td></tr>
        <tr><td>3</td><td>Coherent and appropriate for education, introducing curriculum-relevant concepts, but incomplete or containing some irrelevant material</td></tr>
        <tr><td>4</td><td>Highly relevant, clear, focused, and substantial educational content suitable for structured learning</td></tr>
        <tr><td>5</td><td>Outstanding educational material, perfectly suited to teaching, with detailed reasoning and thorough explanations</td></tr>
      </tbody>
    </table>
  </div>
</details>

I don't work for a big lab and don't have an H100 GPU sitting under my desk, so I wanted to run an experiment that wouldn't cost thousands of dollars. I trained 12 small language models of around 73 million parameters each:

| Setup | Value |
|---|---:|
| Depth | D6 |
| Total parameters | 73.53M |
| Training tokens | 927.99M |
| Seeds | 42 · 1337 · 2026 |
| Filters | All · ≥1 · ≥2 · ≥3 |

About $50 and five hours later, I had the results. For each filter, we get a PTCORE score and a validation BPB (bits per byte, lower is better). PTCORE is shown as a percentage, and each value is the mean ± standard deviation across three seeds. You can also expand the full task-level table to see every individual run.

| Filter | PTCORE (%) ↑ | Final validation BPB ↓ |
|---|---:|---:|
| All scores | 10.4 ± 0.9 | **1.0166 ± 0.0016** |
| Score ≥1 | 10.4 ± 0.3 | 1.0562 ± 0.0009 |
| Score ≥2 | **12.8 ± 1.3** | 1.0849 ± 0.0012 |
| Score ≥3 | 11.7 ± 1.2 | 1.1059 ± 0.0008 |


<details>
  <summary>Expand all D6 task scores</summary>
  <center>
  <a href="{static}/images/108/d6-task-results.webp" target="_blank">
  <img src="{static}/images/108/d6-task-results.webp" alt="PTCORE task scores for all 12 D6 educational-filter runs" style="max-width:100%;border-radius: 2px">
  </a>
  <figcaption>All 12 matched D6 runs. Bold marks the best result for each seed and the best mean for each task. Click to expand.</figcaption>
  </center>
</details>


Two interesting findings:

1. Filtering the pretraining data for documents with higher educational scores improved the base model's performance, but only up to a certain threshold. Filtering by ≥2 performed better than filtering by ≥3.
2. The base models trained without filtering (the first row) achieved the lowest validation BPB. This likely reflects how closely the unfiltered training data matches the validation distribution.

The idea that higher-quality pretraining data creates better language models is not groundbreaking. It's shown in research such as [FineWeb and FineWeb-Edu](https://arxiv.org/abs/2406.17557), as well as models such as Microsoft's [Phi](https://arxiv.org/abs/2306.11644). Still, it's very interesting to see it in practice!

The best base model will need to balance both PTCORE score and validation BPB (quality AND ability to model language).

## Training larger and for longer

During this work, I trained and tested a lot of small language models on the Bagaço dataset. More than I should have, to be very honest.

The two highest-scoring runs were:

- [`ginjinha_d8_ratio80_ptcore5_education_score_gte2`](https://huggingface.co/duarteocarmo/ginjinha/tree/main/ginjinha_d8_ratio80_ptcore5_education_score_gte2) — PTCORE ≈ 0.163 (126M parameters @ 80 tokens per scaling param)
- [`ginjinha_d11_ratio130_ptcore5_education_score_gte1`](https://huggingface.co/duarteocarmo/ginjinha/tree/main/ginjinha_d11_ratio130_ptcore5_education_score_gte1) — PTCORE ≈ 0.162 (279M parameters @ 130 tokens per scaling param)

It's interesting to see a model half the size perform just as well. Filtering the pretraining data can help smaller models close the gap. [For reference, I stored all the Ginjinha runs in this repository](https://huggingface.co/duarteocarmo/ginjinha).


<center>
<a href="{static}/images/108/wandb-ptcore-metric-evolution.webp" target="_blank">
<img src="{static}/images/108/wandb-ptcore-metric-evolution.webp" alt="Earlier five-task PTCORE metric during pretraining for three Ginjinha runs" style="max-width:100%;border-radius: 2px">
</a>
<figcaption>This is an earlier, pretty unstable PTCORE metric. The 126M-parameter runs have the same training budget.</figcaption>
</center>

Here are all 22 runs, sorted by PTCORE. Click an available model to open its weights and evaluation files.

<details style="margin:1rem 0">
  <summary style="cursor:pointer;font-weight:600">Expand all Ginjinha runs</summary>
  <div class="table-scroll">
    <table>
      <thead><tr><th>Tokens</th><th>Total parameters</th><th>Filter</th><th>Model</th><th>PTCORE</th></tr></thead>
      <tbody>
        <tr><td>3.355B</td><td>125.829M</td><td>≥2</td><td><a href="https://huggingface.co/duarteocarmo/ginjinha/tree/main/ginjinha_d8_ratio80_ptcore5_education_score_gte2"><code>D8 · ratio 80</code></a></td><td>0.163</td></tr>
        <tr><td>13.393B</td><td>279.184M</td><td>≥1</td><td><a href="https://huggingface.co/duarteocarmo/ginjinha/tree/main/ginjinha_d11_ratio130_ptcore5_education_score_gte1"><code>D11 · ratio 130</code></a></td><td>0.162</td></tr>
        <tr><td>1.678B</td><td>125.829M</td><td>≥3</td><td><a href="https://huggingface.co/duarteocarmo/ginjinha/tree/main/ginjinha_d8_ratio40_ptcore5_education_score_gte3"><code>D8 · ratio 40</code></a></td><td>0.154</td></tr>
        <tr><td>9.787B</td><td>279.184M</td><td>≥1</td><td><a href="https://huggingface.co/duarteocarmo/ginjinha/tree/main/ginjinha_d11_ratio95_ptcore5_education_score_gte1"><code>D11 · ratio 95</code></a></td><td>0.150</td></tr>
        <tr><td>927.99M</td><td>73.532M</td><td>≥2</td><td><a href="https://huggingface.co/duarteocarmo/ginjinha/tree/main/ginjinha_d6_ratio40_education_score_gte2_seed42"><code>D6 · ratio 40 · seed 42</code></a></td><td>0.140</td></tr>
        <tr><td>1.678B</td><td>125.829M</td><td>≥1</td><td><a href="https://huggingface.co/duarteocarmo/ginjinha/tree/main/ginjinha_d8_ratio40_ptcore5_education_score_gte1"><code>D8 · ratio 40</code></a></td><td>0.138</td></tr>
        <tr><td>3.355B</td><td>125.829M</td><td>≥1</td><td><a href="https://huggingface.co/duarteocarmo/ginjinha/tree/main/ginjinha_d8_ratio80_ptcore5_education_score_gte1"><code>D8 · ratio 80</code></a></td><td>0.137</td></tr>
        <tr><td>3.355B</td><td>125.829M</td><td>All</td><td><a href="https://huggingface.co/duarteocarmo/ginjinha/tree/main/ginjinha_d8_ratio80_ptcore5_education_all_scores"><code>D8 · ratio 80</code></a></td><td>0.133</td></tr>
        <tr><td>1.678B</td><td>125.829M</td><td>≥2</td><td><a href="https://huggingface.co/duarteocarmo/ginjinha/tree/main/ginjinha_d8_ratio40_ptcore5_education_score_gte2"><code>D8 · ratio 40</code></a></td><td>0.133</td></tr>
        <tr><td>927.99M</td><td>73.532M</td><td>≥2</td><td><a href="https://huggingface.co/duarteocarmo/ginjinha/tree/main/ginjinha_d6_ratio40_education_score_gte2_seed1337"><code>D6 · ratio 40 · seed 1337</code></a></td><td>0.131</td></tr>
        <tr><td>927.99M</td><td>73.532M</td><td>≥3</td><td><a href="https://huggingface.co/duarteocarmo/ginjinha/tree/main/ginjinha_d6_ratio40_education_score_gte3_seed2026"><code>D6 · ratio 40 · seed 2026</code></a></td><td>0.130</td></tr>
        <tr><td>927.99M</td><td>73.532M</td><td>≥3</td><td><a href="https://huggingface.co/duarteocarmo/ginjinha/tree/main/ginjinha_d6_ratio40_education_score_gte3_seed42"><code>D6 · ratio 40 · seed 42</code></a></td><td>0.114</td></tr>
        <tr><td>927.99M</td><td>73.532M</td><td>≥2</td><td><a href="https://huggingface.co/duarteocarmo/ginjinha/tree/main/ginjinha_d6_ratio40_education_score_gte2_seed2026"><code>D6 · ratio 40 · seed 2026</code></a></td><td>0.114</td></tr>
        <tr><td>927.99M</td><td>73.532M</td><td>All</td><td><a href="https://huggingface.co/duarteocarmo/ginjinha/tree/main/ginjinha_d6_ratio40_education_all_scores_seed42"><code>D6 · ratio 40 · seed 42</code></a></td><td>0.110</td></tr>
        <tr><td>1.678B</td><td>125.829M</td><td>All</td><td><a href="https://huggingface.co/duarteocarmo/ginjinha/tree/main/ginjinha_d8_ratio40_ptcore5_education_all_scores"><code>D8 · ratio 40</code></a></td><td>0.110</td></tr>
        <tr><td>927.99M</td><td>73.532M</td><td>All</td><td><a href="https://huggingface.co/duarteocarmo/ginjinha/tree/main/ginjinha_d6_ratio40_education_all_scores_seed1337"><code>D6 · ratio 40 · seed 1337</code></a></td><td>0.108</td></tr>
        <tr><td>927.99M</td><td>73.532M</td><td>≥3</td><td><a href="https://huggingface.co/duarteocarmo/ginjinha/tree/main/ginjinha_d6_ratio40_education_score_gte3_seed1337"><code>D6 · ratio 40 · seed 1337</code></a></td><td>0.108</td></tr>
        <tr><td>927.99M</td><td>73.532M</td><td>≥1</td><td><a href="https://huggingface.co/duarteocarmo/ginjinha/tree/main/ginjinha_d6_ratio40_education_score_gte1_seed1337"><code>D6 · ratio 40 · seed 1337</code></a></td><td>0.107</td></tr>
        <tr><td>927.99M</td><td>73.532M</td><td>≥1</td><td><a href="https://huggingface.co/duarteocarmo/ginjinha/tree/main/ginjinha_d6_ratio40_education_score_gte1_seed2026"><code>D6 · ratio 40 · seed 2026</code></a></td><td>0.103</td></tr>
        <tr><td>927.99M</td><td>73.532M</td><td>≥1</td><td><a href="https://huggingface.co/duarteocarmo/ginjinha/tree/main/ginjinha_d6_ratio40_education_score_gte1_seed42"><code>D6 · ratio 40 · seed 42</code></a></td><td>0.102</td></tr>
        <tr><td>927.99M</td><td>73.532M</td><td>All</td><td><a href="https://huggingface.co/duarteocarmo/ginjinha/tree/main/ginjinha_d6_ratio40_education_all_scores_seed2026"><code>D6 · ratio 40 · seed 2026</code></a></td><td>0.093</td></tr>
        <tr><td>9.375B</td><td>279.184M</td><td>≥1</td><td><code>D11 · ratio 91</code></td><td>—</td></tr>
      </tbody>
    </table>
  </div>
</details>


These models can complete Portuguese text pretty well! Below are two unedited completions from the [D8 ratio-40 model trained on scores ≥3](https://huggingface.co/duarteocarmo/ginjinha/tree/main/ginjinha_d8_ratio40_ptcore5_education_score_gte3), generated with a temperature of 0.8 and a top-k of 40:

**Prompt: `O bairro de Alvalade`**

```text
O bairro de Alvalade em Lisboa, um bairro de ruas largas e estreitas, onde os lisboetas passam 2/3 do tempo que passa em Lisboa, não tem nada a ver com a sua dimensão.
A partir de um mapa, o percurso que liga Lisboa ao bairro de Alvalade passa por pequenas ruas com traçado irregular e estreitas, com alguns metros de largura, e com pequenas praças a marcarem a malha urbana dos pequenos núcleos urbanos do bairro.
O percurso que liga Alvalade ao bairro de Alvalade passa por pequenas ruas com traçado irregular e estreita, com algumas metros de largura, e com pequenas praças a marcarem a malha urbana dos pequenos núcleos urbanos do bairro.
Há
```

**Prompt: `A cidade do Porto`**

```text
A cidade do Porto possui uma gastronomia única e uma arquitetura única. Desde os pratos de peixe grelhado ao bacalhau guisado e à doçaria conventual. A cidade do Porto oferece uma experiência culinária única, não se afastando muito dos restaurantes, mas convidando a uma boa esplanada enquanto se aprecia o pôr-do-sol.
Para os viajantes que procuram uma experiência gastronómica de excelência, uma viagem ao Porto é indispensável, uma vez que a cidade é muito conhecida pela sua gastronomia rica e requintada. Desde as famosas caves de Vila Nova de Gaia até às famosas caves de vinho do Porto, cada refeição, à refeição principal, é uma oportunidade para conhecer
```

Not AGI, but you can see how these models could become quite capable with some SFT and RL on top.

## Lessons learned and next steps

This was a fun exercise. We already knew that better-quality data results in better—or at least more capable—models. But running these experiments on a tight budget taught me how structured the research needs to be. I started with a lot of *YOLO*-style runs until I had to stop and think: "OK, what do I want to test here?"

The Ginjinha project also showed me what an enormous advantage labs with access to compute have. If I had a single H100 for a year, I could conduct many more ablations and experiments—and do so *much* faster. Perhaps I should invest in one.

And even though I haven't trained on the entire Bagaço v2 dataset, I did realize that it has a major shortcoming: data quality. Approximately [50% of the documents in Bagaço v2 have an educational score of 0 (i.e., they have zero educational value)](https://huggingface.co/datasets/duarteocarmo/fineweb2-bagaco2#statistics--counts). Yes, you read that right. That's not going to get us where we need to be. It might add some diversity, but we need much more high-quality data.

Yes. I'm working on it!
