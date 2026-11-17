''' Slicing

Using the  array, 
numbers = np.array([12, 24, 36, 48, 60, 72])
print:
1. First three elements
2. Elements from index 2 to 4
3. Last three elements
4. Every second element

'''
import numpy as np
numbers=np.array([12, 24, 36, 48, 60, 72])
print(f"First three elements: {numbers[0:3]}")
print(f"Elements from index 2 to 4: {numbers[2:5]}")
print(f"Last three elements: {numbers[3:]}")
print(numbers[::2])

