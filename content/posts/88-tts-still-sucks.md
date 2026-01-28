title: TTS still sucks
description: Some updates to my rss to podcast pipeline and the quest for the best open-source TTS model.
date: 10th of November 2025
status: published
audio: true
popular: true

or at least the open versions of it. I have this very stupid rule. A couple of years ago I decided to [turn this blog into a podcast](https://duarteocarmo.com/blog/you-can-now-listen-to-this-blog). At the time, I decided to make up a stupid rule: whatever model I use to clone my voice and generate article transcripts needs to be an open model.

Why? Because - as you might have figured by now - I like to make my life hard. The last version of the podcast generation engine was running on [F5-TTS](https://arxiv.org/abs/2410.06885). It was _fine_. I still got some funny messages from people showing me the model completely hallucinating or squeaking here and there. But a year later - I was pretty sure there would be something incredibly better out there.

Now I’m not so sure.

The first step was to look for the best TTS models out there. Thankfully, Artificial Analysis now publishes a leaderboard with the “best” [text-to-speech models](https://artificialanalysis.ai/text-to-speech/leaderboard). After filtering by my stupid rule of open models, we get the below ranking.

<img src="{static}/images/88/tts-rankings.png" alt="tts rankings">

At the top of the leaderboard is [Kokoro](https://huggingface.co/hexgrad/Kokoro-82M). Kokoro is an amazing model! Especially for a modest 82 Million (!) parameters and a mere 360 MB (!). However, like many models in this leaderboard - I can’t use it - since it doesn’t support voice cloning.

I started by looking at some of the stuff from [Fish Audio](https://fish.audio/). Their [codebase](https://github.com/fishaudio/fish-speech) seems to now support their new [S1-mini model](https://huggingface.co/fishaudio/openaudio-s1-mini). When testing it, most of the [emotion markers](https://github.com/fishaudio/fish-speech?tab=readme-ov-file#speech-control) did not work - or were only available in their closed version. The breaks and long pauses either. Also, the [chunking](https://github.com/search?q=repo%3Afishaudio%2Ffish-speech%20chunk&type=code) parameter is completely unused throughout the codebase - so not sure why it’s there. It’s a common business model nowadays: announce a state of the art open model just to attract attention to your real, and the incredible powerful gated model you have to pay for.

My second-best option on the list was [Chatterbox](https://github.com/resemble-ai/chatterbox). This wave of TTS models comes with major limitations. They're all restricted to short character counts - around 1,000–2,000 characters, sometimes even less. Ask them to generate anything longer, and the voice starts hallucinating or speeds up uncontrollably.

**[XTTS-v2](https://huggingface.co/coqui/XTTS-v2)**
<audio controls style="width: 75%; display: block;" preload="metadata"><source src="https://r2.duarteocarmo.com/old/xtts_v2.mp3" type="audio/mpeg"></audio>

**[F5-TTS](https://github.com/SWivid/F5-TTS)**
<audio controls style="width: 75%; display: block" preload="metadata"><source src="https://r2.duarteocarmo.com/old/f5_tts.mp3" type="audio/mpeg"></audio>

**[Chatterbox](https://github.com/resemble-ai/chatterbox)** (latest version)
<audio controls style="width: 75%; display: block" preload="metadata"><source src="https://r2.duarteocarmo.com/old/chatterbox.mp3" type="audio/mpeg"></audio>

The transcript generation process is straightforward. First, text gets extracted from my RSS feed and [pre-processed by an LLM](https://www.notion.so/TTS-still-sucks-29caecef3e2c80bc81ddc9484cab8c59?pvs=21) to make it more "readable". The LLM generates a transcript, a short summary, and a list of links for the show notes. We then chunk the transcript and [fire that off to a bunch of parallel Modal containers](https://github.com/duarteocarmo/podcaster/blob/138d64ad083c2e4355e5f92980762b2d9af7c133/src/podcaster/transcription.py#L52) where we run the Chatterbox TTS model. Once we get everything back, we stitch the wav files together, and _voilà_! The episode is ready. The hosting is an S3 bucket. Really, that’s what you are paying your podcast host for - it’s a lucrative business!

<iframe allow="autoplay *; encrypted-media *; fullscreen *; clipboard-write" frameborder="0" height="450" style="width:100%;max-width:660px;overflow:hidden;border-radius:10px;" sandbox="allow-forms allow-popups allow-same-origin allow-scripts allow-storage-access-by-user-activation allow-top-navigation-by-user-activation" src="https://embed.podcasts.apple.com/us/podcast/duarte-o-carmos-articles/id1719493997"></iframe>

I also made some improvements to the podcast generation side of things. First of all, the podcast is now also available on [Spotify](https://open.spotify.com/show/0qIVAs1ZDWnpJOQeMo1OjY?si=995d03c12ce749bd). Additionally, I fixed the show notes to now include nice clickable links in almost every podcast player. Looking at you Apple and your `CDATA` [requirements](https://help.apple.com/itc/podcasts_connect/#/itcb54353390)!

Some thoughts on the Chatterbox model. It’s definitely better than F5-TTS. But there are however, some common annoyances with almost every open-source voice cloning model. The first is the limited duration of the generated speech. Anything over 1000 characters starts hallucinating. The second is lack of _control_. Some models have [emotion tags](https://github.com/fishaudio/fish-speech?tab=readme-ov-file#speech-control), others have `<pause>` indicators. But almost every single one of these has been massively unreliable. To the point where I am splitting my text in a sentence per line and shipping that off to the TTS model to make things a bit more reliable.

So yes, from one side, TTS has come a long way. But when compared to [other](https://elevenlabs.io/voice-cloning) [proprietary](https://www.minimax.io/audio) [systems](https://inworld.ai/tts), TTS still sucks.

_Note: The rss to podcast pipeline is open source and available if you want to re-use it in [this GitHub repo](https://github.com/duarteocarmo/podcaster)._
