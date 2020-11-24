## File importing
from cashFlow import *
from periodChecking import *
from evaluatingMethods import *


## Testing Array's
project_A = ['Project 1', 15000, 1000, 2000, 3000, 4000, 5000, 6000]
project_B = ['Project 2', 15000, 3500, 3500, 3500, 3500, 3500, 3500]
project_C = ['Project 3', 15000, 6000, 5000, 4000, 3000, 2000, 1000]

projects = [project_A, project_B, project_C]
## End of testing array's

## Class Definition's

cashFlow = NCF(projects)

dataFrame = cashFlow.Table(False)
evaulation = Methods(dataFrame)
evaulation.InternalReturnRate()