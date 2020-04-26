from bs4 import BeautifulSoup

from zeitonline.util import ARTICLE_TITLE, ARTICLE_SUB_TITLE, ARTICLE_SUMMARY, ARTICLE_RELEASE, ARTICLE_SOURCE, ARTICLE_AUTHOR, ARTICLE_COMMENTS_COUNT, ARTICLE_ARTICLE_TEXT, \
    WebsiteInformation


# parse html string document -> staring with the <article> tag of a website. Store parsed data in
# WebsiteInformation class Returns: WebsiteInformation Object -- get WebsiteInformation
class ZeitOnlineParserArticle:
    def __init__(self, html_document, verbose):
        self.verbose = verbose
        self.soup = BeautifulSoup(html_document, 'html.parser')
        self.article_info = WebsiteInformation(verbose, [
            ARTICLE_TITLE,
            ARTICLE_SUB_TITLE,
            ARTICLE_SUMMARY,
            ARTICLE_RELEASE,
            ARTICLE_SOURCE,
            ARTICLE_AUTHOR,
            ARTICLE_COMMENTS_COUNT,
            ARTICLE_ARTICLE_TEXT
        ])
        if not self.verbose:
            print("Article Parser setup\n")

    # start parsing the website Returns: return WebsiteInformation -- parse website article and store all found
    # information in the WebsiteInformation class
    def parse(self):
        # find header information
        header_html = self.soup.header  # header html contains all header information
        body_html = self.soup.find_all(
            "div", {"class": "article-body article-body--article"})  # this html div contains all article paragraphs

        self.soup = BeautifulSoup(str(header_html), 'html.parser')

        header_parse_information = [
            (ARTICLE_SUB_TITLE, "span", "article-heading__kicker"),
            (ARTICLE_TITLE, "span", "article-heading__title"),
            (ARTICLE_SUMMARY, "div", "summary"),
            (ARTICLE_RELEASE, "time", "metadata__date"),
            (ARTICLE_SOURCE, "span", "metadata__source"),
            (ARTICLE_COMMENTS_COUNT, "a", "metadata__commentcount")
        ]
        # get position
        parsed_tags_content = [(name, self.soup.find(tag, {clazz}))
                               for name, tag, clazz in header_parse_information]

        # data-ct-row="author"
        is_author = self.soup.find(
            attrs={"data-ct-row": "author"})
        if is_author is not None:
            self.article_info.update(ARTICLE_AUTHOR, self.soup.find(
                attrs={"itemprop": "name"}), True)
        # update positions
        for parsed_id, parsed_txt in parsed_tags_content:
            self.article_info.update(parsed_id, parsed_txt, True)

        # get article body information
        self.soup = BeautifulSoup(str(body_html), 'html.parser')

        # get paragraph text
        body_text_paragraphs = self.soup.find_all(
            "p", {"paragraph article__item"})
        # concat paragraph text
        article_text_with_spaces = [paragraph.text
                                        .replace("\n", "")
                                        .strip() for paragraph in body_text_paragraphs]

        if not self.verbose:
            print("\nInformation is scraped\n")

        # update article text
        self.article_info.update(
            ARTICLE_ARTICLE_TEXT, ' '.join("".join(article_text_with_spaces).split()), False)

        if not self.verbose:
            print("ARTICLE INFO START \n\n\n\n")
            self.article_info.print_information()
            print("ARTICLE INFO END \n\n\n\n")
        return self.article_info.get_track_content(clear=False)

    def addResource(self):
        pass
