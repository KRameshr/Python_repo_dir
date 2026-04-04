

# public
# protected _ single underscore
# private __ double underscore

class MyClass:
    def __init__(self):
        self.public_var = "I am public"
        self._protected_var = "I am protected"
        self.__UpdateSoftware()
    def drive(self):
        print("Driving the car")

    def __UpdateSoftware(self):      
        print("Updating software...")

    def MaxUpdateSoftware(self,speed):
        self.__speed = speed
        print(f"Max speed is {self.__speed}")


my_car = MyClass()
print(my_car.public_var)
print(my_car._protected_var)
my_car.drive()
my_car.MaxUpdateSoftware(100)
my_car._MyClass__UpdateSoftware()

