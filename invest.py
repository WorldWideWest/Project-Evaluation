import numpy as np
from periodChecking import *
from NetCashFlow import *

investing = np.array([15000])
returning = np.array([1000, 2000, 3000, 4000, 5000, 6000])

period = InvestmentReturnType(investing, returning)
IRType = period.CheckType()

cash = NCFTable(investing, returning)
cash.Table()
