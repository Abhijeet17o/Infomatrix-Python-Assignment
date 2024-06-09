import numpy as np
import pandas as pd

### Q.1 Write a NumPy program to swap rows and columns of a given array in reverse order.
arr = np.array([[1,2,3], [4,5,6], [7,8,9]])
def rev(arr):
    arr1 = arr[::-1]
    print(arr1)
    
    arr2 = arr[:, ::-1]
    print(arr2)
rev(arr)
print()


### Q.2 - Write a NumPy program to find the most frequent value in an array.###
list1 = [6, 9, 5, 1, 4, 6, 7, 8, 9, 8, 7, 1, 7, 5, 1, 0, 1, 5, 5, 0, 8, 9, 0, 7, 0, 7, 6, 5, 1, 1, 9, 5, 3, 8, 7, 9, 6, 3, 4, 5, 9, 7, 2, 7, 0, 2, 2, 6]
arr1 = np.array(list1)

##(a) frequent value##
def freq(arr):
    fdict = dict()
    max = 0
    max_key = str()
    
    for item in arr:
        if str(item) in fdict:
            fdict[str(item)] += 1
        else:
            fdict[str(item)] = 1
            
    for key, value in fdict.items():
        if value > max:
            max_key = key
            max = value
    print(f"Most frequent element is: {max_key}")
    
freq(arr1)

##(b) sort it in descending order##
arr2 = np.sort(arr1)[::-1]
print(arr2)
print()


#Q.3 Write a Pandas Program to create a dataframe such that the column labels are Name, Rollnumber, Subject1, Subject2 and Total

df = pd.DataFrame(
    {
        "Name": ["P", "J", "B"],
        "Roll Number": [1, 5, 3],
        "Subject 1": [50, 55, 59],
        "Subject 2": [40, 57, 55], 
    }
)
df["Total"]= df.loc[:, ["Subject 1", "Subject 2"]].sum(axis=1)

print(df)
print()

# (i) Using Pandas function itself calculate the statistical summary(mean, median, mode, Quartiles, etc) of all the numerical columns.
df1 = df.loc[:,["Subject 1", "Subject 2"]]
print(df1.describe())
print()

# (ii)Sort the entire dataframe based on the alphabetical order 
df2 = df.sort_values(by="Name")
print(df2)
print()

# (iii)Change the dataset such that there are missing values and NAN values in the dataset and handle them appropriately.
df0 = pd.DataFrame(
    {
        "Name": ["P", "J", "B", "Z"],
        "Roll Number": [1, 5, 3, 7],
        "Subject 1": [50, 55, 59, pd.NA],
        "Subject 2": [40, 57, pd.NA, 55], 
    }
)
df0["Total"]= df0.loc[:, ["Subject 1", "Subject 2"]].sum(axis=1)
df3 = df0.fillna(value=0)
print(df3)
