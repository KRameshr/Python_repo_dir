
def factor(n):
    if n < 0:
        return "Negative numbers are not allowed."
    result = 1 
    for i in range(1, n + 1):
        result = result * i
    return result        
print(factor(5))    


def checkString(s):
    if s == s[::-1]:
        return "The string is a palindrome."
    else:
        return "The string is not a palindrome."
print(checkString("Ramesh"))

def check_string():
    user_input  = input("Enter a string: ")
    if 'srs' in user_input.lower():
        print("The string is containing the letter 's'")
    else:
        print("The string doesn't contain the letter 's'")
check_string()


class student:
    def __init__(self):
        self.user_input = None
    def fun1 (self):
        value = input("Enter a string: ")
        self.user_input = value    
        return value
    def message(self):
        if self.user_input is not None:
            print(f"The string is: {self.user_input}")   
        else:     
            print("No string was entered.")

sa = student()
sa.fun1()
sa.message()


double_num =  lambda x , y : x*y
print(double_num(5, 3))


class Super:
    def fun1(self):
        print("This is function 1 in the Super class")

class Modified_Super(Super):
    def fun1(self):
        print("This  is function 1 in the Modified Super class")
    def fun2(self):    
        print("This is the 2 nd function from the Modified Super class")

f1 = Modified_Super()
f1.fun1()

class TestOverloading:
    def Hello(self, arg1):
        print("This function is only having 1 argument")

    def Hello(self, arg1, arg2):
        print("This function is having 2 arguments")

t = TestOverloading()    
t.Hello(1, 2)

try:
    t.Hello(1)
except TypeError as e:
    print(f"Error: {e}")

def addition(*args):
    result = 0
    for num in args:
        result =result + num
    return result

print(addition(1, 2, 3, 4, 5))


class Encapsulation:
    def __init__(self):
        self.originalValue = 10

    def Value(self):
        return self.originalValue

    def setValue(self, newValue):
        self.originalValue = newValue    
obj = Encapsulation()
print(f"Current Value: {obj.Value()}")
obj.setValue(20)
print(f"Updated Value: {obj.Value()}")



import Module

print(Module.addition(5, 3))
print(Module.subtraction(5, 3))
print(Module.multiplication(5, 3))
print(Module.division(5, 3))


from Module import addition
print(addition(10, 5)) 

from Module import subtraction
print(subtraction(10, 5)) 


from Module import multiplication, division
print(multiplication(10, 5)) 
print(division(10, 5)) 
