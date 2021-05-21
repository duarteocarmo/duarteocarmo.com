title: How to build a newsletter using Python and FastAPI
date: 04-11-2021
description: How to build a newsletter using Python, FastAPI, and DynamoDB
thumbnail: images/kindle-highlights-cover.png
status: published

<center>
<img src="{static}/images/newsletter-cover.jpg" alt="Digital library" style="max-width:100%;">
</center>

My favorite way of learning is by reading extensively about a topic. For this, nothing better then my Kindle. But I have been growing increasingly envious of the large bookshelves of scratched and highlighted books that I see in older generations. 

I mean, who doesn't dream about having their own private library of knowledge they can just jump into at any time? So I have been relentlessly building ways of storing the knowledge from my readings. Building my [highlight library](https://duarteocarmo.com/blog/managing-kindle-highlights-with-python-and-github.html) was the first attempt.

But what else can we build to keep us connected to what we read? How can we guarantee we get reminded of important pieces of knowledge that feed into our brains?

This is how I did it. 

## Ah shit, another newsletter 

So the solution that I wanted to build had some high-level requirements:

- It needs to parse all of the highlights in my `My Clippings.txt` file stored on my Kindle
- It should store them somewhere in the Cloud
- It should send me, on a regularly basis, a single passage that I have highlighted in the past

Well, that sounds pretty much like a newsletter to me! I know, I know, the world is full of newsletters. But hey, I certainly don't want to receive a Telegram message of something I highlighted on my Kindle. Email sounds like a "slower" medium to consume knowledge. 

So the premise was set, we are going to build a newsletter service. 

For reference, here's the high-level architecture of what I've built. Don't panic! We'll dive deeper into the details step by step. This is just for reference:

<center>
<img src="{static}/images/kindle-highlights-architecture.png" alt="Kindle higlights architecture diagram" style="max-width:100%;">
</center>

## The backbone: FastAPI

