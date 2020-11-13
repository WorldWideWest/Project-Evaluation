## Library's import

import unittest

## File importing
from NetCashFlow import *
from periodChecking import *
from evaluatingMethods import *


## Testing Array's
investing_A = np.array([15000])
returning_A = np.array([1000, 2000, 3000, 4000, 5000, 6000])

investing_B = np.array([15000])
returning_B = np.array([3500, 3500, 3500, 3500, 3500, 3500])

investing_C = np.array([15000])
returning_C = np.array([6000, 5000, 4000, 3000, 2000, 1000])

## End of testing array's

investing = [investing_A, investing_B, investing_C]
returning = [returning_A, returning_B, returning_C]


cashFlow = NCF(investing_A, returning_A)
cashFlow.Table(False)
cashFlow.OtherProjects(investing_C, returning_C, False)

data = cashFlow.ReturningDataFrame()
evaluation = Methods(data)


class MyTests(unittest.TestCase):
    
    def test_investment_type(self):
        """Testing Investment Type"""
        for i in investing:
            for r in returning:
                IT = InvestmentReturnType(i, r)
                self.assertEqual(IT.CheckType(), [0, 1])
                break

    def test_NCF_Table(self):
        """Testing CSF Table"""
        table = cashFlow.Table(printDataFrame=False)
        self.assertEqual(table, [21000, 6000, 3500, 23.333])

    def test_Other_Projects(self):
        """Testing Adding Columns to DataFrame"""
        self.assertEqual(cashFlow.OtherProjects(investing_C, returning_C, False), [21000, 6000, 3500, 23.333])

    def test_ReturnPeriod(self):
        """Testing the Period Checking"""
        self.assertEqual(evaluation.PeriodOfReturn(), [5, 3])

    if __name__ == '__main__':
        unittest.main()
