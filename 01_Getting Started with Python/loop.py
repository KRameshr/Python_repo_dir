for x in range(0,11):
    print(x, end = " ,")

print("\n")
nums = [x for x in range(0,11)]
for x in nums:
    # print(x, end = ",") 
    if(x == 4):
        break
    print(x)   
    if(x == 4):
        continue
print(x)    


a = 10
while a != 0 :

    print(a)
    a -= 1

while a < len(nums):
    print(nums[a]) 
    a +=1