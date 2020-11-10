import numpy as np


## Project's
## [0] - initial investment

project_A = np.array([15000, 1000, 2000, 3000, 4000, 5000, 6000], dtype=np.int32)
project_B = np.array([15000, 3500, 3500, 3500, 3500, 3500, 3500], dtype=np.int32)
project_C = np.array([15000, 6000, 5000, 4000, 3000, 2000, 1000], dtype=np.int32)

## Method - Net Present Value (NPV)

## 1. Calculation Net Cash Flow (NCF)
print("Net Cash Flow")

NCF_project_A = np.sum(project_A) - project_A[0]
print(f"Net Cash Flow for Project A is: {NCF_project_A}")

NCF_project_B = np.sum(project_B) - project_B[0]
print(f"Net Cash Flow for Project B is: {NCF_project_B}")

NCF_project_C = np.sum(project_C) - project_C[0]
print(f"Net Cash Flow for Project C is: {NCF_project_C}\n")

## 2. Calculating Net Value (NV)

print(f"Net Value of Project A: {NCF_project_A - project_A[0]}")
print(f"Net Value of Project B: {NCF_project_B - project_B[0]}")
print(f"Net Value of Project C: {NCF_project_C - project_C[0]}\n")

## 3. Calculating Average Cash Flow (ACF)

print(f"Average Cash Flow for Projec A: {NCF_project_A/(len(project_A)-1)}")
print(f"Average Cash Flow for Projec B: {NCF_project_B/(len(project_B)-1)}")
print(f"Average Cash Flow for Projec C: {NCF_project_C/(len(project_C)-1)}\n")

## 4. Calculating Average Yearly Profit (AYP)

print(f"Average Yearly Profit for Project A: {((NCF_project_A/(len(project_A)-1))/project_A[0])*100}")
print(f"Average Yearly Profit for Project B: {((NCF_project_B/(len(project_B)-1))/project_B[0])*100}")
print(f"Average Yearly Profit for Project C: {((NCF_project_C/(len(project_C)-1))/project_C[0])*100}\n")


# 1. Method - Period of return (POR)
## Project A
result_A = 0

for i in range(1, len(project_A)):
    result_A += project_A[i]
    if result_A >= project_A[0]:
        print(f"Period of return for this project is: {i} years")
        break

## Project B

result_B = 0


for j in range(1, len(project_B)):
    result_B += project_B[j]

    if result_B > project_B[0]:
        result_B = result_B - project_B[j]
        
        result = project_B[0] - result_B
        period = result / project_B[j]
        period = np.round(period, 2)
        period += j - 1
        print(f"The return period for this investment project is: {period} year's.")
        break

## Project C

result_C = 0


for k in range(1, len(project_C)):
    result_C += project_C[j]

    if result_C > project_C[0]:
        result_C = result_C - project_C[k]
        
        result = project_C[0] - result_C
        period = result / project_C[k]
        period = np.round(period, 2)
        period += k - 1
        print(f"The return period for this investment project is: {period} year's.")
        break