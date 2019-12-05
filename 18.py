#Create a function that takes an integer and returns the factorial of that integer. That is,
#the integer multiplied by all positive lower integers.

def factorial(num):
    x= 1
    for i in range(1,num+1):
        x*=i
    return x

print(factorial(5))