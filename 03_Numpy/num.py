import numpy as np
# numpVarible = np.array([1,2,3,4,5])
# # print(numpVarible)

# numpVarible2 = np.array([[1,2,3],[4,5,6],[7,8,9]])
# #  print(numpVarible2)



# print(np.zeros((3,4)))
# print(np.arange(0,10,2))
# print(np.arange(10,20,2))

# print(np.linspace(5,10,10))
# print(np.linspace(0,10,6))

# print(np.full((4,5),7))
# print(np.random.random((2,3)))

# #  checking size of array
# a = np.array([[1,2,3],[4,5,6],[7,8,9]])
# print(a.size)
# print(a.shape)
# #  checking re size of array

# b = np.array([[1,2,3],[4,5,6],[7,8,9]]) 
# print(f"Original Shape: {b.shape}") # (3, 2)
# b = np.resize(b, (8, 2))

# print(b)

# a = np.arange(24)
# print(a)
# a = a.reshape(4,6)
# print(a)
# print(a.ndim)
# print(a.size)
# print(a.dtype)

# b = np.arange(24, dtype=float)
# print(b.dtype)

# mathtematical operations

a,b = 10,20

print(np.sum([a,b]))
print(np.sum([[2,3],[4,5]]))
print(np.sum([[2,3],[4,5]], axis=0))
print(np.sum([[2,3],[4,5]], axis=1))

print(np.subtract(20,3))
print(np.multiply(20,3))
print(np.divide(20,3))


a = np.array([[1,3,4,5],[2,4,5,6]])
b = np.array([[1,2,3,4],[5,6,7,8]])

print(np.multiply(a,b))
print(np.exp(a))
print(np.exp(b))
print(np.sqrt(a))
print(np.sqrt(b))
print(np.sin(a))
print(np.sin(b))


# element wise operations comparision
a =  [1,2,3,4]
b =  [5,6,7,8]
c = [1,2,3,4]

print(np.equal(a,b))
print(np.equal(a,c))

#  array wise comparision
print(np.array_equal(a,c))
print(np.array_equal(a,b))


# aggregate functions

print("Sum: "+str(np.sum(a)))
print("Min: "+str(np.min(a)))
print("Max: "+str(np.max(a)))
print("Mean: "+str(np.mean(a)))
print("Median: "+str(np.median(a)))
print("Correlation: "+str(np.corrcoef(a)))
print("Std: "+str(np.std(a)))
print("Var", np.var(a))
print("Var", str(np.var(a)))

# broadcasting

a = np.array([[1,2,3],[4,5,6],[7,8,9]])
b = np.array([1,2,3])

print("First Array:\n",a)
print("Second Array:\n",b)
print("Broadcasted Sum:\n",a+b)

# array manipulation


a  = np.array([1,2,3])
b  = np.array([4,5,6])


concatenated = np.concatenate((a,b))
print("Concatenated Array:\n", concatenated)
print(np.hstack((a,b)))
# vertical stack
print(np.vstack((a,b)))
print(np.column_stack((a,b))) 

x = np.arange(16).reshape(4,4)
print(x)
print(np.hsplit(x,2))
print("\n\n",np.hsplit(x,np.array([3,6])))
print("\n\n",np.hsplit(x,np.array([3])))
print("\n\n",np.hsplit(x,np.array([2,3])))

# slicing and indexing
a = ["a","b","c","d","e","f"]
print(a[0:])
print(a[0:3])

# 3D array slicing

a = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(a[0])
print(a[:1])
print(a)

print(a[:1,1:])
print(a[:1,2:])

print(a[:2,1:])
print("--------")
print(a[1:,1:])

# advanced of numpy over list


# define a list
import sys 
my_list = list(range(1000))
print("Size of list: ", sys.getsizeof(my_list)* len(my_list))

# define a numpy array
a = np.arange(1000)
print("Size of numpy array: ", a.size * a.itemsize)

# speed comparison
import time

def use_list():
    initial = time.time()
    # Using 1 million elements to see a real difference
    my_list1 = list(range(1000000))
    my_list2 = list(range(1000000))        
    result = [my_list1[i] + my_list2[i] for i in range(len(my_list1))]
    return time.time() - initial
    
def use_Numpy():
    initial = time.time()
    a = np.arange(1000000)
    b = np.arange(1000000)
    result = a + b  # Vectorized operation
    return time.time() - initial # Added the return here!

list_time = use_list()    
numpy_time = use_Numpy()

print(f"Python List Time: {list_time:.5f} seconds")
print(f"NumPy Array Time: {numpy_time:.5f} seconds")
print(f"NumPy is {list_time / numpy_time:.1f}x faster!")

