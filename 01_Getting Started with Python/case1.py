
sqaure = [x**2 for x in range(1,11)]
print(f"Square: {sqaure}")


  
  #

def is_leap_year(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    return False

test_year = 2026
print(f"the year {test_year} is leaf_year or not ? {is_leap_year(test_year)}")  

def filter_even(numbers):
    return[num for num in numbers if num % 2 == 0]
my_nums = [2,6,7,9]
print(f"Even numbers: {filter_even(my_nums)}")



def common_arrays(arr1, arr2):
    # common = [x for x in arr1 if x in arr2]
    common = list(set(arr1) & set(arr2))
    common.sort()
    if common:
        print(f"Members of the first array present in the second: {common}")
    else:
        print(f"No common members found.")   

list_a = [1, 2, 3, 4, 5]
list_b = [3, 4, 5, 6, 7]
common_arrays(list_a,list_b)