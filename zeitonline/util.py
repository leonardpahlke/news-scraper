TYPE_ARTICLE = "type_article"
TYPE_COMMENTS = "type_comments"
TYPE_NEWS = "type_news"

# article constants
ARTICLE_URL = "url"
ARTICLE_TITLE = "title"
ARTICLE_SUB_TITLE = "sub_title"
ARTICLE_SUMMARY = "summary"
ARTICLE_RELEASE = "release"
ARTICLE_SOURCE = "source"
ARTICLE_AUTHOR = "author"
ARTICLE_COMMENTS_COUNT = "comments_count"
ARTICLE_ARTICLE_TEXT = "article_text"

# comments constants

# news constants
NEWS_LINK = "link"
NEWS_LINK_CONTENTS = "link_contents"
NEWS_TITLE = "news_title"
NEWS_COUNT = "news_count"
NEWS_REFERENCES = "news_references"

# Store Article Information, designed to work with zeit-online content Returns: WebsiteInformation -- access
# information with variables, print information with method <print_information/0>
class WebsiteInformation:
    # track_content contains all scrapped variables
    track_content = {}

    def __init__(self, verbose, variables: list):
        self.verbose = verbose
        # set variables in track
        self.track_content = {}
        for elem in variables:
            self.track_content[elem] = ""

    # ? update article variables in a safe matter
    # ? if get_string flag is set, value.string is called
    def update(self, id, value, get_string=False):
        if value is not None:
            if get_string:
                value = value.string
            if value is not None:
                value = value.strip()
            if not self.verbose:
                print(value)
        else:
            value = ""
        self.track_content[id] = value

    def get_track_content(self, clear=True):
        if not clear:
            return self.track_content
        else:
            clear_track_content = {}
            for key, val in self.track_content.items():
                if val != "":
                    clear_track_content[key] = self._clear_value(val)
            return clear_track_content

    def _clear_value(self, value: str):
        return value\
            .replace("ä", "ae")\
            .replace("ö", "oe") \
            .replace("ü", "ue")\
            .replace("ß", "ss")\
            .replace("\\", "")\
            .strip()

    # ? print article information to console
    def print_information(self):
        print(self.get_track_content())
