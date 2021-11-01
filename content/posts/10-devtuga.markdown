title: Creating devtuga
date: 2019-03-22
description: Creating a hackernews clone from scratch - devtuga

So I finally got to it. After finishing my Msc.Thesis and relaxing for a couple of months in my sunny home country of Portugal, I built a 'big' project. Here are some words about it. 

This is a rundown of some of the tools I used. **(by no means a tutorial!!)**


[I just want the code man.](#links)


## 1.The idea

I keep a lot of great ideas for giant technology companies in my notes app. But this time, the goal was just to build something from scratch.

I'm a big fan of [hackernews](https://news.ycombinator.com) and I also always felt that in Portugal, there are not many "community focused" websites. Therefore, I decided to create a hackernews clone for Portuguese hackers. 


<center>
<img src="{static}/images/hackernews.png" alt="Hackernews" style="width:80%">
  <figcaption>The inspiration</figcaption>
</center>



Alright, that being said. What tools did I use to build it? 

## 2.The technology

#### 2.1.[Python](https://www.python.org/)
I would be lying if I told you python was not my favorite language. If I can build it, I prefer to build it with python. For some years now, I have been totally embedded in the language's ecosystem. From data science projects, web development, devops, guis, or just scripts that help people around me. I think python is big, and it's here to stay. For me, it's a bit like writing poetry. 


```python
fruits = ["apples", "oranges", "bananas"]
for fruit in fruits:
    print(f"I love {fruit}!") # f strings are like crack. 
```

So python 3 was set. But how to build a hackernews clone using it? 


#### 2.2.[Flask](http://flask.pocoo.org/)
I have experimented with various python web frameworks such as [django](https://www.djangoproject.com/) or [pyramid](https://trypyramid.com/), but in my opinion, nothing quite compares to [flask](http://flask.pocoo.org/). The sheer simplicity of it is just mind boggling.  


For example, the snippet bellow, will give you a page with "Hello world" in it. Now isn't that awesome?

```python
from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"
```
This is just a small snipped of the syntax of flask. This actually got more complicated than this, but in flask, the general idea is that each function (in this case function `hello`), returns some HTML (in this case, the string `"Hello World""`). 

OK, you made some pages with some functions, what about data, and models?

#### 2.3.[SQLAlchemy](https://www.sqlalchemy.org/)

In order to make things work in our website, I had to come up with a way of managing all of the posts, users, comments, and votes. This "system" would have to both interact with my code, and at the same time, with a database (because we want to save information).

There are a bunch of ways of doing this, but I decided to use SQL Alchemy. The basic idea is that you define a "model" in your code that can automatically interact with a database. 

Here is an example of the `User` class:

```python
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    posts = db.relationship("Post", backref="author", lazy="dynamic")
    comments = db.relationship("Comment", backref="author", lazy="dynamic")
    about_me = db.Column(db.String(140))
    karma = db.Column(db.Integer, default=1)
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow())
```
This will create a `User` table in our SQL database and allow us, through python code, to interact with the model.  

Browse all the models I created [here](https://github.com/duarteocarmo/devtuga-news/blob/master/app/models.py). 


#### 2.4.[Docker](https://www.docker.com/)
After building a website in flask that worked in my local machine, I had to put it onto the web. As this was a learning process I decided to understand what all the fuss around docker was about. What is docker? It is basically a "mini" virtual machine. So mini, that you can run multiple on the same real virtual machine. Each mini virtual machine is called a container. 

For this process, I had to create two containers. One for my flask application, and one for my database. (why two and not one is a story for another post).

But how do you do that? Well, the simple principle is that you create something called a `Dockerfile` which is a set of instructions docker follows, in order to create a container. Here is an example: 


```docker
FROM python:3.7.1-alpine

COPY requirements.txt requirements.txt 
RUN python -m venv venv 
RUN venv/bin/pip install --upgrade pip
RUN venv/bin/pip install -r requirements.txt
RUN venv/bin/pip install gunicorn==19.8.1
RUN venv/bin/pip install pymysql 

COPY app app
COPY migrations migrations
COPY dev.py config.py boot.sh ./
RUN chmod +x boot.sh

ENV FLASK_APP dev.py

RUN chown -R devtuga:devtuga ./ 

EXPOSE 5000
ENTRYPOINT ["./boot.sh"]
```

After creating these instructions and running them, we basically can have two containers running, here are mine:


```bash
» sudo docker ps
CONTAINER ID        IMAGE                    COMMAND                  CREATED             STATUS                  PORTS                  NAMES
7baab35c09b7        devtuga:latest           "./boot.sh"              4 hours ago         Up 4 hours              0.0.0.0:80->5000/tcp   devtuga
89348e814f92        mysql/mysql-server:5.7   "/entrypoint.sh mysq…"   30 hours ago        Up 30 hours (healthy)   3306/tcp, 33060/tcp    mysql
```

## 3.The process
I took a long time getting everything up and running ([about a month according to the GitHub repository](https://github.com/duarteocarmo/devtuga-news/graphs/commit-activity)) but I had a lot of fun, and frustration also. In the end, I got a much better understanding of how real web applications work. So it was definitely worth it. 


## 4.The Result

So [here's the result](https://devtuga.herokuapp.com/) after some long hours of frustrating but very fun work. 

<center>
<img src="{static}/images/devtuga.png" alt="Hackernews" style="width:120%">
  <figcaption>I called it: <a href="https://devtuga.herokuapp.com/">devtuga.herokuapp.com</a> </figcaption>
</center>


### Link hub 
<a name="links"></a> 

- [Just show me the final result.](https://devtuga.herokuapp.com/)
- [I just came here for the code.](https://github.com/duarteocarmo/devtuga-news)
- [I want a tutorial](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world)
