"""     
        **CLASSE**
    class is a user-defined blueprint or prototype from which objects are created. 
    Bundle functionality together.
    -have object (Instances) each have attributes
    -Inheritence
    -class memberes are public
    
    Python Scopes and Namespaces
        * namespace is a mapping from names to objects eg set of built-in names
        
        * scope is a textual region of a Python program where a namespace is directly accessible
            -Directly accessible” here means that an unqualified reference to a name attempts to find the name in the namespace.
        
        *Attributes may be read-only or writable, deletable with del-keyword (eg del modname.the_answer)
        
    Syntax: Class Definition
        class ClassName:
            # Statement
            
    Syntax: Object Definition
        obj = ClassName()
        print(obj.atrr)
        
"""


class Dog:
    sound = "bark"


""" 
    Object of Python Class
        *Object is an instance of a Class
            -has state eg age, breed,color
            -behaviour eg bark,sleep
            -Identity eg name of dog
"""


class Dog:
    sound = "bark"
    color = "black"
    age = 10

    def bark(self):
        print(self.sound)
        print(self.color)
        print(self.age)


# object instantiation
Rodger = Dog()

# accessing attributes
print(Rodger.color)

# accessing methods
Rodger.bark()

""" 
        # Self parameter*
    When we call a method of this object as myobject.method(arg1, arg2), this is automatically converted by Python into MyClass.method(myobject, arg1, arg2) this is all the special self is about. 
"""


class GFG:
    def __init__(self, name, company):
        self.name = name
        self.company = company

    def show(self):
        print("My name is : " + self.name)
        print("My company is : " + self.company)


object = GFG("John", "URA")
object.show()  # GFG.show(object,name,company)

""" 
        # Pass Statement*
    -The pass statement is used when a statement is required syntactically but you do not want any command or code to execute.
    -It merely permits the program to skip past that section of the code without doing anything. 
"""


class MyClass:
    pass


""" 
    # _init_() method*
    -The __init__() function is called automatically every time the class is being used to create a new object. Used like as a constructor
    
"""


class Person:

    def __init__(self, name):
        self.name = name

    def say_hi(self):
        print('Hello, my name is', self.name)


p = Person('Nikhil')
p.say_hi()

""" 
        #str__() method* 
    -The __str__() function is called whenclass object is used to create a string using the print()  and str() function.
    -used to define how a class object should be represented as a string- give object human-readable textual representation
    -You can alter how objects of a class are represented in strings by defining the __str__() method.
"""


class GFF:
    def __init__(self, name, company):
        self.name = name
        self.company = company

    def __str__(self):
        return f"My name is : {self.name} and my company is : {self.company}."

    def __repr__(self):
        return f"My name is : {self.name} and my company is : {self.company}."


my_obj = GFF("Derrick", "URA")
print(my_obj)

""" 
        #Class and Instance Variables*
    *Class variables are variables that are shared by all instances of a class.
        -are for attributes and methods shared by all linstances.
        -can be accessed through class name
        -there values are assigned outside constructor
    *Instance variables are variables that are unique to each instance. 
        -are for data
        -There values are assigned inside a constructor
"""


class Dog2:
    # class variable
    animal = 'dog'

    def __init__(self, breed, color):
        self.breed = breed
        self.color = color


Rodger = Dog2("Pug", "Brown")
Buzo = Dog2("BullDog", "Brown")

print('Rodger details:')
print('Rodger is a', Rodger.animal)
print('Breed: ', Rodger.breed)
print('Color: ', Rodger.color)

print('\nBuzo details:')
print('Buzo is a', Buzo.animal)
print('Breed: ', Buzo.breed)
print('Color: ', Buzo.color)

print("\nAccessing class variable using class name")
print(Dog2.animal)

# Defining instance variables using the normal method:


class Dog3:
    animal = 'dog'

    def __init__(self, breed):
        self.breed = breed

    def setColor(self, color):
        self.color = color

    # Retrieves instance variable
    def getColor(self):
        return self.color

    def __str__(self):
        return f"Breed: {self.breed}"


Rodger = Dog3("pug")
print(Rodger)
Rodger.setColor("Brown")
print(Rodger.getColor())
