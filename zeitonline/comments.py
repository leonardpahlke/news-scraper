from bs4 import BeautifulSoup
from zeitonline.util import WebsiteInformation


# parse html string document -> staring with the <article> tag of a website. Store parsed data in
# WebsiteInformation class Returns: WebsiteInformation Object -- get WebsiteInformation
class ZeitOnlineParserComments:
    def __init__(self, html_document, verbose):
        self.verbose = verbose
        self.soup = BeautifulSoup(html_document, 'html.parser')
        self.article_info = WebsiteInformation(verbose, [

        ])
        if not self.verbose:
            print("Comments Parser setup\n")

    # start parsing the website Returns: return WebsiteInformation -- parse website comments and store all found
    # information in the WebsiteInformation class
    def parse(self):
        return self.article_info.get_track_content()
