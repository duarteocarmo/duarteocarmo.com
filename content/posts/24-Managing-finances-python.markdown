title: Hacking on my finances
date: 18-10-2020 
description: Notes on using plain text accounting software.
thumbnail: images/fava.png

*Currently, my job has taken a lot of my time. But who doesn't have time for side projects? At the end of the day - they keep us sane. So I’ve been currently hacking on a good way of managing my finances - and oh boy I’m having fun.* 

**Update**: [Part 2: Beancount on Beanstalk](/blog/hacking-on-my-finances-part-2-beancount-on-beanstalk.html)

You can ready the whole story, or just jump to my [current setup.](#so-how-do-i-manage-my-finances-now) 

<center>
<img src="{static}/images/fava.png" alt="Fava example" style="max-width: 100%; margin-bottom: -1em">
<figcaption><a href='https://beancount.github.io/fava/' target='_blank'>Fava</a>, one of the tools I use for keeping my books</figcaption>
</center>

## But why do you even bother? 

I’ve been keeping track of my finances for about 10 years now. No it’s not something you should absolutely do, but being raised in a household where this was the norm, I’ve naturally found myself doing it from a “young age”. 

Of course there are many reasons to track your finances, but for me, the question is pretty simple: I just want to have the power to understand where my money goes, and where my money comes from. And since “information is power”, I’ve been a bit obsessed with documenting. 

## How I have tracked my finances in the past

Like every “tracking aficionado”, I started tracking all of my finances using mobile applications. I’ve used everything from [DailyCost](https://apps.apple.com/us/app/dailycost-expense-tracker/id566587079) to [Spending Tracker](https://apps.apple.com/us/app/spending-tracker/id548615579). But all of these had drawbacks. Not because of the apps themselves, but because they did not fit my mindset/workflow. I want to know how much I have on account X, and how much I owe to someone next month. And even though some modern alternatives already connect to your bank accounts, I wanted something more “hackable”. 

And so I fell into “Excel hell”. I found that I could use a simple app to track my spendings ([Spendee](https://www.spendee.com/)) and then, at regular intervals I would put that information into Excel. There, I would create my own overview of “how things are going”, and “where my money was spent”. 

But keeping track of things in Excel had various drawbacks:

- I had no connection to my banking accounts 
- Currency exchanges are a pain in the ass (I know there are plugins, but come on..)
- I had to create a lot of custom formulas, that were a pain to maintain
- Excel is proprietary software, and I don’t like depending on proprietary software
- The system was not programmable to my needs - hard to extend

So after 7 years tracking my finances in Excel - I decided to look for something better (for me at least)

## Enter plain text accounting

[Plain text accounting](https://plaintextaccounting.org/) is a movement, or even better, a community. It’s a group of people passionate about keeping track of their finances using plain text formats, programmable interfaces, and hackable workflows. 

Imagine having a txt file where you can manage all of your finances - and hack in workflows that fit your needs exactly. That sounded just like the solution I needed.

Upon further investigation of [command line applications](https://plaintextaccounting.org/#plain-text-accounting-apps) (because who likes GUIs?) that are inline with plain text accounting, I found [beancount](https://beancount.github.io/). There are also other alternatives such as [Ledger](https://www.ledger-cli.org/) (written in C++) or [hledger](https://hledger.org/) (written in Haskell). 

But hey, I’m a Python guy, and want to be able to hack on this to my needs, so I went with [beancount](https://beancount.github.io/).

## So how do I manage my finances now? 

*Disclaimer: This is how I do it - your current situation and preferences will most likely be very different from mine - so this is by no means a tutorial - simply a showcase*

### Out and about

At the end of the month, I like to be able to look back and see how much I have spent in different categories such as “Entertainment”, “Groceries”, “Shopping” etc. So when I’m out in about, I usually use [Spendee](https://www.spendee.com/) to keep track of those. Spendee has a whole world of other features - but I simply use it for tracking simple transactions.

### The central piece: [Beancount](https://beancount.github.io/docs/)

The whole overview of my finances, uses beancount. I’m not going to go deep on how awesome beancount is, or the whole feature set that it offers. (for that you can start with the incredible [documentation](https://beancount.github.io/docs/))
It basically takes a “beacount file” and allows you to generate several reports / consistency checks/ queries on that same file.  
Here’s an example of a beancount file:

```
; creating an account and setting some balances
2015-01-01 * "Opening Balance for checking account"
  Assets:US:BofA:Checking                         3490.52 USD
  Equity:Opening-Balances                        -3490.52 USD

; an example expense
2017-04-18 * "Verizon Wireless" ""
  Assets:US:BofA:Checking                          -85.18 USD
  Expenses:Home:Phone                               85.18 USD

; another example expense
2017-04-23 * "Wine-Tarner Cable" ""
  Assets:US:BofA:Checking                          -80.20 USD
  Expenses:Home:Internet                            80.20 USD
```

So every month, I take my spendings, input them into my beancount file, make sure my accounts and assets all match, and basically do my “bookkeeping” on that file. For this, I use a system called “Double entry counting” (learn more [here](https://beancount.github.io/docs/the_double_entry_counting_method.html)). 

### Analyzing everything: [Fava](https://beancount.github.io/fava/)

Even though beancount can generate some [reports](https://beancount.github.io/docs/running_beancount_and_generating_reports.html#tools), I have found that the terminal is not the best place to analyze data. 

Fortunately, [Fava](https://beancount.github.io/fava/) exists. Fava is a web interface for your beancount file. It allows you to have a nice to use, easy to navigate website, where you can:

- Have an overview of your accounts
- Run queries on your transactions (Using the [beanquery language](http://aumayr.github.io/beancount-sql-queries/))
- Visualize your data in different times/accounts/categories


### Access from anywhere

To make sure I can access my beancount files anywhere, I have kept all of them synced to a nice git repo that syncs with my server. 

I have also installed Fava on that server, which basically allows me to access my visualizations in any machine that has a web browser. 

And oh boy do I love this setup. 

## Closing thoughts

I’m still improving on this setup - creating custom scripts that evaluate my position given my constraints, automatically connect to my assets, and even alarm me if something not expected happened. 

And that’s the beauty of not using Excel. I’m now using something I can hack on and make my own - and even though that’s not a complete system - it’s a great system for me. 




*Thanks to [Martin Blais](https://github.com/blais) for creating beancount and for actively maintaining and documenting such an awesome tool.*


**Update:** This post has been featured in the awesome <a href="https://plaintextaccounting.org/#articles-blog-posts" target="_blank">plain text accounting blog</a>.
