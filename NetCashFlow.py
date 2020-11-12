## Table for getting first insights into the investment project
# IMPORTS

import numpy as np
import pandas as pd

# END IMPORTS


class NCF():
    def __init__(self, investing, returning):
        self.investing = investing
        self.returning = returning


    ## Formating 
    pd.options.display.float_format = '{:.2f}'.format
    ## End of Formating

    def Table(self, printDataFrame = True):
        NCF = 0
        NCF = np.sum(self.returning)
        NetValue = NCF - self.investing[0]
        AvgNetCashFlow = NCF / len(self.returning)
        AvgYrProfit = (AvgNetCashFlow / self.investing[0]) * 100
        AvgYrProfit = np.round(AvgYrProfit, 3)

        statistics = pd.DataFrame(
            [
                ['Net Cash Flow', NCF],
                ['Net Value', NetValue],
                ['Average Net Cash Flow', AvgNetCashFlow],
                ['Average Yearly Profit Rate', AvgYrProfit]
            ],
            columns = ['Description', 'Project']
        ) 
        
        self.dataFrame = pd.DataFrame(columns = ['Year', 'Description', 'Project'])

        ## Adding the investment 
        for i in range(len(self.investing)):
            if self.dataFrame.empty:
                self.dataFrame = self.dataFrame.append(
                    {'Year': i, 'Description': 'Investment', 'Project': self.investing[i]}, ignore_index=True)
            else:
                pass
        
        ## Adding the return's
        if not self.dataFrame.empty:

            for j in range(0, len(self.returning)):
                self.dataFrame = self.dataFrame.append(
                    {'Year': j+1, 'Description': 'Return', 'Project': self.returning[j]}, ignore_index=True)

        ## Adding the table summary        
        self.dataFrame = self.dataFrame.append(statistics, ignore_index=True)
        if printDataFrame == True:
            print(self.dataFrame)
        else:
            pass

        return  [NCF, NetValue, AvgNetCashFlow, AvgYrProfit]
    
    def OtherProjects(self, newInvestment, newReturning, printDataFrame = True):
        i = 1
        i += 1
        structure = []

        NCF = 0
        NCF = np.sum(newReturning)
        NetValue = NCF - newInvestment[0]
        AvgNetCashFlow = NCF / len(newReturning)
        AvgYrProfit = (AvgNetCashFlow / newInvestment[0]) * 100
        AvgYrProfit = np.round(AvgYrProfit, 3)

        statistics = [NCF, NetValue, AvgNetCashFlow, AvgYrProfit]

        for j in newInvestment:
            structure.append(j)
        for k in newReturning:
            structure.append(k)
        for g in statistics:
            structure.append(g)

        self.dataFrame[f"Project {i}"] = structure 

        if printDataFrame == True:
            print(self.dataFrame)
        else:
            pass
        
        return [NCF, NetValue, AvgNetCashFlow, AvgYrProfit]

    def ReturningDataFrame(self):
        return self.dataFrame