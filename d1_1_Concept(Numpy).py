'''
Introduction to NumPy
1. What is NumPy?
    NumPy (Numerical Python) is a Python library used for numerical and mathematical operations.

    It helps us work efficiently with:
    - Arrays
    - Mathematical calculations
    - Numerical data
    - Multidimensional data
    - Statistical operations
    NumPy is widely used in Data Science, Machine Learning, and AI.
2. Why do we use NumPy?
    Consider a normal Python list:
    numbers = [10, 20, 30, 40, 50]
    print(numbers)
    We can store multiple values in a list. But NumPy provides specialized arrays that make numerical operations easier and more efficient.
    For example:
    import numpy as np

    numbers = np.array([10, 20, 30, 40, 50])

    print(numbers + 5)
    o/p
    [15 25 35 45 55]
    Notice that NumPy adds 5 to every element automatically.

    With a normal Python list, you would generally need a loop or list comprehension to do this.
3. Install and import NumPy
    If you haven't installed NumPy yet, open your VS Code terminal:
    python -m pip install numpy
    To use NumPy in Python:
    import numpy as np
    Here:
    - import loads the library.
    - numpy is the library name.
    - np is its commonly used alias.
4. Creating NumPy arrays
    The most common way to create a NumPy array is using np.array().

    Example 1: One-dimensional array (1D)
    import numpy as np

    numbers = np.array([10, 20, 30, 40, 50])

    print(numbers)

    o/p
    [10 20 30 40 50]
    A 1D array is similar to a simple list of values.

    Example 2: Two-dimensional array (2D)
    import numpy as np

    numbers = np.array([
        [10, 20, 30],
        [40, 50, 60]
    ])

    print(numbers)
    o/p: 
    [[10 20 30]
    [40 50 60]]
    A 2D array has rows and columns, like a table.
5. Important NumPy array properties
    NumPy provides four important properties.

    Let's use this array:
    import numpy as np

    arr = np.array([
        [10, 20, 30],
        [40, 50, 60]
    ])

    print(arr.ndim)
    print(arr.shape)
    print(arr.size)
    print(arr.dtype)
    Understand each property:
    Property	Meaning	Output
    ndim	Number of dimensions	2
    shape	Number of rows and columns	(2, 3)
    size	Total number of elements	6
    dtype	Data type of elements	int64 or another integer type
    
    Remember these four concepts. They are frequently used in Data Science and Machine Learning.


NumPy indexing and slicing
    Python indexing starts from 0.
Slicing syntax
    numbers[start:stop:step]
    - start – Index from where to start.
    - stop – Index where to stop (stop index is excluded).
    - step – How many positions to move forward each time.

    numbers[::1]  # Every element
    numbers[::2]  # Every second element
    numbers[::3]  # Every third element
    numbers[1::2] # Start at index 1, then every second element
    numbers[::-1] # Reverse the array
'''