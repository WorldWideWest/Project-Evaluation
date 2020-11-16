## Library's import

import unittest
from unittest.mock import patch

## File importing
from classes.cashFlow import *
from classes.periodChecking import *
from classes.evaluatingMethods import *


## Testing Array's
project_A = ['Project 1', 15000, 1000, 2000, 3000, 4000, 5000, 6000]
project_B = ['Project 2', 15000, 3500, 3500, 3500, 3500, 3500, 3500]
project_C = ['Project 3', 15000, 6000, 5000, 4000, 3000, 2000, 1000]

projects = [project_A, project_B, project_C]
## End of testing array's

## Class Definition's

cashFlow = NCF(projects)

## End of Class Definition's

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
        
        self.assertEqual(table, [5, 4.29, 3])


    if __name__ == '__main__':
        unittest.main()
