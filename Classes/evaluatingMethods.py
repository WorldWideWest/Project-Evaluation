## Library's import

import numpy as np
import pandas as pd
import os

## End of Library's import

## Classes import

from ..classes.support.parsing import Parsing

## End of Classes import


class Methods():
    def __init__(self, dataFrame):
        self.dataFrame = dataFrame
        self.dataFrame = pd.DataFrame(self.dataFrame)
    

    def PeriodOfReturn(self):
        # parser = Parsing(self.dataFrame)
        # periodDataFrame = parser.Parse()


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
                    period = i + ((rateDifference/array[i]) - 1)

                    period = np.round(period, 2)                   
                    returnSum = returnSum - difference  
                    periodsTable.append(period)
                    break
                
            table = table.append({"Project Name": project, "Return Period": period}, ignore_index = True)

        print(table) 
        return periodsTable       
