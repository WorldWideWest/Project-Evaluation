## Library's import

import numpy as np
import pandas as pd

## End of Library's import

## Classes import

from FinancialTable import *
from parsing import *

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

    def DiscountedPeriodOfReturn(self, interestRate, printDataFrame = True, periodChecking = True):
       #pd.options.display.float_format = '{:.15f}'.format
        parser = Parser(self.dataFrame)
        fullDataFrame = parser.Parse(dropCols=["Description"], printDataFrame=False)

        values = [1]
        finance = Factor()
        discountDF = pd.DataFrame()


        for i in range(1, len(fullDataFrame['Year'])):
            rate = finance.II(interestRate, i)
            values.append(rate)
        
        fullDataFrame.insert(1, f"Discount Factor ({interestRate})", values)

        for col in fullDataFrame.columns:
            if col == "Year" or col == f"Discount Factor ({interestRate})":
                pass
            else:
                fullDataFrame[f"{col} Discounted"] = fullDataFrame[f"Discount Factor ({interestRate})"] * fullDataFrame[col]
                discountDF[f"{col} Discounted"] = fullDataFrame[f"Discount Factor ({interestRate})"] * fullDataFrame[col]
        

        if periodChecking == True:
            periodCheck = parser.PeriodChecking(discountDF, printDataFrame=True)
            print(periodCheck)
        else:
            pass

        if printDataFrame == True:
            print(fullDataFrame)
            return fullDataFrame
        else:
            return fullDataFrame
        

        
            
            


