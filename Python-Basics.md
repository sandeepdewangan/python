
# Python-I

Source: www.learnbyexample.org

## Integers

**Integers in binary, octal and hexadecimal formats**
```python
# binary
print(0b10111011)
# Prints 187

# octal
print(0o10)
# Prints 8

# hex
print(0xFF)
# Prints 255
```

**Scientific notation**

```python
print(42e3)
# Prints 42000.0

print(4.2e-3)
# Prints 0.0042
```

**Identity Operators**

Identity operators are used to check if two objects point to the same object, with the same memory location.
```python
x = [1,2,1]
y = [1,2,1]
# Returns true if both variables are the same object
print(x is y) # False
print(x not is y)
```

**Membership Operators**

Membership operators are used to check if a specific item is present in a sequence (such as a string, tuple, list, or range) or a collection (such as a dictionary, set, or frozen set).
```python
x = ['apple', 'ball', 'cat']
print('apple' in x)  # True
```

## Lists
Lists are ordered and mutable.
```python
L = []  # An empty list
L = list('abc')  # Constructor
L = list((1, 2, 3))  # Convert a tuple to a list
L.append('blue')  # add item to a list
L.insert(1,'blue')  # insert at specific position
L.extend(L2)   # combine two list
# OR
L = L1 + L2
L.pop(1)   # Remove an Item by Index or simple use pop to remove last item
L.remove('blue')   # Remove an Item by Value, removes only first instance
del L[1:4]   # Remove Multiple Items
L.clear()   # Remove all items
L.copy()	# Returns a shallow copy of the list
```

**List Replication**
```python
L = ['red']
L = L * 3
print(L)
# Prints ['red', 'red', 'red']
```
**Presence of item**
```python 
L = ['A', 'B', 'C']
print('A' in L)  # True 
```

**Iterate through a list**
```python 
L = [1, 2, 3, 4]
for item in L:
    print(item)

# OR, if we want to modify the list

for item in range(len(L)):
    print(L[item])
```

**Slicing**

```python 
L = [0,1,2,3,4,5,6,7,8,9]
# start, stop, step
print(L[0:9:2])
```



**List Comprehension**

A comprehension is a compact way of creating a Python data structure from iterators. With comprehensions, you can combine loops and conditional tests with a less verbose syntax.

Without Comprehension

```python
L = []
for i in range(5):
    L.append(i**2)
```

With Comprehension

```python
# [expression for var in iterable]
# expression is evaluated once for each item
# iterable is collection of items

L = [i**2 for i in range(5)]
```

```python
# (x, x2)
L = [(i, i**2) for i in range(5)]
# [(0, 0), (1, 1), (2, 4), (3, 9), (4, 16)]
```

**List Comprehension with if Clause**

```python
num = [2, 4, 6, 8, 10]
L = [i for i in num if i >= 6]
```

**Nested List Comprehensions**

```python
vector = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
L = [number for list in vector for number in list]
```

**Transpose of Matrix using Comprehension**

```python
matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]
L = [[row[i] for row in matrix] for i in range(3)]
print(L)
# Prints [[1, 4, 7], [2, 5, 8], [3, 6, 9]]
```

**List Comprehensions + Function**

```python
def myfuc(c):
    return c*2

L = [myfuc(c) for c in 'foo']
#['ff', 'oo', 'oo']
```

**Above example with map()**

```python
L = list(map(myfuc, 'foo'))
#['ff', 'oo', 'oo']
```

**Lambda function**

A lambda function is a small anonymous function. A lambda function can take any number of arguments, but can only have one expression.

```python
square = lambda x:  x**2
print(square(4))
```

**List Comprehension vs map() + lambda**

```python
L = [i**2 for i in range(5)]   # This is faster in execution
print(L)

L = list(map(lambda a: a**2, range(5)))		# Slower
print(L)
```

**Filter Function**

