from bs4 import BeautifulSoup
from zeitonline.util import WebsiteInformation, NEWS_LINK, NEWS_LINK_CONTENTS, NEWS_TITLE, NEWS_REFERENCES, NEWS_COUNT


# parse html string document -> staring with the <article> tag of a website. Store parsed data in
# WebsiteInformation class Returns: WebsiteInformation Object -- get WebsiteInformation
class ZeitOnlineParserNews:
    # news online reponse structure
    zeit_news = {}

    # constructor
    def __init__(self, html_document, verbose):
        self.verbose = verbose
        # link scrapper libary to html_document
        self.zeit_news = {
        NEWS_COUNT: "",
        NEWS_REFERENCES: []
    }
        self.soup = BeautifulSoup(html_document, 'html.parser')
        if not self.verbose:
            print("Start news parsing - \n" + str(self.zeit_news))

    # start parsing the website Returns: return WebsiteInformation -- parse website new articles and store all found
    # information in the WebsiteInformation class
    def parse(self):
        news = self.soup.find_all(
            "a", {"class": "zon-teaser-standard__combined-link"})  # this html a contains all teaser article links
        news_collected = []
        for news_teaser in news:
            # exclude schach, sodoku and liveblog posts
            if ("liveblog" not in news_teaser["href"]) and \
                    (not news_collected.__contains__(news_teaser["href"]) and
                     ("http://schach.zeit.de/" not in news_teaser["href"]) and
                     ("https://sudoku.zeit.de/" not in news_teaser["href"])):
                # add link to local list
                news_collected.append(news_teaser["href"])
                # store news info in response dict
                self.addResource(news_teaser["href"],
                                 news_teaser["href"].replace('https://www.zeit.de/', "").replace("/", ','),
                                 news_teaser["title"])

        self.zeit_news[NEWS_COUNT] = self.zeit_news[NEWS_REFERENCES].__len__()
        return self.zeit_news

    def addResource(self, articleLink, articleLinkContents, articleTitle):
        self.zeit_news[NEWS_REFERENCES].append({
            NEWS_LINK: articleLink,
            NEWS_LINK_CONTENTS: articleLinkContents,
            NEWS_TITLE: articleTitle
        })