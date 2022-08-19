import unittest
import functions
from bs4 import BeautifulSoup
import requests

class Test(unittest.TestCase):
    bs = None
    def setUpClass():
        url = 'https://www.imdb.com/chart/top/'
        r = requests.get(url)
        Test.bs = BeautifulSoup(r.content, 'html.parser')
    def test_titleText(self):
        pageTitle = Test.bs.find('h1').get_text()
        self.assertEqual('IMDb Top 250 Movies', pageTitle);
    def test_contentExists(self):
        content = [b.attrs.get('title') for b in Test.bs.select('td.ratingColumn strong')]
        self.assertIsNotNone(content)
    

if __name__ == '__main__':
    unittest.main()
