from bs4 import BeautifulSoup
from zeitonline.util import WebsiteInformation, NEWS_LINK, NEWS_LINK_CONTENTS, NEWS_TITLE, NEWS_REFERENCES, NEWS_COUNT
import requests


# parse html string document -> staring with the <article> tag of a website. Store parsed data in
# WebsiteInformation class Returns: WebsiteInformation Object -- get WebsiteInformation
class ZeitOnlineParserNews:
    def __init__(self, html_document, verbose):
        self.verbose = verbose
        self.soup = BeautifulSoup(html_document, 'html.parser')
        self.news_info = WebsiteInformation(verbose, [
            NEWS_COUNT,
            NEWS_REFERENCES
        ])
        self.news_info.track_content[NEWS_REFERENCES] = []
        if not self.verbose:
            print("News Parser setup\n")

    # start parsing the website Returns: return WebsiteInformation -- parse website new articles and store all found
    # information in the WebsiteInformation class
    def parse(self):
        news = self.soup.find_all(
            "a", {"class": "zon-teaser-standard__combined-link"})  # this html a contains all teaser article links
        news_collected = []
        for news_teaser in news:
            if ("liveblog" not in news_teaser["href"]) & (not news_collected.__contains__(news_teaser["href"])):
                news_collected.append(news_teaser["href"])
                self.news_info.track_content[NEWS_REFERENCES].append({
                    NEWS_LINK: news_teaser["href"],
                    NEWS_LINK_CONTENTS: news_teaser["href"].replace('https://www.zeit.de/', "").replace("/", '\\'),
                    NEWS_TITLE: news_teaser["title"]
                })
        self.news_info.update(NEWS_COUNT, str(self.news_info.track_content[NEWS_REFERENCES].__len__()))
        print(self.news_info.get_track_content(clear=False))
        return self.news_info.get_track_content(clear=False)