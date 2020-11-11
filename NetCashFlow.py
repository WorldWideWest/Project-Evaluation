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



        statistics = pd.DataFrame(
            [
                ['Net Cash Flow', NCF],
                ['Net Value', NetValue],
                ['Average Net Cash Flow', AvgNetCashFlow],
                ['Average Yearly Profit Rate', AvgYrProfit]
            ],
            columns = ['Description', 'Project']
        ) 
        
        
        
        
        

        dataFrame = pd.DataFrame(columns = ['Year', 'Description', 'Project'])







        ## Adding the investment 
        for i in range(len(self.investing)):
            if dataFrame.empty:
                dataFrame = dataFrame.append(
                    {'Year': i, 'Description': 'Investment', 'Project': self.investing[i]}, ignore_index=True)
            else:
                pass
        
        ## Adding the return's
        if not dataFrame.empty:

            for j in range(0, len(self.returning)):
                dataFrame = dataFrame.append(
                    {'Year': j+1, 'Description': 'Return', 'Project': self.returning[j]}, ignore_index=True)

        ## Adding the table summary        

        dataFrame = dataFrame.append(statistics, ignore_index=True)
                
                
        print(dataFrame)

        return [NCF, NetValue, AvgNetCashFlow, AvgYrProfit]

