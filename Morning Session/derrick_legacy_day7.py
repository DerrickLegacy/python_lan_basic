# Inheritance and Polymorphism
"""summary

Inheritance and method overriding
Polymorphism and method resolution
order
Abstract classes and interfaces

    """

# Inheritance and method overriding
"""summary
--description
Inheritance and method overriding allows a class(child class) to inherit attributes and methods
from another class (parent class).

Key concepts
Base class (parent class): Class whose properties are inherited by another class.
Derived class (child class): Class that inherits attributes and properties from another base class.

    """

# Example 1: Syntax Create a class where a dog inherits from animal and overrides with a speak method


class Animal:
    def speak(self):
        return "Mwe Mwe Mwe Mwe Mwe"


class Doog(Animal):
    def speak(self):
        return "Barks"


# Implementatiion of inherited classes

animal = Animal()
dog = Doog()

print(animal.speak())
print(dog.speak())
# Reading and Writing Files


# Polymorphism
# Polymorphism allows objects of different classes to be treated as objects of a common superclass.
# Method resolution Order (MRO). - order of looking for a method in a hierarchy classes


# How polymorphism works in python
class Animaal:
    def speak(self):
        return "Mwe Mwe Mwe Mwe Mwe"


class Dog(Animaal):
    def speak(self):
        return "Barks"


class Snake(Animaal):
    def speak(self):
        return "Hisses"


def make_animal_speak(animal):
    print(animal.speak())


make_animal_speak(Snake())

# Exercise 1: Create a simple application to manage different types of vehicles. Implement derived class to demo inheritance and polymorphism.

""" 
    Requirements
    1. -Base classvehicle
       -Atrributes:
            make
            model
            year
    2. Derived classes
        a) car inherits from vehicle
            -Attributes:
                number of doors
            -override display_info()
        b) Motocycle inherits from vehicle
            -Attributes: 
                type of bike(cruiser, sport, touring)
                override display_info()
# Exercise 2: Polymorphism
    Create a fn that accepts a list of vehicles object and call their displya_info() method to print a details of each vehicle
"""


# Sol 1
class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def display_info(self):
        print(f"Make: {self.make}")
        print(f"Model: {self.model}")
        print(f"Year: {self.year}")


class Car(Vehicle):
    def __init__(self, make, model, year, number_of_doors):
        super().__init__(make, model, year)
        self.number_of_doors = number_of_doors

    def display_info(self):
        super().display_info()
        print(f"Number of doors: {self.number_of_doors}")


class Motorcycle(Vehicle):
    def __init__(self, make, model, year, type_of_bike):
        super().__init__(make, model, year)
        self.type_of_bike = type_of_bike

    def display_info(self):
        super().display_info()
        print(f"Type of bike: {self.type_of_bike}")


def print_vehicle_info(vehicles):
    for vehicle in vehicles:
        vehicle.display_info()
        print()


car = Car("Toyota", "Corolla", 2020, 4)
motorcycle = Motorcycle("Harley-Davidson", "Street 750", 2019, "Cruiser")

vehicles = [car, motorcycle]

print_vehicle_info(vehicles)


"""summary
Working with text files
Handling CSV files
JSON and XML file processing
"""

# 1 . Working with text files: open, read ,write and close
# NOte: Python has inbuilt functions to handle text files.

""" 

    OPening file : open() - Modes (r,w,a,r+)
    Reading file : read()
    Writing file : write()
    Close file : close()
    
    Modes::
        r: open an existing file for a read operation.
        w: open an existing file for a write operation. If the file already contains some data, then it will be overridden but if the file is not present then it creates the file as well.
        a:  open an existing file for append operation. It won’t override existing data.
        r+:  To read and write data into the file. The previous data in the file will be overridden.
        w+: To write and read data. It will override existing data.
        a+: To append and read data from the file. It won’t override existing data.
"""

# Example 3: Write a file and read a file

# Write
with open("derrick.txt", "w") as file:
    file.write("This is my first file\n")
    file.write("I love python programming.")

    
# Read
with open("derrick.txt", "r") as file:
    print(file.read())


# Handling CSV files

""" 
    CSV - Comma Separated Values
    Concepts:
        -Reading CSV - use 'csv.reader()'
        -Writing CSV - use 'csv.writer()'
        DictReader and DictWriter - Theses classes read and write CSv files as dictionaries
        
"""
# Example:
import csv

# 1 Writing 
with open('derrick.csv', 'w', newline='') as csv_file:
     csv_writer = csv.writer(csv_file)
     csv_writer.writerow(['Name', 'Age'])
     csv_writer.writerow(['Derrick', '15'])
     csv_writer.writerow(['Ahaabwe', '16'])

# Read csv file  
with open('derrick.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)
    for line in csv_reader:
        print(line)
print()
""" 
    JSON (Javascript Object Notation) and XML (eXtensible Markup Language)
    Concepts:
        -Reading JSON - use 'json.load()'
        -Writing JSON - use 'json.dump()'
        -Reading XML - use 'xml.etree.ElementTree.parse()'
        -Writing XML - use 'xml.etree.ElementTree.ElementTree()'
"""

# Example 6: Write and Read JSON files
print("JSON ,XML files")
import json

# Write
student_data =  {
            'name': 'Derrick',
            'age': 15,
            'year':3
        }
with open('derrick.json', 'w') as json_file:
    json.dump( student_data,json_file)

# Read the file
with open('derrick.json', 'r') as json_file:
    student_data = json.load(json_file)
    print(student_data)
    
# Exercise:
# 1. Write and read XML
# 2. Using abstraction calculate the area and perimeter of a rectangle


import xml.etree.ElementTree as ET

# Create the root element
root = ET.Element("shapes")

# Create a rectangle element
rectangle = ET.SubElement(root, "rectangle")
ET.SubElement(rectangle, "width").text = "10"
ET.SubElement(rectangle, "height").text = "5"

# Create a tree from the root element and write it to a file
tree = ET.ElementTree(root)
tree.write("shapes.xml")



import xml.etree.ElementTree as ET

# Parse the XML file
tree = ET.parse('shapes.xml')
root = tree.getroot()

# Iterate through elements and print their content
for rectangle in root.findall('rectangle'):
    width = rectangle.find('width')
    height = rectangle.find('height')
    print(f"Rectangle: Width={width}, Height={height}")


