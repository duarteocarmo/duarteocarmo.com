title: Portuguese variety identification: The bitter lesson
description: 
date: 9th of March 2026
status: published

Given some text in Portuguese, how easy is it to determine if it's from Brazil or Portugal? For native speakers, this is pretty easy - it's almost a feeling. But for machines, not so much. 

And this might seem like a useless problem at first. But in the age of language models, this is actually an important problem.

When I [contributed Portuguese datasets to EuroEval](/blog/a-benchmark-for-language-models-on-european-portuguese.html) last year, I had a hard time finding exclusively European Portuguese data. Most of the Portuguese on the Internet is *obviously* Brazilian. When I created [Bagaço](/blog/bagaco-a-pretraining-dataset-for-european-portuguese.html), a pretraining dataset for European Portuguese, the most obvious solution was to filter data for `.pt` domains. This is far from ideal.

It stuck in my mind: If we want to build good European Portuguese models, we need a robust way of detecting it, at scale.

In *[Enhancing Portuguese Variety Identification with Cross-Domain Approaches](https://arxiv.org/abs/2502.14394)* the authors take a stab at the problem. They fine-tune [BERTimbau](https://huggingface.co/neuralmind/bert-large-portuguese-cased) to classify text into PT-PT or PT-BR. The key idea: by hiding specific types of words (places, names, etc.) the model is forced to learn the structural/grammatical differences between the languages. It works well, but there's a problem.

It doesn't *scale* well. Running that model to filter pre-training data (at internet scale) could take *days*, even with dedicated hardware. I needed something good, but that also scaled well. Most pre-training datasets use something like FastText or [variants](https://github.com/cisnlp/GlotLID) to filter data by language. It scales really well and doesn't need any type of dedicated hardware.

After some [hiccups](https://github.com/LIAAD/portuguese_vid/issues/3) (and a lot of tokens) I finally managed to reproduce the results from the paper. After that, I started training a series of FastText models on [their same dataset](https://huggingface.co/datasets/liaad/PtBrVId). The results were *mediocre* at best. Different configurations of the data, some oversampling, parameter tuning, nothing got close to the baseline performance (theirs).

Then I thought: what if I just need more data? 

After some digging, I found [this dataset](https://huggingface.co/datasets/bastao/VeraCruz_PT-BR) from [Fabio Bastos](https://www.linkedin.com/in/fab-bastos/) - he basically did the exact domain level filtering, but for a much larger dataset: [CulturaX](https://huggingface.co/datasets/uonlp/CulturaX). Separating it into Portuguese and Brazilian sources - exactly what I need to train a model. I downloaded a subset of ~6M rows, and lo and behold: similar performance but 10x faster. Also, the quantized version of the model packs a whole lot of punch but in only 70MB (!)

As a sanity check, I ran the model on a subset of FineWeb2 that had been filtered for Portuguese. You can start to see all the random web pages our `.pt` filter would never catch! 

```text
Loading model...
Downloading parquet...Loaded 33,846 rows

Classifying with threshold=0.7...
Classified 33,846 rows in 30.1s (1,125 rows/sec)
Score distribution:
	mean=0.320  median=0.176

Total: 33,846 → PT-PT: 6,102 (18.0% kept)

25 random PT-PT URLs:
- https://blogtailors.com/4997524.html
- https://www.bodyboardcenter.com/pt/apparel/734-sen-no-sen-not-diet-atoll-polo
- https://www.pinterest.pt/explore/reuni%C3%B5es/
- https://abapinho.com/2017/09/plantuml-finalmente-o-uml-da-para-usar/
- https://www.sabado.pt/portugal/detalhe/como-jose-veiga-denunciou-rui-rangel
- http://www.poadvogados.pt/Areas/InsolvRecoverE/?MOBILE=1
- https://psq.pt/pragas/detalhe/plantas_daninhas
- https://www.viralagenda.com/pt/events/926945/palestra-intervir-com-criancas-e-jovens-em-risco-como-actuar
- http://confessionsfashiongirl.blogspot.com/2009/11/coisinhas-sem-as-quais-nao-podia-viver_08.html
- https://www.powrenism.com/forum/welcome-to-the-forum/exercice-dorsaux-sans-materiel-myogen-dianabol
- https://topbinamvf.web.app/berezny38567def/forex-seminbrio-manchester-1780.html
- https://foreveryoung.sapo.pt/rustic-chicken-ja-conhece-a-nova-proposta-da-mcdonalds/
- https://www.cmjornal.pt/portugal/detalhe/buscas-no-rio-em-guimaraes-para-encontrar-eletricista-caes-detetaram-odor-a-cadaver?ref=Famosos_CmaoMinuto
- https://aralumiar.wordpress.com/2007/01/
- http://iclub.pt/video-do-4o-iclub-dinner/
- http://www.hotfrog.pt/empresa/lisboa/odivelas/avarias-ao-domicilio
- https://www.rowenta.pt/eficiencia-energetica-by-rowenta
- https://culturadeborla.blogs.sapo.pt/so-visto-recebe-rui-mendes-domingo-as-1620804?mode=reply
- https://www.viralagenda.com/pt/events/876099/viagem-ao-tempo-da-talha-dourada-de-lagos-as-igrejas-de-santo-antonio-e-de-nossa-senhora-da-luz
- https://codimagem.com/2023/05/12/giros-gr%C3%A1tis-eletr%C3%B4nicos/
- https://www.turbo.pt/byd-han-ev/
- http://apracas.pt/article/list/1/noticias/
- https://www.noticiasaominuto.com/politica/864278/cgtp-diz-que-greve-mostrou-que-autoeuropa-nao-vive-acima-da-lei
- http://nave-azul.blogspot.com/2010/11/portal-101110.html
- http://gbtrabalhoshubj.ischadia.info/mensagem-de-fernando-pessoa-terceira-parte-o-encoberto.html
```

We didn't use any fancy models, we didn't do any fancy delexicalization, we just threw more data at the problem. Now isn't that a [bitter lesson](https://www.cs.utexas.edu/~eunsol/courses/data/bitter_lesson.pdf)?

The model and code are available on [GitHub](https://github.com/duarteocarmo/eupt_vid) and [Hugging Face](https://huggingface.co/duarteocarmo/fasttext-euptvid).