```python
# With list comprehension
L = [x for x in range(10) if x % 2 == 0]
print(L)
# Prints [0, 2, 4, 6, 8]

# With filter() function
L = list(filter((lambda x: x % 2 == 0), range(10)))
print(L)
# Prints [0, 2, 4, 6, 8]
# filter() is slightly faster if you are using a built-in function.
```

## Tuple

Tuples are ordered and immutable.

```python
# A tuple with mixed datatypes
T = (1, 'abc', 1.23, True)

# An empty tuple
T = ()

# A tuple without parentheses
T = 1, 'abc', 1.23, True

# Singleton Tuple
T = (4,)
print(type(T))

# Convert a list to a tuple
T = tuple([1, 2, 3])
```

**Tuple Packing and Unpacking**

```python
# Packing
T = ('red', 'green', 'blue', 'cyan')

# Unpacking
T = ('red', 'green', 'blue', 'cyan')
(a, b, c, d) = T
```

**Change inside tuple items** 

The tuple immutability is applicable only to the top level of the tuple itself, not to its contents.

 For example, a list inside a tuple can be changed as usual.

```python
T = (1, [2, 3], 4)
T[1][0] = 'xx'
print(T)
# Prints (1, ['xx', 3], 4)
```

**Delete a tuple**

```python
T = ('red', 'green', 'blue')
del T
```

## Set

Python set is an unordered collection of unique items. 

They are commonly used for computing mathematical operations such as union, intersection, difference, and symmetric difference.

```python
# A set of strings
S = {'red', 'green', 'blue'}

# Dont allows duplicate
S = {'red', 'green', 'blue', 'red'}
print(S)
# Prints {'blue', 'green', 'red'}

# Set constructor
# Set of items in an iterable
S = set('abc')
print(S)
# Prints {'a', 'b', 'c'}

# Add element to set
S.add('yellow')

# Add multiple items to a set
S.update(['yellow', 'orange'])

# Remove item
S.remove('red') # Throws error if item not found
# OR
S.discard('red') # Doesnot throw any error

# pop - pops random items from the set
x = S.pop()

# clear- removes all items
S.clear()
```

<mark>**NOTE**</mark>: 

* A set itself is mutable (changeable), but it cannot contain mutable objects like lists and dictionaries.
* Therefore, immutable objects like numbers, strings, tuples can be a set item, but lists and dictionaries are mutable, so they cannot be.

**Set Operations**

```python
A.union(B)
A.intersection(B)
A.difference(B)
A.symmetric_difference(B)
```

**Frozen Set**

Frozenset is just like set, only immutable (unchangeable).

```python
S = frozenset({'red', 'green', 'blue'})
```



## Dictionary

Generally known as associative arrays, hashes, or hash maps.

**Creating a dictionary**

```python
D = {'name': 'Bob',
     'age': 25,
     'city': 'New York',
     'email': 'bob@web.com'}

# Using keyword arguments
D = dict(name = 'Bob',
         age = 25,
         job = 'Dev')
print(D)
# Prints {'name': 'Bob', 'age': 25, 'job': 'Dev'}
```

**Combine separate list of keys and values to form a dictionary**

```python
keys = ['Name', 'Age', 'Gender']
values = ['Sandeep', '33', 'M']

D = dict(zip(keys, values))
print(D)
```

**Default value for all the keys**

```python
# Initialize dictionary with default value '0' for each key
keys = ['a', 'b', 'c']
defaultValue = 0

D = dict.fromkeys(keys,defaultValue)
print(D)
# Prints {'a': 0, 'b': 0, 'c': 0}
```

<mark>**NOTE:**</mark> Key must be unique else, it will be overridden.

```python
D = {'name': 'Bob',
     'age': 25,
     'name': 'Jane'}
print(D)
# Prints {'name': 'Jane', 'age': 25}
```

**Accessing**

```python
D['Name'] # Throws exception if key doesnot exist.
# OR
D.get('Name') # Doesnot throw error
```

**Add, Update, Merge, Remove**

