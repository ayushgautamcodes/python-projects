#while loop
"""
i = 1
while i<=10:
    print(i)
    i+=2
"""
#for loop
"""
for i in range(1,11):
    print(i)
"""
#table using for loop
"""
n = int(input("Enter the no. you want to print table of = "))
for i in range(1,11):
    print(n,"*",i,"=",i*n)
"""
#table using while loop
"""
n = int(input("Enter the no. you want to print table of = "))
i = 1
while i <=20:
    if i == 11:
        break
    print(n,"*",i,"=",i*n)
    i+=1
"""
numbers = [1,2,3,4,5]
def sum_of_numbers(numbers):
    total = 0
    for num in numbers:
        total += num
    return total
print(sum_of_numbers(numbers))