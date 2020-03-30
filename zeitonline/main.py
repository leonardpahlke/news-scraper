from bs4 import BeautifulSoup
from zeitonline.article import ZeitOnlineParserArticle
import requests

from zeitonline.util import TYPE_ARTICLE, TYPE_COMMENTS


# returns a response json with all content found
def run(parse_type, path, verbose, url):
    if path == url:
        print("REQUEST ERROR")
    if not verbose:
        print(parse_type, path, verbose, url)
    if parse_type == TYPE_ARTICLE:
        url = url if url != "" else "https://www.zeit.de/" + path
        page = requests.get(url)
        soup = BeautifulSoup(str(page.text), 'html.parser')
        article = soup.find(
            "article", {"class": "article article--padded article--article"})
        if not verbose:
            print("article found")
        return ZeitOnlineParserArticle(str(article), verbose).parse()
    elif parse_type == TYPE_COMMENTS:
        print("WARNING Not yet supported")
        pass