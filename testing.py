## Library's import

import unittest

## File importing
from NetCashFlow import *
from periodChecking import *
from evaluatingMethods import *


## Testing Array's
investing_A = np.array([15000])
returning_A = np.array([1000, 2000, 3000, 4000, 5000, 6000])

# investing_B = np.array([15000])
# returning_B = np.array([3500, 3500, 3500, 3500, 3500, 3500])

IT = InvestmentReturnType(investing_A, returning_A)
CSF = NCF(investing_A, returning_A)
EVAL = Methods(CSF.ReturningDataFrame())

class MyTests(unittest.TestCase):
    
    def test_investment_type(self):
        """Testing Investment Type"""
        self.assertEqual(IT.CheckType(), [0, 1])


    def test_NCF_Table(self):
        """Testing CSF Table"""
        table = CSF.Table(printDataFrame=False)
        self.assertEqual(table, [21000, 6000, 3500, 23.333])

    # def test_Other_Projects(self):
    #     """Testing Adding Columns to DataFrame"""
    #     self.assertEqual(CSF.OtherProjects(investing_B, returning_B), [21000, 6000, 3500, 23.333])

    ## Disabled until we implement the add to list feture

    def test_ReturnPeriod(self):
        """Testing the Period Checking"""
        self.assertEqual(EVAL.PeriodOfReturn(), [15000, 5])

    if __name__ == '__main__':
        unittest.main()
