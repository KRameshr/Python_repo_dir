#  hello world well to lear python :)

print("Let's Deal with Lists")
nums = [1,2,3,4,5,6]
print(nums)

nums.append(88)
print(nums)

x= nums.pop()
print(x)

for x in nums :
    print(x)
print(" Done ")
print(type(nums))

#  -----------------------------------------------------
print("Let's Deal with topules")
nums = (1,2,3,4,5,6)
print(nums)


for x in nums :
    print(x)
print(" Done ")
print(type(nums))

# nums.append(88)
# print(nums)

# x= nums.pop()
# print(x)
print("tuple is not add or remove")


#  -----------------------------------------------------
print("Let's Deal with Dictionary")
mydict = {
    "employeeName":"K Ramesh",
    "employeeSalary":5000,
    "employeePhonenumber":"8947556985"
 }

# add the details in Dictionary 

mydict["employeeID"] = "EMP101"
mydict["employeeDept"] = "Sales"
mydict["employeeEmail"] = "ramesh.k@company.com"

print("--- Employee Record ---")
for key, value in mydict.items():
    print(f"{key}: {value}")
print("--- Employee Record ---")

print("employeeID" in mydict)
print(type( mydict))
print(mydict["employeeID"])



#  -----------------------------------------------------
print("Let's Deal with Comprehensive")

l = []
for x in range(1,100) :
  l.append(x)
print(l)  
print("<---------------------------------------------------------------------->")
ll = [x for x in range(1,100)]
print(f"values:  {ll}")

t = [x for x in range(1,100)]
s = {x for x in range(1,100)}
d = {x :x*x for x in range(1,100)}
print(f"values:  {t}")

print("<---------------------------------------------------------------------->")

print(f"values:  {s}")
print("<---------------------------------------------------------------------->")

print(f"values:  {d}")

