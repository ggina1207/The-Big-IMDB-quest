import unittest
import functions
from bs4 import BeautifulSoup
import requests
import re

#https://www.tutorialspoint.com/python_web_scraping/python_web_scraping_testing_with_scrapers.htm
class TestSubPage(unittest.TestCase):
    bs = None
    def setUpClass():
        url = 'https://www.imdb.com/title/tt0110912/'
        r = requests.get(url)
        TestSubPage.bs = BeautifulSoup(r.content, 'html.parser')
    def test_titleText_subpage(self):
        pageTitle = TestSubPage.bs.find('h1').get_text()
        self.assertEqual('Ponyvaregény', pageTitle);
    def test_contentExists_subpage(self):
        content = [b for b in TestSubPage.bs.find('a', attrs={'class': 'ipc-metadata-list-item__label ipc-metadata-list-item__label--link', 
                                                    'href' : re.compile('awards')})]
        self.assertIsNotNone(content)
    

if __name__ == '__main__':
    unittest.main()