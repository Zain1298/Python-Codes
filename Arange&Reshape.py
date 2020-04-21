import numpy as np 

#This will print numbers from 1 to 10
arr = np.arange(1,11)
print(arr)
#Shows the size of an array
print(arr.size)

#Prints the array into 2 rows & 5 columns
print(arr.reshape(2,5))

#or 
#if no. of columns are not known and no. of rows are known
#so the correct no. of rows 
#and put a negative number in a column so coulmns can be known by seeing the answer.
print(arr.reshape(2,-1))



