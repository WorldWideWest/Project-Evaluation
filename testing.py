# Library's import

import unittest
from unittest.mock import patch

# File importing
from cashFlow import *
from periodChecking import *
from evaluatingMethods import *


# Testing Array's
project_A = ['Project 1', 15000, 1000, 2000, 3000, 4000, 5000, 6000]
project_B = ['Project 2', 15000, 3500, 3500, 3500, 3500, 3500, 3500]
project_C = ['Project 3', 15000, 6000, 5000, 4000, 3000, 2000, 1000]

projects = [project_A, project_B, project_C]
# End of testing array's

# Class Definition's

cashFlow = NCF(projects)

# End of Class Definition's


class MyTests(unittest.TestCase):

    def test_investment_type(self):
        """Testing Investment Type"""
        IRType = InvestmentReturnType(project_A)
        check = IRType.CheckType()
        self.assertEqual(check, [0, 1])

    def test_NCF_Table(self):
        """Testing CSF Table"""
        cashFlow.Table()

    def test_ReturnPeriod(self):
        """Testing the Period Checking"""

        dataFrame = cashFlow.Table(False)
        evaulation = Methods(dataFrame)
        table = evaulation.PeriodOfReturn()


    def test_discounted_Period_OF_Return(self):
        dataFrame = cashFlow.Table(False)
        evaulation = Methods(dataFrame)
        check = evaulation.NetPresentValue(5)

    def test_IRR(self):
        dataFrame = cashFlow.Table(False)
        evaulation = Methods(dataFrame)
        IRR = evaulation.InternalReturnRate(
            discountRates=[5, 10, 15, 20])
        self.assertEqual(list(IRR[1].iloc[:, 1]), [8.401320039839792, 10.609224716728805, 14.31470908026346])
    
    if __name__ == '__main__':
        unittest.main()
 