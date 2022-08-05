title: Down from the Cloud
date: 08-05-2022 11:00
description: Leaving the Cloud and self-hosting all my services in a single server
status: published
slug: down-from-the-cloud-self-hosting
thumbnail: images/41/glances.png

I love the Cloud. For years, I've been deploying software to it. Azure, GCP, AWS, you name it. I've used most of them. To be honest, they're the same pig, but with different lipstick (like the Danes say). Package up your app, make some CI/CD magic, select your service, and I'm good to go. Still remember when I helped a whole bank move to the Public Cloud. The benefits are mostly obvious. 

But I'm no bank. And it's not all rainbows and unicorns. For starters, those 10 elastic beanstalk applications can start adding up. What if I want to change from Cloud A to Cloud B? It's not like Amazon is going to make my life easy. It's a convenience/lock-in trade-off. What about user data? What about _my_ data? Some of the [best](https://marco.org/2014/02/23/the-value-of-background-fetch) [software](https://twitter.com/levelsio/status/1308145873843560449) I use doesn't even use the Cloud. 

Let's come down from the Cloud (at least the public one): Self-hosting. How _hard_ is it, really? 

## Get a server
This one should be straightforward. There's no shortage of server providers. Just browsed [LowEndBox](https://lowendbox.com/) for a while I decided to go with a dedicated server from [Hetzner](https://www.hetzner.com/). Something relatively close to Copenhagen to ensure my connection to the server is snappy enough. 

I don't run a lot of very high traffic sites (yet!). Something around the 50 EUR/month price point serves just fine. You'll be surprised with how much stuff you can run in this machine. I have 10 services running and my memory barely goes above 10%. Let's not jinx it. 

## Containerize all the things
I have a love-hate relationship with Docker. For me, it's still the most straightforward way of exchanging and packaging up software to ensure nothing breaks. But how I hate when my container starts getting fat. I'm talking about you, PyTorch. 

Every application will run inside its own containerized environment. To ensure this doesn't get overly complicated, I went with `docker compose`. Why not Kubernetes you may ask? Because I have other things to do. 

Inside the server, things look a little something like: 

```bash
|-- Caddyfile <- more on this later
`-- projects
    |-- project-1 <- first application
    |   |-- ...
    |   |-- Dockerfile
    |   `-- docker-compose.yml <- docker compose file
    `-- project-2 <- second application
        |-- ...
        |-- Dockerfile
        `-- docker-compose.yml <- second docker compose file
```

Every project gets its own `docker-compose.yml` file. Every project runs on its specific server port. For example, to run `project-1`, I `cd` into the directory and start the container: `docker compose up --force-recreate --build -d`. This automatically starts the service on the port I specify on the `docker-compose.yml` file. 

Using the process above, I can have a bunch of different applications running on a lot of different ports, but in a single server. Hopefully (1) saving money, and (2) increasing the power and control over them. 

Hopefully, I won't land on dependency-nightmare-land.

## Continuously deploy

Self-hosting sounds great. Having to `ssh` into a server _every time_ I want to update a service, doesn't. If there's one thing I'm not willing to compromise on, it's continuous deployments. The whole `git push` automatically updates the app thing is super convenient. 

Enter GitHub actions. With them, you can automate the ssh'ing and re-deployment part. It's not the most _secure_ option. But hey, it works pretty well. Surprisingly, it's also much faster than deploying on Elastic Beanstalk or Cloud Run. 

Here's what these actions look like:

```yaml
name: Deploy to server
on:
  push:
   branches:
   - master 
jobs:
  build:
    runs-on: ubuntu-latest
    steps:
    
    - name: Checkout source code
      uses: actions/checkout@v1

    - uses: actions/checkout@master
    - name: Copies repository to server
      uses: appleboy/scp-action@master
      with:
        host: ${{ secrets.HOST }} <- these are defined in your repo settings.
        username: ${{ secrets.USERNAME }}
        password: ${{ secrets.PASSWORD }}
        port: 22
        overwrite: true
        source: "."
        target: "/root/projects/project-X"

    - uses: appleboy/ssh-action@master
      name: Stops and updates docker container as deamon
      with:
        host: ${{ secrets.HOST }}
        username: ${{ secrets.USERNAME }}
        password: ${{ secrets.PASSWORD }}
        port: 22
        script: |
          cd projects/project-X
          docker compose down
          docker compose up --force-recreate --build -d
          docker ps
```

## HTTPS, we meet again

Alright, it's time to expose these apps to the world. I'll admit it. The sheer mentioning of _https certificates_ or _DNS_ runs a chill down my spine. After loosing a couple of hours in the [reverse proxy documentation for Nginx](https://docs.nginx.com/nginx/admin-guide/web-server/reverse-proxy/) and getting a bit mad, I found this little thing called [Caddy](https://caddyserver.com/). Oh boy, that was easy.

Caddy solves the whole subdomain, reverse proxy, multiple websites on the same server, HTTPS _mambo jumbo_. The docs are great, and it's super straightforward to use. I definitely recommend their [Getting Started](https://caddyserver.com/docs/getting-started) docs. 

First step is to point some A record in your DNS to your server's IP address. I use Cloudflare for this, do recommend. Once Caddy is installed in the server, all you need to do is create a `Caddyfile`:

```text
project-1.mydomain.com {
        reverse_proxy localhost:3000
}

project-2.mydomain.com {
        reverse_proxy localhost:5000
}

home.mydomain.com {
        respond "Base domain"
}
```

After that, run `caddy start`, and we're done. Yes. Your eyes are not kidding you. That's absolutely it. `project-1.mydomain.com` is connected to my app running on port `3000`, and `project-2.mydomain.com` is connected to the container on port `5000`. HTTPS? Automatic. Reverse proxy? Done. 

Caddy automatically enables HTTPS for all of the apps you specify on your `Caddyfile`. It also automatically issues new certificates and renews them. Changes? A simple `caddy reload` and you're up and running again.

I can have as many subdomains/domains pointing to the same server as I want, as long as the server can handle it. 

## Closing thoughts

<img src="{static}/images/41/glances.png" alt="Glances" style="max-width:100%;">

One of the services I'm currently self hosting is called [Glances](https://nicolargo.github.io/glances/). With it, all of my server's metrics an url away. With about 5 containers, the CPU is still below 10%. 

No. I don't have all the elasticity that the Public Cloud gives me. But do I need it? The deployment method is the same (`git push`), the speed of services are the same (mostly static with Cloudflare on top), the cost is lower, and data is controlled by me. Sounds like a treat.



