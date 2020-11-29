# Library's import

from parsing import *
from FinancialTable import *
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# End of Library's import

# Setting the options

sns.set()

# End of options

# Classes import


# End of Classes import


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

    def NetPresentValue(self, interestRate, printDataFrame=True, periodChecking=True):
       #pd.options.display.float_format = '{:.15f}'.format
        parser = Parser(self.dataFrame)
        fullDataFrame = parser.Parse(
            dropCols=["Description"], printDataFrame=False)

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
                fullDataFrame[f"{col} Discounted"] = fullDataFrame[
                    f"Discount Factor ({interestRate})"] * fullDataFrame[col]

                # Period Checking dataFrame
                discountDF[f"{col} Discounted"] = fullDataFrame[
                    f"Discount Factor ({interestRate})"] * fullDataFrame[col]

        totalData = ["NaN", "TOTAL"]
        NPVData = ["NaN", "Net Present Value"]

        for col in range(2, len(fullDataFrame.columns)):
            total = 0
            total = fullDataFrame.iloc[1:, col].sum()
            totalData.append(total)

            if 'Discounted' in fullDataFrame.columns[col]:
                NPV = total - fullDataFrame.iloc[0, col]
                NPVData.append(NPV)

            else:
                NPVData.append("-")

        totalDF = pd.DataFrame(columns=fullDataFrame.columns,
                               data=[totalData])

        NPVDF = pd.DataFrame(columns=fullDataFrame.columns,
                             data=[NPVData])

        fullDataFrame = fullDataFrame.append(totalDF)
        fullDataFrame = fullDataFrame.append(NPVDF)

        if periodChecking == True:
            periodCheck = parser.PeriodChecking(
                discountDF, printDataFrame=True)
            print(periodCheck)
        else:
            pass

        self.fullDataFrame = fullDataFrame

        if printDataFrame == True:
            print(fullDataFrame)
            return self.fullDataFrame, periodCheck
        else:
            return self.fullDataFrame, periodCheck

    def InternalReturnRate(self, discountRates=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]):

        finance = Values()
        parser = Parser(self.dataFrame)
        parsedDataFrame = parser.Parse(
            dropCols=["Description"], printDataFrame=False)

        preparedValues = []

        for rate in discountRates:
            totals = []
            differences = []
            if rate == 0:
                totals.append(rate)

                for col in range(1, len(parsedDataFrame.columns)):
                    total = 0
                    total = parsedDataFrame.iloc[1:, col].sum()
                    totals.append(total)

                for col in range(1, len(parsedDataFrame.columns)):
                    for val in range(1, len(totals)):
                        difference = 0
                        difference = totals[val] - parsedDataFrame.iloc[0, col]
                        differences.append(difference)
                        break

                for item in differences:
                    totals.append(item)
                preparedValues.append(totals)
            else:
                differences.clear()
                totals.clear()
                totals.append(rate)

                for col in range(1, parsedDataFrame.shape[1]):
                    discuntedSum = 0
                    for row in range(1, parsedDataFrame.shape[0]):
                        value = 0
                        value = finance.II(
                            parsedDataFrame.iloc[row, col], rate, row)
                        discuntedSum += value

                        if row == (parsedDataFrame.shape[0] - 1):
                            totals.append(discuntedSum)

                for val in range(1, len(totals)):
                    for col in range(1, len(parsedDataFrame.columns)):
                        difference = 0
                        difference = totals[val] - parsedDataFrame.iloc[0, col]
                        differences.append(difference)
                        break

                for item in differences:
                    totals.append(item)
                preparedValues.append(totals)

        # Creating DataFrame for the IRR values

        columns = ['Discount Rate']
        visualization = []

        for col in range(1, len(parsedDataFrame.columns)):
            column = f'{parsedDataFrame.columns[col]} CVCF'
            columns.append(column)

        for col in range(1, len(parsedDataFrame.columns)):
            column = f'{parsedDataFrame.columns[col]} NPV'
            columns.append(column)
            visualization.append(column)

        irrDataFrame = pd.DataFrame(
            columns=columns,
            data=preparedValues
        )
        print("CVCF - Current Value of the Cash flow\nNPV - Net Present Value")
        print(irrDataFrame)

        # Visualizing the content of the irrDataFrame

        sns.set_style("whitegrid")
        fig = plt.figure(figsize=(10, 8))
        ax = fig.add_subplot(1, 1, 1)

        ax.spines["bottom"].set_position(("data", 0.0))
        ax.spines["bottom"].set_color("black")

        plt.plot(irrDataFrame["Discount Rate"], irrDataFrame[visualization])
        plt.show()

        # End of Visualizationsa

        IRRates = []
        IRRColumns = []
        IRRDF = pd.DataFrame(columns=["Project", "IRR"])
        

        for col in irrDataFrame.columns:
            if "NPV" in col:
                npv_1, npv_2 = 0, 0
                irr_1, irr_2 = 0, 0
                IRR = 0
                for i in range(len(irrDataFrame[col])):
                    if irrDataFrame.at[i, col] < 0:
                        npv_2 = irrDataFrame.at[i, col]
                        npv_1 = irrDataFrame.at[i-1, col]

                        irr_2 = irrDataFrame.at[i, "Discount Rate"]
                        irr_1 = irrDataFrame.at[i-1, "Discount Rate"]

                        IRR = irr_1 + ((irr_2 - irr_1) / (npv_2 - npv_1)) * (0 - npv_1)
                
                        IRRDF = IRRDF.append({"Project":col, "IRR": IRR}, ignore_index=True)
                        break

        
        
        for col in IRRColumns:
            irr = 0
            for irr in IRRates:
                IRRDF[col] = irr
                break
        print(IRRDF)