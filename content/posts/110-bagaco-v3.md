title: Bagaço v3: Now with PDFs and Wikipedia!
description: Building the third version of Bagaço. An European Portuguese pretraining dataset of 29 Billion tokens
date: 25th August 2026
status: published
thumbnail: images/110/source-comparison-square.webp
toc: false

<center>
<a href="{static}/images/110/source-comparison.webp" target="_blank">
<img src="{static}/images/110/source-comparison.webp" alt="Bagaço v3 sources compared by document share, average document length, and average educational score" style="max-width:100%;border-radius: 2px">
</a>
<figcaption>Source composition and averages.</figcaption>
</center>

I'm proud to announce [Bagaço v3](https://huggingface.co/datasets/duarteocarmo/bagaco3), the third version of the largest European Portuguese pretraining dataset for large language models.

Why a new version? After my work on [Ginjinha]({filename}/posts/108-pretraining-llms-european-portuguese.md), one thing became pretty apparent: [Bagaço]({filename}/posts/96-bagaco-dataset.md) was large and diverse, but lacked high-quality data. I believe Bagaço v3 fixes that.

This new version builds on top of [Bagaço v2]({filename}/posts/103-bagacov2-dataset.md) and the great work from the Hugging Face team, and adds documents from Wikipedia ([FineWiki](https://huggingface.co/datasets/HuggingFaceFW/finewiki)) and from PDFs across the web ([FinePDFs](https://huggingface.co/datasets/HuggingFaceFW/finepdfs)). But that's not the full story. Let's get into the details.

<center>
<a href="{static}/images/110/sources-table.webp" target="_blank">
<img src="{static}/images/110/sources-table.webp" alt="Bagaço v3 source statistics table" style="max-width:100%;border-radius: 2px">
</a>
<figcaption>Bagaço v3 sources.</figcaption>
</center>

To create Bagaço v3, I started by using [DataTrove](https://github.com/huggingface/datatrove) to build a pipeline that merged Bagaço v2 (originally from FineWeb2), FineWiki, and FinePDFs. It filters the last two by European Portuguese score (using [my own classifier](https://huggingface.co/duarteocarmo/fasttext-euptvid), which I [wrote about here]({filename}/posts/98-fasttext-vs-bert-portuguese.md)), and deduplicates everything using MinHash deduplication.

<iframe
  src="https://huggingface.co/datasets/duarteocarmo/bagaco3/embed/viewer/default/train"
  frameborder="0"
  width="100%"
  height="560px"
></iframe>

But we don't want to dump everything into the same place just like that. Just like Bagaço v2, v3 adds two dimensions to this dataset: **educational score** (from 0 to 5) and **category** (Arts, Business, Games, etc.). To get this done, I used Gemini 3.7 Flash and OpenRouter's batch API and started by annotating 36K documents with the following prompt:

```text
Below is an extract from a web page. Evaluate whether the page has a high educational value
and could be useful in an educational setting for teaching from primary school to grade school
levels using the additive 5-point scoring system described below. The text will be in Portuguese.
Evaluate its educational value based on content quality, not language.

- 1 point: basic information relevant to educational topics, even with ads/promotional material.
- 2 points: addresses elements pertinent to education but doesn't align closely with standards.
- 3 points: appropriate for educational use, introduces key concepts relevant to school curricula.
- 4 points: highly relevant for grade school education, clear writing, substantial content.
- 5 points: outstanding educational value, perfectly suited for primary/grade school teaching.

The extract:
<extract>
{document_text}
</extract>

After examining the extract, briefly justify your total score (up to 100 words)
and provide the educational score (0-5). Also classify the extract into one category: Society,
Arts, Business, Science, Sports, Lifestyle, Health, Games, or News.

Respond ONLY with a JSON object in this format:
{"justification": "up to 100 words", "educational_score": 0, "category": "category"}

Examples of good responses:
{"justification": "The extract clearly explains photosynthesis and its role in plant growth, with useful scientific concepts for students.", "educational_score": 4, "category": "Science"}
{"justification": "The extract is mainly a product listing and offers little explanation beyond basic promotional information.", "educational_score": 1, "category": "Lifestyle"}
```

With that annotated dataset, I used the _classic_ embeddings + `LogisticRegression` to [train a classifier and apply it to the whole dataset](https://huggingface.co/datasets/duarteocarmo/bagaco3/tree/main/classifier). 4× RTX 4090s and 2 hours later, I had the entire dataset annotated. After some testing and many experiments with [pi-autoresearch](https://github.com/davebcn87/pi-autoresearch), an extension inspired by Karpathy's autoresearch project, I didn't find anything that really beat it.

<center>
<a href="{static}/images/110/label-distributions.webp" target="_blank">
<img src="{static}/images/110/label-distributions.webp" alt="Bagaço v3 documents and characters by predicted category and educational score" style="max-width:100%;border-radius: 2px">
</a>
<figcaption>Documents and characters by predicted label.</figcaption>
</center>

Bagaço v3 adds ~2 million documents to the 32M documents from Bagaço. Why the effort for a 7% increase? If you look closely - even though we only add 2M documents, the character increase is around 40% (!). And that might very well translate into many more tokens. Bagaço v3 has an estimated 29 billion (!) tokens. And hopefully, many more high-quality ones.

And there we go - a [shiny new dataset](https://huggingface.co/datasets/duarteocarmo/bagaco3). Now all we have to do is train on it (again).
