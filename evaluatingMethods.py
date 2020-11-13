import numpy as np
import pandas as pd

class Methods():
    def __init__(self, dataFrame):
        self.dataFrame = dataFrame
        self.dataFrame = pd.DataFrame(self.dataFrame)
    
    def PeriodOfReturn(self):

        # PARSING THE DATAFRAME

        periodDataFrame = self.dataFrame

        ## Droping worthless columns
        periodDataFrame = periodDataFrame.drop(["Year", "Description"], axis = 1)
        periodDataFrame = periodDataFrame.drop(
            [
                periodDataFrame.index[-4],
                periodDataFrame.index[-3],
                periodDataFrame.index[-2],
                periodDataFrame.index[-1]
            ]
        )

        i = 0
        returnSum = 0
        periodsTable = []

        

        table = pd.DataFrame(
            {
                "Project Name": [],
                "Return Period": []    
            }
        )

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
                    period = i + (rateDifference/array[i])

                    period = np.round(period, 2)                   
                    returnSum = returnSum - difference  
                    periodsTable.append(period)
                    break
                
            table = table.append({"Project Name": project, "Return Period": period}, ignore_index = True)

        print(table) 
        return periodsTable       
