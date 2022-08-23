import unittest
from pandas.testing import assert_frame_equal
from functions import *

class TestRatingAdj_1(unittest.TestCase):
    def setUp(self):
        movie_list=pd.DataFrame([[1234567,8.0],[345678,9.5],[2345678,7.5],[542345,8.5]], columns=['Values', 'Ratings'])
        rating_nr = 'Values'
        rating_adj = 'Ratings'
        max_value = max(movie_list['Values'])
        ReviewPenalizer(movie_list, rating_adj=rating_adj, rating_nr=rating_nr, max_value=max_value)
        self.rating=movie_list.Ratings.to_list()
        self.expected=[6.9, 7.5, 7.5, 6.7]
    
    def test_count_rating_values(self):
        self.assertCountEqual(self.rating, self.expected)

    def test_list_rating_values(self):
        self.assertListEqual(self.rating, self.expected)
        
if __name__ == '__main__':
    unittest.main()