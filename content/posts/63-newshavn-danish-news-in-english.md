title: NewsHavn: Danish news, in English
date: 02-26-2024 20:30
description: Automatic translation of Danish news using Go and Mistral 7B. 
status: published
thumbnail: images/63/newshavn.png

_Conversas de café_. Literally translated, means "coffee shop conversations". 

An upcoming election, the weather next week, a corruption scandal, a new policy. Just some examples of _Conversas de café_. 

As an expat living in Denmark for the past 7 years (without speaking the language), that's perhaps one of the things I miss most. Maybe it's because of where I'm from, but for me, water cooler conversations _are_ Culture. 

_Learn the language_, _use Google Translate_, _read [some](https://www.thelocal.dk/) expat focused website_. No thanks. I want to read the same stuff people around me read. I want to understand what worries _them_, not other expats.

Enter [NewsHavn](https://newshavn.duarteocarmo.com/).

<center>
<a href="https://newshavn.duarteocarmo.com" target="_blank">
<img src="{static}/images/63/website.png" alt="Newshavn.duarteocarmo.com" 
style="max-width:100%;border-radius: 2px">
<figcaption></figcaption>
</a>
</center>

Newshavn parses the RSS feeds of a couple of big Danish newspapers and uses [Mistral 7B](https://github.com/duarteocarmo/NewsHavn/blob/8758d1f8214e2c54c24c06d0c0ba42b92e78c474/parser/parse.go#L173) to translate them. The design is inspired by [NPR](https://text.npr.org/). The code is all [opensource](https://github.com/duarteocarmo/NewsHavn). 

For this one, I decided to use Go (again). I must say, Go is growing on me. Rust is fun and efficient, but I feel like Go strikes the right balance between strictness and flexibility. Another thing I love about Go is its concurrency model. [Goroutines](https://gobyexample.com/goroutines) are just beautiful, and make me want to write more concurrent code. It feels like it's a no-bullshit language, and I'm a fan of no-bullshit. 