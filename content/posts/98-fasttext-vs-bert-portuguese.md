title: Portuguese variety identification: The bitter lesson
description: Training a text classifier to detect European Portuguese text at scale. Matching fine-tuned BERT by scaling training data. 
date: 9th of March 2026
status: published
thumbnail: images/98/cover.png


<div class="iframe-container">
  <iframe
    scrolling="no"
    id="results-frame"
    src="{static}/html/98/euptvid-results.html"
    title="FastText vs BERT results"
    loading="lazy">
  </iframe>
</div>

Given some text in Portuguese, how easy is it to determine if it's from Brazil or Portugal[ref]Or [somewhere else](https://en.wikipedia.org/wiki/Portuguese-speaking_world)![/ref]? For native speakers, this is pretty easy – it's almost a feeling. But for machines: not so much. 

This might seem like a useless problem at first. But in the age of language models and some of my research, I've seen this problem more than once.

When I [contributed Portuguese datasets to EuroEval](/blog/a-benchmark-for-language-models-on-european-portuguese.html), I had a hard time finding exclusively European Portuguese data. Most of the Portuguese on the Internet is *obviously* of the Brazilian variant. When I created [Bagaço](/blog/bagaco-a-pretraining-dataset-for-european-portuguese.html), a pretraining dataset for European Portuguese, the most obvious solution was to filter data for `.pt` domains. This works as a proxy, but is far from ideal.

It stuck in my mind: If we want to build good European Portuguese models we need robust ways of detecting that language variant in the wild.

In *[Enhancing Portuguese Variety Identification with Cross-Domain Approaches](https://arxiv.org/abs/2502.14394)* the authors take a stab at the problem. They fine-tune [BERTimbau](https://huggingface.co/neuralmind/bert-large-portuguese-cased) to classify text into PT-PT or PT-BR. The key idea: by hiding specific types of words (places, names, etc.) the model is forced to learn the structural/grammatical differences between the languages. It works well, but there's a problem: It doesn't scale!

Running a BERT based model to filter pre-training data (at internet scale) could take *days* even with dedicated hardware. I needed something as good as their model but that I could run fast for hundreds of Gigabytes of text. Most pre-training datasets use something like [FastText](https://fasttext.cc/) or [variants](https://github.com/cisnlp/GlotLID) to filter data by language. It scales really well[ref]So well that forced Claude into building a [Rust implementation](https://github.com/duarteocarmo/fasttext.rs) for it.[/ref] and doesn't need any type of dedicated hardware.

After some [hiccups](https://github.com/LIAAD/portuguese_vid/issues/3) (and a lot of tokens) I finally managed to reproduce the results from the paper. Once that was done, I started training a series of FastText models on [their same dataset](https://huggingface.co/datasets/liaad/PtBrVId). The results were *mediocre* at best. Different configurations of the data, some oversampling, parameter tuning, nothing got close to the baseline performance (theirs).

Then I thought: what if I just need more data? 

After some digging, I found [this dataset](https://huggingface.co/datasets/bastao/VeraCruz_PT-BR) from [Fabio Bastos](https://www.linkedin.com/in/fab-bastos/) - he basically did the exact domain level filtering as [Bagaço](https://huggingface.co/datasets/duarteocarmo/fineweb2-bagaco), but for a much larger dataset: [CulturaX](https://huggingface.co/datasets/uonlp/CulturaX). Separating it into Portuguese and Brazilian sources: exactly what I need to train a model. I started training classifiers, and the more data I trained on, the better performance I got. Once I trained on ~6M rows lo and behold: similar performance but **10x** faster. 

Actually, the quantized version of the model I trained packs a whole lot of punch but in only 70MB! The quantized model is so small it runs in your browser:

<div class="iframe-container">
  <iframe
    scrolling="no"
    id="demo-frame"
    src="{static}/html/98/demo.html"
    title="FastText Portuguese variety classifier demo"
    loading="lazy">
  </iframe>
</div>


As a sanity check, I ran the model on a subset of [FineWeb2](https://huggingface.co/datasets/HuggingFaceFW/fineweb-2) that had been filtered for Portuguese. Here's a snippet of the output:

```text
Loading model...
Downloading parquet...Loaded 33,846 rows
Classifying with threshold=0.7...
Classified 33,846 rows in 30.1s (1,125 rows/sec)
Score distribution:
mean=0.320  median=0.176
Total: 33,846 → PT-PT: 6,102 (18.0% kept)
Random PT-PT URLs:
- https://blogtailors.com/4997524.html
- https://www.bodyboardcenter.com/pt/apparel/734-sen-no-sen-not-diet-atoll-polo
- https://abapinho.com/2017/09/plantuml-finalmente-o-uml-da-para-usar/
- https://www.sabado.pt/portugal/detalhe/como-jose-veiga-denunciou-rui-rangel
- http://www.poadvogados.pt/Areas/InsolvRecoverE/?MOBILE=1
- https://www.viralagenda.com/pt/events/926945/palestra-intervir-com-criancas-e-jovens-em-risco-como-actuar
- http://confessionsfashiongirl.blogspot.com/2009/11/coisinhas-sem-as-quais-nao-podia-viver_08.html
- https://www.powrenism.com/forum/welcome-to-the-forum/exercice-dorsaux-sans-materiel-myogen-dianabol
- https://topbinamvf.web.app/berezny38567def/forex-seminbrio-manchester-1780.html
- https://foreveryoung.sapo.pt/rustic-chicken-ja-conhece-a-nova-proposta-da-mcdonalds/
- https://aralumiar.wordpress.com/2007/01/
- http://iclub.pt/video-do-4o-iclub-dinner/
- http://www.hotfrog.pt/empresa/lisboa/odivelas/avarias-ao-domicilio
- https://www.rowenta.pt/eficiencia-energetica-by-rowenta
- https://codimagem.com/2023/05/12/giros-gr%C3%A1tis-eletr%C3%B4nicos/
- http://apracas.pt/article/list/1/noticias/
- https://www.noticiasaominuto.com/politica/864278/cgtp-diz-que-greve-mostrou-que-autoeuropa-nao-vive-acima-da-lei
- http://nave-azul.blogspot.com/2010/11/portal-101110.html
- http://gbtrabalhoshubj.ischadia.info/mensagem-de-fernando-pessoa-terceira-parte-o-encoberto.html
```

As you can see, lots of these would never pop up if we just filtered for `.pt` domains. Also, the percentage kept aligns well at ~18% of text in the `pt` split being European Portuguese.

There's a parallel to LLMs in this post. Unlike the original paper, we didn't do any fancy delexicalization, we didn't even curate a pristine mix of data from different sources. We threw 6M rows of web data at the problem, and the problem got fixed. This is a known lesson in the world of computing: [it's called the Bitter Lesson](https://www.cs.utexas.edu/~eunsol/courses/data/bitter_lesson.pdf). 

The model and code are available on [GitHub](https://github.com/duarteocarmo/eupt_vid) and [Hugging Face](https://huggingface.co/duarteocarmo/fasttext-euptvid).

<style>
  .iframe-container {
    width: 100%;
    max-width: 800px;
    margin: 2rem auto;
    text-align: center;
  }

  #results-frame {
    width: 100%;
    height: 440px;
    border: none;
    display: block;
    box-sizing: border-box;
  }

  #demo-frame {
    width: 100%;
    height: 420px;
    border: none;
    display: block;
    box-sizing: border-box;
  }

  @media (max-width: 480px) {
    #results-frame { height: 300px; }
    #demo-frame { height: 380px; }
  }
</style>