import numpy as np
import pandas as pd

class Methods():
    def __init__(self, dataFrame):
        self.dataFrame = dataFrame
        self.dataFrame = pd.DataFrame(self.dataFrame)
    
    def PeriodOfReturn(self):

        periodDataFrame = self.dataFrame
        ## Droping worthless columns
        periodDataFrame = periodDataFrame.drop(["Year", "Description"], axis = 1)
        periodDataFrame = periodDataFrame.drop(
            [
                periodDataFrame.index[-4],
                periodDataFrame.index[-3],
                periodDataFrame.index[-2],
                periodDataFrame.index[-1]])

        columns = periodDataFrame.columns
        year = 0
        

        for column in columns:
            columnIndex = periodDataFrame.columns.get_loc(column)
            returnPeriod = periodDataFrame.iloc[:, columnIndex].values
            
            returnPeriod = np.array(returnPeriod)

        for i in range(1, len(returnPeriod)):
            year += returnPeriod[i]
            if year == returnPeriod[0]:
                break
        return [year, i]
                
                


            






