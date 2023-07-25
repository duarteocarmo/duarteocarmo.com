title: Four years of Python
date: 10-06-2021
description: Lessons learned from fours years of writing Python
status: published
slug: four-years-python
thumbnail: images/python-illustration.png

The other day I realized: I've been programming in Python for about 4 years now. I do get paid to write code, but for some reason still don't consider myself a _pro._ I did learn some valuable lessons though.

For those who just got started with Python, you'll hopefully take something out of these lessons. For the experienced, see this as a celebration of our beloved language.

### Reading is better than Googling

A couple of years ago, something changed in my workflow: When learning a new library (e.g,. transformers), instead of recklessly googling for how to do things, I actually started reading the library's documentation. I've noticed that reading documentation actually gives me a much better understanding of the library and the features I want to use. Also, when doing so, I actually understand better the full power of every external dependency I add to my project, which is much more fulfilling then Googling and forgetting.

What led me to read more docs, was the sheer trouble in setting up Vim's auto complete. Now that I don't have it - I must say I don't miss it. ([supertab](https://github.com/duarteocarmo/dotfiles/blob/38a7343b56dddc7bcd3a1625bd729d826da268b0/.config/nvim/init.vim#L36) is just fine, and makes me study docs when I don't know what I'm doing)

### Explicit is better than implicit

As you get more experienced writing code, you'll start making your code more and more concise. As you optimize (e.g., list comprehensions, case matching), your code will become harder to read.

And I believe Python was (and _is_) designed this way. [Explicit is better than implicit](https://www.python.org/dev/peps/pep-0020/#id2), so be careful when mastering the full power of Python. Brandon Rhode's talk below summarizes this phenomenon perfectly:

<center>
<iframe allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen="" src="https://www.youtube-nocookie.com/embed/S0No2zSJmks?start=869" title="YouTube video player" width="95%" height="330" frameborder="0"></iframe>
</center>

### First make it work then make it pretty

When all of those repos start pilling up, you'll notice that you'll start thinking of all of the smallest details your project needs to accomplish from the start. How will I test this? How will I package it? What type of abstractions will I build?

I still remember one of my first managers telling me _"first make it work, THEN make it pretty"._ Damn that was good advice. Keep things super simple from the start, and add complexity as you come across it. You might notice some things start being duplicated, or convoluted, that's when it's time to abstract them.

### Test early, and test often

Writing code can be an unrewarding feat. Often, you'll develop features in your code that do not directly benefit your end-users or business owners. An end-user does not care if you've used Heroku or Elastic Beanstalk or a certain class. Worse: end-users don't _even_ notice it.

Testing is often downplayed by management. "Why are you spending a week on something that does not benefit our customers directly? That seems low priority."

Remember to _not only_ start testing early, but to communicate to your stakeholders the importance, and benefit of testing (e.g., reliability, robustness, ability to develop faster in the future, up time..).

### Continuously learn

Dad's a doctor - and from a very young age I've seen him studying every weekend for a couple of hours. He also regularly goes to conferences, and learns whatever there was new to learn in his field.

We're not doctors, but [our craft](https://www.calnewport.com/blog/2011/08/11/the-career-craftsman-manifesto/) lies in creating reliable, fast, and scalable systems; in this case, by leveraging Python.

![alt-text-2]({static}/images/python-books.png)

Whether it's contributing to open-source, going to [PyCon](https://pycon.org/) or [PyData](https://pydata.org/), or answering questions in Stack Overflow - we should strive to get continuously better in our craft. Recently, [Practices of the Python Pro by Dane Hillard](https://www.manning.com/books/practices-of-the-python-pro), and The [Hacker's Guide to Scaling Python by Julien Danjou](https://scaling-python.com/) have been incredibly useful in further developing my knowledge of the language.

The more I work with Python (and other languages), the more I fall in love with our craft. On the surface, it's pretty easy to get a small script running, and doing something simple.

However, as your work evolves, and you grow, things start getting complicated, convoluted, and challenging. And that's where these principles can make a difference.

See you out there, fellow Pythonista.
