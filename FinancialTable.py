import numpy as np

class Factor():

    def I(self, p, n):
        i = 0 
        i = p / 100

        r = (1 + i)**n

        return np.round(r, 15)

    def II(self, p, n):
        i = 0 
        i = p / 100

        r = 1 / ((1 + i)**n)

        return np.round(r, 15)

    def III(self, p, n):
        i = 0 
        i = p / 100

        r = (((1 + i)**n) - 1) / i

        return np.round(r, 15)

    def IV(self, p, n):
        i = 0
        i = p / 100

        r = (1 - (1 / (1 + i)**n)) / i
        
        return np.round(r, 15)


class Values():
    def I(self, PV, p, n):
        i = 0 
        i = p / 100

        FV = PV * (1 + i)**n

        return np.round(FV, 15)

    def II(self, FV, p, n):
        i = 0 
        i = p / 100

        PV = FV / ((1 + i)**n)

        return np.round(PV, 15)

    def III(self, R, p, n):
        i = 0 
        i = p / 100

        FV = R * ((((1 + i)**n) - 1) / i)

        return np.round(FV, 15)

    def IV(self, R, p, n):
        i = 0
        i = p / 100

        PV = R * ((1 - (1 / (1 + i)**n)) / i)
        
        return np.round(PV, 15)