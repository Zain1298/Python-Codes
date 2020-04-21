import numpy as np

#This function prints 20 random numbers from 1 to 50 
arr = np.random.randint(1,50,20)
print(arr)
#shape is 1D array
print(arr.shape)

#Now this will convert 1D array into 2D array
arr = arr.reshape(2,10)
print(arr)
#Now the shape is 2D array
print(arr.shape)

#Rearrnage into 1D array
arr = arr.reshape(20)
print(arr)

