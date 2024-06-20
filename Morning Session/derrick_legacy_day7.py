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
import xml.sax.handler

# 1 Writing
with open("derrick.csv", "w", newline="") as csv_file:
    csv_writer = csv.writer(csv_file)
    csv_writer.writerow(["Name", "Age"])
    csv_writer.writerow(["Derrick", "15"])
    csv_writer.writerow(["Ahaabwe", "16"])

# Read csv file
with open("derrick.csv", "r") as csv_file:
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
student_data = {"name": "Derrick", "age": 15, "year": 3}
with open("derrick.json", "w") as json_file:
    json.dump(student_data, json_file)

# Read the file
with open("derrick.json", "r") as json_file:
    student_data = json.load(json_file)
    print(student_data)

# Exercise:
# 1. Write and read XML
# 2. Using abstraction calculate the area and perimeter of a rectangle

""" 
        XML -Extensible Markup Language 
    a) XML is extremely useful for keeping track of small to medium amounts of data without requiring an SQL- based backbone.
        1.XML Modules(xml package)
            xml.etree.ElementTree - the ElementTree API, a simple and lightweight XML processor
            xml.dom - the DOM API definition.
            xml.dom.minidom - a minimal DOM implementation.
            xml.dom.pulldom - support for building partial DOM trees.
            xml.sax - SAX2 base classes and convenience functions.
            xml.parsers.expat - the Expat parser binding. 
            
            Most Used API to xml data
            -SAX -Simple API for XML
            -DOM
            
            SAX
             -stanadrd interface for event driven xml parsing
             -Requires we create our own content handler
             -Requires calling startDocument and endDocument at start and end of xml file
             -ContentHandler is called at the start and end of each element.
             
             The make_parser Method
              xml.sax.make_parser( [parser_list] )- creates and returns a new parser object. parser_list is optional
            
            The parse Method
              xml.sax.parse( xmlfile, contenthandler[, errorhandler])
            The parseString Method
              xml.sax.parseString(xmlstring, contenthandler[, errorhandler])
             
              *xmlfile - This is the name of the XML file to read from.             
              *contenthandler - This must be a ContentHandler object.
              *errorhandler - If specified, errorhandler must be a SAX ErrorHandler object.  

"""

# ElementTree XML API
""" 
    -Has an elemt tree module- a simple light weight XML processor API
    -The 'ElementTree' in this module treats the whole XML document as a tree. 
    -'Element' class represents a single node in this tree.
    -Reading and writing operations on XML files are done on the ElementTree level
    -Each element is characterised by tag and attribute in dict object format
    -FOr trees, starting element, attrib is empty dictionary
"""

import xml.etree.ElementTree as ET

# Create the root element
root = ET.Element("shapes")

# a) CREATING OR WRITING XML FILE
rectangle = ET.SubElement(root, "rectangle")
ET.SubElement(rectangle, "width").text = "10"
ET.SubElement(rectangle, "height").text = "5"

# Create a tree from the root element and write it to a file
tree = ET.ElementTree(root)
tree.write("shapes.xml")


# b) READING XML
# Parse the XML file
tree = ET.parse("shapes.xml")
root = tree.getroot()

# Iterate through elements and print their content
for rectangle in root.findall("rectangle"):
    width = rectangle.find("width").text # type: ignore
    height = rectangle.find("height").text # type: ignore
    print(f"Rectangle: Width={width}, Height={height}")

# More: Constructing a tree out of a diction
import xml.etree.ElementTree as et

employeemployees=[{'name':'aaa','age':'21','sal':'5000'},{'name':'xyz','age':'22','sal':'6000'}]
root = et.Element('employees')

for employee in employeemployees:
    child = et.SubElement(root,"employee")
    name = et.SubElement(child,"name").text = employee['name']
    age = et.SubElement(child,"age").text = employee['age']
    salary = et.SubElement(child,"sal").text = employee['sal']
    
tree = et.ElementTree(root)
# tree.write("employees.xml")
print("Employees XML file created successfully")

# writing using open()
with open("employees.xml",'wb') as xml_file:
    tree.write(xml_file)

# Reading the employees       #   

tree = et.parse('employees.xml')
root = tree.getroot()

for employee in root.findall('employee'):
    name = employee.find('name').text # type: ignore
    age = employee.find('age').text # type: ignore
    sal= employee.find('sal').text # type: ignore
    print(f"Name {name}, Age : {age}, Sal : {sal}")
    

# Abstraction 

""" 
    Abstract Classes
        ● A class which contains one or more abstract methods is called an abstract class.
        ● An abstract method is a method that has method declaration but not has any implementation(body).
        ● An abstract class can be considered as a blueprint for other classes, allows you
        to create a set of methods that must be created within any child classes built
        from your abstract class.
        ● Abstract classes cannot be instantiated(initialised with values using an object i.e can never have an object) 
            and they need subclasses to provid implementations for those abstract methods which are defined in abstract classes.
        ● Abstract classes having abstract methods only are called interfaces.
        Classes implementing the abstract class can have their own methods

        The abc module(from ABC helper class) provides the infrastructure for defining Abstract Base Classes (ABCs) in Python
"""

from abc import ABC, abstractmethod

class Animal(ABC):
    # @abstractmethod
    def doAction(self):
        pass
    
class Human(Animal):
    def doAction(self):
        print("I can walk and run")

class Snake(Animal):
    def doAction(self):
        print("I can crawl")

class Dog(Animal):
    def doAction(self):
        print("I can bark")
        
class Lion(Animal):
    def __init__(self, sex):
        self.sex = sex
    def doAction(self):
        print("I can roar")   
        
    def getGender(self):
        print(self.sex);   
        
a = Animal()#- throws an error
lion = Lion('male')
lion.getGender()