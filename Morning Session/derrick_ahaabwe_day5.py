# Friday June-15-2024
# Defining Functions
""" 
        Function syntax and parameters
        Return values
        Lambda functions
        Functions in python defined using the 'def' keyword, followed by function name
        parenthesis (), inside the parenthesis you put a parameter name, and the colon.
 """


# Example 1
def multiply(a, b):
    return a * b

result = multiply(5, 10)
print(result)

# Example 2: Multiple return values
def get_coordinates():
    return 10, 20

x, y = get_coordinates()
print(x, y)

# Exercise 1: Define a function greet with a parameter name, set to 'Guest', and print a message
# I am a software programmer
def greet(name="Guest"):
    print(f"I am {name}, a satisfied software programmer")


greet()
def greet(name="Derrick"):
    print(f"I am {name}, a  software programmer")

# Example 3: Return multiple return values
def get_name_and_position():
    name = "Derrick Ahaabwe"
    position = "I am a satisfied software programmer"
    return name, position

name, position = get_name_and_position()
print(name, position)
print()

# Exercise 2: Return multiple return values of your name and age
def get_name_and_age():
    name = "Derrick"
    age = "16"
    return name, age


name, age = get_name_and_age()
print(name, age)

# Notes
"""summary
    def - keyword to define a function
    function_name  - Name of the function
    parameters - Optional, arguments passed to the function
    Docstrings - Optional, describes the function purpose
    return - Optional, returns a value from the function
     
    """

# Syntax for defining a function

# def function_name(parameters):
#     """Docstring Optional"""
#     # Function body
#     # return value

""" 
        LAMBDA FUNCTION
    Lambda function are small anonymous functions defined using the laambda keyword.\
    They are restricted to a single expression

    Syntax for lambda function
    lambda parameter: expression

 """

# Example 4: Create a lambda function to add two numbers
add = lambda a, b: a + b
print(add(45, 70))

# def add (a, b): return a + b
# print(add(45, 70))

# Example 5: Use cases of lambda function for sorting
coordinates = [(1, 2), (2, 3), (3, 1), (5, 0)]
coordinates.sort(key=lambda coordinate: coordinate[1])
print(coordinates)

#  Map, Filter and Reduce
# Example 6: Get the squares of 1 to 5 using map, filter and reduce
number_squares = [1, 2, 3, 4, 5]
squares = list(map(lambda x: x**2, number_squares))
print(squares)


# Exercise 3: Define a function to get user info that accepts arbitrary keyword arguments and prints
# each key value pair
def get_user_info(**kwargs):

    # **kwargs allows passing an arbitray number of keywords to an argument or to a function
    for key, value in kwargs.items():
        print(" details:", f"{key} is {value}")

user_info = get_user_info(name="John", age=25, course="BSSE")

# Example 7: how to handle a **kwargs in Functions
def ahaabwe_function(a, b, **kwargs):
    print(f"a: {a}, b: {b}")

    for key, value in kwargs.items():
        print(f"{key}:{value}")

ahaabwe_function(1, 2, x=100, y=200, z=300)