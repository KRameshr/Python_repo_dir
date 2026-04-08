

class SomeClass:
    def __init__(self):
        self.setBalance(10) 

    def setBalance(self, balance):
        self.__balance = balance

    def getBalance(self):
        print(self.__balance )
        

    def public(slef):
        print("Public Function")

    def __private(self):
        print("Private Function")

obj = SomeClass()
obj.setBalance(20)
obj.getBalance()
obj.public() 
obj._SomeClass__private() 



