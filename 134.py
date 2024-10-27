# Write a program to find max of 3 numbers
num1=int(input("Enter 1 st number : "))
num2=int(input("Enter 2 nd number : "))
num3=int(input("Enter 3 rd number : "))
if num1>num2 and num1>num3:
         print(f"{num1} is greater")
elif num2>num3 and num2>num1:
    print(f"{num2} is greater")
else :
    print(f"{num3} is greater")
