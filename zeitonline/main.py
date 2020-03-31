from bs4 import BeautifulSoup
from zeitonline.article import ZeitOnlineParserArticle
import requests

from zeitonline.news import ZeitOnlineParserNews
from zeitonline.util import TYPE_ARTICLE, TYPE_COMMENTS, TYPE_NEWS

URL_ZEIT_ONLINE = "https://www.zeit.de/"


# returns a response json with all content found
def run(parse_type="", path="", verbose=True):
    if not verbose:
        print(parse_type, path, verbose)
    if parse_type == TYPE_ARTICLE:
        if path == "":
            print("REQUEST ERROR -> PATH IS AN EMPTY STRING")
            return {'error': "REQUEST ERROR -> PATH IS AN EMPTY STRING"}
        else:
            url = URL_ZEIT_ONLINE + path
            url = url.replace('"', "")
            page = requests.get(str(url))
            soup = BeautifulSoup(str(page.text), 'html.parser')
            article = soup.find(
                "article", {"class": "article article--padded article--article"})
            if not verbose:
                print("article found")
            return ZeitOnlineParserArticle(str(article), verbose).parse()
    elif parse_type == TYPE_COMMENTS:
        print("WARNING Not yet supported")
        return {'error': "REQUEST ERROR -> Not yet supported"}
    elif parse_type == TYPE_NEWS:
        page = requests.get(URL_ZEIT_ONLINE)
        return ZeitOnlineParserNews(str(page.text), verbose).parse()
