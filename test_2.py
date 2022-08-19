import unittest
import functions
from bs4 import BeautifulSoup
import requests
import re

class Test(unittest.TestCase):
    bs = None
    def setUpClass():
        url = 'https://www.imdb.com/title/tt0110912/'
        r = requests.get(url)
        Test.bs = BeautifulSoup(r.content, 'html.parser')
    def test_titleText(self):
        pageTitle = Test.bs.find('h1').get_text()
        self.assertEqual('Ponyvaregény', pageTitle);
    def test_contentExists(self):
        content = [b for b in Test.bs.find('a', attrs={'class': 'ipc-metadata-list-item__label ipc-metadata-list-item__label--link', 
                                                    'href' : re.compile('awards')})]
        self.assertIsNotNone(content)
    

if __name__ == '__main__':
    unittest.main()