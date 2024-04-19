#5.Write a Python function to calculate the factorial of a number (a non-negative integer). The function 
#accepts the number as an argument.

n = int(input("Enter a number to compute the factorial: "))

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)
print(f"Factorial of = {n} is {factorial(n)}")