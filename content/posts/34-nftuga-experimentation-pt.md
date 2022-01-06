title: Os NFTs são estúpidos. Bora fazer uns
date: 26-12-2021
description: Criando NFTs a partir de caras de deputados geradas por inteligência artificial 
status: published
slug: nftuga-nft-experimentation
thumbnail: images/nftuga/model-results.png
lang: pt
translation: true

[English](/blog/nftuga-nft-experimentation) | [Português](/nftuga-nft-experimentation-pt) 

As pessoas mais velhas não gostam de ideias novas. Os nossos pais e avós não percebem a maior parte das novidades de tecnologia que estão a nossa volta. Até o meu pai às vezes diz que *não confia* em shopping online. Cago-me a rir. 

A primeira vez que eu me senti velho no mundo da tecnologia foi com o aparecimento dos [NFTs](https://www.theverge.com/22310188/nft-explainer-what-is-blockchain-crypto-art-faq). Porque é que eu havia de pagar por uma fotografia na internet sabendo que posso simplesmente fazer um screenshot? Não faz sentido nenhum. 

Mas se há uma razão pela qual eu trabalho em tecnologia é porque  estas coisas me deixam curioso. E a melhor matar a curiosidade, é meter as mãos na massa. 

Decidi fazer uns NFTs. Chamei-lhes: *NFTugas*. 

![training-nftuga-gif]({static}/images/nftuga/nftuga-gif.gif)

## Caras deputados geradas artificialmente

Todos os NFTs que eu vejo na Internet são um bocado iguais. Uma colecção de avatares com diferentes combinações de certas características (e.g., tipo [estes](https://opensea.io/collection/boredapeyachtclub), ou [estes](https://www.larvalabs.com/cryptopunks)). Mas nós estamos aqui para fazer arte - portanto decidi fazer uma coisa ligeiramente diferente..

Há muito tempo que tenho uma ideia na minha cabeça: Gerar caras de deputados Portugueses só com inteligência artificial. Estúpido não é? Completamente - mas pode ser divertido. E isso é o que interessa. 

Para este tipo de projecto, costumam-se usar [GANs](https://en.wikipedia.org/wiki/Generative_adversarial_network) (Generative Adversarial Networks). Em resumo, cria-se um modelo *generator* (e.g., cria novas caras) e um modelo *discriminator* (e.g., detecta se as caras são falsas ou não). "Treinar" este modelo significa por o nosso gerador contra o nosso discriminador durante um longo período de tempo. Quanto mais a batalha se prolonga, mais o *generator* começa a tentar enganar o nosso *discriminator*, e acaba por criar umas caras bem estranhas. 

<center>
![raw-dataset]({static}/images/nftuga/raw-images.png)
</center>

## Ensinar um modelo a criar caras 

Ideia decidida, era hora de criar o nosso dataset. Consegui [scrappar](https://github.com/duarteocarmo/nftuga/blob/master/download_images.py) do site do parlamento cerca de 1500 caras de deputados ([dataset final](https://www.kaggle.com/duarteocarmo/diplomatas-download)) - alguns em funções, outros reformados. Depois de alguma ginastica, e de treinar os nossos modelos durante ~8 horas, finalmente consegui uns resultados interessantes. Além disso, usei deteção facial para reduzir as fotografias só ás caras em questão e melhorar os resultados. Deixo o link do [notebook](https://www.kaggle.com/duarteocarmo/nftuga-training) para os mais curiosos. 

Era hora de criar uns NFTs. Com o nosso *generator* criado, gerei cerca de 100 caras de deputados. Destas, selecionei 20 que achei mais *interessantes*. Algumas parecem uma mistura de homens e mulheres (não há muitas), umas parecem  extra-terrestres, outras, parece que fizeram uma cirurgia plástica que correu mal. Não lhes queria dar um nome qualquer (*tipo NFTuga #004*) - portanto decidi dar um nome de uma aldeia portuguesa a cada um deles. Há um chamado *Gasparões*, outro chamado *Quintas da Torre*, etc. (lista completa em baixo do post)

<center>
![model-results]({static}/images/nftuga/model-results.png)
</center>

## De PNGs a NFTs: Nada fácil 

Conheço razoavelmente os mundos do Ethereum e Bitcoin, mas recentemente tenho ouvido falar bastante de *[Solana](https://solana.com)*. Supostamente é mais rápida, melhor para o nosso ambiente, e mais propicia para NFTs. Ora, eu gosto de coisas baratas, principalmente se fazem bem a nosso ambiente. Estava escolhida a blockchain então - estes NFTs iam ser [criados](https://www.sofi.com/learn/content/what-is-nft-minting/) na Solana. 

Comecei a investigar o que é que queria dizer *criar* um NFT. A maneira mais fácil claro, seria usar coisas como o [OpenSea](https://opensea.io) ou no nosso caso, o [Solsea](https://solsea.io/) onde podemos fazer o upload de um `png`, e deixar que eles criem automaticamente um NFT. Fácil? Sim. Demasiado até. Não estou interessado em coisas fáceis. Estou mais interessado em perceber como é que isto funciona. 

Enquanto estava a estudar a assunto, descobri uma framework chamada [Metaplex](https://github.com/metaplex-foundation/metaplex). Eles descrevem-se como "a protocol built for developers to create NFTs on Solana". Parece ser o que eu estava a procura. Comecei por criar uma loja online para os meus NFTs viverem, mas a loja era super lenta e nada estável. Finalmente, acabei por descobrir um conceito chamado "[Candy-machine"](https://docs.metaplex.com/create-candy/introduction). É basicamente uma ferramenta que nos permite transformar todos as nossas caras em NFTs seguindo uma data de instruções e comandos específicos definidos na documentação. 

## NFTugas na blockchain Solana

Depois de muitas tentativas falhadas, la acabei por conseguir criar os 20 NFTugas na blockchain. Fiquei surpreendido pela qualidade das ferramentas que existem no espaço (pelo menos no espaço Solana) que deixam um pouco a desejar. Além de que as transações na blockchain parecem ser *bastante* caras. No total, acabei por gastar a volta de 30 EUR só para os criar (não estamos a falar de mais de 2 MB de imagens).

Também acabei por aprender bastante durante o processo - o meu objectivo principal. Fico feliz também por ter 20 itens "únicos", criados por mim (or por um AI que eu criei) numa blockchain. Se calhar ficarão lá muito tempo. Se calhar isto é tudo uma bolha e rebenta amanhã. Segue jogo. 

Continuam a ser estúpidos? Sim, tão estúpidos quanto [uma banana numa parede por 120.000 USD](https://news.artnet.com/market/maurizio-cattelan-banana-art-basel-miami-beach-1722516). Ou seja, a arte, e o valor dos objectos é proporcional ao valor que nós lhe atribuímos. Se existem pessoas que acreditam que o valor de um token digital é superior a um milhão de euros, quem sou eu para as desmentir? 

A Bobino já me pediu um dos NFTugas, e outros dois amigos também me pediram para lhes enviar um. Se estiveres interessado/a manda -me um email com a tua public key, ou preenche [este](https://forms.gle/q9NeyfQdwbFBaSbc8) formulário e eu mando-te um também.  

Deixo aqui a lista completa dos 20 NFTugas com links para os poderes ver na blockchain:

- [gasparões](https://explorer.solana.com/address/EmfVGHYqTa76x82jh8133Hp6iQvE43e8NSimfm4jXywq) - *Vendido*
- [cetos](https://explorer.solana.com/address/HLugPDkBNZfgFhvuHeYxP5W9LEYbQi2BmPaYkyek7vKm) - *Reservado*
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
- [senhor_da_serra](https://explorer.solana.com/address/Caiv1ZKkqxg4x2tKK422ny51MDuvCqkSgnX8jbkRYspj) - *Reservado*
- [torre_dos_namorados](https://explorer.solana.com/address/ESRtgAmNRaxupepvuFD61JFDS85j9YRfc6cDJX633Uw6)
- [santana](https://explorer.solana.com/address/AntpwziEwHw9SaSAUF1cpXysDbVrfnZfzbB61jSC6DP1)
- [cacela_velha](https://explorer.solana.com/address/HiRHzSe8CCjTqdGTtojKiKf45t3WJsPieu54Vd2XAEJP)
- [arrota_da_moita](https://explorer.solana.com/address/gNZ6g1jn1QRmSNuaHLaLSqpZebZT4fEgfy8R14rTBHS)
- [ribolhos](https://explorer.solana.com/address/CYDXjb7D4rkTt1JWvc7DSRtf5pRWADFTiNJGRuUMi3kQ)
- [quintas da torre](https://explorer.solana.com/address/7LQ2r5p7cQrabyWK8hgHEcHnasMkqabwyrpY2ikPrDqW)
- [helenos](https://explorer.solana.com/address/GiB3Goa2nEBFKLdZjNxrXGjBfNasEXopCR18NaUTR2fc)

