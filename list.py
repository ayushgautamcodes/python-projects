"""
marks = [90, 85, 73, 78, 92]
marks[1] = 88
marks.append(99)
marks.remove(78)
marks.pop(3)
marks.sort()
print(marks)
"""
"""
numbers = [1,2,3,4,5]
for n in numbers:
    print(n)
"""
"""
numbers = [1,2,3,4,5]
def sum_of_numbers(numbers):
    total = 0
    for num in numbers:
        total += num
    return total
print(sum_of_numbers(numbers))
"""
"""
numbers = [1,2,3,4,5]
print(sum(numbers))
"""
num = [1,2,3,4,5]
def largest(num):
   largest = num[0]
   for n in num:
       if n > largest:
          largest = n
   return largest
print(largest(num))