title: A simple system to stay in touch with people
date: 03-21-2022 14:30
description: A simple python script that reminds you to reach out
status: published
slug: infrequent-tiny-crm

<img src="{static}/images/37/infrequent_screenshot.png" alt="Embeddings" style="max-width:100%;">

Someone once told me that my professional network is one of the most important things I'll build throughout my career. For years I've struggled to find a system that would help me stay in touch with my network. So I decided to build my own - let me show you how it works. 

## The idea

The idea is pretty simple, you want to stay in touch with a group of people, by talking to them every X days/months/years. Let's say you want to keep up with Jane every two months. If two months have passed and you haven't talked, you should get nudged into doing it. 

To solve this, I started with a recurring item in my to-do list, but it quickly got messy. I tested [Dex](https://getdex.com/), but they would only allow me to keep tabs on 15 people. [Monica](https://www.monicahq.com/) looks like a fun deployment challenge - that's not what I'm looking for. 

What I really wanted was something *simple*. Something like other [small things](https://kindle-highlights.email/) I've built before? I bet I could build something simple using a bit of Python. 

## How it works

At the core of the tool is a simple folder. In it, every person that I want to stay in touch with, gets their own markdown file:

```bash
├── infrequent.py
└── people
    ├── john-snow.md
    ├── arya-stark.md
    ├── ...
    └── sansa-stark.md
```

At the top of the file: the person's name, our relationship, and the frequency at which we should keep in touch. After that, every entry is a header with a date of contact, and some notes about what happened in that date. Here's an example:

```md
Name: John Snow
Relationship: Idol
Interval(every): 2 months

## 21-03-2022
- Was recruiting for more troops
- Dead walkers in the wall

## 13-03-2022
- Had to go to the wall 
- He was starting to notice something changing in the weahter
```

Using a small script I call `infrequent.py`, I parse all the files in the `people` folder. The script retrieves the person's details and dates of interactions. Using some datetime logic, I then identify the people I'm late reaching out to:

```python
...
interaction_dates.sort()
last_interaction_date = interaction_dates[-1]
next_interaction_date = last_interaction_date + time_delta

message = f"{name} - {relation} - (Cadency: every {contact_frequency}, {delay_in_days} days passed since last contact)"

if next_interaction_date < today:
    to_contact.append(message)
...
```

Once every person is processed, the same script sends me an email with the people I'm late reaching out to, using [SES](https://aws.amazon.com/ses/). 


## How I use it

I store the `people` folder and the `infrequent.py` script in a GitHub repository - [similar to this one](https://github.com/duarteocarmo/tiny-crm-demo). Thanks to GitHub actions, the script runs every Friday morning. When it does, I receive an email with the names of people I'm late reaching out to. 

Every time I interact with someone in the folder, I update their file, and push the changes back to GitHub. It's simple, and works surprisingly well. 

[Here's a copy of my repo](https://github.com/duarteocarmo/tiny-crm-demo) in case you want to play around with the script. Feel free to [email me](mailto:me@duarteocarmo.com) if you have problems getting it to run. 

*This post was inspired by [this](https://sive.rs/hundreds) article*













