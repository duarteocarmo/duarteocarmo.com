title: TTS doesn't suck anymore
description: 6 months ago I wrote a blog post on how TTS still sucked. It's been 6 months, and the tables have turned. We have options now.
date: 26th of May 2026
status: published
audio: true
thumbnail: images/104/qwen3-tts-introduction.webp


About 6 months ago I wrote a small rant on how [open source TTS models still sucked]({filename}/posts/88-tts-still-sucks.md). 6 months later, I'm happy to report that isn't the case anymore.

January this year, [Qwen](https://qwen.ai/home), the famous Chinese AI lab, released [Qwen3-TTS](https://github.com/QwenLM/Qwen3-TTS), an open-weights series of TTS models. The release included 2 CustomVoice models (pre-made voices + style control), 2 base models (zero-shot voice cloning + fine-tuning), and a VoiceDesign model (create voices from descriptions). With a 0.6B and a 1.7B variant - they're all quite small.
	
<center>
<a href="{static}/images/104/qwen3-tts-introduction.webp" target="_blank">
<img src="{static}/images/104/qwen3-tts-introduction.webp" alt="Qwen3-TTS introduction" style="max-width:100%;border-radius: 2px">
</a>
<figcaption>
Qwen3-TTS in a nutshell. <a href="https://github.com/QwenLM/Qwen3-TTS">credits</a>.
</figcaption>
</center>

There are a lot of things to like. First, it *fully* supports voice cloning - via fine-tuning or zero-shot conditioning. [Voxtral](https://mistral.ai/news/voxtral), for example, [doesn't](https://www.reddit.com/r/LocalLLaMA/comments/1s6rmoi/the_missing_piece_of_voxtral_tts_to_enable_voice/). Second: the license is Apache 2.0 - which means we can do whatever we want with it ([beware](https://github.com/fishaudio/fish-speech/blob/main/LICENSE)). Third, it's supported by a strong inference engine. In this case [vLLM-Omni](https://docs.vllm.ai/projects/vllm-omni/en/latest/). And more importantly: it avoids many of the small issues other open-source TTS models had when generating longer pieces of text — squeaks, audio drops, weird pacing, etc.

There are some caveats. There is a [small bug](https://github.com/QwenLM/Qwen3-TTS/pull/178) on the fine-tuning code which creates some weird accelerations. The [base models don't support "style-guidance"](https://github.com/QwenLM/Qwen3-TTS/issues/14#issuecomment-3789452120) - e.g., you can't tell your fine-tuned model to sound very angry - or very sad.

For some reason, it's not on the Speech Arena [leaderboard](https://artificialanalysis.ai/text-to-speech/leaderboard?open-weights=true) for Open Weights models. There are [two entries](https://artificialanalysis.ai/text-to-speech/model-families/qwen) in the ranking - not sure what model they refer to. But from my experience, it's not all about the model. The inference around it and how it "behaves in the wild" is what matters most and Qwen3-TTS delivers.

<center>
<a href="{static}/images/104/tts-leaderboard-annotated.webp" target="_blank">
<img src="{static}/images/104/tts-leaderboard-annotated.webp" alt="Annotated open weights TTS leaderboard" style="max-width:100%;border-radius: 2px">
</a>
<figcaption>
The open weights TTS leaderboard with a bit of context.
</figcaption>
</center>

I spent a morning getting a [dataset](https://huggingface.co/buckets/duarteocarmo/voice/tree/samples) ready for fine-tuning by reading a couple of articles out loud, and generating training samples with [MacWhisper](https://goodsnooze.gumroad.com/l/macwhisper) and [Parakeet](https://huggingface.co/nvidia/parakeet-tdt-0.6b-v2). I tweaked some of the [fine-tuning code](https://github.com/duarteocarmo/podcaster/tree/master/finetune_qwen) to avoid the acceleration bug, and trained a 0.6B base model on a [Scaleway H100](https://www.scaleway.com/en/h100/). I updated my [podcaster](https://github.com/duarteocarmo/podcaster) package so that it runs the fine-tuned model on [Modal](https://modal.com/). Instead of running on scheduled GitHub actions (we all know how those go) - it now runs fully on my [Coolify](https://coolify.io/) instance.

Here's an example article transcription with the old vs. the new model:

**Chatterbox (original - not the new ones)**
<audio controls style="width: 75%; display: block; margin-top: 0.5rem" preload="metadata"><source src="{static}/images/104/chatterbox.mp3" type="audio/mpeg"></audio>

**Qwen3-TTS 0.6B fine-tune - 200 samples, 6 epochs** - [Hugging Face](https://huggingface.co/duarteocarmo/qwen_tts_finetune_0.6B_e10_l1e6) [ref] I trained on only 30 minutes of audio - I should add a lot more in the future to make the audio even better. Might sound a bit *less* like me - but certainly cleaner to listener's ear imo.[/ref]
<audio controls style="width: 75%; display: block; margin-top: 0.5rem" preload="metadata"><source src="{static}/images/104/qwen3-tts.mp3" type="audio/mpeg"></audio>


TTS is moving fast. There are a lot of things I haven't tested yet. [OmniVoice](https://github.com/k2-fsa/OmniVoice) is one of them, StepFun's [Step-Audio-EditX](https://github.com/stepfun-ai/Step-Audio-EditX) is another.

But the main takeaway is that TTS *doesn't* suck anymore. We have options now.