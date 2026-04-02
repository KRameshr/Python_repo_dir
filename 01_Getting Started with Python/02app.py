x=20

if x<20:
  print('x is < 20')
elif x == 20 :
   print('x is equal to 20')   
else:
   print('x is > to 20')   

if x < 25:
  print('x is < 20')
  if x < 15:
    print('x is < 15')  
  else:
    print('x is > 15')   
else:
   print('x is > to 20')



# inputone = float(input("Enter first number : "))
# inputtwo = float(input("Enter second number : "))
# inputthree = float(input("Enter third number : "))

# if(inputone >= inputtwo) and (inputone >= inputthree):
#   gretest = inputone
# elif(inputtwo >= inputone) and (inputtwo >= inputthree ) :
#   gretest = inputtwo
# else:
#   gretest = inputthree

# print(f"gretest number is {gretest} from {inputone} , {inputtwo} , {inputthree}")


cout = 0
while cout <= 10:
  print(cout, end = ",")
  cout += 1


nums = [ 10, 23, 4, 26, 4, 75, 24, 54 ]  
i = 0
while i < len(nums):
    if nums[i] % 2 == 0:
        print(nums[i])
    i += 1


# 1. Create an empty array (list)
user_list = []

# 2. Get user defined inputs
n = int(input("How many numbers do you want to enter? "))

for i in range(n):
    val = int(input(f"Enter number {i+1}: "))
    user_list.append(val)

print(f"\nAnalyzing your list: {user_list}")
print("Prime numbers found:")

# 3. Fetch prime numbers using a for loop
for num in user_list:
    if num > 1:  # Prime numbers must be greater than 1
        is_prime = True
        
        # Check for divisors from 2 up to the square root of num (or num-1)
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                is_prime = False
                break
        
        if is_prime:
            print(num)