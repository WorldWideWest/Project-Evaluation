## From the aspect of investment and income, investment project's devide into group's:
## 1. Single Investment Cycle - Single Return Cycle
## 2. Multiple Investment Cycle's - Single Return Cycle
## 3. Single Investment Cycle - Multiple Return Cycle's
## 4.  Multiple Investment Cycle's - Multiple Return Cycle's

class InvestmentReturnType():
    def __init__(self, investmentCycle, returnCycle):
        self.investmentCycle = investmentCycle
        self.returnCycle = returnCycle


    def CheckType(self):
        if len(self.investmentCycle) == 1 and len(self.returnCycle) == 1:
            print("Single Investment Cycle - Single Return Cycle")
            IRType = [0, 0]
            return IRType
        elif len(self.investmentCycle) >= 1 and len(self.returnCycle) == 1:
            print("Multiple Investment Cycle's - Single Return Cycle")
            IRType = [1, 0]
            return IRType
        elif len(self.investmentCycle) == 1 and len(self.returnCycle) >= 1:
            print("Single Investment Cycle - Multiple Return Cycle's")
            IRType = [0, 1]
            return IRType
        elif len(self.investmentCycle) >= 1 and len(self.returnCycle) >= 1:
            print("Multiple Investment Cycle's - Multiple Return Cycle's")
            IRType = [1, 1]
            return IRType



