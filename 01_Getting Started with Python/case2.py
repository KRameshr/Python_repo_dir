# 1. Create 1st tuple with values -> (10, 20, 30), 2nd tuple with values -> (40, 50, 60):
t1 = (10, 20, 30)
t2 = (40, 60, 50)
# a. Concatenate the two tuples and store it in “t_combine”
t_combine = t1 + t2
print(f"a. Combined Tuple: {sorted(t_combine)}")
# b. Repeat the elements of “t_combine” 3 times
t_combine  = t_combine * 3
print(f"b. Repeated Combined Tuple: {t_combine}")
# c. Access the 3rd element from “t_combine”
print(f"c. 3rd element of Combined Tuple: {t_combine[2]}")
# d. Access the first three elements from “t_combine”
print(f"d. First three elements of Combined Tuple: {t_combine[:3]}")
# e. Access the last three elements from “t_combine”
print(f"e. Last three elements of Combined Tuple: {t_combine[-3:]}")




# 2. Create a list ‘my_list’ with these elements:
# a. First element is a tuple with values 1, 2, 3
# b. Second element is a tuple with values “a”, “b”, “c”
# c. Third element is a tuple with values True, False
# 3. Append a new tuple – (1, ‘a’, True) to ‘my_list’:
# a. Append a new list – *“sparta”, 123+ to my_list

my_list = [(1, 2, 3), ("a", "b", "c"), (True, False)]
my_list.append((1, "a", True))
my_list.append(["sparta", 123])
print(f"Updated List: {my_list}")


# Create a dictionary ‘fruit’ where:
# a. The first key is ‘Fruit’ and the values are (“Apple”, “Banana”, “Mango”,
# “Guava”)
# b. The second key is ‘Cost’ and the values are (85, 54, 120, 70)
# c. Extract all the keys from ‘fruit’
# d. Extract all the values from ‘fruit’

fruit = {
    "Fruit": ("Apple", "Banana", "Mango", "Guava"),
    "Cost": (85, 54, 120, 70)
}

for key in fruit.keys():
    print(f"Key: {key}")
for value in fruit.values():
    print(f"Value: {value}")

# 5. Create a set named ‘my_set’ with values (1, 1, “a”, “a”, True, True) and print the result. 
my_set = {1, 1, "a", "a", True, True}
print(f"Set: {my_set}")