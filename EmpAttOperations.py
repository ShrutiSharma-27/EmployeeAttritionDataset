# Getting dataset
!kaggle datasets download -d patelprashant/employee-attrition

# Importing Libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Reading csv
Data = pd.read_csv("WA_Fn-UseC_-HR-Employee-Attrition.csv")

# Getting an idea of data inside the dataset
Data.head()

Data.shape

Data.columns

#plot showing relation between education and department given education should be equal to 1 and hence show the number of employees in each department with respect to their education which should be equal to 1.
# Using seaborn library 
sns.countplot(x ='Department', data = Data[Data.Education == 1])         # Data.Education == 1 : To extract only the rows with Education = 1

# To give title & labels to the plot
plt.title('Relation between Education & Departments.')
plt.ylabel('No. of employees with Education=1')
plt.xlabel('Department Name')

# To show plot
plt.show()

#Compute the median, average and modal monthly income for both male and female.
# To count unique values of monthly income
def UNIQUE(LIST):
  UniVal = []
  Count = []        # Count of corresponding elements stored in a list
  for a in LIST:
    UniVal.append(a)
    c = 0             # Variable for count of each element
    for duplicate in LIST:
      if duplicate == a :
        c = c + 1
        LIST.remove(a)
      else:
        pass
    Count.append(c)
  print(LIST, Count)

# For Male

MaleINC_List = []                                 #List to store all monthly incomes of gender - male
for a in range (len(Data)):
  if Data.Gender[a] == 'Male' :
    MaleINC_List.append(Data.MonthlyIncome[a])

MaleINC_List.sort()                              #To arrange monthly incomes of males in ASCENDING order
print(MaleINC_List)

# MEDIAN
N = len(MaleINC_List)                              #Here, N=882
print ('Total males = ',N)
MMedian = (MaleINC_List[440] + MaleINC_List[441])/2  # Median = [(882/2)th obsv + (882/2 + 1) obsv.]/2  ; 441th & 442th elements have 440 & 441 index respectively.
print(MMedian)

# AVERAGE
sum = 0 
for e in MaleINC_List :
  sum = sum + e
avg = sum/1470
print(avg)

# MODE
UNIQUE(MaleINC_List)

# For Female

FemaleINC_List = []                                 #List to store all monthly incomes of gender - feale
for b in range (len(Data)):
  if Data.Gender[b] == 'Female' :
    FemaleINC_List.append(Data.MonthlyIncome[b])

FemaleINC_List.sort()                              #To arrange monthly incomes of females in ASCENDING order
print(FemaleINC_List)


# MEDIAN
FN = len(FemaleINC_List)
print ('Total females = ',FN)
FMedian = (FemaleINC_List[293] + FemaleINC_List[294])/2  # Median = [(588/2)th obsv + (588/2 + 1) obsv.]/2  ; 294th & 295th elements have 293 & 294 index respectively.
print(FMedian)


# AVERAGE
Fsum = 0 
for j in FemaleINC_List :
  Fsum = Fsum + j
Favg = Fsum/1470
print(Favg)

# MODE
UNIQUE(MaleINC_List)
