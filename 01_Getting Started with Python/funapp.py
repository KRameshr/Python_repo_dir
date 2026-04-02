def downlodeFile(data):
    print("Downloading file...")
    print("File downloaded successfully "+ data)
    print("Log to DB "+ data)
    print("Close connection "+ data + "\n\n")



downlodeFile("Python for Beginners")  
downlodeFile("ftp://example.com/file.txt")  
downlodeFile("www.example.com/file.txt")    



def crateMultiple(x):
    return lambda y : x * y

multiply = crateMultiple(5)    
        # pass y
def execute(func , value):
    return func(value)        
print(multiply(9))
print(execute(multiply, 9))