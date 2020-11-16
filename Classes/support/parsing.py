import pandas as pd


class Parsing():
    def __init__(self, dataFrame):
        self.dataFrame = pd.DataFrame(dataFrame)

    def Parse(self):
        self.dataFrame = self.dataFrame.drop(["Year", "Description"], axis = 1)
        self.dataFrame = self.dataFrame.drop(
            [
                self.dataFrame.index[-4],
                self.dataFrame.index[-3],
                self.dataFrame.index[-2],
                self.dataFrame.index[-1]
            ]
        )

        return self.dataFrame