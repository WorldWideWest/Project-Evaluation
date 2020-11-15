## Table for getting first insights into the investment project
# IMPORTS

import numpy as np
import pandas as pd

# END IMPORTS

## PRoblems to fix
## The other projects dataFrame does not add more then 2 cols

class NCF():
    def __init__(self, projects):
        self.projects = projects
        self.dataFrame = pd.DataFrame(columns = ['Year', 'Description'])

    ## Formating 
    pd.options.display.float_format = '{:.2f}'.format
    ## End of Formating

    def Table(self, printDataFrame = True):
        
        self.testingFrame = []

        for project in self.projects:
            projectName = project[0]
            data = project[1:]

            ## Variable Declaration        
            cashFlow = 0
            netValue = 0
            avgCashFlow = 0
            avgYrProfit = 0
            ## End of Declarations

            ## Table Summary Calculation's
            cashFlow = np.sum(data[1:])
            netValue = cashFlow - np.sum(data[0])
            avgCashFlow = cashFlow / (len(data) - 1)
            avgYrProfit = (avgCashFlow / data[0]) * 100
            avgYrProfit = np.round(avgYrProfit, 3)
            ## End of Table Summary Calculation's

            ## Adding THE FIRST PROJECT
            if self.dataFrame.empty:
                self.dataFrame = self.dataFrame.append(
                    {'Year': 0, 'Description': 'Investment', f'{projectName}': data[0]}, ignore_index = True)
                
                for i in range(1, len(data)):
                    self.dataFrame = self.dataFrame.append(
                        {'Year': i, 'Description': 'Return', f'{projectName}': data[i]}, ignore_index = True)

                ## Creating the summary in the empty DataFrame
                summary = pd.DataFrame(
                [   ['Net Cash Flow', cashFlow],
                    ['Net Value', netValue],
                    ['Average Net Cash Flow', avgCashFlow],
                    ['Average Yearly Profit Rate', avgYrProfit]],
                columns = ['Description', f'{projectName}']) 

                ## Appending the summary to the dataFrame
                self.dataFrame = self.dataFrame.append(summary, ignore_index=True)

                self.testingFrame.append([cashFlow, netValue, avgCashFlow, avgYrProfit])
                
            ## ADDING ALL THE OTHER PROJECT'S
            elif not self.dataFrame.empty:
                structure = []
                summary = [cashFlow, netValue, avgCashFlow, avgYrProfit]
                
                for i in data:
                    structure.append(i)
                for j in summary:
                    structure.append(j)
                
                self.dataFrame[f'{projectName}'] = structure

                self.testingFrame.append([cashFlow, netValue, avgCashFlow, avgYrProfit])
        
        if printDataFrame == True:
            print(self.dataFrame)
            return self.dataFrame
        else:
            return self.dataFrame


        