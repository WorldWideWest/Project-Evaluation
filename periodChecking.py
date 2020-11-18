## From the aspect of investment and income, investment project's devide into group's:
## 1. Single Investment Cycle - Single Return Cycle
## 2. Multiple Investment Cycle's - Single Return Cycle
## 3. Single Investment Cycle - Multiple Return Cycle's
## 4. Multiple Investment Cycle's - Multiple Return Cycle's

class InvestmentReturnType():
    def __init__(self, project):
        self.investmentCycle = [project[1]]
        self.returnCycle = project[1:]


    def CheckType(self, printOption = False):

        if len(self.investmentCycle) == 1 and len(self.returnCycle) == 1:
            if printOption == False:
                pass
            else:
                print("Single Investment Cycle - Single Return Cycle")
            return [0, 0]

        elif len(self.investmentCycle) >= 1 and len(self.returnCycle) == 1:
            if printOption == False:
                pass
            else:
                print("Multiple Investment Cycle's - Single Return Cycle")
            return [1, 0]

        elif len(self.investmentCycle) == 1 and len(self.returnCycle) >= 1:
            if printOption == False:
                pass
            else:
                print("Single Investment Cycle - Multiple Return Cycle's")
            return [0, 1]

        elif len(self.investmentCycle) >= 1 and len(self.returnCycle) >= 1:
            if printOption == False:
                pass
            else:
                print("Multiple Investment Cycle's - Multiple Return Cycle's")
            return [1, 1]