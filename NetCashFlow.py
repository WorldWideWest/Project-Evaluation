## Table for getting first insights into the investment project
# IMPORTS

import numpy as np
import pandas as pd

# END IMPORTS


class NCFTable():
    def __init__(self, investing, returning):
        self.investing = investing
        self.returning = returning

    def Table(self):
        NCF = 0
        NCF = np.sum(self.returning)
        NetValue = NCF - self.investing[0]
        AvgNetCashFlow = NCF / len(self.returning)
        AvgYrProfit = (AvgNetCashFlow / self.investing[0]) * 100
        AvgYrProfit = np.round(AvgYrProfit, 3)
        
        print(f"Net Cash Flow for this project: {NCF}")
        print(f"Net Value for this project: {NetValue}")
        print(f"Average Net Cash Flow for this project: {AvgNetCashFlow}")
        print(f"Average Yearly Profit Rate for this project: {AvgYrProfit}%")

        return [NCF, NetValue, AvgNetCashFlow, AvgYrProfit]
