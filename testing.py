## Library's import

import unittest

## File importing
from NetCashFlow import *
from periodChecking import *


## Testing Array's
investing = np.array([15000])
returning = np.array([1000, 2000, 3000, 4000, 5000, 6000])

IT = InvestmentReturnType(investing, returning)
CSF = NCFTable(investing, returning)

class MyTests(unittest.TestCase):
    
    def test_investment_type(self):
        """Testing Investment Type"""
        self.assertEqual(IT.CheckType(), [0, 1])


    def test_NCF_Table(self):
        """Testing CSF Table"""
        self.assertEqual(CSF.Table(), [21000, 6000, 3500, 23.333])


    if __name__ == '__main__':
        unittest.main()
