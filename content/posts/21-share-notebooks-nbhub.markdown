title: NbHub: Share your jupyter notebooks with the world 
date: 22-06-2020 
description: A hacked command line tool that allows you to share jupyter notebooks with the world. 

*__TL;DR__: I created a small python package that allows you to share your jupyter notebooks right from the command line (like [this one](https://nbhub.duarteocarmo.com/notebook/e6b917cb) for example). To get started, visit [nbhub.duarteocarmo.com](https://nbhub.duarteocarmo.com). or `pip install nbhub`.*

## Sharing jupyter notebooks is a pain

We use jupyter notebooks for a wide range of things: quick analyses, serious projects, experimentation, and even for creating dashboards. However, when you want to share your work with someone that is not necessarily familiar with what a “jupyter notebook” actually is, you run into some problems. 

Let’s take a look at some of the options you have available when you want to share a notebook:

* __Send the file__: Given that the person you want to share the notebook with has a good grasp on files that end with “.ipynb”, you can potentially just send them the notebook file, and let them open it on their computer.  A major drawback here is that if the person you are sharing the notebook with has no clue about what a notebook is, they will have no idea on how to fire up a “.ipynb” file.
* __Convert to a friendlier format and then send it__:  If the person you want to share the notebook with has no idea of what a notebook is, you can start by converting the notebook to, let’s say, an HTML format, and then send them the file via email. To do this, you would probably use a tool such as [nbconvert](https://nbconvert.readthedocs.io/en/latest/). But have you seen a notebook converted to PDF? It looks far from ideal. Also, if you convert it to HTML, not everyone (unfortunately) knows how to open “.HTML” files in their computer.
* [__NbViewer__](https://nbviewer.jupyter.org/): Given that your notebook is hosted in a public repo, this is your best option. You simply go to the website, paste the url for a notebook you want to share, [and voila](https://nbviewer.jupyter.org/github/duarteocarmo/technological_capabilities/blob/master/notebooks/4_1_Macro%20Level%20Analysis.ipynb)! However, you’ll need to set up a rapport gist to do this. And your notebook will be accessible to anyone. 
* [__GitHub__](https://github.com/duarteocarmo/technological_capabilities/blob/master/notebooks/4_1_Macro%20Level%20Analysis.ipynb): If your notebook is in a public repo, you can also send them the link to the notebook in GitHub. But notice how the table of contents does not work, you can’t link to a specific section, and you need to host your notebook in a repo.

These are good options, but each one of them has drawbacks. In an ideal world, sharing a notebook should be as easy as sharing a link to a google doc, I envision something that:

* Does not require you to convert your notebook. 
* Does not require you to create a repo, public or private. 
* Does not require the person you are sharing the notebook with to learn anything new. (how to deal with .ipynb files, how to open .html files)
* Keeps a functioning table of contents. 
* Allows you to link to a specific section. 
* Allows you to set a simple password when sharing, so that your work isn’t exposed to the whole world. 
* Allows you to share notebooks without leaving your beloved command line. 

Enter [__NbHub__](https://nbhub.duarteocarmo.com/). 

## NbHub: share your notebooks from the command line. 

*⚠️__Preliminary note__: NbHub is a proof of concept, or better, __NbHub is a hack__. It was developed in a weekend, has no guarantees of security or encryption, and is missing features like sharing notebooks with a password.  For now, it’s a glorified self-hosted nbviewer alternative with a cli tool.*

Let’s first see how it works from a user’s perspective, and then I’ll dive deeper into how it works. 

To get started, simply install the command line tool using pip (even though you should be using something like [pipx](https://github.com/pipxproject/pipx)):

```bash
$ pip3 install nbhub
```

Now, let’s say I want to share the “Analysis.ipynb” notebook with someone. Simply run:

```bash
$ nbhub Analysis.ipynb
```

You’ll be walked through a simple command-line script that asks you a couple of questions. Once you are done, you’ll receive a link such as [this one](https://nbhub.duarteocarmo.com/notebook/e6b917cb). By clicking it, you’ll see that your notebook is now on the web. You can just send that link to someone, and they’ll see your notebook. 

Another thing that I love, is that if I’m sharing a very large notebook, I can even link to a specific section of it. For example, click [here](https://nbhub.duarteocarmo.com/notebook/e6b917cb#five) to jump to the “contextual relationships” section of the example notebook. 

## How NbHub works

NbHub consists of: 

* A [web server](#the-webserver) that receives a GET request with a notebook data field, and responds with a link to a notebook on that same web server. 
* A [command-line tool](#the-cli-tool): The main package that walks the user through the process of sharing the notebook. 


Let’s dive a bit deeper into these two:

### The Webserver
The web server is a [FastAPI](https://fastapi.tiangolo.com/) app with 3 endpoints:

* `get("/")`: the homepage, or what you see when you visit [nbhub.duarteocarmo.com](nbhub.duarteocarmo.com). 
* `post(“/upload”)`: the endpoint that receives a post request with a notebook in the data field, converts it to .html, and then stores it in the server. 
* `get(“/notebook/id”)`: the endpoint that exposes a stored notebook, so that the user can see it. 

You can visit the [GitHub repo](https://github.com/duarteocarmo/nbhub_webservice), or read the code below:

```python 
@app.get("/") # present homepage
async def home():
    home_page = pathlib.Path("static/home.html").read_text()
    return fastapi.responses.HTMLResponse(content=home_page, status_code=200)


@app.post("/upload") # endpoint that receives notebook, converts and stores. 
async def respond(request: fastapi.Request):
    unique_id = str(uuid.uuid4()).split("-")[0]
    id_list = [item.stem for item in NOTEBOOK_STORAGE.glob("**/*.html")]

    while unique_id in id_list:
        unique_id = str(uuid.uuid4()).split("-")[0]

    notebook_path = NOTEBOOK_STORAGE / f"{unique_id}.ipynb"
    html_path = NOTEBOOK_STORAGE / f"{unique_id}.html"

    try:

        form = await request.form()
        contents = await form[SITE_POST_LABEL].read()

        notebook_json_keys = json.loads(contents).keys()

        assert "nbformat" in notebook_json_keys
        assert len(notebook_json_keys) == 4
        assert sys.getsizeof(contents) / 1000000 < NOTEBOOK_SIZE_LIMIT

        file = open(notebook_path, "wb")
        file.write(contents)
        file.close()

        converter = subprocess.run(["jupyter", "nbconvert", notebook_path])

        notebook_path.unlink()
        return {
            "status": "success",
            "path": f"http://{SITENAME}/notebook/{html_path.stem}",
            "password": "None",
            "expiry date": "None",
        }
    except Exception as e:
        print(str(e))
        raise fastapi.HTTPException(status_code=404, detail="ERROR")


@app.get("/notebook/{notebook_id}") # serve notebook with particular ID
async def read_notebook(notebook_id: str):
    file = pathlib.Path(NOTEBOOK_STORAGE / f"{notebook_id}.html")
    if file.is_file():
        file_contents = file.read_text()
        return fastapi.responses.HTMLResponse(
            content=file_contents, status_code=200
        )

    else:
        raise fastapi.HTTPException(
            status_code=404, detail="Notebook does not exist."
        )
```
### The CLI tool 
The command-line application is a [Click](https://click.palletsprojects.com/en/7.x/) application that emulates a post request with a given notebook. It also performs some user side checks. 

You can visit the [GitHub Repo](https://github.com/duarteocarmo/nbhub), or read the main code below as well:

```python
import click
import requests

POST_URL = "https://nbhub.duarteocarmo.com/upload"
SITE_POST_LABEL = "notebook-data"
SITE_URL = "https://nbhub.duarteocarmo.com"

@click.command()
@click.argument(
    "notebook",
    required=False,
    type=click.Path(
        exists=True,
        file_okay=True,
        dir_okay=True,
        readable=True,
        allow_dash=False,
    ),
)
def main(notebook):
    """Share notebooks from the command line.

    NOTEBOOK is the jupyter notebook file you would like to share.
    """
    check_notebook(notebook)
    click.echo("\nWelcome to NbHub!")
    click.echo(f"Consider supporting us at: {SITE_URL}\n")
    click.echo(f"You are about to publish {notebook}\n")
    click.confirm("Are you sure you want to publish it?", abort=True)
    if click.confirm("Do you wish to set a password?"):
        click.echo("")
        click.echo(
            f"Private notebooks are not available yet! 😬, check {SITE_URL} for updates"
        )

    else:
        assert status_ok(POST_URL) == True
        files = {SITE_POST_LABEL: open(notebook, "rb")}
        response = requests.post(POST_URL, files=files)
        if response.status_code == 200:
            link = response.json().get("path")
            click.echo("")
            click.echo("Published! ✨")
            click.echo(f"Visit your notebook at: {link}\n")

        else:
            click.echo("Sorry, something went wrong 😔")


def check_notebook(notebook):
    if not notebook:
        click.echo("No notebook provided, nothing to do 😇")
        click.Context.exit(0)


def status_ok(url):
    click.echo("\nQuerying the interwebs.. 🌎")
    try:
        requests.get(url)
    except Exception:
        click.echo("Sorry.. Our service appears to be down atm.")
        click.Context.exit(0)
        return False

    return True


if __name__ == "__main__":
    main()
```

## The road ahead
My idea with NbHub was simply to build something that works for me. For the past 2 months, I have been using it every week with clients or co-workers in projects. Of course, I haven’t been using it for sensitive information since the password feature is still missing. 

In the main repo, I included a [road-map](https://github.com/duarteocarmo/nbhub#roadmap) of features I would like to implement to make the tool even more awesome: 

* Date limit on notebooks to be destroyed.
* Ability to set a password on link creation for private notebooks.Or protecting notebooks with passwords. 
* Improvements to CLI like only accepting notebook format.
* Web server improvements (auto clean ups, encryption, etc.)

For now, I’ll keep using it as a hack, because this hack works, and hacks are awesome. 
