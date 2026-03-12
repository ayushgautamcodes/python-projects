"""
celsius = int(input("Enter the temprature in CELCIUS = "))
fahrenheit = (celsius*9/5)+32
print(celsius,"degree celsius is equals to",fahrenheit,"degree fahrenheit")
"""
"""
n = int(input("Enter any number = "))
if n%2==0:
    print("even")
else:
    print("odd")
"""
"""
for i in range(1, 10, 2):
    print(i)
"""
"""
i=5
while i>=1:
    print(i)
    i-=1
"""
"""
def say_hello():
    print("hello world")

say_hello()
"""
"""
def add(a,b):
    return a+b
a = int(input(" enter the first no.: "))
b = int(input(" enter the second no.: "))
print(add(a,b))
"""
"""
def square(a):
    return a*a
a = int(input(" enter the no.: "))
print(square(a))
"""
"""
def is_positive(a): 
    return a % 2 == 0
a = int(input("Enter the no.: "))
if is_positive(a):
    print("True")
else:
    print("False")
"""
"""
def max_of_two(a,b):
    return a > b
a = int(input("Enter no. a : "))
b = int(input("Enter no. b : "))
if max_of_two(a,b):
    print("a")
else:
    print("b")
"""

def sum_upto_n(n):
    return n*(n+1)/2
n = int(input("enter the no.: "))
print(sum_upto_n(n))

