'''
Create this array:
numbers = np.array([12, 24, 36, 48, 60, 72])

Print:
1. First element
2. Third element
3. Last element
4. Second-last element

'''
import numpy as np
numbers=np.array([12, 24, 36, 48, 60, 72])
print(f"First Element: {numbers[0]}")
print(f"Third element: {numbers[2]}")
print(f"Last element: {numbers[-1]}")
print(f"Second-last element: {numbers[-2]}")

'''
2D indexing

Create:
data = np.array([    [10, 20, 30],    [40, 50, 60],    [70, 80, 90]])

Print:
1. Element 10
2. Element 50
3. Element 90
4. Entire second row
5. Entire third column
'''
arr=np.array([    [10, 20, 30],    [40, 50, 60],    [70, 80, 90]])
print(arr[0,0])
print(arr[1,1])
print(arr[2,2])
print(arr[1])
print(arr[:, 2])

'''
Create this NumPy array:
[    [5, 10, 15],    [20, 25, 30],    [35, 40, 45]]



Write code to print:
1. The first row.
2. The second column.
3. The element 25.
4. The last row.
5. All elements in the first column.
'''
arr=np.array([    [5, 10, 15],    [20, 25, 30],    [35, 40, 45]])
print(arr[0])
print(arr[:,2])
print(arr[1,1])
print(arr[2])
print(arr[:,1])