title: The short tale of an online scam
date: 24-06-2021
description: How I used Python to get back at an online scammer - and what I discovered in the process
status: published
thumbnail: images/30/cover.png
slug: tale-online-scammer-python

I'm moving places soon. I absolutely hate moving - but hey, it's like everything else in life: you push through. This time, there was a nice plot twist: someone tried to scam me online. This made things... interesting. Let's talk about it. 

## When it sounds too good to be true it's because...

As usual, like everyone in Denmark, I put up my old bed for sale in [DBA.dk](https://www.dba.dk/). It's the Danish version of Craigslist, I don't use it that much but has served useful in the past. After posting it, two days went by and nobody replied. But then I received an interesting WhatsApp message: 

![alt-text-1]({static}/images/30/whatsapp_screenshot.png)  

Check [this](https://github.com/duarteocarmo/dba_scam/tree/master/screenshots) link for screenshots of the whole conversation. 

For those not fluent in Danish, "Dimitriy" (the name on his WhatsApp account) is telling me that he'll purchase the bed I'm selling. He also suggests that we should use a *very* convenient service by [PostNord](https://www.postnord.dk/en) (the danish post company). This service supposedly arrives at my place, packages everything up, and brings it to him. Sounds super convenient. Right?

![alt-text-1]({static}/images/30/whatsapp_screenshot_2.png)  

He has set everything up via PostNord so that I only have to confirm receiving the money by going to the link. He even sent me a link to where I can confirm everything. Now, my Danish is certainly lacking (e.g., non-existent) -  but when someone sends me a link like: 

```bash
https://postnord-dk.delivery-85367.icu/andet-unoliving-ikea-ja-id-10807800110
```

My radar starts beeping - and yours should too. The page looks pretty nice - and perfectly emulates [PostNord](https://www.postnord.dk/en)'s website. It has my name and everything - looks pretty legit:

![alt-text-1]({static}/images/30/home_page.png)  

After clicking the big yellow button to "confirm the transaction", I'm brought (surprising!) to a page to input my credit card details. I decided to start filling all of the credit card forms while monitoring the `POST` requests the website might be sending. 

![alt-text-1]({static}/images/30/card_confirmation.png)  

1. First I'm asked to input a credit card number and last name
2. It then asks for an expiration date and a CVC number 
3. Once that is done, it prompts the user to input his/her [NemID](https://en.wikipedia.org/wiki/NemID) username and password (e.g., the login solution used for most state services in Denmark - e.g., banks, digital post)
4. And finally - it asks for a confirmation of my bank account's balance - just to ensure they retrieve the right amount. 

If I had put all of this information correctly, Dimitriy would pretty much own me at this point. 

You can check all of the web pages I went through in [this](https://github.com/duarteocarmo/dba_scam/) repo. 

## Sending some surprises 

I'm pretty well versioned in Python - I know it can serve me well when trying to get back at Dimitriy. While going through the forms in his scam website, I noticed a `POST` request firing from my browser with the following information:

```http
POST / HTTP/1.1
Host: postnord-dk.delivery-85367.icu
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:89.0) Gecko/20100101 Firefox/89.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8
Accept-Language: en
Accept-Encoding: gzip, deflate, br
Content-Type: application/x-www-form-urlencoded
Content-Length: 81
Origin: https://postnord-dk.delivery-85367.icu
DNT: 1
Connection: keep-alive
Referer: https://postnord-dk.delivery-85367.icu/andet-unoliving-ikea-ja-id-10807800110
Cookie: ssupp.vid=viKziAQroXxx; ssupp.visits=1
Upgrade-Insecure-Requests: 1
Sec-GPC: 1

Body:card_number=5156+1542+2403+1977&page=nemidnotif&nemlogin=9999999&nempassword=1876
```

The last line of the snippet shows all the information Dimitriy would get straight from my browser. (e.g., `card_number`, `nemlogin`, `nempassword`)

In an attempt to add some confusion to his operation, I decided to create a little script. This little script would send him about 5000 different combinations of the above parameters in a completely random fashion. Fun.  

My hope is that Dimitriy is storing the information about all his victims in the same database (or even spreadsheet). By sending him 5000 fake combinations of victim details, he'll have a hard time finding the *actual* victims. Yes, this could be a long shot - Dimitriy could have a more sophisticated setup, and I suspect he does. 

But for the kicks, let's just use some python to piss him off:

    :::python
    import asyncio
    import concurrent.futures
    import requests
    import random
    
    # create some fake data
    URL = "https://postnord-dk.delivery-85367.icu/andet-unoliving-ikea-ja-id-10807800110#"
    totals = 5000
    card_numbers = [str(random.randint(5156000000000000, 9999999999999999)) for i in range(totals)]
    card_number_list = [f"{x[0:4]}+{x[4:8]}+{x[8:12]}+{x[12:16]}" for x in card_numbers]
    page = "nemidnotif"
    nemlogin_list = [f"{random.randint(111111, 999999)}-{random.randint(1111, 9999)}" for i in range(totals)]
    nempassword_array = [random.randint(1111, 9999) for i in range(totals)]
    
    # send a request to Dimitriy
    def send_data():
        try:
            params = {
                "card_number": random.choice(card_number_list),
                "page": page,
                "nemlogin": random.choice(nemlogin_list),
                "nempassword": random.choice(nempassword_array),
            }
            response = requests.post(URL, params=params)
            print("Sent data.")
            return response
        except Exception as e:
            print(str(e))
            return None
    
    # parallelize requests using asyncio
    async def main():
        with concurrent.futures.ThreadPoolExecutor(max_workers=20) as executor:
            loop = asyncio.get_event_loop()
            futures = [
                loop.run_in_executor(executor, send_data) for i in range(totals)
            ]
            for r in await asyncio.gather(*futures):
                print(r)
    
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())

When running this, I successfully submitted about 4000 `POST` requests. After that, the website started denying my requests. Dimitriy probably noticed that we were up to no good. 

Now that we've served our cold dish. Let's try to find a bit more about this scam. 

## Looking closer

When looking closer at the link (`https://postnord-dk.delivery-85367.icu`) it looks like that the attacker is automatically generating specific delivery links for each victim. Actually, I received another link from him the previous day (`https://postnord-dk.delivery-94512.icu`). It looks like when the attacker selects a victim he quickly generates a link. Once he has the information, he then kills the link and brings the website offline. It's actually pretty smart, for us to completely block his operation, we would have to continuously scan every `postnord-dk.delivery-XXXXX.icu` url. This can be done of course but requires much more effort. 

I also managed to retrieve all of the `whois` information. I [saved the results in this gist](https://gist.github.com/duarteocarmo/f83c47e6512593a971d7c4198c28ca51). I'm not an expert in reading `whois` outputs, but it appears that our attacker *could* be based in Iceland. I doubt it. But If you're an expert in reading these outputs, do reach out! ([email](mailto:me@duarteocarmo.com) is best)

Finally, I also downloaded all of the web pages as I navigated through the scammer's website ([check this repo](https://github.com/duarteocarmo/dba_scam)). When looking at their source code, I came across a file called `cpg_waiter.js` (link [here](https://github.com/duarteocarmo/dba_scam/blob/master/html_pages/card_prompt_1/Modtag%20pengene_files/cpg_waiter.js)). This file contains a lot of source code comments in Russian. This makes me think this scammer was probably leveraging some Russian-built tool to scam out DBA re-sellers. I also found [another GitHub user](https://github.com/dzubchik/fake-olx/blob/2dde01b22bfea6e8af294e09ccb742ee5c877662/%D0%9E%D1%82%D1%80%D0%B8%D0%BC%D0%B0%D0%BD%D0%BD%D1%8F%20%D0%BD%D0%B0%20%D0%B1%D0%B0%D0%BD%D0%BA%D1%96%D0%B2%D1%81%D1%8C%D0%BA%D1%83%20%D0%BA%D0%B0%D1%80%D1%82%D1%83_files/cpg_waiter.js) that came across this file. Maybe he purchases the whole engine from someone? Maybe he/she is in fact Russian? I don't know.

## I know that I know nothing

It's been fun getting some revenge from this scammer. But I have to admit that I'm still super intrigued about who this person is and what tools they are using. 

I did learn a couple of valuable lessons in the process. (1) That these types of scams are getting more and more sophisticated - and leveraging social engineering to make them more believable. Also, (2) if you want to protect other people from falling victims to scams like these: tell them to <u>always</u> look at the url bar. <u>Always</u>. 

*If you have some valuable information/experience with these types of scams, do [reach out](mailto:me@duarteocarmo.com), and I'll include it in this post.* 

<hr>

#### Updates & notes

- A nice reddit user by the name of Sungod23 took the time to dive a bit deeper into the scam. One of the name [servers points to Russia](https://www.ip-adress.com/website/ns2.nameserverflux.be). And another name server [points to an IP in Ukraine](https://www.ip-adress.com/website/ns1.well-wall.to). It looks like my suspicion from Russia appears accurate. 
- Another user by the name of Julian, suggested I report the scam to namecheap, and to the Danish authorities. I have informed the Danish authorities prior to writing this post. And I just sent an email to namecheap reporting it as well. 