```python
# Update or Add new
D['name'] = 'Sam'

# Merge two dictionary
D1.update(D2)

# Remove
D.pop('age')
# OR
del D['age']

# Remove last inserted item
D.popitem()

# Remove all
D.clear()
```

**Get All Keys, Values and Key:Value Pairs**

```python
D = {'name': 'Bob',
     'age': 25,
     'job': 'Dev'}

# get all keys
print(list(D.keys()))
# Prints ['name', 'age', 'job']

# get all values
print(list(D.values()))
# Prints ['Bob', 25, 'Dev']

# get all pairs
print(list(D.items()))
# Prints [('name', 'Bob'), ('age', 25), ('job', 'Dev')]
```



## Strings

```python
# Multiline string
S = """
      This is string
      and can span
      multiple lines
"""

# String Constructor
# int to string conversion
S = str(42)

# Join string together
S = ('In this way we can'
     'join strings'
     'togheter'
     )

# String search
S = 'Stay Hungry, Stay Foolish'
x = S.find('Foolish')
# x Prints position of word if found else -1
```

**Raw String**

```python
S = r'C:\new\text.txt'
```

**String Formatting / String Interpolation**

```python
# Format 1
S = "%s is %d years old" % ('Sandeep', 33)

# Format 2
S = "{0} is {1} years old" .format('Sandeep', 33)

# Format 3
name='Sandeep'
age=33
S = f"{name} is {age} years old"
```

# If Else, While, For

**Conditional Expressions (ternary operator)**

Syntax

`variable = statement (True) if condition else statement`

```python
x, y = 7, 5
max = x if x > y else y
print(max)
# Prints 7
```

**while/for else**

```python
# The else clause will be executed when the loop terminates normally
x = 6
while x:
    print(x)
    x -= 1
else:
    print('Done!')
```

Above code works with for loop.

**range()**

```python
# range(start,stop,step)
for i in range(0,100,5):
    print(i)
```

**Unpacking**

```python
# Tuple unpacking
T = [(1, 2), (3, 4), (5, 6)]
for (a, b) in T:
    print(a, b)

# Dictionary unpacking
D = {'name': 'Bob', 'age': 25}
for x, y in D.items():
	print(x, y)
```

## Functions

**Types of Arguments**

```python
# - Positional Arguments
def func(name, job):
    print(name, 'is a', job)
func('Bob', 'developer')

# - Keyword Arguments:
# To avoid positional argument confusion, 
# you can pass arguments using the names of their corresponding parameters.
def func(name, job):
    print(name, 'is a', job)
func(name='Bob', job='developer')

# - Default Arguments
def func(name, job='developer'):
    print(name, 'is a', job)
    
# - Variable Length Positional Arguments (*args)
# Unlimited number of arguments.
# * , it collects all the unmatched positional arguments into a tuple
def call_me(*args):
    print(args)
call_me(1, 2, 3, 4)
# (1, 2, 3, 4)

# - Variable Length Keyword Arguments (**kwargs)
# Works for keyword arguments. Based on key value pairs.
def call_me(**args):
    print(args)
call_me(name='Sandeep', age=33, gender='male')
# {'name': 'Sandeep', 'age': 33, 'gender': 'male'}
```

**Return Multiple Values**

```python
def add_sub(a, b):
    return a+b, a-b

result = add_sub(3,2) # (5, 1)
# OR
add, sub = add_sub(3,2) # unpack
```

**Docstring**

Docstrings are usually triple quoted to allow for multi-line descriptions.

```python
def hello():
    """This function prints
       message on the screen"""  
    print('Hello, World!')

help(hello)

# Help on function hello in module __main__:
# hello()
#    This function prints
#    message on the screen

# OR

# Print docstring in a raw format
print(hello.__doc__)
```

**Assigning Functions to Variables**

```python
def hello():
    print("Hello")

namaste = hello
namaste()
```

This feature can be used to implement jump table. Jump table is a dictionary of functions to be called on demand.