In the past I have experimented with a lot of different Python based web frameworks (e.g., Django, Flask, Pyramid). But recently, I have been hearing a lot of rage about [FastAPI](https://fastapi.tiangolo.com/). Word on the street is that its super fast, and async out of the box. This sounded pretty exciting, so I decided to give it a shot. (Note: If you are building something serious, do some research first)

The [web app](https://github.com/duarteocarmo/kindle-highlights-newsletter/blob/master/app/main.py#L23) is made of four simple endpoints:

- A home page that should display a form for users to sign up to the newsletter ([link](https://github.com/duarteocarmo/kindle-highlights-newsletter/blob/c6830513bbb0da05613f221102a47d3fe38409f7/app/main.py#L23))
- A way of handling submitted form data from users ([link](https://github.com/duarteocarmo/kindle-highlights-newsletter/blob/c6830513bbb0da05613f221102a47d3fe38409f7/app/main.py#L28))
- An endpoint to confirm subscriptions to the newsletter ([link](https://github.com/duarteocarmo/kindle-highlights-newsletter/blob/c6830513bbb0da05613f221102a47d3fe38409f7/app/main.py#L54))
- An endpoint to unsubscribe from the newsletter ([link](https://github.com/duarteocarmo/kindle-highlights-newsletter/blob/c6830513bbb0da05613f221102a47d3fe38409f7/app/main.py#L65))

One interesting thing I noticed, is that every time I wanted to send an email or register a user in a database, things could get pretty long . This where I started to leverage some of the async capabilities of FastAPI. `Async` methods and `background_tasks` became super useful to handle user requests. 

Let's look at some example code (from [here](https://github.com/duarteocarmo/kindle-highlights-newsletter/blob/master/app/main.py)):

```python
# full code: https://github.com/duarteocarmo/kindle-highlights-newsletter/blob/master/app/main.py
@app.post("/")
async def sign_up(
    request: Request,
    background_tasks: BackgroundTasks,
    file: UploadFile = File(...),
    email: str = Form(...),
):
    highlights = await parse_highlights_file(file) # Parse highlights from user
    email_valid = await email_is_valid(email) # Check if email is valid

    if not highlights or email_valid is False:
        return FileResponse("static/error.html")

    subscribed_status = await check_user_subscribed(email) # Check if user is subscribed

    if subscribed_status is False:

		# Note: none of these background tasks block our webpage. Pretty awesome.

        background_tasks.add_task(register_user, email)
        background_tasks.add_task(send_confirmation_to, email)
        background_tasks.add_task(upload_highlights, highlights, email)
        return templates.TemplateResponse("sign_up.html", {"request": request})
    else:
        return templates.TemplateResponse("success.html", {"request": request})
```

## Data layer: So Cloud, much native

Databases are a pain. I can't even begin to tell you how much I hate database migrations. Yes, I understand transforming python to SQL code can be insanely hard. But I mean, I just want to store something. So how hard can this possibly be? The premise was set: I was not going to use something like [SQLAlchemy](https://www.sqlalchemy.org/), even though FastAPI [recommends it](https://fastapi.tiangolo.com/tutorial/sql-databases/). 

So I thought of storing everything in a [SQLite](https://www.sqlite.org/index.html) database - that sounded like a good idea at first. But I also don't want to store a database file in the middle of my source code. I know, I know, I have serious issues. 

One thing that came to mind was [mongoDB](https://www.mongodb.com/) - a documented oriented database is pretty simple to get up and running. But I have moved to the dark side, I must admit. And have been putting everything in AWS whenever I can. So what does AWS offer as a mongo clone? Let me introduce you to [DynamoDB](https://aws.amazon.com/dynamodb/)!

In the process, I found a very handy utility called [PynamoDB](https://pynamodb.readthedocs.io/en/latest/), which allows you to interface with your DynamoDB through your python code. All I needed to do was to define some models, and I could pretty quickly get to storing and retrieving data from my database. 

So I created a `models.py` file, which I could query from anywhere within my application - here's an example of my database model for a highlight (something the user highlighted in their kindle):

```python
# full code: https://github.com/duarteocarmo/kindle-highlights-newsletter/blob/master/app/models.py
from pynamodb.models import Model
from pynamodb.attributes import (
    UnicodeAttribute,
    UTCDateTimeAttribute,
    BooleanAttribute,
    NumberAttribute,
)

class HighlightModel(Model):
    """
    Kindle highlight
    """

    class Meta:
        table_name = "kindle-highlights-contents"
        region = "eu-west-1"

    email = UnicodeAttribute(hash_key=True, null=False)
    author = UnicodeAttribute(null=False)
    book = UnicodeAttribute(null=False)
    content = UnicodeAttribute(null=False)
    date_string = UnicodeAttribute(null=False)
    highlight_index = NumberAttribute(range_key=True, null=False)
```

Great you have a web service, you are storing some data on the Cloud. How do we deploy this? 

## Deployment: Elastic Beanstalk, thank you for existing

FastAPI [recommends](https://fastapi.tiangolo.com/deployment/docker/) Docker to deploy your applications. To do so, all I needed to do was to create a [Dockerfile](https://github.com/duarteocarmo/kindle-highlights-newsletter/blob/master/Dockerfile) and a [`docker-compose.yml` file](https://github.com/duarteocarmo/kindle-highlights-newsletter/blob/master/docker-compose.yml). Also, by using this image, you supposedly get [automatic performance scaling](https://github.com/tiangolo/uvicorn-gunicorn-fastapi-docker) which sounded pretty appealing (for when someone decided to DDoS my website)

For me, by far the easiest way to deploy a docker-based application nowadays is [AWS Elastic Beanstalk](https://aws.amazon.com/elasticbeanstalk/). In short, AWS takes a .zip file with your application, together with a `docker-compose.yml` file, and automatically runs it in EC2 instances. Additionally, you can integrate this process into your workflow with [GitHub actions](https://github.com/features/actions) - but we'll get deeper into that in a second. 

To send all my emails, I use Amazon's [SES (Simple Email Service)](https://aws.amazon.com/ses/). I was much cheaper than other solutions e.g., SendGrid. And it allowed me to keep everything in AWS (user lock-in? Yes. 200%)

One thing to note, is that my application should not only receive some highlights and an email from the users, and store them on a database. My application actually needs to send out emails with individual users every week. To do this, I needed some sort of scheduled task running every Friday. I started with [APScheduler](https://github.com/tiangolo/fastapi/issues/520#issuecomment-716969948) as advised in a shady GitHub issue. But I noticed that whenever I had more than 1 worker running my application, the jobs would run unreliably, our twice instead of once. In fact, I quickly discovered I was [screwed](https://apscheduler.readthedocs.io/en/stable/faq.html#how-do-i-share-a-single-job-store-among-one-or-more-worker-processes).

So where can I run scheduled tasks to send regular emails to my users? Cron? No, we are in the Cloud native era. 

## CI/CD: GitHub - (ab)using GitHub actions

In the final application, I managed to use GitHub actions for two, pretty critical tasks:

- **To automatically upgrade/update my application**([action file](https://github.com/duarteocarmo/kindle-highlights-newsletter/blob/master/.github/workflows/elastic_beanstalk.yml)): Every time I commit to my repository's master branch, GitHub automatically takes my application, and re-deploys it to Elastic Beanstalk. Taking all of my environment variables and secrets, zipping everything, and deploying 
- **To automatically send the newsletter to all my users**([action file](https://github.com/duarteocarmo/kindle-highlights-newsletter/blob/master/.github/workflows/send_newsletter.yml)): I created a GitHub action that runs my `send_email.py` ([link](https://github.com/duarteocarmo/kindle-highlights-newsletter/blob/master/send_email.py)) script, every Friday morning. The job is a bit flaky, and doesn't run quite on time. But hey, it runs. 

## Conclusion

This took much more time than I expected to build. I gained a renewed respect for all the different newsletter services out there (at least the ones built from scratch). Through building my own newsletter platform I got to discover and learn a bunch of new technologies that will for sure serve me well in the future. 

So what was the end result for this project? 

[Kindle-highlights.email](https://kindle-highlights.email/), a free and open-source project where any user can upload their highlights file, and receive one highlighted passage every Friday morning. This allows me to keep track of important pieces of knowledge I want to remember in the future, and hopefully help a couple of folks out there looking to build something similar!

<center>
<img src="{static}/images/kindle-highlights.png" alt="Kindle higlights architecture diagram" style="max-width:100%;">
</center>

Have comments? Questions? Features? Just create an issue in the [GitHub repo](https://github.com/duarteocarmo/kindle-highlights-newsletter).
