title: Taralli: Home-Cooked Food Tracking Without the BS
description: Taralli is a home-cooked food tracking app that lets you write what you ate in any language and gives you back calories, macros, fiber, and food group — no scanning, no bullshit.
date: 7th of April 2025
status: published
thumbnail: images/79/cover.png

For years, I never really cared about *what* I ate, *how much* I ate, or *when* I ate it.

But sometime late last year, I finally decided to listen to Vitto. I started noticing that what I eat actually had an impact on how much I ran, how well I slept - and generally, how good I felt. So I decided to do what most people (at a certain point) do: I downloaded [the](https://www.myfitnesspal.com/) [usual](https://macrofactorapp.com/macrofactor/) [suspects](https://lifesum.com/).

Frustration quickly followed. I don't want the pizza from Trader Joe's, I want frozen pizza from [Pingo Doce](https://www.pingodoce.pt/). I'm not eating the Doritos sold in the American supermarket, I just ate the healthy ones from [Kvickly](https://kvickly.coop.dk/). I want to track two handfuls of peanuts. I want to track a _pão de deus com queijo_ from the [Padaria Portuguesa](https://apadariaportuguesa.pt/). With the usual suspects, it was painful. Everything was either too specific, too general, or matched a food database I didn't care about.

After talking with Nuno and a couple of other friends, I quickly realized they weren't actually taking photos, scanning barcodes, or meticulously entering calories and macros in these apps. They were asking ChatGPT. That made sense. For some - certainly for me, it's actually more important to track _something_ than to be extremely accurate. Perfect is the enemy of good. It still holds.

Enter [Taralli](https://apps.apple.com/dk/app/taralli/id6743634022).

![taralli app screenshots]({static}/images/79/taralli-screenshot-food.webp)  

Taralli allows you to track *anything* you eat (really!). A [pão com chouriço](https://www.pingodoce.pt/receitas/pao-com-chourico/), a [pão de Deus](https://encomendas.apadariaportuguesa.pt/produto/pao-de-deus/), half a handful of peanuts – whatever language, whatever text, whatever you're eating, Taralli can handle it. Just type what you ate, and it'll handle the rest. It gives you macros, calories, fiber, and food group. It also has a bunch of analytics from the past week so you can see what's going on at a high level. You can also connect it to Apple Health to track your weight (if you're interested in that sort of stuff.)

Taralli is built using [SwiftUI](https://developer.apple.com/xcode/swiftui/). What would have taken me 3-4 months and a lot of googling about SwiftUI took me something like a couple of weeks and the help of Claude 3.7 Sonnet (and still a lot of googling about SwiftUI I have to admit). I'm not sure I would say the whole thing was ["vibe coded"](https://x.com/karpathy/status/1886192184808149383?lang=en). I mean, I _still_ found some bugs, I _still_ had to make some important decisions about how things work together and are architected - otherwise this app would be a mess. But I have to admit that building the whole thing is way easier now. Except the Apple review process, I can confirm that one is still painful.

For estimating the calories I'm using `gpt-4o-mini` with some [structured generation](https://platform.openai.com/docs/guides/structured-outputs) served over FastAPI. It actually sucks right now. Accuracy isn’t great, and it makes some pretty basic mistakes. I’ve got plans to fix that — but I’ll leave them for another release. [Remember](https://duarteocarmo.com/blog/simple-software), first make it work, _then_ make it pretty.

![taralli app screenshots]({static}/images/79/taralli-screenshot-graphs.webp)  

You'll notice that unlike other apps, Taralli doesn't tell you what to do. That's because I don't care what you do. The goal of Taralli is to help you track. And its goal stops there. Just write anything in the text box. The more specific you are, the better.

So here's [Taralli](https://apps.apple.com/dk/app/taralli/id6743634022). Food tracking without the BS.