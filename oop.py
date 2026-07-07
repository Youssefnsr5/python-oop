# OOP: Classes, Objects, Inheritance, Polymorphism, Encapsulation, Apstraction 

# CLASS
# Class: A blueprint for creating objects. It defines a set of attributes and methods that the created objects will have.
# class Name:
# constructor: A special method that is called when an object is created. It is used to initialize the attributes of the object.
# def __init__(self): # implement when create object from class, public method
# self: refers to the current instance of the class. It is used to access the attributes and methods of the class.
# method: A function that is defined inside a class and is used to perform a specific action on the objects created from the class. ex: display_info, name_with_title, etc.
# the__init__ method is called automatically when an object is created from the class. It is used to initialize the attributes of the object. 
class Car:
    def __init__(self, make, model, year): # constructor 
        self.make = make # instance attribute, unique to each instance of the class
        self.model = model
        self.year = year

    def display_info(self): # method attribute
        print(f"{self.year} {self.make} {self.model}")
    
    def name_with_title(self):
        if self.year >= 2025:
            return f"{self.make} {self.model} is a future car." 
        elif self.year <= 2024 and self.year >= 2020:
            return f"{self.make} {self.model} is a modern car."
        else:
            return f"{self.make} {self.model} is a classic car."
             
# OBJECT
# Object: An instance of a class. It is created using the class constructor and can access the attributes and methods defined in the class.
car1 = Car("Toyota", "Camry", 2020)

# car1.display_info()
# print(car1.name_with_title())

#//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
class Employee: #   uppercamelcase: convention for class names
 # Class Attribute (it's public: accessible from outside the class, but it's shared by all instances of the class) 
    company_name = "Tech Company" # class attribute, shared by all instances of the class
    employees_count = 0
    
    #Public Methods:
    def __init__(self, name, id, salary, position): # constructor (instance method, public method)
        self.name = name # instance attribute, unique to each instance of the class
        self.id = id
        self.salary = salary
        self.position = position
        Employee.employees_count += 1 # increment the employees count when a new employee is created
        
    def increase_salary(self, amount): # method to increase the salary of an employee
        self.salary += amount # increase the salary of the employee by the specified amount
    
        
    # Destructor    
    def __del__(self): # called when an object is destroyed
        Employee.employees_count -= 1 # decrement the employees count when an employee is destroyed
    
    @classmethod # (decorator) class method, can access class attributes and modify them, but cannot access instance attributes
    # class methods are defined using the @classmethod decorator and take the class itself as the first argument (cls)
    # class methods: can use it without attribute of the instance, but it can access class attributes and modify them
    def update_company_name(cls, new_name): # class method to update the company name
        cls.company_name = new_name # update the company name using the class method
        
    @staticmethod # (decorator) static method, cannot access class attributes or instance attributes, but can perform a specific action related to the class
    def calculate_bonus(salary, bonus_percentage): # static method to calculate the bonus for an employee
        return salary * bonus_percentage / 100 # calculate the bonus based on the salary and bonus percentage
    
    def display_info(self):
        print(f"Name: {self.name}, ID: {self.id}, Salary: {self.salary}, Position: {self.position}")
        print(f"Company Name: {Employee.company_name}") # access class attribute using the class name
        print(f"Employees Count: {Employee.employees_count}") # access class attribute using the class name
    
    
        
        
employee1 = Employee("Alice", 42410, 50000, "Software Engineer")
bonus_employee1 = Employee.calculate_bonus(employee1.salary, 20)
# employee1.display_info()
# print(f"Bonus: {bonus_employee1}")


employee2 = Employee("Bob", 42411, 60000, "Data Scientist")
# employee2.display_info()


Employee.update_company_name("New Tech Company") # call class method to update the company name
# employee1.display_info()


# ////////////////////////////////////////////////////////////////////////////////////////////////////////////////

# INHERITANCE
"""
inheritance: allows a Child Class to inherit attributes
and methods from a Parent Class.
The Child Class can also have its own unique attributes and methods,
and can override the inherited methods to provide a specific implementation for the Child Class.
////////////////////////////
super() does:
1- call parent class method 
2- avoid code duplication
3- handel multiple inheritance correctly
///////////////////////////
Types of Inheritance:
 1- Single Inheritance: A Child Class inherits from a single Parent Class.
    EX: class Manager(Employee): 
 2- Multiple Inheritance: A Child Class inherits from multiple Parent Classes.
    EX: class Manager(Employee, AnotherClass):
 3- Hierarchical Inheritance: Multiple Child Classes inherit from a single Parent Class.
    EX: class Manager(Employee), class Developer(Employee), etc.
 4- Multilevel Inheritance: A Child Class inherits from a Parent Class, which in turn inherits from another Parent Class.
    EX: class Manager(Employee), class SeniorManager(Manager), etc.
 5- Hybrid Inheritance: A combination of two or more types of inheritance.
    EX: class Manager(Employee), class Developer(Employee), class SeniorManager(Manager), etc.
"""
class Manager(Employee): # Manager class inherits from Employee class
    def __init__(self, name, id, salary, position, department): # constructor for Manager class
        super().__init__(name, id, salary, position) # call the constructor of the parent class (Employee class) to initialize the inherited attributes
        self.department = department # unique attribute for Manager class
    
    # Overloading: allows a Child Class to provide a specific implementation for a method that is already defined in the Parent Class.
    def display_info(self): # override the display_info method from the Employee class
        super().display_info() # call the display_info method from the parent class to display the inherited attributes
        print(f"Department: {self.department}") # display the unique attribute for Manager class    

