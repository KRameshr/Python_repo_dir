# 1. Create a function that takes dimensions as tuples e.g. (3, 3) and a numeric
# value and returns a NumPy array of the given dimension filled with the
# given value e.g.: solve((3, 3), 5) will return
# [
# [5, 5, 5],
# [5, 5, 5],
# [5, 5, 5]
# ]


import numpy as np

def solve(dimension, value):
    return np.full(dimension, value)

result = solve((3,3),5)
print("Output Array:")
print(result)


print(f"\nType: {type(result)}")

# ------------------------------------
def sum_arrays(*arrays):
    return np.sum(arrays, axis=0)

arr1 = np.array([[2,3],[4,5]])
arr2 = np.array([[6,7],[8,9]])
arr3 = np.array([[6,7],[8,9]])
result = sum_arrays(arr1, arr2,arr3)
print("result :\n", result)
# -----------------------------------
def top_left_sub_matrix(matrix, n, m):
    arr = np.array(matrix)
    return arr[0:n, 0:m] 
  

data = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

result = top_left_sub_matrix(data, 2, 2)
print("Original Matrix:\n", np.array(data))
print("\nTop-Left 2x2 Sub-Matrix:\n", result)


def top_left_sub_matrix(matrix, n, m):
    arr = np.array(matrix)
    return arr[-n:, -m:] 
  

data = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

result = top_left_sub_matrix(data, 2, 2)
print("Original Matrix:\n", np.array(data))
print("\nTop-Left 2x2 Sub-Matrix:\n", result)



def stan_mean_solution(arr):

    data = np.array(arr)
    mean_val = np.mean(data)
    std_val = np.std(data)
    
    # Return as a dictionary
    return {
        'mean': mean_val,
        'std_dev': std_val
    }


data = [1,1,1]

print(stan_mean_solution(data))




# 3x3

matrix = np.arange(1, 10).reshape(3, 3)
print(matrix)

user_input = input("Enter numbers separated by space: ").split()
arrary_int = np.array(user_input, dtype=int)
print(arrary_int)
arrary_folat = arrary_int.astype(float)
print(arrary_folat)

inital = np.array([10, 20, 30])
appenedarray = np.append(inital,[40, 50, 60, 70, 80, 90])
print(appenedarray)

a = np.array([1, 2, 3])
b = np.array([10, 20, 30])

sumArray = a + b
print("sumArray:", sumArray)

array1= np.arange(10,100,10).reshape(3,3)
print(array1)

first_row = array1[0]
last_row = array1[-1,-1]
print(first_row)
print(last_row)