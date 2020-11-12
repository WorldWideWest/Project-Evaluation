import numpy as np
from periodChecking import *
from NetCashFlow import *

project_A_investing = np.array([15000])
project_A_returning = np.array([1000, 2000, 3000, 4000, 5000, 6000])

period = InvestmentReturnType(project_A_investing, project_A_returning)
IRType = period.CheckType()

cash = NCFTable(project_A_investing, project_A_returning)
cash.Table(printDataFrame=False)


project_B_investing = np.array([15000])
project_B_returning = np.array([3500, 3500, 3500, 3500, 3500, 3500])

cash.OtherProjects(project_B_investing, project_B_returning)