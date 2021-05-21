title: Can I go home yet? 
date: 23-07-2020 
description: An investigation on Denmark's travel ban and how its implementation criteria has evolved since.
thumbnail: images/others.png

On the 18th of June, Denmark [announced new travel policies after the Coronavirus outbreak](https://www.reuters.com/article/us-health-coronavirus-denmark-borders/denmark-will-reopen-to-most-european-nations-except-portugal-much-of-sweden-idUSKBN23P1OD). From that date on, it allowed travel to all European countries except for Portugal and Sweden. Of course, this caused several news outlets to write on the issue ([Local.dk](https://www.thelocal.dk/20200618/denmark-opens-to-tourists-from-every-eu-country-but-sweden), [Politiken.dk](https://politiken.dk/rejser/art7839386/Nu-kan-danskerne-tage-til-endnu-flere-steder-i-Sverige), [Reuters.com](https://www.reuters.com/article/us-health-coronavirus-denmark-borders/denmark-will-reopen-to-most-european-nations-except-portugal-much-of-sweden-idUSKBN23P1OD)). But now, one month later, let us try to investigate the issue, and whether these bans make sense.

Curious about why the decision was made, I stumbled upon a couple of interesting official danish sources on the decision. The first is [a statement](https://www.justitsministeriet.dk/nyt-og-presse/pressemeddelelser/2020/danmark-aabner-graenserne-yderligere-og-lemper) where the official new policy was stated. This statement dates from June 18th and states that:

*"[...]To be "open", a country must have less than 20 infected per. 100,000 inhabitants per. week. Once a country is open, the critical level for when a country changes status to "quarantine country" will be at 30 infected per. 100,000 inhabitants.[...]"*

I also stumbled upon the [official document](https://www.ssi.dk/-/media/arkiv/dk/aktuelt/sygdomsudbrud/covid19/covid-19-rejsekriterier/16_07_2020_tors/tabel_11_1.pdf?la=da) where all of these calculations where made. Where we can clearly see that both Portugal and Sweden have more than 20 infected people per week per 100.000 people. On the other hand, countries such as Spain, or Romania have less than that number, and were hence declared as "open for travel".

Since I am planning to go to Denmark on the beginning of August, and have heard no updates on the situation since, let's try to see how the situation evolved since the announcement:

<center>
<img src="{static}/images/portugal.png" alt="Vim" style="max-width: 100%">
</center>

**A good initial decision.** Taking data from [the official Johns Hopkins repository](https://github.com/CSSEGISandData/COVID-19), and some [manipulation](https://nbhub.duarteocarmo.com/notebook/573bf718). I was able to plot the number of cases per 100.000 people of the last 7 days, for every day since February 1st. We can clearly see that in the date of the announcement, Portuguese cases were in the *Orange Zone* (.i.e slightly above 20 per 100k pax per week). However, you might notice that in the last couple of weeks, the number of cases in Portugal has started to decrease, falling into the *Open to travel zone*. 

**Coronavirus is unpredictable.** In the original [list of travel bans](https://www.ssi.dk/-/media/arkiv/dk/aktuelt/sygdomsudbrud/covid19/covid-19-rejsekriterier/16_07_2020_tors/tabel_11_1.pdf?la=da), countries such as Spain and Romania (to my surprise), were green lighted and allowed traveling to and from. Because at the date of the announcement, their number of cases per 100k people fell below 20. 

Has this changed?

Yes!!

<center>
<img src="{static}/images/others.png" alt="Vim" style="max-width: 100%">
</center>

Upon closer inspection, notice how the number of cases per capita in Portugal has decreased in the last couple of weeks. On the other hand, **the metric for Spain and Romania** has exploded. This means that, according to the original criteria, these two countries should now be banned from all travel (Romania even approaches the red *Quarantine region*).

To answer the original question of this post: Yes, I should be allowed to go home now. (I'm from Portugal but live in Denmark.)

But that's just a tip of a large iceberg. And a bit shallow on my behalf. 

Let's take some real conclusions:

* **Coronavirus response is unstable:** Coronavirus moves extremely fast, what was true for Portugal a month ago (cases rising) might not be true a month after. And what was true for Spain a month ago can also start changing very quickly. 
* **Policy is hard:**  Policy making, especially in such times, is no small task. I love that Denmark can swiftly propose a legislation that is transparent and measurable. 
* **Metrics should be regularly updated:** Having chosen a specific metric to define travel restrictions, we should make sure to update it regularly. As far as I know, the [original list](https://www.ssi.dk/-/media/arkiv/dk/aktuelt/sygdomsudbrud/covid19/covid-19-rejsekriterier/16_07_2020_tors/tabel_11_1.pdf?la=da) only updates every 2 weeks. But as we have seen here, a lot of things can change in 2 weeks. 


Thanks for reading my rant about going home 😆!

**Update:** [Here's a link](https://mybinder.org/v2/gh/duarteocarmo/canigohome/master?urlpath=%2Fvoila%2Frender%2Fnotebooks%2FCanIgoHome.ipynb) for a live dashboard of the stats. 


**Update 2:** The list of banned countries [has been updated](https://www.ssi.dk/-/media/arkiv/dk/aktuelt/sygdomsudbrud/covid19/covid-19-rejsekriterier/30_07_2020_83ha/tabel_11_1_europa.pdf?la=da) and I will be able to return on Sunday (2/8/2020).
