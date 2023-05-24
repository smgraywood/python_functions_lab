# 1. Write a function named `sum_to` that accepts a single integer, `n`, and returns the sum of the integers from 1 to `n`.
    
#     For example:
    
#     sum_to(6)  # returns 21
# sum_to(10) # returns 55

def sum_to(n):
  result = 0
  for i in range 1, n+1:
    result += i
  return result

# 2. Write a function named `largest` that takes a list of numbers as an argument and returns the largest number in that list. Do not use built in python functions like max() for this challenge.
    
#     For example:
    
#     ```python
#     largest([1, 2, 3, 4, 0])  # returns 4
#     largest([10, 4, 2, 231, 91, 54])  # returns 231
#     ```

def largest(list):
  if not numbers:
        return None
    largest_num = numbers[0]
    for num in numbers:
        if num > largest_num:
            largest_num = num
    return largest_num
  
# 3. Write a function named `occurrences` that takes two string arguments as input and counts the number of occurrences of the second string inside the first string.
    
#     For example:
    
#     ```python
#     occurrences('fleep floop', 'e')   # returns 2
#     occurrences('fleep floop', 'p')   # returns 2
#     occurrences('fleep floop', 'ee')  # returns 1
#     occurrences('fleep floop', 'fe')  # returns 0
#     ```

def occurrences(string, sub_string):
  count = 0
  sub_len = len(sub_string)
  for i in range(len(string)):
    if string[i:i+sub_len] == sub_string:
      count += 1
  return count
      

# 4. Write a function named `product` that takes an *arbitrary* number of numbers, multiplies them all together, and returns the product. (HINT: Review your notes on `args`).
    
#     For example:
    
#     ```python
#     product(-1, 4) # returns -4
#     product(2, 5, 5) # returns 50
#     product(4, 0.5, 5) # returns 10.0
#     ```
    
def product(*args):
  for arg in args:
      return args[arg] * args[arg + 1]
  
  
