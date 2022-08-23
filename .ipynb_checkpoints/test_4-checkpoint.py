import unittest
from pandas.testing import assert_frame_equal
from functions import *

class TestRatingAdj_2(unittest.TestCase):
    def setUp(self):
        movie_list=pd.DataFrame([[3,9.0],[15,8.1],[0,7.5],[10,8.3],[5,7.7]], columns=['Values', 'Ratings'])
        oscar_nr = 'Values'
        rating_adj = 'Ratings'
        OscarCalculator(movie_list, rating_adj=rating_adj, oscar_nr=oscar_nr)
        self.rating=movie_list.Ratings.to_list()
        self.expected=[9.5, 9.6, 7.5, 9.3, 8.2]
    
    def test_count_oscar_values(self):
        self.assertCountEqual(self.rating, self.expected)

    def test_list_oscar_values(self):
        self.assertListEqual(self.rating, self.expected)
        
if __name__ == '__main__':
    unittest.main(verbosity=2)