```python
def findSquare(x):
    return x**2

def findCube(x):
    return x**3

exponent = {'square': findSquare, 'cube': findCube}

print(exponent['square'](4)) # 16
print(exponent['cube'](4))   # 64
```

**global keyword**

```python
x = 42          # global scope x
def myfunc():
    global x    # declare x global
    x = 0
    print(x)    # global x is now 0

myfunc()
print(x)        # x is 0
```

**Lambda Function**
A lambda is simply a way to define a anonymous function in Python.

```python
doubler = lambda x: x*2
```

<mark>**NOTE**:</mark> There’s no need to use the `return` keyword, the lambda does this automatically for you.

* No statements allowed
* Single expression only

## Classes and Objects

A class is the blueprint from which individual objects are created. 

* In Python, everything is an object – integers, strings, lists, functions, even classes themselves. However, Python hides the object machinery with the help of special syntax. For example, when you type `num = 42`, Python actually creates a new object of type integer with the value 42, and assign its reference to the name `num`.

* `__init__()` is the special method that initializes an individual object. 
* The `self` parameter refers to the individual object itself. It is used to fetch or set attributes of the particular instance.
* Self should always be the first parameter of any method in the class, even if the method does not use it.

```python
class Car:
    # attribute
    wheels = 4
    
    # initialize with instance attributes
    def __init__(self, color, style):
        self.color = color
        self.style = style
    
    def showDescription(self):
        print(f"This car is a {self.style} style and its color is {self.color}")

# Create an object
c = Car(color='Red', style='SUV')
c.showDescription()

# Delete attributes
del c.color

# Delete object
del c
```

**Inheritance**

Extend the functionality of an existing class

```python
class Vehicle():
    def description(self):
        print("I am a Vehicle")


class Car(Vehicle):
    pass

v = Vehicle()
c = Car()

v.description() # I am a Vehicle
c.description() # I am a Vehicle
```

**Override a method**

```python
class Vehicle():
    def description(self):
        print("I am a Vehicle")


class Car(Vehicle):
    def description(self):
        print("I am a Car")

v = Vehicle()
c = Car()

v.description() # I am a Vehicle
c.description() # I am a Car
```

**super() **

Use to reuse the method of the base class and add some new stuff

```python
super().__init__(color) 
```

**Multiple Inheritance**

Python also supports multiple inheritance

```python
class BaseClass1():
    pass
class BaseClass2():
    pass
class SubClass(BaseClass1, BaseClass2):
    pass
```

## Decorators

A decorator is a function that accepts a function as input and returns a new function as output, allowing you to extend the behavior of the function without explicitly modifying it.

Every decorator is a form of **metaprogramming**.

**Metaprogramming** is about creating functions and classes whose main goal is to manipulate code (e.g., modifying, generating, or wrapping existing code).

**Simple Decorator**

```python
def decorated(func):
    def wrapper():
        print("****************")
        func()
        print("****************")
    return wrapper

@decorated
def hello():
    print("Hello World!")

hello()
```

<mark>**INCOMPLETE**</mark>

## @Property

In other languages, Programmers often have to write getter and setter methods to access such private attributes.

However in Python, all the attributes and methods are public, so it is useless to write getters or setters.

If you want to prevent direct access to an attribute, you should define it as a **property**.

```python
class Person():
    def __init__(self, value):
        self.hidden_name = value
    
    def get_name(self):
        return self.hidden_name
    
    def set_name(self, value):
        self.hidden_name = value

    # The get_name() and set_name() methods act like normal getter and setter until this line.
    name = property(get_name, set_name)


p = Person('Sandeep')
print(p.name)
```

**OR** (USE BELOW)

```python
class Person():
    def __init__(self, value):
        self.hidden_name = value
    
    @property
    def name(self):
        return self.hidden_name
    
    @name.setter
    def name(self, value):
        self.hidden_name = value


p = Person('Sandeep')
print(p.name)
```

Example @property

```python
class Rectange():
    def __init__(self, w, h):
        self.w = w
        self.h = h
    
    def area(self):
        return self.h * self.w

r = Rectange(2, 3)
print(r.area())
```

