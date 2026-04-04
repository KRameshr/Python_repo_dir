#  single inharitance

class Shape:
    def __init__(self):
        print("This is a shape classs")

class Circle(Shape):   
    def __init__(self):
        super().__init__()
        print("This is a circle class")

# c1 = Circle()

class  vehicle:
    def start(self):
        print("This is a vehicle start")
    def stop(self):
        print("This is a vehicle stop")

class Car(vehicle):
    def say(self):
        super().start()
        print("This is a car class")
        super().stop()
c1 = Car()  
c1.say()  





# Multiple Inheritance: Circle inherits from BOTH Shape and Color

class Shape:
    def __init__(self):
        self.type = "Circle"
        print("This is a Shape class")

class Color:
    def __init__(self):
        self.hue = "Red"
        print("This is a Color class")

class Circle(Shape, Color):
    def __init__(self):
        #  call the parent constructors to initialize the attributes
        Shape.__init__(self)  
        Color.__init__(self)
        print(f"This is a {self.hue} {self.type}")
c1 = Circle()

#  multilevel inharitance : 

class Shape:
    def __init__(self):
        self.type = "Circle"
        print(f"1. This is a {self.type} class")


class Color(Shape):
    def __init__(self):
        super().__init__()
        self.type = "Red"
        print(f"2. This is a {self.type} class")

class Circle(Color):
    def __init__(self):
        super().__init__()
        self.hue = "Red"
        print(f"3. This is a {self.hue} {self.type}")

c1 = Circle()       

#  hierarchical inharitance 
print(f" hierarchical inharitance")
class Shape:
    def __init__(self):
        self.type = "Circle"
        print(f"1. This is a {self.type} class")
    def info(self): 
        print(f"2. This is a {self.type} class")

# child 1
class clour(Shape):
    def __init__(self):
        super().__init__()
        self.heue = "Red"
        print(f"1. This is a {self.heue} {self.type} class")

c1 = clour()
c1.info()


# child 2
class Square(Shape):
    def __init__(self):
        super().__init__()
        self.heue = "Red"
        print("Child 2: This is a Square")

c2 = Square()
c1.info()


#  hybrid inharitance :  
print("hybrid inharitance :")
class Shape:
    def __init__(self):
        print("1. Base Shape Class (Grandparent)")

class Circle(Shape):
    def __init__(self):
        super().__init__()
        print("2. Circle Class (Parent A)")    


class Color:
    def __init__(self):
        print("2. Color Class (Parent B)")      

class RedCircle(Circle, Color):
    def __init__(self):
        Circle.__init__(self)
        Color.__init__(self)
        print("3. RedCircle Class (The Hybrid Child)")
obj = RedCircle()        


# Overriding (Method Overriding)
# Overriding happens in Inheritance. It is when a Child class provides a specific implementation for a method that is already defined in its Parent class.


class Parent:
    def greet(self):
        print("Hello from Parent")

class Child(Parent):
    def greet(self): # This OVERRIDES the Parent method
        print("Hello from Child")

c = Child()
c.greet() # Output: Hello from Child



# overloading (Operator Overloading)
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # Overloading the '+' operator
    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

p1 = Point(1, 2)
p2 = Point(3, 4)
p3 = p1 + p2  # This uses the __add__ method!
print(f"New Point: {p3.x}, {p3.y}") # Output: 4, 6 



# polymorphism : Polymorphism allows us to use a single interface to represent different underlying data types. In Python, this is often achieved through method overriding in inheritance.
class Animal:
    # We add 'self' so this can be called by an object
    def speak(self):
        print("I am an Animal")

    def walk(self):
        print("I am walking")

class Dog(Animal):
    # This overrides the parent's speak method
    def speak(self):
        print("I am a Dog")

# 1. Create instances (objects) using parentheses ()
animal_obj = Animal()
dog_obj = Dog()

# 2. Call the methods
animal_obj.speak()  # Calls the Parent version
dog_obj.speak()     # Calls the Overridden Child version
dog_obj.walk()      # Calls the Inherited Parent version