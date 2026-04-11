def greet(name):
    return "Hello , {0}".format(name)

 
def say_goodbye():
    print("Good bye")


def main():
    print("module being executed - START")  
    print("module being executed - END") 

# print(__name__) #main
if __name__ == "__main__": main()
     