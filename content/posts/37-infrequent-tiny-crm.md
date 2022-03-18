title: Infrequent: The smallest CRM you've ever used  
date: 03-21-2022 09:00
description: A tiny CRM that reminds you of who to talk to
status: draft
slug: infrequent-tiny-crm

<a href="https://projector.tensorflow.org/?config=https://raw.githubusercontent.com/duarteocarmo/esco-visualizations/master/projector_config.json">
<img src="{static}/images/37/infrequent_screenshot.png" alt="Embeddings" style="max-width:100%;">
</a>

Someone once gave me advice that your professional network is one of the most important things you'll build during your career. For years I've struggled to find a system that would allow me to regularly stay in touch with my network. So I decided to build my own - let me show you how it works. 


## The idea 

The idea is pretty simple, you have a group of people that you would like to stay in touch with by talking to them every X days/months/years. If I want to keep up with Jane every 2 months, and 2 months have passed and we haven't talked, I want to get nudged into talking to her. 

I started with recurring item in my to-do list, but it quickly got messy. I tested [Dex](https://getdex.com/), but they only allowed my to keep tabs on 15 people. [Monica](https://www.monicahq.com/) looked like a fun deployment challenge, but *no thanks*. 

What I really wanted was something simple. Something similar to [small things](https://kindle-highlights.email/) I've built before. 

I bet I could build something simple in Python. 


## Building the smallest CRM you've ever seen 


```bash
├── infrequent.py
└── people
    ├── john-snow.md
    ├── arya-stark.md
    ├── ...
    └── sansa-stark.md
```


At the core of the tool is a folder, where every person that I want to keep in touch with, gets their own markdown file. A the top, the file contains the person's name, our relationship, the interval at which I want to stay in contact with them. After that, every entry is a header with a date of contact, and some notes about what happened in that date. 

```markdown
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

Using a small scrip I called `infrequent.py`, I then parse all the files in the `people` folder. This script retrieves the person's details and dates of interactions. Using some datetime logic it then stores the people I need to reach out to. 

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

Once all the files are parsed, the same script then sends me an email with the people I need to reach out to, using [Amazon SES](https://aws.amazon.com/ses/). 

## How I use `infrequent.py`

I have the `people` folder and the `infrequent.py` script stored in a GitHub repository. Thanks to GitHub actions, every Friday morning, I receive an email with people I'm late reaching out to. 

Then, every time I interact with someone in the folder, I update their file, and push the changes back to GitHub. It works surprisingly well!

I created this [shell GitHub repo](https://github.com/duarteocarmo/tiny-crm-demo) in case you want to play around with the script. Feel free to email me if you have problems getting it to run. 

## Why would you even? 

There is a long list of reasons why I think this approach beats something "off-the-shelf". Most of them are personal. But some of them may also apply to you: 

- I'm not *tied* into any personal CRM provider, and own everything about this data
- I get to infinitely tweak and adapt this system to my liking (include LinkedIn links, automatically emailing people, etc)
- It's free! Thanks GitHub actions 


*This post was inspired by [this](https://sive.rs/hundreds) post, [this](https://jakobgreenfeld.com/stay-in-touch) post, and [this](https://news.ycombinator.com/item?id=30334269) HN comment.* 