In above code, we have used area as a function, to **use as a property** we can decorate it.

```python
class Rectange():
    def __init__(self, w, h):
        self.w = w
        self.h = h
    
    @property
    def area(self):
        return self.h * self.w

r = Rectange(2, 3)
print(r.area)
```



## Exceptions 

Basic Flow

```python
try:
    x = 1/0
except ZeroDivisionError:
    print("Zero Division Error")
except Exception as e:
    print("Display the error type", e)
except (ZeroDivisionError, ValueError):
    print("Catch multiple errors")
except:
    print("Something else gone wrong")
else:
    print("The else clause is executed only if no exceptions are raised.")
finally:
    # clean-up actions
    print("A finally clause is always executed, whether an exception has occurred or not.")
```

**Raising an Exception**

1. **Named Exception**

```python
raise NameError("Somethign went wrong")
```

2. **User-defined Exceptions**

```python
class MyException(Exception):
    pass

raise MyException('This is custom exception with class')
```

## Text File Handling

Basic Operations

```python
# ‘r’	Read (default)	Open a file for read only
# ‘w’	Write	Open a file for write only (overwrite)
# ‘a’	Append	Open a file for write only (append)
# ‘r+’	Read+Write	open a file for both reading and writing
# ‘x’	Create	Create a new file

# Opening a file
f = open(r'data.txt', 'w')

# Reading a file
# read() method reads the entire file
print(f.read())

# read first 3 chars.
print(f.read(3))

# read line by line
for line in f:
    print(line)

# read lines into list of strings
d = f.readlines()
print(d)

# Writing a file
f.write('Data')

# Write Multiple Lines
lines = ['New line 1\n', 'New line 2\n', 'New line 3']
f.writelines(lines)

# Flush Output Buffer
# When you write to a file, the data is not immediately written to disk instead it is stored in buffer memory. 
# It is written to disk only when you close the file or manually flush the output buffer.
f.flush()

# Close a File
f.close()

# Check closed status
print(f.closed)
```

**Python way to read and write a file**

```python 
with open(r'data.txt', 'r') as f:
    print(f.read())
```

**OR**

```python
f = open('myfile.txt')
try:
    # File operations goes here
finally:
    f.close()
```

**Delete a file**

```python
import os

# check file exists
if os.path.isfile('myfile.txt'):
    os.remove('data.txt')
else:
    print('File doesnot exists')
```

**Random Access**

- 0 – indicates the beginning of the file (default)
- 1 – indicates the current pointer position
- 2 – indicates the end of the file

```python
# go to the 7th character and read one character
f.seek(6)
print(f.read(1))

# go to the 3rd character from current position (letter G)
f.seek(3, 1)

# go to the 3rd character before the end
f.seek(-3, 2)

# Check the current position of the file pointer
f.tell()
```

## CSV File Handling

Reading CSV

**The reader() method splits each row on a specified delimiter and returns the list of strings.**

```python
import csv

f = open(r'data.csv', 'r')

for line in f:
    reader = csv.reader(f) # delimiter=',' DEFAULT
    for row in reader:
        print(row)

f.close()
```

Writing to aCSV

```python
import csv

with open(r'data.csv', 'w') as f:
    writer = csv.writer(f)
    writer.writerow(['Vijay','25','F'])
    writer.writerow(['Gagan','30','M'])
```

**Comma in CSV data, wrap data into quotes**

```python
import csv

with open('myfile.csv', mode='w') as f:
    writer = csv.writer(f, quotechar='"') # while reading -> csv.reader(f, quotechar='"')
    writer.writerow(['Bob', '25', '113 Cherry St, Seattle, WA 98104, USA'])
    writer.writerow(['Sam', '30', '150 Greene St, New York, NY 10012, USA'])

# OUTPUT
Bob,25,"113 Cherry St, Seattle, WA 98104, USA"
Sam,30,"150 Greene St, New York, NY 10012, USA"
```

 





























