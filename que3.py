#Write a program to accept three integer numbers and find its average.

num1=int(input("Enter number 1 :"))
num2=int(input("Enter number 2:"))
num3=int(input("Enter number 3 :"))

print(f"num1 = {num1},num2 = {num2},num3 = {num3}")

add=num1+num2+num3
print(f"Addition is = {add}")

avg=add/3
print(f"Average = {avg}")