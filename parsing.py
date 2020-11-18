import numpy as np
import pandas as pd


class Parser():
    def __init__(self, dataFrame):
        self.dataFrame = pd.DataFrame(dataFrame)

    def Parse(self, dropCols = ["Year", "Description"], printDataFrame = True):
        self.dataFrame = self.dataFrame.drop(dropCols, axis = 1)
        self.dataFrame = self.dataFrame.drop(
            [
                self.dataFrame.index[-4],
                self.dataFrame.index[-3],
                self.dataFrame.index[-2],
                self.dataFrame.index[-1]
            ]
        )
        if printDataFrame == True:
            print(self.dataFrame)
            return self.dataFrame
        else:
            pass
        return self.dataFrame

    def PeriodChecking(self, periodDataFrame, printDataFrame = True):
        i = 0
        returnSum = 0
        periodsTable = []
    
        table = pd.DataFrame(
            {
                "Project Name": [],
                "Return Period": []    
            }
        )

        if 'Year' in periodDataFrame.columns:
            periodDataFrame = periodDataFrame.drop(['Year'], axis = 1)
        elif 'Description' in periodDataFrame.columns:
            periodDataFrame = periodDataFrame.drop(['Description'], axis = 1)
        for project in periodDataFrame:

            returnSum = 0
            array = np.array(periodDataFrame[project])
            
            for i in range(1, len(array)):

                returnSum += array[i]

                if returnSum == array[0]:
                    period = i
                    periodsTable.append(period)
                    break
                    
                elif returnSum > array[0]:
                    
                    difference = returnSum - array[0]
                    rateDifference = array[i] - difference
                    period = i + ((rateDifference/array[i]) - 1)

                    period = np.round(period, 2)                   
                    returnSum = returnSum - difference  
                    periodsTable.append(period)
                    break
                
            table = table.append({"Project Name": project, "Return Period": period}, ignore_index = True)

        if printDataFrame == True:
            print(table)
            return periodsTable
        else:
            return periodsTable    

        