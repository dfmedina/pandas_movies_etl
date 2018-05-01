import unittest
import pandas as pd


class TestPandasEtl(unittest.TestCase):

    def setUp(self):
        self.data_set = '../dataset/movie_metadata.csv'
        pass

    def test_import_csv(self):
        movies_df = pd.read_csv(self.data_set)
        print(movies_df.keys())

    def test_count_movies(self):
        movies_df = pd.read_csv(self.data_set)
        print(movies_df.groupby('movie_title').nunique())
        print(movies_df.movie_title.value_counts())
        print(len(movies_df.movie_title))
