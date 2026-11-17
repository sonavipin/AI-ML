import numpy as np
'''
Create an array

Create a NumPy array containing:

5, 10, 15, 20, 25

Print the array.
'''
arr=np.array([5, 10, 15, 20, 25])
print(arr)

'''
Create a 2D array

Create this array:
10 20 30
40 50 60


Print it.
'''
arr=np.array([[10,20,30],[40,50,60]])
print(arr)

'''
Array properties

Using your 2D array, print:
- Number of dimensions
- Shape
- Total number of elements
- Data type
'''
print(f"Number of dimensions: {arr.ndim}")
print(f"Shape: {arr.shape}")
print(f"Total number of elements {arr.size}")
print(f"Data type: {arr.dtype}")

'''
Numerical operations
Create this array:
marks = np.array([75, 80, 65, 90, 85])
Calculate and print:
np.sum(marks)np.mean(marks)np.min(marks)np.max(marks)
'''
marks=np.array([75, 80, 65, 90, 85])
print(f"Sum: {np.sum(marks)}")
print(f"Mean: {np.mean(marks)}")
print(f"Min: {np.min(marks)}")
print(f"Max: {np.max(marks)}")