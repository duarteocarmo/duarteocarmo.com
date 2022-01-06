title: NFTs are dumb. Let's make some
date: 26-12-2021
description: Putting artificially generated faces of Portuguese politicians on Solana
status: published
slug: nftuga-nft-experimentation
thumbnail: images/nftuga/model-results.png
lang: en

[English](/blog/nftuga-nft-experimentation) | [Português](/nftuga-nft-experimentation-pt) 

Old people don't like new ideas. We see it everywhere around us. Our parents still don't understand most of today's tech trends. Even my dad still *doesn't trust* online shopping. Which I find hilarious.

The rise of [NFTs](https://www.theverge.com/22310188/nft-explainer-what-is-blockchain-crypto-art-faq) is the first time I *really* felt old when talking tech. Why the hell would someone pay for a photo when you can just right-click it? It makes no sense. 

But there's a reason I work with technology - I have a natural tendency to be curious about things like this. And I also know, that the best way to learn about something - is to build it. 

So I decided to built some NFTs. I called them: *NFTugas*.

![training-nftuga-gif]({static}/images/nftuga/nftuga-gif.gif)

## Artificially generated faces of Portuguese politicians

From what I've noticed, most NFTs look pretty similar. Their usually a collection of pixelated avatars. Each one having different combinations of certain attributes (e.g., like [these](https://opensea.io/collection/boredapeyachtclub) or [these](https://www.larvalabs.com/cryptopunks)). The look all the same - and we're making art over here - so we'll take another route.

For a long time I've been pondering on the idea of making artificially generated faces of Portuguese politicians. Stupid right? I know - but in my head it does sound kind of artistic. 

[GANs](https://en.wikipedia.org/wiki/Generative_adversarial_network) (Generative Adversarial Networks) are what's usually used for this type of project. On a high level, you create a *generator* (e.g., make faces) and a *discriminator* (e.g., tells if faces are fake or real). *Training* a GAN means battling the generator against the discriminator for a long period of time. As the generator tries to trick the discriminator more and more, it starts coming up with some pretty weird faces.

<center>
![raw-dataset]({static}/images/nftuga/raw-images.png)
</center>

## Teaching a model how to make faces

The premise was set -  I [downloaded](https://github.com/duarteocarmo/nftuga/blob/master/download_images.py) 1500 photos of past and present members of the Portuguese Parliament (here's the [Kaggle dataset](https://www.kaggle.com/duarteocarmo/diplomatas-download)). After some data wrangling, 8.5 hours of model training, and being blocked for using too many GPU resources, I finally got to some satisfactory results. I used an implementation of GAN in which cropped the images to the facial boundaries. If you're interested in diving deeper into the technical stuff, [here's the Kaggle notebook](https://www.kaggle.com/duarteocarmo/nftuga-training). 


It was now time to take the face generator and create some NFTugas. From a pool of 100 randomly generated images, I selected 20 that I believe were *interesting*. Some look like a mix of male and female (and the latter are rare, *especially* in Portuguese Parliament), others look a bit like aliens, or not humans at all. I didn't want to give them boring names such as "BORED APE #007". So I scrapped names of Portuguese villages from the web, and assigned them to the 20 selected images (names like *fanhais*, or *charneca*). 

<center>
![model-results]({static}/images/nftuga/model-results.png)
</center>

## From PNGs to NFTs: A bumpy road

I'm familiar with Ethereum and Bitcoin. Recently, I've been hearing a lot about *[Solana](https://solana.com)* as well. *Supposedly*, Solana is faster, better for the environment, NFT friendly, and cheaper to operate on. I like cheap, and I would also say I'm a pretty big fan of our Planet - so these NFTs would be [minted](https://www.sofi.com/learn/content/what-is-nft-minting/) on Solana. 

I investigated how the hell one is supposed to create NFTs on Solana. The easiest way would be to use things like [Opensea](https://opensea.io) or [Solsea](https://solsea.io/). These basically let you upload an image, and automatically create NFTs from it. That sounds too easy, and not very educational, at least for me.

While researching, I came accross [Metaplex](https://github.com/metaplex-foundation/metaplex), a "protocol built for developers to create NFTs on Solana" - that's what they call it. It's just like a tool to conduct NFT operations on Solana. I started by creating a [Storefront](https://docs.metaplex.com/create-store/init-store) for NFTuga - but it ended up being incredibly slow and laggy. After that, I decided I would be happy to simply put the NFTugas on the chain. To do it, I used something called the *Candy-Machine*. Candy-machines allow you to take `png` files and mint them into the block-chain, without having to create a whole storefront for it.

## NFTugas on the Solana blockchain

After some trial and a lot of error, I did managed to mint all 20 unique NFTugas into the Solana blockchain. I'm surprised by how immature some of the developer tooling is - at least on Solana. Also, transactions on the chain seem to be *very* expensive. I spent about ~30 EUR to mint (e.g., create) about 20 NFTs (we are talking no more than 2MB). 

So are NFTs stupid? Yeah. As stupid as a [banana on a wall selling for 120.000 USD](https://news.artnet.com/market/maurizio-cattelan-banana-art-basel-miami-beach-1722516). The value of objects is only determined by what individuals are willing to pay for them. If people believe that a digital token on Ethereum is worth a million dollars, who the hell am I to prove them wrong? 

I *did* learn a lot during the process, which was my main goal.  And even though I wasn't totally sold on the concept, I did end up with 20 unique items in a database that might exist for a long time. Bobino already asked me for one, and I'll give a couple away to friends as well. 

If you, dear reader are interested in any of these, leave me an email with your public key address on Solana, or fill out [this](https://forms.gle/q9NeyfQdwbFBaSbc8) form, and I'll send you one as well. 

Here's the list to all 20 NFTugas, with links to their location on the Solana blockchain:

- [gasparões](https://explorer.solana.com/address/EmfVGHYqTa76x82jh8133Hp6iQvE43e8NSimfm4jXywq) - *Sold*
- [cetos](https://explorer.solana.com/address/HLugPDkBNZfgFhvuHeYxP5W9LEYbQi2BmPaYkyek7vKm) - *Reserved*
- [cumieira](https://explorer.solana.com/address/BU1ZcT5xthBfiF9tgSKUACVKdCEvvZppbST2Eh7gHz9H) 
- [ameais](https://explorer.solana.com/address/)
- [fanhais](https://explorer.solana.com/address/GG2wNV2gJTgnsfNbryc3Eb7pKHvxr1hEMU192y6pxtUY)
- [sernelha](https://explorer.solana.com/address/391L2c8ZDHZExvfN6joy36Pna4K1pLEPBYz6Ay7wo5zM)
- [charneca](https://explorer.solana.com/address/8hf2UiWPtpmuE7gPFu3D2cU3b4z2PRNHG9BxSUVwvkaR)
- [albarraque](https://explorer.solana.com/address/85Cm9f2XUWSEsCWwHibce2miitcrz2ajCvx6AQ2ACmpd)
- [cernadela](https://explorer.solana.com/address/F7ni1Qa9iSiVK8yLr4ZwPUKbAriRzaNUjeTcHUqgW1bQ)
- [cavada_nova](https://explorer.solana.com/address/6pxqLQs9w4c2tyKJ4jRnpFcdi1G5Zo31McnqzihmNSxp)
- [moita_redonda](https://explorer.solana.com/address/7niUipVkr58B6zfdx92VUNak1CBWxMfEaAu3MJ5xy8Zv)
- [gradissimo](https://explorer.solana.com/address/GSaAtwFjja979nSYeK7jYJ5rF5teDKGHyie2MPjV7KXG)
- [senhor_da_serra](https://explorer.solana.com/address/Caiv1ZKkqxg4x2tKK422ny51MDuvCqkSgnX8jbkRYspj) - *Reserved*
- [torre_dos_namorados](https://explorer.solana.com/address/ESRtgAmNRaxupepvuFD61JFDS85j9YRfc6cDJX633Uw6)
- [santana](https://explorer.solana.com/address/AntpwziEwHw9SaSAUF1cpXysDbVrfnZfzbB61jSC6DP1)
- [cacela_velha](https://explorer.solana.com/address/HiRHzSe8CCjTqdGTtojKiKf45t3WJsPieu54Vd2XAEJP)
- [arrota_da_moita](https://explorer.solana.com/address/gNZ6g1jn1QRmSNuaHLaLSqpZebZT4fEgfy8R14rTBHS)
- [ribolhos](https://explorer.solana.com/address/CYDXjb7D4rkTt1JWvc7DSRtf5pRWADFTiNJGRuUMi3kQ)
- [quintas da torre](https://explorer.solana.com/address/7LQ2r5p7cQrabyWK8hgHEcHnasMkqabwyrpY2ikPrDqW)
- [helenos](https://explorer.solana.com/address/GiB3Goa2nEBFKLdZjNxrXGjBfNasEXopCR18NaUTR2fc)

