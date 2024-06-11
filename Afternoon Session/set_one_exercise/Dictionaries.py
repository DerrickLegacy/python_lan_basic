# Exercise5
"""
-Dictionaries: Just a mapping for key value pairs(or other objects)
-Better suited when a collection's items are named or labeled—fields  record
"""
# Creating a dictionary
dictionary_name = dict()
print(dictionary_name)

# Or
Shoes = {
    "brand": "Nick",
    "color": "black",
    "size": 40
}

# Accessing values using keys- e.g returns the size of the shoes
print(Shoes["size"])

# changes the value of the brand from Nick to Adidas
Shoes.update({"brand": "Adidas"})
print(Shoes)

# Adds the type to the Shoes dictionary
Shoes["type"] = "sneakers"
print(Shoes)

# returns a list of the keys of the dictionary
dictionary_keys = list(Shoes.keys())
print(dictionary_keys)

# returns a list of the values of the dictionary
dictionary_values = list(Shoes.values())
print(dictionary_values)

# checks in the dictionary and returns a ture since "size exists in the dictionary"
x = "size" in Shoes
print(x)

# loops through the dictionary and prints each key with its value
for x, y in Shoes.items():
    print(x, ":", y)

# removes color from the dictionary
del Shoes["color"]
print(Shoes)

# empties the dictionary
Shoes.clear()
print(Shoes)

# created a dictionary called company
Company = {

    "company_name": "Global Star Solution",
    "location": "Kampala",
    "number_of_employees": 23,
    "tin_number": 124790083736
}
print(Company)


# make a copy from the company dictionary
mycompany = Company.copy()
print(mycompany)


# nested
MakerereUniversity = {
    "Cocis": {
        "year": 2002,
        "number_of_courses": 8
    },
    "Cobams": {
        "year": 1997,
        "number_of_courses": 34
    },
    "Law": {
        "year": 1990,
        "number_of_courses": 15

    },
}

# Updateing nestedndictionary objects
MakerereUniversity.update({
    "Cocis": {
        "year": 2022,
        "number_of_courses": 4
    },
    "Cobams": {
        "year": 1997,
        "number_of_courses": 64
    },
    "Law": {
        "year": 1790,
        "number_of_courses": 15

    },
})
print(MakerereUniversity["Cocis"])
print(MakerereUniversity["Cocis"]["year"])


# Zipping: Combines two lists into a dictionary while mapping them as key:value pairs.
bob2 = dict(zip(['name', 'job', 'age'], ['Bob', 'dev', 40]))
print(bob2)

"""
    Some of the other dictionary acceptable methods
    1. contains()
    2. get()- Returns the value of the specified key
    3. clear()	Removes all the elements from the dictionary
    4. pop() - Removes the element with the specified key and return value
    5. len() - Returns length of array
    6. popItem() - Removes the last inserted key-value pair
    7. items() - Returns a list containing a tuple for each key value pair
    8. copy()
    9.values()	- Returns a list of all the values in the dictionary
"""
my_dictionary = dict()
my_dictionary.update({'a': 1, 'b': 2, 'c': 3})

# print all dictionary methods
print(dir(my_dictionary))

new_dict = my_dictionary.copy()
print(new_dict)
print(my_dictionary.items())
print(my_dictionary.get('b'))
print(len(my_dictionary))
print(my_dictionary.pop('a'))
