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
    'technology': 'React',
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


"""       **PRACTICE ON DICTIONARIES**
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
result_1 = [key for (key, value) in table.items() if value == V]
print(result_1)
result_2 = [key for key in table.keys() if table[key] == V]
print(result_2)


# Other Ways to Make Dictionaries
D = {'name': 'Bob', 'age': 40}  # Traditional literal expression
D = {}
D['name'] = 'Bob'
D['age'] = 40  # Assign by keys dynamically
dict(name='Bob', age=40)  # dict keyword argument form. use assignments
dict([('name', 'Bob'), ('age', 40)])  # dict key/value tuples form
print(dict([('name', 'Bob'), ('age', 40)]))

# Dictionary comprehensions
"""
     Dictionary comprehensions allow you to create dictionaries in a concise and readable way,
     zip() - combines key list mapping them to values respectively
"""
D = dict(list(zip(['a', 'b', 'c'], [1, 2, 3])))
D1 = dict(zip(['a', 'b', 'c'], [1, 2, 3]))
print(D)
print(D1)
print(zip(['a', 'b', 'c'], [1, 2, 3]))

# Using comprehension to achieve the same result
D = {k: v for (k, v) in zip(['a', 'b', 'c'], [1, 2, 3])}
D1 = {v: v**2 for v in [1, 2, 3, 4, 5, 6, 7, 8, 9]}  # Or
D1 = {v: v**2 for v in range(1, 11)}
print(D1)

D = {c: c * 4 for c in 'SPAM'}  # Loop over any iterable
D1 = {c: c+"!!" for c in ['SPAM', 'EGGS', 'HAM']}
print(D)
print(D1)

# Initializing dictionaries frokey lists
D = dict.fromkeys(['a', 'b', 'c'], "defaultValue")  # Or below
D1 = {key: "defaultValue" for key in ['a', 'b', 'c']}
Dict = dict.fromkeys('spam')  # No default value- default is "None" Or
Dict1 = {key: None for key in 'spam'}
print(Dict1)

# More Dictionary Comprehensions
D = dict(a=1, b=2,  d=4, e=5, f=6, c=3, g=7)
for (k, v) in D.items():
    print(k, v, end="")
print()


for key in D:
    print(key, end=' ')

print()
for key in sorted(D.keys()):
    print(key, D[key], end="")
print()

""" 
    Real-Life Problem
Imagine you are managing a company's employee database, and you need to create a dictionary that maps each employee's name to their respective email addresses. You have two lists, one containing the employee names and the other containing their email addresses. You want to create a dictionary where the names are the keys and the email addresses are the values.

employee_names = ["Alice Johnson", "Bob Smith", "Charlie Davis", "Dana Lee"]
employee_emails = ["alice.johnson@example.com", "bob.smith@example.com", "charlie.davis@example.com", "dana.lee@example.com"]

"""
# Solution
employee_names = ["Alice Johnson", "Bob Smith", "Charlie Davis", "Dana Lee"]
employee_emails = ["alice.johnson@example.com", "bob.smith@example.com",
                   "charlie.davis@example.com", "dana.lee@example.com"]

employee_dict = {
    name: email for (name, email) in zip(
        employee_names, employee_emails)}
print(employee_dict)


employee_ages = [28, 34, 29, 42]
employee_dict_with_contacts = {name: {email, age} for name, email, age in zip(
    employee_names, employee_emails, employee_ages)}
print(employee_dict_with_contacts)

"""
    Dictionary Comprehensions with Conditionals
"""


D = {k: v for (k, v) in zip(['a', 'b', 'c'], [1, 2, 3]) if v > 2}
D1 = {k: v for (k, v) in zip(['a', 'b', 'c'], [1, 2, 3]) if v % 2 == 0}
developers = {'Jane': 'Python', 'Jade': 'JavaScript',
              'John': 'Python', 'Doe': 'JavaScript'}

python_developers = {key: value for (
    key, value) in developers.items() if value == 'Python'}

print(python_developers)
# {'Jane': 'Python', 'John': 'Python'}

""" 
        DICTIONARIES IN SUMMARY
    Operation               Interpretation
    D = {}  -Empty dictionary
    D = {'name': 'Bob', 'age': 40} -Two-item dictionary
    E = {'cto': {'name': 'Bob', 'age': 40}} -Nesting
    D = dict(name='Bob', age=40) -Alternative construction techniques:
    D = dict([('name', 'Bob'), ('age', 40)]) -keywords, key/value pairs, zipped key/value pairs, key lists
    D = dict(zip(keyslist, valueslist))
    D = dict.fromkeys(['name', 'age'])
    D['name'] -Indexing by key
    E['cto']['age']
    'age' in  -     DMembership: key present test
    D.keys() - Methods: all keys,
    D.values() - all values,
    D.items() - all key+value tuples,
    D.copy()copy  (top-level),
    D.clear()clear (remove all items),
    D.update(D2)merge by keys,
    D.get(key, default?) - fetch by key, if absent default (or None),
    D.pop(key, default?) - remove by key, if absent default (or error)
    D.setdefault(key, default?) - fetch by key, if absent set default (or None),
    D.popitem() - remove/return any (key, value) pair; etc.
    len(D) - Length: number of stored entries
    D[key] = 42 - Adding/changing keys
    del D[key]  - Deleting entries by key
    list(D.keys())  - Dictionary views (Python 3.X)
    D1.keys() & D2.keys()
    D.viewkeys(), D.viewvalues()  - Dictionary views (Python 2.7)
    D = {x: x*2 for x in range(10)} - Dictionary comprehensions (Python 3.X, 2.7)
"""
