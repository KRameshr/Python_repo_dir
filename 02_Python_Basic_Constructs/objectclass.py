# 1. What is an "Instance"?
# An instance is a specific object created from a blueprint (the Class).

# Class: The blueprint for a Car.

# Instance: The specific red Tesla in your driveway with license plate "XYZ-123".

# If you create three different cars in your code, you have three instances of the Car class.

# 2. What is "self"?
# self is the internal name the instance uses to refer to itself.

# When you are inside the class code, you don't know if the user will name their variable my_car, tesla, or old_truck. So, you use self as a placeholder to say: "Whichever instance is currently running this code, use its data."

# 3. The "Name Tag" Analogy
# Imagine a room full of 100 employees from XYZ Corporation.

# Each employee is an Instance.

# Each employee has a name tag that says "Self".

# When you tell the crowd, "Look at your name tag," every person looks at their own specific tag. They don't look at the person next to them.


# In Python, __init__ is short for "initialize." It is a special method (known as a constructor) that Python automatically calls the exact moment you create a new "object" from a class.

# As a Data Analyst, you can think of it as the "Setup Phase" for your data structures.

# 1. What does it actually do?
# The purpose of __init__ is to assign values to the object's properties when it is first born. It ensures that every object starts with the data it needs to function


class className:
    # The __init__ method sets up the initial state
    def __init__(self, name, age):
        # 'self' ensures the name is pinned to the RIGHT instance
        self.name = name
        self.age = age

    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)
person1 = className("Alice", 30)
person2 = className("Bob", 25)
person1.display()
person2.display()

# 1. Define the Vehicle class (from your screenshot)
class Vehicle:
    name = ""
    kind = "car"
    color = ""
    value = 100.00
    
    def description(self):
        # Uses old-style string formatting to build the description
        desc_str = "%s is a %s %s worth $%.2f." % (self.name, self.color, self.kind, self.value)
        return desc_str

# 2. Your code goes here (The solution)

# Create car1 and set its attributes
car1 = Vehicle()
car1.name = "Fer"
car1.color = "red"
car1.kind = "convertible"
car1.value = 60000.00

# Create car2 and set its attributes
car2 = Vehicle()
car2.name = "Jump"
car2.color = "blue"
car2.kind = "van"
car2.value = 10000.00

# 3. Test the output (as shown in your screenshot)
print(car1.description())
print(car2.description())


class Fruite:
    def __init__(self):
        print("This is a Fruite class")

f1 = Fruite()        

class Circite(Fruite):
    def __init__(self):
        super().__init__()
        print("This is a Circite class")
c1 = Circite()        


class a:
    def __len__(self):
        return  10
    def __str__(self):
        return "This is a class a"  

print(len(a()))
print(str(a()))
