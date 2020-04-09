from bs4 import BeautifulSoup
from zeitonline.util import WebsiteInformation


# parse html string document -> staring with the <article> tag of a website. Store parsed data in
# WebsiteInformation class Returns: WebsiteInformation Object -- get WebsiteInformation
class ZeitOnlineParserComments:
    def __init__(self, html_document, verbose):
        self.verbose = verbose
        self.soup = BeautifulSoup(html_document, 'html.parser')
        self.comments_info = WebsiteInformation(verbose, [

        ])
        if not self.verbose:
            print("Comments Parser setup\n")

    # start parsing the website Returns: return WebsiteInformation -- parse website comments and store all found
    # information in the WebsiteInformation class
    def parse(self):
        return self.comments_info.get_track_content()


if __name__ == "__main__":
    url = "https://www.zeit.de/politik/ausland/2020-03/praesidentschaftswahl-polen-pis-coronavirus-pandemie"

    from selenium import webdriver
    from selenium.webdriver.common.keys import Keys

    driver = webdriver.Firefox()
    driver.get(url)
    # assert "Python" in driver.title
    elem = driver.find_element_by_name("a")
    elem.clear()
    elem.send_keys("pycon")
    elem.send_keys(Keys.RETURN)
    assert "No results found." not in driver.page_source
    driver.close()
