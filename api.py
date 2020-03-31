from fastapi import FastAPI
from pydantic import BaseModel

from zeitonline.main import run
from zeitonline.util import TYPE_ARTICLE, TYPE_NEWS

app = FastAPI()


class Article(BaseModel):
    title: str
    sub_title: str
    summary: str
    release: str
    source: str
    author: str
    comments_count: str
    article_text: str


@app.get("/")
def read_root():
    return {"Routes": ["/article/{category}/{sub_category}/{title}/{date}", "/article/{url}", "/test"]}


# ? zeit-online article url reference category, sub_category,  title, date
@app.get("/article/{category}/{sub_category}/{title}/{date}")
def article(category: str, sub_category: str, title: str, date: str):
    if date is None:
        date = ""
    return _article(path=category + "/" + sub_category + "/" + date + "/" + title)


# ? zeit-online url
@app.get("/article/{url}")
def article(url: str):
    url = url.replace("\\", "/")
    return _article(path=url)


# ? category, sub_category,  title
@app.get("/test")
def test():
    return _article(path="politik/ausland/2020-03/donald-trump-coronavirus-wirtschaft-usa-ostern", verbose=False)# ? category, sub_category,  title


@app.get("/news")
def news():
    return run(parse_type=TYPE_NEWS)


def _article(path="", verbose=True, url=""):
    content = run(parse_type=TYPE_ARTICLE, path=path, verbose=verbose)
    if not verbose:
        print("\nAPI.PY ARTICLE INFORMATION\n\n")
        print(content)
    return content


def _news(path="", verbose=True, url=""):
    content = run(parse_type=TYPE_ARTICLE, path=path, verbose=verbose)
    if not verbose:
        print("\nAPI.PY ARTICLE INFORMATION\n\n")
        print(content)
    return content

# uvicorn api:app --reload
# http://localhost:8080/article/politik/ausland/donald-trump-coronavirus-wirtschaft-usa-ostern/2020-03