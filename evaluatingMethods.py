## Library's import

import numpy as np
import pandas as pd

## End of Library's import

## Classes import

from classes.support.parsing import Parser
from classes.support.FinancialTable import FinancialTables

## End of Classes import


class Methods():
    def __init__(self, dataFrame):
        self.dataFrame = dataFrame
        self.dataFrame = pd.DataFrame(self.dataFrame)
    
    def PeriodOfReturn(self):
        parser = Parser(self.dataFrame)
        periodDataFrame = parser.Parse()

        periodCheck = parser.PeriodChecking(periodDataFrame, True)
        return periodCheck

    # def DiscountedPeriodOfReturn(self, factor):
    #     parser = Parser(self.dataFrame)
    #     discountedDataFrame = parser.Parse(dropCols=["Description"])









