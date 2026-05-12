## Bagaço v2: The largest open pre-training dataset for European Portuguese 

A couple of months ago I released Bagaço - a pretraining dataset for European Portuguese. The idea was simple: take the FineWeb 2 dataset, limit it to web pages that look like they came from Portugal, and classify them into categories (Sports, Culture, etc.) and educational score. 

Pulling the European Portuguese from the wider corpus was a bit of a frustrating experience. It's a bit like finding a needle in the haystack. I fled the problem, and just included anything with a `.pt` domain in the url. But that didn't feel like it was enough. 

Which lead me to the next phase: European Portuguese variety identification. Or – in other words – spotting European Portuguese in the wild. After learning some bitter lessons, I built two FastText based classifiers that achieved SOTA performance, but with 10x the throughput. So that I could run the classifier at scale. 

With those two pieces in place, maybe you guessed where this was going: Bagaço v2. 

Bagaço v2 is – to my knowledge – the largest open-source pre-training dataset for European Portuguese. 33M documents, 37GB of text, approximately 9.3 Billion tokens. 

It takes the Portuguese split from CulturaX, and uses the classifier I built to only keep the European Portuguese documents (with a confidence over 70%) – like before – it also gives each document an educational score and content category.

I recently wrote about AMÁLIA and the future of European Portuguese LLMs. One of the main conclusions was that to build a strong European Portuguese LLM you need to find the right data. 

My hope is that Bagaço v2 takes us one step closer. 





- Bagaco a couple of months ago 
- Then portuguese variety indentification 
- There is a very natural next step
- Some statistics about the dataset
- I hope this will help whatever the the goals are 
- https://duarteocarmo.com/blog/portuguese-variety-identification-the-bitter-lesson
- https://huggingface.co/datasets/duarteocarmo/fineweb2-bagaco2
- https://huggingface.co/datasets/uonlp/CulturaX


