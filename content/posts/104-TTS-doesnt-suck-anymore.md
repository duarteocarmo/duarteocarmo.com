title: TTS doesn't suck anymore
description: 
date: 26th of May 2026
status: draft
audio: true
thumbnail: TODO


About 6 months ago I wrote a small rant on how open source TTS models sucked. Now, 6 months later, I'm happy to report that TTS doesn't suck anymore. 

Earlier in January this year, Qwen, the famous Chinese AI lab released [Qwen3-TTS](https://github.com/QwenLM/Qwen3-TTS), an open-weights series of TTS models. They released 2 CustomVoice models (pre-made voices + style control), 2 base models (zero-shot voice cloning + fine-tuning) and a VoiceDesign model (create voices from descriptions). They are all quite small, with a 0.6B and a 1.7B variant. 

For the use case of article narration for this blog, there are a lot of things to like. First, it fully supports voice cloning - via fine tuning and zero-shot conditioning. Voxtral, for example, [doesn't](https://www.reddit.com/r/LocalLLaMA/comments/1s6rmoi/the_missing_piece_of_voxtral_tts_to_enable_voice/). Second is the license - Apache 2.0 - which means we can do whatever we want with it. And third, it's supported by vLLM for deployment and inference, via [vLLM-Omni](https://docs.vllm.ai/projects/vllm-omni/en/latest/).  

There are, of course, some caveats. For instants, there is a [small bug](https://github.com/QwenLM/Qwen3-TTS/pull/178) on the fine-tuning code which creates some weird accelerations once you train it. Second, the [base models don't support "style-guidance"](https://github.com/QwenLM/Qwen3-TTS/issues/14#issuecomment-3789452120) - e.g., you can't tell your fine-tuned model to sound very angry - or very sad. Apparently - it's coming soon. And more importantly, it doesn't have all the small issues when generating longer pieces of text like other open-source TTS models did. 

For some reason, it's not on the Speech Arena [leaderboard](https://artificialanalysis.ai/text-to-speech/leaderboard?open-weights=true) for Open Weights models. There are [two entries](https://artificialanalysis.ai/text-to-speech/model-families/qwen) on the ranking - which I am not sure what they refer to. From my experience, it's not all about the model. Often, the inference around it, and behaviour in production is what matters most - and I have to say that Qwen3-TTS has been a wonderful surprise. 

[include tests here]

For the use case of this blog, I spend a morning getting a [dataset](https://huggingface.co/buckets/duarteocarmo/voice/tree/samples) ready for fine-tuning by reading a couple of articles out loud, and generating training samples with [MacWhisper](https://goodsnooze.gumroad.com/l/macwhisper) with Parakeet. I tweaked some of the [fine-tuning code](https://github.com/duarteocarmo/podcaster/tree/master/finetune_qwen) to avoid the acceleration bug, and trained a 0.6B base model on a [Scaleway H100](https://www.scaleway.com/en/h100/). I updated my [podcaster](https://github.com/duarteocarmo/podcaster) package so that it runs the fine-tuned model on Modal.com. Instead of running on scheduled GitHub actions (we all know how those go) - it now runs fully on my [Coolify](https://coolify.io/) instance. 

TTS is moving fast. There are a lot of things I haven't tested yet. [OmniVoice](https://github.com/k2-fsa/OmniVoice) is one of them, StepFun's [Step-Audio-EditX](https://github.com/stepfun-ai/Step-Audio-EditX) is another. 

TTS doesn't suck anymore. We have options now. 