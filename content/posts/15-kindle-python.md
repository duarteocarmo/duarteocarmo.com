title: Managing kindle highlights with Python and GitHub
date: 25-02-2020

**tl;dr:** *use [this script](#code) to build a [GitHub Repo like this one](https://github.com/duarteocarmo/my-personal-zen) where you store all the highlights from your kindle books in an organized way.*

**⚠️ Update:** Want to receive your kindle highlights as a newsletter? Well, I [built something your will probably like!](https://kindle-highlights.email/)

## Kindle sucks, kindle is great

We all love reading in our Kindle. You can travel with more than one book at the time, you can search for words you don't understand, you have access to millions of books you can't find in your local library.. It's great!

But when we're older, all of the shelves in our houses will have no books, our kids won't know what we read, and we won't be able to revisit them. 

One option is to bulk buy the physical copies in some years. 

While that doesn't happen, why not keep all the most important highlights in a nicely kept [GitHub Repo](https://github.com/duarteocarmo/my-personal-zen/tree/master/books)?

## Highlights 

When reading in my Kindle, I tend to highlight a lot of passages I find interesting. When you do so, the device locally stores a `My Clippings.txt` file that aggregates all of your highlights across different books. 

## Using GitHub

In the [books](https://github.com/duarteocarmo/my-personal-zen/tree/master/books) folder of *"my-personal-zen"* repo you can notice that every book has its own markdown file where I keep all of the highlights related to it. For example, [here](https://github.com/duarteocarmo/my-personal-zen/blob/master/books/Mans%20Search%20for%20Meaning.md) are my favorite parts of Viktor Frankl's *Man's Search for Meaning*. 

## Python for the (parsing) win

To make this happen, I created a small python [script](https://github.com/duarteocarmo/my-personal-zen/blob/master/highlight_parser.py) that parses a `My Clippings.txt` file every time I connect my Kindle to my computer. And then its just a matter of moving these files to a repo and pushing it to GitHub. 

Here's a walk through of the code that you can also find in full [here](https://github.com/duarteocarmo/my-personal-zen/blob/master/highlight_parser.py):<a name="code"></a> 

We start by creating a `Book` class:

```python
class Book:
    book_list = set()

    def __init__(self, title, author):
        self.author = author
        self.title = title
        self.highlights = []
        Book.book_list.add(self.title)

    def add_highlight(self, highlight):
        if highlight:
            self.highlights.append(highlight)

    def __str__(self):
        return f"<Book Object>Title:{self.title}\tAuthor:{self.author}\tHighlights:{len(self.highlights)}"

    def write_book(self, format="markdown"):
        if self.title == None or len(self.highlights) == 0:
            print(f"Not writting because name is None.")
            return False
        clean_title = "".join(
            [c for c in self.title if c.isalpha() or c.isdigit() or c == " "]
        ).rstrip()
        with open(f"{clean_title}.md", "w+") as file:
            file.write(f"# {clean_title}")
            file.write("\n")
            for h in self.highlights:
                clean_text = h.replace("\n", " ")
                file.write(f"- {clean_text}")
                file.write("\n")

            file.close()
```
After that, we create a `Highlight` class:

```python
class Highlight:
    total_highlights = 0

    def __init__(self, raw_string):
        (
            self.title,
            self.author,
            self.content,
        ) = Highlight.parse_single_highlight(raw_string)

    def __str__(self):
        return f"<Highlight Object> Title:{self.title}\tAuthor:{self.author}\tContent:{self.content}"

    @staticmethod
    def parse_single_highlight(highlight_string):
        splitted_string = highlight_string.split("\n")
        author_line = splitted_string[1]
        content = splitted_string[-2]
        regex = r"\((.*?)\)"
        match = re.search("\((.*)\)", author_line)

        if match:
            author = match.group(1)
            title = author_line[: match.start()]
            return title, author, content

        return None, None, None


```

Once those are created, just run the following script to output the markdown files:
```python
current_directory = pathlib.Path.cwd()
parsed_books = list(
    set(file.stem for file in current_directory.glob("**/*.md"))
)
highlight_separator = "=========="
highlight_json = dict()
library = []


with open("My Clippings.txt", "r") as file:
    data = file.read()

highlights = data.split(highlight_separator)

for raw_string in highlights:
    h = Highlight(raw_string)
    if h.title not in Book.book_list:
        b = Book(h.title, h.author)
        b.add_highlight(h.content)
        library.append(b)
    else:
        for b in library:
            if b.title == h.title:
                b.add_highlight(h.content)

for book in library:
    if book.title:
        if book.title.strip() not in parsed_books:
            book.write_book(format="markdown")
        else:
            print(f"{book.title} is already written.")
```

Now you are all set!
