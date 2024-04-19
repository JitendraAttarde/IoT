# Write a Python function to find the maximum of three numbers.

num1=int(input("Enter number 1 :"))
num2=int(input("Enter number 2:"))
num3=int(input("Enter number 3 :"))

print(f"num1 = {num1},num2 = {num2},num3 = {num3}")

def function1():
    if((num1>=num2) and (num1>=num3)):
        print("number 1 is greater")
    elif((num2>=num1) and (num2>=num3)):
        print("number 2 is greater")
    else :
        print("number 3 is greater")

function1()