manager1 = Manager("Charlie", 42412, 70000, "Manager", "IT")
#manager1.display_info()


#////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

# POLYMORPHISM
"""
Polymorphism: allows objects of different classes to be treated as objects of a common superclass.
It is the ability of an object to take on many forms.
polymorphism = Overloading + Overriding
  1- Overloading: allows a Child Class to provide a specific implementation for
     a method that is already defined in the Parent Class.
     (method name is the same, but the implementation is different)
  2- Overriding: allows a Child Class to provide a specific implementation for 
     a method that is already defined in the Parent Class.
     (method name is the same, but the implementation is different)
"""
class Developer(Employee): # Developer class inherits from Employee class
    def __init__(self, name, id, salary, position, programming_language): # constructor for Developer class
        super().__init__(name, id, salary, position) # call the constructor of the parent class (Employee class) to initialize the inherited attributes
        self.programming_language = programming_language # unique attribute for Developer class
    
    def display_info(self): # override the display_info method from the Employee class
        super().display_info() # call the display_info method from the parent class to display the inherited attributes
        print(f"Programming Language: {self.programming_language}") # display the unique attribute for Developer class

#/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

# ABSTRACTION
"""
Apstraction: the process of hiding the implementation details and showing only the functionality to the user.
It allows the user to focus on what the object does instead of how it does it.
--
Apstraction can be achieved using:
1- Abstract Classes: not have a complete implementation and cannot be instantiated (no have an object of their own). They are defined using the ABC module and the @abstractmethod decorator.


"""
from abc import ABC, abstractmethod

#class Programming(metaclass=ABCMeta): # abstract class, cannot be instantiated
class Programming(ABC): # not an abstract class, can be instantiated
    @abstractmethod # abstract method, must be implemented by the subclasses
    def has_oop(self):
        pass
    
    def has_name(self):
        pass
class Python(Programming): # Python class inherits from Programming class
    def has_oop(self):
        return "Yes, Python supports OOP."
    
    def has_name(self):
        return "Python is a programming language."

class Pascal(Programming): # Pascal class inherits from Programming class
    def has_oop(self):
        return "No, Pascal does not support OOP."
    
    def has_name(self):
        return "Pascal is a programming language."
    
python = Python()
pascal = Pascal()
# print(python.has_oop())
# print(pascal.has_oop())


# in Abstract class:
 
#print(s.has_oop())

# not an abstract class:
s = Programming() # this will not raise an error because we can create an object of a
# print(s.has_oop()) # this will not raise an error because we can call the method of the class, but it will return None because the method is not implemented in the Programming class


#///////////////////////////////////////////////////////////////////////////////////////////////////////////

# ENCAPSULATION
"""
    Private Attributes: can only be accessed by the class itself, not by outside code or subclasses. They are defined using double underscores (__) before the attribute name.
    Protected Attributes: can be accessed by the class and its subclasses, but not by outside code. They are defined using a single underscore (_) before the attribute name.
    Public Attributes: can be accessed by anyone, both inside and outside the class. They are defined without any underscores before the attribute name.
    --
    1- Private Attributes: The syntax is _ClassName__AttributeName.
         EX: self.__private_attr can be accessed using self._EncapsulationExample__private_attr.
         
    2- Protected Attributes: They can also be accessed using name mangling, but it is not recommended to do so.
         EX: self._protected_attr can be accessed using self._EncapsulationExample__protected_attr, 
         but it is not recommended to do so.
    
"""
class EncapsulationExample:
    def __init__(self, public_attr, protected_attr, private_attr):  # constructor
        self.public_attr = public_attr # public attribute
        self._protected_attr = protected_attr # protected attribute
        self.__private_attr = private_attr # private attribute
    
    #Protected Methods:
    def _protected_method(self): # protected method
        return "This is a protected method."
    
    #Private Methods:
    def __private_method(self): # private method
        return "This is a private method."
    
    #Public Methods:
    def public_method(self): # public method
        return "This is a public method."
    



