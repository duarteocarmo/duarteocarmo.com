title: Fine-tuning FLAN-T5 to replace your friends
date: 17-05-2023 16:30
description: #TODO
status: draft
slug: fine-tune-flan-t5
thumbnail: #TODO


They say that the best way to learn about something is to build it yourself. Everyone talks about OpenAI this, and OpenAI that. How about we fine tine a Large Language Model ourselves? How hard can it really be? Spoiler, it's not the easiest thing, but I'm here to talk you through it. 

In this blog post, you'll learn how to fine tune a Large Language Model (more particularly, Google's [FLAN-T5](https://huggingface.co/google/flan-t5-base)). For a particularly funny example, in this example, I'll use the the Telegram group chat where I talk with my friends - but you can use whatever you like. 


This blog post also comes in form of a notebook that you can download and run [right here](). 

Here's how we'll structure things: 

1. [Why FLAN-T5](#1-why-flan-t5)
2. [Setting up your environment](#2-setting-up-the-environment) 
3. [Preparing the data](#3-preparing-the-data)
4. [Fine-tuning the model](#4-fine-tuning-the-model)
5. [Curating the generation](#5-curating-the-generation)


Even though I love taking credit for ideas that are not mine, this blog post was inspired by the work of some other awesome folks. Particularly [this](https://www.philschmid.de/fine-tune-flan-t5#1-setup-development-environment) one, and [this](https://www.izzy.co/blogs/robo-boys.html) one. 

Let's get started. 

## 1. Why FLAN-T5

There are a lot of Large Language Models (e.g., LLMs) out there. In the past few months, and the explosion of things like GPT-3 and GPT-4, lots of companies and open source organizations have started building their own LLMs. Some of these models [leaked](https://www.theverge.com/2023/3/8/23629362/meta-ai-language-model-llama-leak-online-misuse), others are [powerful](https://openai.com/) but only available through an API.

There are some of theses LLMs that are actually free an open source, even for comercial use. Eugene Yan, has compiled a great [repo](https://github.com/eugeneyan/open-llms) with some of these options. 

In 2020, Google released [Exploring the Limits of Transfer Learning with a Unified Text-to-Text Transformer](https://arxiv.org/pdf/1910.10683.pdf), where they presented their T5 model. T5 is a encoder-decoder model that was trained in a variety of tasks (e.g., translate to german, summarize the following sentence, etc). [FLAN-T5](https://huggingface.co/docs/transformers/model_doc/flan-t5) is basically the exact same thing as T5, but pretty much [better at everything it does](https://huggingface.co/google/flan-t5-small#tldr). 

![](https://camo.githubusercontent.com/623b4dea0b653f2ad3f36c71ebfe749a677ac0a1/68747470733a2f2f6d69726f2e6d656469756d2e636f6d2f6d61782f343030362f312a44304a31674e51663876727255704b657944387750412e706e67)

There are a couple of other reasons why we're going to go with Flan-T5 for this guide: 

* It's free, open source, and commercially available
* It has several [sizes](https://huggingface.co/docs/transformers/model_doc/flan-t5#overview) we can use (from small, all the way to xxl)
* It's compatible with the whole [Hugging Face](https://huggingface.co) 🤗 ecosystem, making our life easier 

With that. Let's setup our environment. 

## 2. Setting up the environment

_Note: If you have a local machine with a GPU, feel free to skip until the installation section. This tutorial was run on a NVIDIA A100 with 40GB of RAM_

Before we start, please make sure you have a [Hugging Face](https://huggingface.co) account. Once you have that set up, create and copy a new token. Paste it somewhere, we'll need it for later. 


The following cell, will install all required python libraries, as well as some local ones we'll need. (e.g., git, git-lfs)


```python
%%capture
%pip install pytesseract evaluate tqdm transformers datasets rouge-score accelerate nltk tensorboard jupyter-black py7zr --upgrade
!apt-get install git --yes
!apt-get install git-lfs --yes
```

Take your Hugging Face token, and replace it with in the field below. This will log you into the Hugging Face hub, which we'll need to push and pull models. 


```python
%%capture
!huggingface-cli login --token XXXXXXXXXXXXXXXX
```



## 3. Preparing the data

Let' start by defining some variables we'll need. Don't worry, I'll explain what each one of these means.


```python
import json
import pandas
import jupyter_black
from datetime import timedelta

from datasets import Dataset

jupyter_black.load()

TELEGRAM_EXPORT = "anonym_telegram.json"  # anonymized for obvious reasons
CONVERSATION_LIMIT = 20_000  # limit number of messages
TEST_SIZE = 0.2  # % of test data
IS_NEW_SESSION_CUTOFF_MINS = (
    120  # if the time between messages is more than this, it's a new session
)
```

Let's preprocess this into a dataframe for our needs: 


```python
# load data in
with open(TELEGRAM_EXPORT, "r") as f:
    data = json.load(f)
    messages = data["messages"]

# create a dataframe
df = pandas.DataFrame(messages)[["text", "from", "date"]]

# filter empty messages
df = df[df["from"].isna() == False]
df = df[df["text"].isna() == False]
df = df[df["text"].str.len() > 0]

df["date"] = pandas.to_datetime(df["date"])  # convert to datetime
df.sort_values("date", inplace=True)  # sort by date
df = df.tail(CONVERSATION_LIMIT)  # limit number of messages
```


```python
df.sample(5, random_state=134314)  # show some random samples
```


<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>text</th>
      <th>from</th>
      <th>date</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>237648</th>
      <td>Bem malta</td>
      <td>André Ferreira</td>
      <td>2023-02-20 14:57:00</td>
    </tr>
    <tr>
      <th>253995</th>
      <td>Não sei o nome</td>
      <td>Pedro Oliveira</td>
      <td>2023-05-01 18:41:40</td>
    </tr>
    <tr>
      <th>242455</th>
      <td>Ui. Aquele olho meio aberto meio zarolho?</td>
      <td>André Ferreira</td>
      <td>2023-03-08 19:23:44</td>
    </tr>
    <tr>
      <th>249497</th>
      <td>Adidas? Comercialuxo não?</td>
      <td>Luís Rodrigues</td>
      <td>2023-04-05 14:48:41</td>
    </tr>
    <tr>
      <th>254731</th>
      <td>Tens cá.</td>
      <td>Tiago Pereira</td>
      <td>2023-05-04 16:43:06</td>
    </tr>
  </tbody>
</table>
</div>



Now, the goal is to get our data into a format where the model can understand the conversation, and respond to what has been going on. Something like: 

```json
{
    "conversation": "Person X: Where were you yesterday?\nPerson Y: I was at home! You?",
    "response": "Person X: Me too, but thought of going out."
}
```

This will allow the model to see a thread and respond in the most realistic manner possible to the conversation that was already going on. However, we also know that group chats are pretty async, so we don't necessarily want a "good morning" message, to be a direct response to whatever happened last night. 


```python
# telegram exports have some artifacts, let's clean them up
def clean_text(text: str) -> str:
    if isinstance(text, list):
        text = "".join([o.get("text", o) if isinstance(o, dict) else o for o in text])

    return text


# clean up and rename columns
df["text"] = df["text"].apply(clean_text)
df["chat"] = "telegram"
df.rename(
    columns={"from": "sender", "date": "message_date", "text": "response"}, inplace=True
)


# create new sessions
df["last_event"] = df.groupby("chat")["message_date"].shift(1)
df["is_new_session"] = (
    (df["message_date"] - df["last_event"]).fillna(
        pandas.Timedelta(minutes=IS_NEW_SESSION_CUTOFF_MINS)
    )
    >= timedelta(minutes=IS_NEW_SESSION_CUTOFF_MINS)
).astype(int)
df["chat_session_id"] = (
    df.sort_values(["chat", "message_date"]).groupby("chat")["is_new_session"].cumsum()
)
```

Now that we have everything setup, it's time to create a `conversation` column, that has all the messages before a certain response: 


```python
sess_dict = df.to_dict("records")
items = []
counter = 0
for row in sess_dict:
    context = []
    cstring = ""
    for i in range(10, 0, -1):
        if sess_dict[counter - i]["chat_session_id"] == row["chat_session_id"]:
            msg = (
                f"{sess_dict[counter-i]['sender']}: {sess_dict[counter-i]['response']}"
            )
            if len(context) > 0:
                cstring += "\n"
            context.append(msg)
            cstring += msg
    if len(context) < 2:
        for i in range(5, 0, -1):
            msg = (
                f"{sess_dict[counter-i]['sender']}: {sess_dict[counter-i]['response']}"
            )
            context.append(msg)
            cstring += "\n"
            cstring += msg
    items.append(cstring)
    counter += 1


# create the conversation column
df["conversation"] = items

# create the response column
df["response"] = df.apply(lambda row: f"{row.sender}: {row.response}", axis=1)

print(f"Your dataframe shape is {df.shape}")
print(f"You have the following columns: {', '.join(df.columns.tolist())}")

# Your dataframe shape is (20000, 8)
# You have the following columns: response, sender, message_date, chat, last_event, is_new_session, chat_session_id, conversation
```

Let's see what a single example looks like: 

```python
item = df.sample(1, random_state=314)[["conversation", "response", "sender"]].to_dict(
    "records"
)[-1]

print(f"Conversation:\n{item['conversation']}\n")
print(f"Response:\n{item['response']}\n")

#    Conversation:
#    Hugo Silva: Lembram se do meu amigo alex frances?
#    Tiago Pereira: Claro ya
#    Hugo Silva: Ele correu a maratona de paris outra vez..
#    Tiago Pereira: E…
#    Tiago Pereira: Ou é só isso?
#    Hugo Silva: Numero 304 overall...
#    Hugo Silva: Crl
#    Tiago Pereira: Eia cum crlh
#    Hugo Silva: Pa doente
#    Tiago Pereira: 3’46. Que louco fds
#    
#    Response:
#    Hugo Silva: Doente completo
```

Our final preprocessing step is to load our datfram in the [Datasets](https://huggingface.co/docs/datasets/index) format: 


```python
cols_for_dataset = ["conversation", "response"]
df = df[cols_for_dataset]

data = Dataset.from_pandas(df).train_test_split(test_size=0.2)
print(data)

#   DatasetDict({
#       train: Dataset({
#           features: ['conversation', 'response', '__index_level_0__'],
#           num_rows: 16000
#       })
#       test: Dataset({
#           features: ['conversation', 'response', '__index_level_0__'],
#           num_rows: 4000
#       })
#   })
```


Great. Now let's prepare the fine-tuning of the model!

## 4. Fine-tuning the model

## 5. Curating the generation
