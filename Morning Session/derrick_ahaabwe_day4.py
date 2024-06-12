# Dictionaries
# Creating and using dictionaries
# Dictionary methods and operations
"""summary
    
    Dictionaries in python are collections of keys and values pairs
    -Unordered
    -mutable and
    -indexed by keys
    
    """

# Example 1: Create a dictionary
# Create a dictionary for a student pursuing software engineering
# the key must be your name, age, technology interest and year of study. put
# your own details


student_dict = {
    'name': 'Derrick',
    'age': '15',
    'technolo': 'React',
    'coures': 'BSSE',
    'year': '2015',
}

print(student_dict['age'])
# Access Values
print(student_dict['age'])
print(student_dict['technology'])

# Modify values
# Exercise 1: Modify your age
student_dict['age'] = '16'

# # Example2: adding keys and values
student_dict['email'] = 'ahaabwe@gmail.com'
student_dict['hobbies'] = ['grill', 'bake', 'fry']
student_dict['technology'] = 'C#'

print(student_dict)

# Exercise 2: Remove a key and value from student dictionary
del student_dict['age']
print(student_dict)

# Common Dictionary methods
"""summary
    1. get() - returns the value for the specified key if the key is in the dictionary
        if not it returns the default value
    2. update() - Updates the dictionary with the elements from another dictionary
    3. pop() - Removes the specified key and return the corresponding value
"""
# Example 3: Use the get method to get the value

print(student_dict.get('technology'))
print(student_dict.get('town'))  # returns None for non-existant key

# Exercise 3: Use the update method to change value in age
student_dict.update({'age': '80'})
print(student_dict)

# Exercise 4: Use the if to check if the key 'age' is present in the dictionary
if 'age' in student_dict:
    print(" Age is present as : ", student_dict['age'])

else:
    print(" Age missing from dictionary.")

print()

# keys(), values() and the items() methods
print(student_dict.keys())
print(student_dict.values())
print(student_dict.items())

"""summary

keys() returns a view of objects that displays a list of all keys
values() returns a view of objects that displays a list of all values
items() returns a view of objects that displays a list of dictionary keys and
values tuple pairs

 """

# Exercise : Use the update method to change the course and add a new
# key "WhatsApp_Number" to the dictionary

student_dict.update({
    'course': 'BSC',
    'WhatsApp_Number': '0756998763'
})
print(student_dict)


""" 
        MORE DICT METHODS
    1.dir() - return methods available for dictionary
    2. key() - returns dict keys
    3. values() - returns dict values    
    4. item() - returns dict key value pair turples
    5. get() - help to solve error that would be as a result of non-existant keys by returning none if no existence
    6. update() - similar to concatenation. merges the keys and values of one dictionary into another
    7. pop() - deletes a key from a dictionary and returns the value it had
"""
print(dir(student_dict))
print(student_dict.values())
print(student_dict.keys())
list_of_student_dict_items = list(student_dict.items())
print(list_of_student_dict_items)

D = {'spam': 2, 'ham': 1, 'eggs': 3}
print(D.get('spam'))
print(D.get('toast'))
print(D.get('toast', 88))

D2 = {'toast': 10, 'muffin': 5}
D.update(D2)
print(D)

popped_value = D.pop('muffin')
print(D, popped_value)


table = {
    'Holy Grail': '1975',
    'Life of Brian': '1979',
    'The Meaning of Life': '1983'
}

table_turple = table.items()
V = '1975'
result = [key for (key, value) in table.items() if value == V]
print(result)
