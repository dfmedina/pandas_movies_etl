import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import unittest


class PandasIntro(object):

    def __init__(self):
        pd.set_option('max_columns', 50)

    def generate_series(self, series, index=['A', 'Z', 'C', 'Y', 'E']):
        # create a Series with an arbitrary list with an specified index
        return pd.Series([series], index)


    d = {'Chicago': 1000, 'New York': 1300, 'Portland': 900, 'San Francisco': 1100,
         'Austin': 450, 'Boston': None}

    cities = pd.Series(d)

    print(cities)
    print(cities['Chicago'])
    print(cities[['Chicago', 'Portland', 'San Francisco']])
    print(cities[cities < 1000])

    less_than_1000 = cities < 1000
    print(less_than_1000)
    print('\n')
    print(cities[less_than_1000])

    data = {'year': [2010, 2011, 2012, 2011, 2012, 2010, 2011, 2012],
            'team': ['Bears', 'Bears', 'Bears', 'Packers', 'Packers', 'Lions', 'Lions', 'Lions'],
            'wins': [11, 8, 10, 15, 11, 6, 10, 4],
            'losses': [5, 8, 6, 1, 5, 10, 6, 12]}
    football = pd.DataFrame(data, columns=['year', 'team', 'wins', 'losses'])
    print(football)


class TestPandasIntro(unittest.TestCase):

    def setUp(self):
        self.pandas = PandasIntro()

    def test_series_generation(self):
        self.pandas.generate_series([7, 'Heisenberg', 3.14, -1789710578, 'Happy Eating!'])