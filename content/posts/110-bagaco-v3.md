title: Bagaco v3: Now with pdfs and wikipedia!
description:
date: 25th August 2026
status: draft

Bagaco version 3 iterates on Bagaco v2 and now adds documents from both Wikipedia and PDFs from accross the web. 

You might be thinking to yourself? Cool, but what was Bagaco version 2 missing? After my work on Ginjinha, one thing became pretty aparent, data quality plays a big part in training large language models from scratch. I believe Bagaco v3 fills in that void. 

To create it, I used datatrove to build a pipeline that merged Bagaco v2 (originally from FineWeb2), FineWiki, and FinePDFs. It filters the last two by European Portuguese score, and deduplicates everything using MinHash duplication. 

But we don't want to dump everything into the same place just like that. Just like Bagaco v2, v3 - also adds two dimensions to this dataset: educational score (from 0 to 5) and a Category (Arts, Business, Games, etc). To get this done, I used Gemini 3.7 flash and OpenRouters's batch api - and annotated 36K documents with the following prompt: 

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

With that annotated dataset, I use the _classic_ embeddings + `LogisticRegression` to train a classifier and apply it to the whole dataset. To do so, I used 4xRTX 3090's ~ 60 mins. After some optimizations and a lot of autoresearch, I didn't find anything that really beat it. 

Bagaco v3 adds ~2 Million documents to the 32M documents from Bagaco. Why the effort you ask? For a x% increase? Well - if you look closely - even though we only add 2M documents, the character increase is more like 30% more characters. And that might very well translated into many more tokens. Bagaco v3  has an estimated 29 Billion (!) tokens. And, hopefully many more high quality ones. 


And there we go - a shiny new dataset. Now all we have to do is train on it (again). 
