import numpy as np

class FinancialTables():

    def I(self, PV, p, n):
        i = 0 
        i = p / 100

        FV = PV * (1 + i)**n

        return np.round(FV, 2)

    def II(self, FV, p, n):
        i = 0 
        i = p / 100

        PV = FV / (1 + i)**n

        return np.round(PV, 2)

    def III(self, R, p, n):
        i = 0 
        i = p / 100

        FV = R * ((((1 + i)**n) - 1) / i)

        return np.round(FV, 2)

    def IV(self, R, p, n):
        i = 0
        i = p / 100

        PV = R * ((1 - (1 / (1 + i)**n)) / i)
        
        return np.round(PV, 2)