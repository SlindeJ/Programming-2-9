num1 = int(input("Please input a positive number: "))
num2 = int(input("Please input another positive number: "))

while (num2 > 0):
  temp = num1 % num2
  num1 = num2
  num2 = temp
  
print("The GCD is ", str(num1))    #??? I have no idea why this works