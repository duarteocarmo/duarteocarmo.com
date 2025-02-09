title: What the hell Is GPQA, anyway?
date: Wed 15 Jan 2025
description: MMLU, HumanEval, SimpleQA, GPQA. Confused? You’re not alone. A short deep-dive into LLM evaluations and benchmarks, focused on GPQA.
status: published
slug: what-the-hell-is-gqpa-anyway
thumbnail: images/75/cover.png

In the period of the generative AI boom, everything is happening all at once. Every day a new model comes out, every week a billion dollar company teases a great new advancement. 

More often than not, they'll show us [some](https://www.anthropic.com/news/claude-3-family) [fancy](https://ai.meta.com/blog/llama-3-2-connect-2024-vision-edge-mobile-devices/) [version](https://openai.com/index/gpt-4o-mini-advancing-cost-efficient-intelligence/) of this:

<img src="{static}/images/75/0c345aa068fce110d80e914f8cd8898d.png" alt="Benchmark example" style="max-width:100%;border-radius: 2px;">

[We all love a misterious chart.](https://www.theverge.com/2024/10/28/24281965/honestly-this-is-a-work-of-art)  [ref][Source](https://arxiv.org/pdf/2412.08905)[/ref]

A healthy person might look at this and just think - great - the higher the score the better the model. Unfortunately - I'm [not healthy](https://duarteocarmo.com/blog/the-marathon), and I'm a bit sick we just throw these tables around like they're the absolute truth. 

A **40.9 score in GPQA** - what the _hell_ does that even mean?

## Table of contents and code

[TOC]

[Code and prompts](https://gist.github.com/duarteocarmo/3eeb2200af74880e034d45e63e30aafe)


## A quick intro to GPQA


GPQA stands for "Graduate-Level Google-Proof Q\&A Benchmark." It is a [dataset](https://huggingface.co/datasets/Idavidrein/gpqa) and [methodology](https://github.com/idavidrein/gpqa) introduced in a [paper](https://arxiv.org/pdf/2311.12022) by researchers from NYU, Cohere, and Anthropic. In essence, GPQA focuses on a subset of exceptionally challenging questions from the fields of physics, chemistry, and biology.

The dataset is available in three versions, each with varying levels of difficulty:

* **Extended Set**: 546 questions.
* **Main Set**: 448 questions.
* **Diamond Set**: 198 questions (the most challenging subset).

Here’s an example of a question from the dataset:

```text
Methylcyclopentadiene (which exists as a fluxional mixture of isomers) was allowed to react with methyl isoamyl ketone
and a catalytic amount of pyrrolidine. A bright yellow, cross-conjugated polyalkenyl hydrocarbon product formed (as
a mixture of isomers), with water as a side product. These products are derivatives of fulvene. This product was then
allowed to react with ethyl acrylate in a 1:1 ratio. Upon completion of the reaction, the bright yellow color had disappeared.
How many chemically distinct isomers make up the final product (not counting stereoisomers)?
A) 2
B) 16
C) 8
D) 4
```


For context, a 'non-expert' human—with unlimited time and internet access—achieves roughly 30.4% accuracy on the main set.

With that in mind, it’s intriguing to see how large language models (LLMs) are tested against these tasks. Fortunately, the prompts used for evaluation are openly shared in both the [paper](https://arxiv.org/pdf/2311.12022) and the [repository](https://github.com/idavidrein/gpqa).

Zero-shot prompt: 

```text
What is the correct answer to this question: What is the solubility of the stochiometric tricalcium
phosphate in a solution with the pH level of a) pH = 9, b) pH = 7 and c) pH = 5 (25 °C)?
The Ksp for Ca3(PO4)2 is 2𝑥10− 29, the dissociation constants of phosphoric acid are Ka1 =
7.5𝑥10− 3, Ka2 = 6.2𝑥10− 8 and Ka3 = 1.8𝑥10− 12.
Choices:
(A) 1.96𝑥10− 5; 1.35𝑥10− 4; 4.37𝑥10− 3
(B) 1.67𝑥10− 5; 1.51𝑥10− 4; 4.81𝑥10− 3
(C) 1.54𝑥10− 5𝑀; 1.42𝑥10− 4; 4.67𝑥10− 3
(D) 1.43𝑥10− 5; 1.29𝑥10− 4; 4.58𝑥10− 3

Format your response as follows: "The correct answer is (insert answer here)".
```

Zero-shot chain-of-thought prompt:
```text
What is the correct answer to this question: What is the solubility of the stochiometric tricalcium
phosphate in a solution with the pH level of a) pH = 9, b) pH = 7 and c) pH = 5 (25 °C)?
The Ksp for Ca3(PO4)2 is 2𝑥10− 29, the dissociation constants of phosphoric acid are Ka1 =
7.5𝑥10− 3, Ka2 = 6.2𝑥10− 8 and Ka3 = 1.8𝑥10− 12.
Choices:
(A) 1.96𝑥10− 5; 1.35𝑥10− 4; 4.37𝑥10− 3
(B) 1.67𝑥10− 5; 1.51𝑥10− 4; 4.81𝑥10− 3
(C) 1.54𝑥10− 5𝑀; 1.42𝑥10− 4; 4.67𝑥10− 3
(D) 1.43𝑥10− 5; 1.29𝑥10− 4; 4.58𝑥10− 3
Let’s think step by step:
...MODEL RESPONSE HERE...

Based on the above, what is the single, most likely answer choice? Answer in the format "The
correct answer is (insert answer here)".
```

A curious reader might notice that the 'zero-shot' chain-of-thought (COT) prompt actually involves two calls to the model: the first to generate a response and the second to finalize the answer. This approach is likely **not** representative of how these models are typically used in real-world scenarios—but we’ll explore that further in a moment.

This raises an interesting question: how can we reproduce these results ourselves?

## Trying to reproduce GPQA

If you’ve explored LLM evaluations, you’re likely familiar with the [Open LLM Leaderboard](https://huggingface.co/spaces/open-llm-leaderboard/open_llm_leaderboard#/?params=-1%2C8\&official=true\&rankingMode=dynamic\&columns=rank%2Cmodel.type_icon%2Cid%2Cmodel.average_score%2Cmetadata.params_billions%2Cmetadata.submission_date%2Cevaluations.gpqa.normalized_score%2Cmetadata.base_model%2Cevaluations.mmlu_pro.normalized_score%2Cevaluations.musr.normalized_score) by Hugging Face. The leaderboard recently received an update, allowing users to filter by 'Only Official Providers'—handy if you want to focus on well-known providers.

Here’s a snapshot of the top-performing models under 8 billion parameters, sorted by GPQA score:


<img src="{static}/images/75/86a23c7296cb79b43c2eff265f26cf56.png" alt="Open LLM leaderboard" style="max-width:100%;border-radius: 2px;">

You'll notice there are some familiar names in there like Phi, or Qwen 2.5 7B. Of course, models from OpenAI, Google or Claude are off this list, since it relates to Open models - which those aren't. 

[Digging a bit deeper](https://huggingface.co/docs/leaderboards/open_llm_leaderboard/about), we notice two interesting things: 

1. This leaderboad uses the zero-shot version of this dataset, and measures the normalized accuracy. It doesn't specify which variant of the dataset it uses - we'll assume the `main` variant for now - but that could be wrong. 
2. Another intesting tid-bit is how they run these benchmarks: '_...using the [Eleuther AI Language Model Evaluation Harness](https://github.com/EleutherAI/lm-evaluation-harness) , a unified framework to test generative language models..._'

Great - so now we have at least _some_ clue of how to reproduce this. 


## Testing EleutherAI's LM Evaluation Harness

There are [several frameworks](https://github.com/openai/simple-evals?tab=readme-ov-file) for evaluating large language models (LLMs), including [OpenAI’s evals](https://github.com/openai/evals) and EleutherAI’s [LM Evaluation Harness](https://github.com/EleutherAI/lm-evaluation-harness). EleutherAI’s framework, while powerful, can feel overwhelming at first. It supports a wide range of [models and APIs](https://github.com/EleutherAI/lm-evaluation-harness?tab=readme-ov-file#model-apis-and-inference-servers) and a significant number of [tasks](https://github.com/EleutherAI/lm-evaluation-harness/tree/main/lm_eval/tasks#tasks).

After some poking around, I managed to find the [part of the repo](https://github.com/EleutherAI/lm-evaluation-harness/blob/main/lm_eval/tasks/gpqa/README.md#tasks) that relates the benchmark we're interested in. 

We can see that they support the following [tasks](https://github.com/EleutherAI/lm-evaluation-harness/tree/main/lm_eval/tasks/gpqa#tasks): 

```text
* `gpqa_{main, diamond, extended}_zeroshot`
* `gpqa_{main, diamond, extended}_n_shot`
* `gpqa_{main, diamond, extended}_generative_n_shot`
* `gpqa_{main, diamond, extended}_cot_zeroshot`
* `gpqa_{main, diamond, extended}_cot_n_shot`
```

We can also see the [config and prompt](https://github.com/EleutherAI/lm-evaluation-harness/blob/main/lm_eval/tasks/gpqa/zeroshot/_gpqa_zeroshot_yaml#L9) they use for the `gpqa_main_zeroshot` task which is the one we're interested in. The attentive reader might notice already that [the prompt](https://github.com/EleutherAI/lm-evaluation-harness/blob/bb098f13b05e361f01a5afe7b612779ce362b3f2/lm_eval/tasks/gpqa/zeroshot/_gpqa_zeroshot_yaml#L9) that is being used here is quite different from the one from the original paper. But let's ignore that for now. 

Here’s how I tried to run the evaluation:

```
lm-eval --model openai-chat-completions \
		--model_args model=gpt-4o-mini,num_concurrent=10,max_retries=3 \
		--tasks gpqa_main_zeroshot \
		--apply_chat_template \
		--output_path results \
		--log_samples \
		--wandb_args project=lmeval \
		--use_cache model_cache 
```

This errors out: 

```text
NotImplementedError: Loglikelihood (and therefore `multiple_choice`-type tasks) is not supported for chat completions as OpenAI does not provide prompt logprobs. See https://github.com/EleutherAI/lm-evaluation-harness/issues/942#issuecomment-1777836312 or https://github.com/EleutherAI/lm-evaluation-harness/issues/1196 for more background on this limitation.
```

Oh wait? What's happening here? Well - most of these multiple-choice benchmarks use loglikelihood to understand what the choice is with the highest probability. This is a bit weird - since it's not the methodology outlined in the original GPQA paper. However, seems to be a deliberate choice to maintain the framework consistent.[ref]See [this](https://github.com/EleutherAI/lm-evaluation-harness/issues/942#issuecomment-1777836312) and [this](https://github.com/EleutherAI/lm-evaluation-harness/issues/1196).[/ref]

However, there's another benchmark we could run and appears to work - the zero-shot chain-of-thought one.

```
lm-eval --model openai-chat-completions \
		--model_args model=gpt-4o-mini,num_concurrent=10,max_retries=3 \
		--tasks gpqa_main_cot_zeroshot \ #<- cot version
		--apply_chat_template \
		--output_path results \
		--log_samples \
		--wandb_args project=lmeval \
		--use_cache model_cache 
```
This gives us: 

```
|        Tasks         |Version|     Filter     |n-shot|  Metric   |   |Value |   |Stderr|
|----------------------|------:|----------------|-----:|-----------|---|-----:|---|-----:|
|gpqa_main_cot_zeroshot|      1|flexible-extract|     0|exact_match|↑  |0.1205|±  |0.0154|
|                      |       |strict-match    |     0|exact_match|↑  |0.0000|±  |0.0000|
```

Now, I haven’t dug too deeply into these results for the COT version, but they seem very low since they rely on the `flexible-extract` metric, which _could_ perform poorly if it’s regex-based. One thing we notice is that the [prompt](https://github.com/EleutherAI/lm-evaluation-harness/blob/main/lm_eval/tasks/gpqa/cot_zeroshot/_gpqa_cot_zeroshot_yaml#L9) used here is closer to the original one from the paper. However, it lacks the two-model-call approach outlined there.

At this point, I was starting to lose faith in this entire evaluation system. What’s the most straightforward way to achieve an interesting score on this benchmark? Something that can work for any model, whether open or closed?


## Running GPQA zero-shot with DsPy

[DSPy](https://dspy.ai/) is a great framework out of Standford that provides some structure around prompting for LLMs. It also provides some great optimizers so we can programatically optimize a prompt without having to write much of it. 

We start by getting the data in: 

```python
import polars as pl
# Load the dataset from Hugging Face and prepare it
df = (
    pl.scan_csv("hf://datasets/Idavidrein/gpqa/*_main.csv")
    .collect()
    .sort("Question")
)
```

The next step is to configure our llm and the Signatures (think data-model) we'll use: 

```python
lm = dspy.LM("openai/gpt-4o-mini", temperature=0.00)
dspy.configure(lm=lm)

class Answer(dspy.Signature):
    """Respond to the question with the correct answer"""
    question: str = dspy.InputField()
    choices: list[str] = dspy.InputField()
    answer: str = dspy.OutputField()
    
generate_answer = dspy.Predict(Answer)
```

Here's an example of how to use it: 

```python
answer = generate_answer(
    question="What's the capital of Le Marche?", choices=["Ancona", "Senigallia"]
)
# prints Prediction(answer='Ancona')
```

Let's juggle our data into a dataset:

```python
dataset = []
random.seed(42)
for row in df.to_dicts():
    choices = [
        row["Correct Answer"],
        row["Incorrect Answer 1"],
        row["Incorrect Answer 2"],
        row["Incorrect Answer 3"],
    ]
    random.shuffle(choices)
    example = dspy.Example(
        choices=choices,
        question=row["Question"],
        correct_answer=row["Correct Answer"],
    ).with_inputs("question", "choices")
    dataset.append(example)

class EvaluateZeroShot(dspy.Signature):
    """Evaluate the answer to the question"""
    question: str = dspy.InputField()
    choices: list[str] = dspy.InputField()
    answer: str = dspy.InputField()
    correct_answer: str = dspy.InputField()
    is_correct: bool = dspy.OutputField()

evaluate_answer = dspy.Predict(EvaluateZeroShot)

def validate_response(example, prediction, trace=None):
    eval = evaluate_answer(
        question=example.question,
        choices=example.choices,
        answer=prediction.answer,
        correct_answer=example.correct_answer,
    )
    return eval.is_correct

evaluator = Evaluate(
    devset=trainset, num_threads=10, display_progress=True, display_table=True
)
accuracy, predictions, scores = evaluator(generate_answer, metric=validate_response)
print(f"Accuracy: {accuracy}") # prints 33.48
```

Great, so a single run for GPQA gives us a 33.48% accuracy. Still a bit far off the 40.2% that is [advertised by OpenAI](https://openai.com/index/gpt-4o-mini-advancing-cost-efficient-intelligence/) - but again - there's apparently no way we can effectively verify that. 

## A small DSPy side-track 

There's a couple of interesting experiments we run with DSPY. 

The first one, is to try a Chain-of-thought prompt (COT) to understand how that might influence our score:

```python
cot = dspy.ChainOfThought("question, choices -> answer")
accuracy, predictions, scores = evaluator(cot, metric=validate_response)
print(f"Accuracy: {accuracy}") # prints 35.71
```

That's a ~7% increase on our GPQA score. Probably just noise. 

Another interesting thing we could do, is to try to optimize our prompt for this specific GPQA benchmark. An important note is that we don't need to even fine-tune a model, we're just going to optimize our prompt. 

To do that, we'll use 98 questions that are in the extended version of the dataset, but not in the main version of it. Our goal is to optimize on those 98 and then see if an optimized prompt performs better on our main version. 

Here we go: 

```python
df_extended = (
    pl.scan_csv("hf://datasets/Idavidrein/gpqa/*_extended.csv", cache=True)
    .collect()
    .sort("Question")
)
df_extended = df_extended.filter(~pl.col("Question").is_in(df_main["Question"])) # returns 98 questions

# build extended_set from df_extended (omitted for brevity)

cot = dspy.ChainOfThought("question, choices -> answer") # base format
tp = dspy.MIPROv2(metric=validate_response, auto="light", num_threads=10) # optimization
optimized_cot = tp.compile(cot, trainset=extended_set) # run optimization

# evaluate optimized prompt
accuracy, predictions, scores = evaluator(optimized_cot, metric=validate_response)
print(f"Accuracy: {accuracy}") # prints 38.39
```

This produces an [optimized prompt](https://gist.github.com/duarteocarmo/3eeb2200af74880e034d45e63e30aafe#file-optimized_cot-json) with some few example questions. When evaluating, we get a further increased score of another 7.5%. As you can see - the results of these benchmark are HIGHLY prompt dependent. It seems to be possible to even optimize a much smaller model to be able to perform well on this 'benchmark'. 


## Final thoughts

Alright, after this deep dive, you should have a clearer idea of what GPQA is and how it works. Most benchmarks you see out there are variations of these multi-choice questions—some harder, some easier, some slightly different.

But this exercise also revealed a few important things about the benchmark ecosystem and its flaws:

**Benchmarks are not scientific.**
Many benchmarks feel more like pseudo-science than systematic evaluations. Frameworks often fail to replicate the original paper’s prompts and methodology. If this inconsistency exists here, imagine how it plays out in other benchmarks. Using log-likelihood to evaluate multi-choice questions might make sense in some cases, but the GPQA paper doesn’t mention it at all. So, what’s really going on here?

**Prompts matter—a lot.**
As we saw with DSPy, small tweaks in prompts can make a huge difference, sometimes boosting scores by 5–10%. Add a "you are a physics expert" to your prompt, and you might get even better results. This raises the question: how sensitive are these benchmarks to prompts? Are some models more affected than others? Definitely worth exploring.

**The issue of trust.**
Benchmarks should inspire confidence in a model’s performance, but instead, they often raise more questions than answers. For instance, what [does a 40.2 GPQA score for GPT-4o-mini really mean](https://openai.com/index/gpt-4o-mini-advancing-cost-efficient-intelligence/)? What dataset version? What prompt? Without these details, it’s hard to trust the results—especially when they’re not reproducible.

**How can we evaluate?**
I once heard in a podcast: "There’s nothing like a good vibe evaluation." Sure, when building products with LLMs, good [evaluations](https://hamel.dev/blog/posts/evals/) matter. But when comparing models, questions of [preference](https://lmarena.ai/) are often more valuable than multi-choice benchmarks. Efforts like the [OpenLLM leaderboard](https://huggingface.co/spaces/open-llm-leaderboard/open_llm_leaderboard) are interesting, but do they really tell us much about these models? With closed models, at least, the mystery adds intrigue.

Benchmarks are fun, but in the end, the true test of a model is how well it performs in the real world. That's what matters.
