title: Upgrading this website's podcast with F5-TTS
date: Tue 12 November 2024
description: Updating podcaster, the static site to podcast with a new text-to-speech model
status: published
slug: podcast-tts-f5-tts-python
thumbnail: images/58/podcaster.png

For the [past year]({filename}/posts/58-this-article-is-now-a-podcast.md), this website's [podcast companion](https://podcasts.apple.com/us/podcast/duarte-o-carmos-articles/id1719493997) has been running on a text-to-speech model called [XTTS-v2](https://huggingface.co/coqui/XTTS-v2). It's not _horrible_. And those who have heard my voice before might notice some similarities. But it's far from a _pleasant_ listenning experience.

But the world of text-to-speech (TTS) has been gradually moving along. [NotebookLM](https://notebooklm.google/) made headlines, and everyone is sure the future of AI will sit somewhere between agents (whatever those are) and text-to-speech. NotebookLM is an awesome product. But it's still, at its core, a closed source product[ref]There are [some](https://github.com/lucidrains/soundstorm-pytorch) [open](https://github.com/meta-llama/llama-recipes/tree/main/recipes/quickstart/NotebookLlama) [source](https://huggingface.co/spaces/gabrielchua/open-notebooklm) implementations the core tech is still very much closed source.[/ref].

Unfortunately, for state of the art text-to-speech there is still a single undisputed champion out there: [ElevenLabs](https://elevenlabs.io/). Or should I say, there _was_?

Late this year a new model from Microsoft came out, called [E2-TTS](https://arxiv.org/abs/2406.18009). Sometime after, [F5-TTS](https://github.com/SWivid/F5-TTS) was released - an improvement over E2 focued on inference and optimization. I was amazed by the [demos](https://www.microsoft.com/en-us/research/project/e2-tts/) - they sounded _crisp_ and _natural_. After browsing the code for a little bit, it seemed like an easy thing to test out.

I tested the engine with [one of my latest posts]({filename}/posts/69-iceland):

|                                                 |                                                                                                                                                                                              |
|-------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [XTTS-v2](https://huggingface.co/coqui/XTTS-v2) | <audio controls style="width: 100%; display: block" preload="metadata"><source src="https://r2.duarteocarmo.com/old/old.mp3" type="audio/mpeg"></audio>                                      |
| [F5-TTS](https://github.com/SWivid/F5-TTS)      | <audio controls style="width: 100%; display: block" preload="metadata"><source src="https://r2.duarteocarmo.com/transcripts/10bb68f8f7200f19b71bb095af3c5f32.mp3" type="audio/mpeg"></audio> |

I mean, would you just hear that. No more weird accelerations and squeeky voices. The new model is just much more stable and reliable than the previous one. It's light day and night! It's still not perfect though. One might argue the voice gets a bit _too_ intense some times. The problem with prounounciation persists. It still doesn't know how to say my name properly - but then again - most people also can't.

I tried getting around the prounounciation by specifying the phoneme sequence[ref]See the [demo page](https://www.microsoft.com/en-us/research/project/e2-tts/) for details[/ref], but that didn't seem to change much. It did give me a good idea to [preprocess](https://github.com/duarteocarmo/podcaster/blob/master/src/podcaster/parser.py#L109) the audio with an LLM - and that also makes things smoother.

Running F5-TTS was also trivial thanks to Modal's great product (still haven't paid a penny I must say, but would happily). Only this specific function needs to run on a GPU, and it does so just by using [Modal's decorator](https://modal.com/docs/guide/gpu):

```python
@app.function(
    gpu=MODAL_GPU,
    mounts=[
        modal.Mount.from_local_dir(
            LOCAL_DATA_DIR, remote_path=MODAL_REMOTE_DATA_DIR
        )
    ],
    timeout=400,
)
def transcribe(
    article: ParsedArticle,
    reference_voice_file: str = REFERENCE_VOICE,
    reference_text_file: str = REFERENCE_TEXT,
    model_name: str = MODEL_NAME,
) -> bytes:
    with open(reference_text_file, "r") as voice_text:
        reference_text = voice_text.read()

    command = [
        "f5-tts_infer-cli",
        "--model",
        model_name,
        "--ref_audio",
        reference_voice_file,
        "--ref_text",
        reference_text,
        "--gen_text",
        article.text_for_tts,
    ]

    result = subprocess.run(command, check=True)
    assert result.returncode == 0, f"Error: {result.stderr}, \n{result.stdout}"

    target_file = "tests/infer_cli_out.wav"
    assert Path(target_file).exists(), f"File {target_file} does not exist."

    mp3_file = convert_to_mp3(target_file)

    with open(mp3_file, "rb") as audio_file:
        audio_bytes = audio_file.read()

    return audio_bytes
```

If you're interested in thre rest of the code, [Podcaster](https://github.com/duarteocarmo/podcaster) is free and open source.

---