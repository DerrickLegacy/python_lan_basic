
# Python Practices
"""
-Follow PEP 8
1. Indentations
2. Maximum Lines
3. Blank Space
4. Use meaningful name
"""
# OPERATORS
"""
Name of Operator    Symbol
Addition            x+y
Subtraction         x-y
Multiplication      x*y
Division            x/y
Modulus             x%y
Exponentiation      x**y
Floor Division      x//y

# Comparison Operators
Name of Operator    Symbol
Equal               x==y
Not Equal           x!=y
Greater than        x>y
Less than           x<y
Greater than or equal to x>=y
Less than or equal to x<=y


# Logical Operators
Name of Operator    Symbol
and                 and 
or                  or  
not equal           not 

#Membership Operator
Name of Operator    Symbol
in                  x in y
not in              x not in y

#Bitwise Operator
Name of Operator    Symbol
AND                 &
OR                  |
XOR                 ^
NOT                 ~

# Python Cases
1. snake_case
2. camelCase
3. PascalCase
4. UPPERCASE
5. kebab-case

"""
# Compressions (list, dictionaries comprehension)
"""
Comprehension provides a concise way to create lists and dictionaries
list - [...]
dictionary - {...}
"""
# Example 1: Basic List Comprehension
# List of Squares in the range of 10
list_of_squares = [x**2 for x in range(10)]
print(list_of_squares)

# Exercise 1: Create a list of even square in the range of 20
list_of_even_squares = [x**2 for x in range(20) if x % 2 == 0]
print(list_of_even_squares)

# Dictionary Compression
# create a list of cars and count the length of characters
favourite_cars = {"BWM", "Jeep"}
car_length = {car: len(car) for car in favourite_cars}
print(car_length)

# Exercise 2: Create a list of tuples where each turple contains a number and its cube for numbers between 1 and 10 using dictionary comprehension

list_of_turples = [{(x, x**3)} for x in range(11)]
print(list_of_turples)

list_of_turples2 = {x: x**3 for x in range(1, 11)}
for key in list_of_turples2:
    print(key, '=>', list_of_turples2[key])
