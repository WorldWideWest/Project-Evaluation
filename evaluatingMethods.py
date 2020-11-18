## Library's import

import numpy as np
import pandas as pd

## End of Library's import

## Classes import

from classes.support.FinancialTable import *
from classes.support.parsing import *

## End of Classes import


#pd.options.display.float_format = '${:,.14f}'.format
class Methods():
    def __init__(self, dataFrame):
        self.dataFrame = dataFrame
        self.dataFrame = pd.DataFrame(self.dataFrame)
    
    def PeriodOfReturn(self):
        parser = Parser(self.dataFrame)
        periodDataFrame = parser.Parse(printDataFrame=False)

        periodCheck = parser.PeriodChecking(periodDataFrame, True)
        return periodCheck

    def DiscountedPeriodOfReturn(self, interestRate):
       #pd.options.display.float_format = '{:.15f}'.format
        parser = Parser(self.dataFrame)
        source = parser.Parse(dropCols=["Description"], printDataFrame=False)

        values = [1]
        finance = Factor()

        for i in range(1, len(source['Year'])):
            rate = finance.II(interestRate, i)
            values.append(rate)
        
        source.insert(1, f"Discount Factor ({interestRate})", values)

        for col in source.columns:
            if col == "Year" or col == f"Discount Factor ({interestRate})":
                pass
            else:
                source[f"{col} Discounted"] = source[f"Discount Factor ({interestRate})"] * source[col]

        print(source)
            
            











