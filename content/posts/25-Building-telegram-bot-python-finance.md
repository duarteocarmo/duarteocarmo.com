title: Building a Telegram bot in Python to track your portfolio
date: 23-11-2020 
description: Building a telegram bot using Python to track your investment portfolio


_In the past months, I’ve been spending a lot of time researching about investing: building your portfolio, back testing it, tracking its performance, and acting accordingly. One of these endeavors (and my stubbornness to build my own tools) has led me to create a telegram bot, here’s a small write up in hope you'll build your own._

## A Telegram Bot? Have you heard of Yahoo Finance?

Yes, I have actually heard about and used [Yahoo Finance](https://finance.yahoo.com/) to track my portfolio, but there are a couple of reasons why I think it doesn't quite cut it:

- **<u>Notification systems</u>**: When you set up an app such as [Yahoo Finance](https://apps.apple.com/us/app/yahoo-finance/id328412701) with your Portfolio, you can either create a widget that you visit every so often, or you can set up a system to alert you about a particular set of stocks. I consider myself a passive investor, and will not check my performance every day, or even every week. I want a system that adapts to my "passive needs". Every so often let me know the worth of my portfolio. That's it. 
- **<u>Accuracy</u>**: Before researching more on the topic I thought investment instruments (i.e., stocks or funds) were pretty standardized across apps and markets. Well, I was clearly wrong. Most financial data is a bit messy. Some apps can't show your particular funds, some do, but reference other exchanges. The whole thing is a bit of a mess. So by building something I control, I can make sure I am getting the right information from the right sources, at the right time. (Particularly being an [European investor](https://indexfundinvestor.eu/) - where information is even more scarce)
- **<u>Customization</u>**: I don't want to simply track the value of my portfolio, I also want to control how it has evolved according to my expectations. And why stop there? There is a very specific set of items I want to keep track of. Let's say tomorrow I want to know a particular piece of information about a recent IPO. Building my own system allows me to customize it exactly to both my present AND my future needs. 

Given these constraints (and my stubbornness to build my own tools), I decided I needed some sort of "programmable" notification system. Having heard a bit about telegram/discord bots, and being a subscriber to a couple of telegram channels myself, I decided to give [Telegram](https://telegram.org/) a shot. 

## Building a basic bot

I can't say I was surprised to see a great Python wrapper written exactly for this purpose: [python-telegram-bot](https://github.com/python-telegram-bot/python-telegram-bot). Can't tell you how easy it was to set everything up using their extensive [Wiki](https://github.com/python-telegram-bot/python-telegram-bot/wiki). 

Let me walk you a bit through the process. You start by installing the library:

```bash
$ pip3 install python-telegram-bot 
```

Once that's up an running, I created a simple "shell" bot that responds whenever you send the message `/start`, let's call it `bot.py`:

```python
# bot.py
from telegram.ext import (
    Updater,
    CommandHandler,
    MessageHandler,
    Filters,
    CallbackContext,
)
from telegram import Update

# define your API token: https://core.telegram.org/bots#3-how-do-i-create-a-bot 
API_TOKEN = "YOUR API TOKEN" 

# what your bot should reply when we send the /start command
def start(update: Update, context: CallbackContext):
    update.message.reply_text("Welcome :)")

# the main function, with some boilerplate
def main():
    updater = Updater(API_TOKEN, use_context=True)
    dispatcher = updater.dispatcher
    dispatcher.add_handler(CommandHandler("start", start)) # this line is what matters most
    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()
```

If you now navigate back to your terminal and simply run this script by doing `python bot.py`, you'll see that something is running in your terminal. Then, when you message your telegram bot, you get a nice little prompt back with "Welcome :)". 

## Getting information on your portfolio (example)

But we want to get a little more fancy, ideally, as an example, let's say that we want our bot to inform us on our portfolio worth. We create a `portfolio.py` file:

```python
# portfolio.py
import yfinance as yf # pip install yfinance

# you bought 2 stocks of Microsoft
ACQUISITION_PRICE = 150
ACQUISITION_QTTY = 2
STOCK_NAME = "MSFT"

# a function that returns our gains on the purchase of MSFT stocks
def get_current_value():
    msft = yf.Ticker("MSFT")
    last_value = yf.info.get("previousClose")
    
    previous_worth = ACQUISITION_QTTY * ACQUISITION_PRICE 
    current_worth = ACQUISITION_QTTY * last_value
    gain = current_worth - previous_growth
    
    return f"Your current gains on {STOCK_NAME}: {gain:.2f}"
```

The above function, `get_current_value` will inform on how much your Microsoft stock is worth at any point in time, from when you purchased it. 

## Integrating financial updates with our Telegram bot

Now that we have both a telegram bot and a basic script to update us on our portfolio performance, it's time to bring both together. 

To do so, we create two functions:

- `alarm`: a function that gets the value of our portfolio, and returns it to the user as a response
- `set_update`: a function that makes our bot run our alarm once a week (to decrease our stress level)

```python
# ... the rest of your bot.py file

def alarm(context): # FIRST IMPORTANT ADDITION
    job = context.job # get context
    text = get_current_value() # run our financial update
    context.bot.send_message(job.context, text=text) # respond with the string returned by the function

def set_update(update: Update, context: CallbackContext): # SECOND ADDITION
    chat_id = update.message.chat_id # get our chat ID
    secconds_between_runs = 24 * 7 * 60 * 60  # run every week (24 hours * 7 days * 60 mins * 60 secs)

    update.message.reply_text("Financial updates will run!") # confirm to user that it will run
    context.job_queue.run_repeating(
        alarm, interval=secconds_between_runs, first=30, context=chat_id
    ) # run the alarm as a recurring update and the first message runs 30 seconds after our update is set

def main():
    updater = Updater(API_TOKEN, use_context=True)
    dispatcher = updater.dispatcher
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("set_update", set_update)) # NEW COMMAND
    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()
```

After this, every time you send your bot the message `/set_update`, it will schedule our financial update to be run every week! (feel free to try it live by making it run every 10 minutes or so)

## Adding a bit of security and deploying

We don't want the whole world to access our bot (or our financial updates), so, it's smart to limit your bot to respond only to yourself (or your telegram username). And easy way to do so is to add an `if` statement to your `set_update` function like so:

```python
def set_update(update: Update, context: CallbackContext):
	...
    if username == AUTHORIZED_USERNAME:
        update.message.reply_text("Financial updates will run!")
        context.job_queue.run_repeating(
            alarm, interval=every_seconds, first=30, context=chat_id
        )
    else:
        update.message.reply_text(
            "Sorry, but you are not authorized to use this command.."
        )
```

This ensures your bot only gives financial updates to YOU, which is pretty important.. 

For deployment, you only need to leave your `bot.py` script running somewhere. I chose to use one of my Virtual Private Servers and run the script in a [tmux](https://en.wikipedia.org/wiki/Tmux) session. But there are also some [good alternatives in the docs](https://github.com/python-telegram-bot/python-telegram-bot/wiki/Where-to-host-Telegram-Bots) if you re interested!

## Closing thoughts

This was a very simple example of how you can get your bot up and running really quickly. But some things differ from the setup that I have actually in place (and the one you'll probably build):

- Here we used the `yfinance` data to track performance, but you can use WHATEVER you want. As an example, my bot is running some scrappers on stock exchanges related to my portfolio (and not available through the library)
- You can also add forward looking KPIs and information (what was the best performing stock of the ones you're watching?)
- Add some alerts about news using a library like [Newspaper3k](https://newspaper.readthedocs.io/en/latest/)! To make everything even more dynamic :) 

This is why hacking on your own tools is more rewarding than just using an off the shelf app: Yes, it takes time, and yes, it can seem a lot less "fancy". But you learn a lot while doing it, and more importantly: you build it to become YOUR tool, not A tool. 

<br>

_Thanks for reading! If you like this post, consider [reaching out](mailto:me@duarteocarmo.com)! I'm thinking of starting a newsletter, and I'm interested in knowing if you would potentially sign up!_
