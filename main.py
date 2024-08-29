
#* Datatypes in Python
num: int = 10  # 'num' is expected to be an int, and it is set to 10
decimal: float = 2.5  # 'decimal' is expected to be a float, and it is set to 2.5
text: str = 'Hello World'  # 'text' is expected to be a string, and it is set to 'Hello World'
active: bool = False  # 'active' is expected to be a bool, and it is set to False

names: list = ['Aayansh', 'Alice', 'Prasin']  # 'names' is expected to be a list, set to a list of strings
coordinates: tuple = (1.5, 2.5)  # 'coordinates' is expected to be a tuple, set to a tuple of floats
unique: set = {1, 4, 2, 9}  # 'unique' is expected to be a set, set to a set of integers
data: dict = {'name': 'Bob', 'age': 20}  # 'data' is expected to be a dictionary, set to a dictionary with keys 'name' and 'age'


#! Type anotation --> It is optional in python
name: str = 'Bob'  #It is similar to name = 'Bob'
age: int = 11

#! In Python, constants are typically defined using variables with names written in uppercase letters
from typing import Final
VERSION= '1.0.12' #by using capslocked variables
# By convention, this signals to other developers that these variables should not be modified. Python itself doesn't enforce constants (like some other programming languages do), so it's up to the developers to follow these conventions to maintain the immutability of these variables.
print(VERSION)


#! Variable declaration
name = 'Bob' #string
age = 20 #number
binary=True #boolean
a,b,c=1,2,"Nischal"  #multiple variables assigning 
address="Earth"

#! Basic Printing Functions
print(name,age)
print(a,b,c)
print(a+b)
print(str(b)+c) #prints 2Nischal
print(type(binary))

print("My name is", c)
print("My name is"+ c)
print(f"My name is {c} and I am from {address} and I am {age} years old")

#! Functions
from datetime import datetime

#with no parameters
def date() -> None:  #Here none is a return type
    print('This is the current time:')
    print(datetime.now())

date()
date()

#with parameters
def greet(name) -> None:
    print(f"Hello, {name}!")

greet('BOB')

#with returning
def add(a: float,b: float) -> float:
    return a+b

print(add(1,2))


#! lambda Functions
#inplace of return we use the keyword lambda

mul=lambda a,b : a*b
print(mul(1,2))


#! Classes

class Car: #class names should be uppercase at first letter
    def __init__(self,color,horsepower): #self vaneko yesma volvo hune vo la
        self.color = color
        self.horsepower= horsepower

    def drive(self): #methods
        print(f"{self.color} is driving!")

    def get_into(self):
        print(f'{self.color} with {self.horsepower}')

    def __str__(self) -> str:
        return f'{self.color} with {self.horsepower} hp'

    

volvo =Car('red',200) #volvo is an object
print(volvo.color)
print(volvo.horsepower)
volvo.drive()
volvo.get_into()
print(volvo)

BMW =Car('blue',300)
print(BMW.color)
print(BMW.horsepower)
volvo.get_into()
volvo.drive()


#input
a=input("Enter a number")  #input always takes as string so need to be converted to int
print(a)
print(type(a))

b=int(input("Enter one num"))
print(b)
print(type(b))








