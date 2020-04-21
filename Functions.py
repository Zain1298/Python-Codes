import numpy as np

#This function prints two matrices containing only zeros
arr = np.zeros((2,3))
print(arr)
#This function prints two matrices containing only ones
arr = np.ones((2,3))
print(arr)
#This function prints only ones in the diagonal
arr = np.eye(4,4)
print(arr)
#This function prints only given array in the diagonal 
arr=np.diag([1,2,3,4])
print(arr)
#This function prints the diagonal of any matrix
arr=np.eye(3,4)
np.diag(arr)
print(arr)
#This function prints the random number from 1 to 19
rand_arr = np.random.randint(1,20,6)
print(rand_arr)
