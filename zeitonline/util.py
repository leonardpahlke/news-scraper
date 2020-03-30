TYPE_ARTICLE = "type_article"
TYPE_COMMENTS = "type_comments"

# constants
TITLE = "title"
SUB_TITLE = "sub_title"
SUMMARY = "summary"
RELEASE = "release"
SOURCE = "source"
AUTHOR = "author"
COMMENTS_COUNT = "comments_count"
ARTICLE_TEXT = "article_text"


# Store Article Information, designed to work with Zeit Online content Returns: WebsiteInformation -- access
# information with variables, print information with method <print_information/0>
class WebsiteInformation:
    # track_content contains all scrapped variables
    track_content = {}

    def __init__(self, verbose, variables: list):
        self.verbose = verbose
        # set variables in track
        for elem in variables:
            self.track_content[elem] = ""

    # ? update article variables in a safe matter
    def update(self, id, value, get_string):
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

    def get_track_content(self):
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
