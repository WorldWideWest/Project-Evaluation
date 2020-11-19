import numpy as np
from periodChecking import *
from cashFlow import *
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
    
    task = str(input("Do you want to Rate your Project's? (Yes/No) "))
    
    if task.title() == "Yes":
        pass
    else:
        print("Do you want to see your cash flow compared to a interest rate?\n (If we add the interest Rate then we have a more realistic veiw\n of the cash flow of the project, because 1$ today and in 5 years won't have the same value)\n")
        rate = str(input("Do you want this compare (Yes/No) "))
        interest = float(input("What interset rate would you have in your bank? "))

        print("The Cash Flow for your Project's are: \n")
        cashFlow = NCF(projects)
        dataFrame = cashFlow.Table()
        print("\n")
        print("The return period's of your project's are: \n")

        evaluation = Methods(dataFrame)
        evaluation.PeriodOfReturn()
        
        print("\n")

        if rate.title() == "Yes":
            print("You chosed see the Discounted Period of Return\n")
            evaluation.NetPresentValue(interestRate=interest, printDataFrame=True, periodChecking=True)



