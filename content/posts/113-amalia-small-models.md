title: AMALIA and smaller reasoning models
date: 2026-09-14
status: draft
thumbnail: 

<!-- TODO: Add a thumbnail. -->

A few weeks ago there was a bit of a scandal in Portugal. People were really, really mad that the government had took so long to correct all of the different high school exams for Portuguese high school students for this year. Once that happened, I saw a weird post on LinkedIn by someone saying that we have Amalia now, so we should just throw it at all the Portuguese exams and have it correct the exams itself, somehow arguing that this would be a good idea

Let's be serious. Using an LLM to correct high school exams is a horrible idea, at least as where the technology stands nowadays. But that piqued my interest. Is actually Amalia the best model to actually correct Portuguese high school exams. What they might not know is that the Amalia team actually released not only the model Amalia, but also a lot of different benchmarks and evaluations to test how good models are in Portuguese. And one of the evaluations is called PT exams and it does exactly this. It tests how good a model is in correcting or in performing in Portuguese high school exams

And so I decided to compare Amalia with a bunch of smaller models, just to see how good Amalia performed compared to others. And the results were a bit surprising. Amalia is actually not the best performer model when we compare it with much smaller models. There's even models that are as small as like 2B, 2 billion parameters, which are actually like almost four times smaller than Amali and perform quite much better. 


<figure style="width:100%;max-width:700px;margin:2rem auto">
  <object
    data="{static}/images/113/intelligence.svg"
    type="image/svg+xml"
    aria-label="Portuguese benchmark intelligence"
    style="display:block;width:100%;aspect-ratio:700/520;border-radius:2px"
  >
    <a href="{static}/images/113/intelligence.svg">Open interactive chart</a>
  </object>
</figure>

If you know a thing or two about LLMs, you'll probably call my bullshit by now. Even though the models that I compared Amalia to are much smaller, they're actually reasoning models. They use something called inference test time scaling to improve their performance. This basically means that we let the LLM babble or produce more text for a longer time and eventually the scores improve. I also tested some non-reasoning variants But the proof of the matter is that the reasoning variants perform really, really well. Of course, it's a little bit unfair to compare Amali with any of these other models. These are things coming from Big Lag blobs from NVIDIA to Alibaba Quen. So we're comparing it with a smaller team, with a smaller budget, and albeit like a smaller goal, but it's still interesting to see how much smaller models can outperform Momalia in even Portuguese-focused tasks. 

<figure style="width:100%;max-width:700px;margin:2rem auto">
  <object
    data="{static}/images/113/frontier.svg"
    type="image/svg+xml"
    aria-label="Portuguese benchmark intelligence compared with model size and output tokens"
    style="display:block;width:100%;aspect-ratio:700/520;border-radius:2px"
  >
    <a href="{static}/images/113/frontier.svg">Open interactive chart</a>
  </object>
</figure>

The catch here is obvious. These models use many more tokens in order to achieve the performance that they achieve. They think for a long while, and so you as a user have effectively to wait a much longer time to get results. But in cases like the LFM model, it's actually pretty surprising how a small model can pack so much punch in just a small form factor. This is effectively more likely because of their very deep pre-training that they've done for their models. And also, of course, the inference time scaling, which is also pretty surprising. 


<figure style="width:100%;max-width:700px;margin:2rem auto">
  <object
    data="{static}/images/113/tokens.svg"
    type="image/svg+xml"
    aria-label="Output tokens used for the Portuguese benchmarks"
    style="display:block;width:100%;aspect-ratio:700/520;border-radius:2px"
  >
    <a href="{static}/images/113/tokens.svg">Open interactive chart</a>
  </object>
</figure>

Now, what's the takeaway? Not much. We always knew that Amalia was an okay model, but we never really wanted to compare it to big lab models. But I think it's still interesting to compare with much smaller models. And I think this finally has something to say about the power of reasoning. Test time scaling is actually effectively surprising in terms of how good of results it can achieve, although it's obviously not the most efficient and effective technique since you've been spending many more tokens. But still, I think this tells us something regarding what would be cool to achieve in the fureeat of Malia. Could he have a much smaller model that everyone could run on their own hardware but that also performed well in Portuguese? For the moment, that appears to be the Quen or LFM models. But it would be really nice to have an Amalia model that packs a punch, but it looks like in order for it to pack a punch, it needs to change some of the ways it's trained. 


