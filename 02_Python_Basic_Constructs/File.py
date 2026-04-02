f = open("sample.txt","x")
f.write("This is a sample file created using Python.\n")
f.close()

with open("sample.txt","r") as f:
    content = f.read()
    print(content)