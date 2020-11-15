import numpy as np
from periodChecking import *
from NetCashFlow import *
from evaluatingMethods import *


print("Welcome to the Investment Project effciency Rating's\n")

projects = []
task = "yes"

while (task.title() == "Yes"):
    projectData = []
    project = str(input("Please input Project name: "))
    invest = float(input("Amount to Invest into the project: "))
    returnAmount = float(input("Amount of Return: "))
    ## Saving Input
    projectName = project
    projectData.append(project)
    projectData.append(invest)
    projectData.append(returnAmount)

    year = str(input("Do you have another year of returns: (Yes/No) "))
    while(year.title() == "Yes"):
        returnAmount = float(input("Amount of Return: "))
        projectData.append(returnAmount)
        year = str(input("Do you have another year of returns: (Yes/No) "))
    projects.append(projectData)
    
    task = str(input("Do you want to Rate your Project's? (Yes/No)"))
    
    if task.title() == "Yes":
        pass
    else:
        cashFlow = NCF(projects)
        cashFlow.Table()



