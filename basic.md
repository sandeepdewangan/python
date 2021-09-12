# Python Basics
Reference: Book-Python crash course by ERIC MATTHES

## Notes
1. **List** [ ] are mutable and **Tuple** ( ) are immutable.
2. PEP	guideline - line limit 79 characters.
3. . For deleting elements from list, dictionaries use `del var_name`



## Formatting String
```python
first = "Sandeep"
last = "Dewangan"
format_name = f"{first} Kumar {last}"
print(format_name)
```
### Underscore in numbers
* Use underscores  to make large numbers more readable.
```python
a = 40_00_000
```

## Dictionary
* Dictionary { } holds value as key, value pair.

**Accessing Values with Keys**
To Get Values with custom error message use `get` function to get key.
`mydict.get('college', 'No such key exits.')`

**Looping through Dict.**
```python
for key, value in mydict.items():
    print(key)
```
Looping through keys  `mydict.keys()`
Looping through values`mydict.values()`

## Typecasting
They all are functions.

`int()`
`str()`
`float()`

## While loop
```python
# remove all occurances of cat
pets = ['dog', 'cat', 'elephant', 'deer', 'cat']
while 'cat' in pets:
    pets.remove('cat')
```
## Functions
**Arbitrary number of arguments**
```python
def fruits(*names):
    print(names) # ('grapes', 'apple', 'bananana')
    
fruits('grapes', 'apple', 'bananana')
```
**Arbitrary keyword arguments**
```python
def user(id, **info):
	# info type is of dict.
    
user(1001, name='sandeep', college='bit', city ='raipur')
```
## Module
Store functions in a separate file called a `module` and then import that module into main program.
**Imports all functions inside module**
STEP 01: Create pizza.py 
```python
def make_pizza(type, **others):
	#TODO
```
STEP 02: Import module
```python
import pizza
pizza.make_pizza()
```
**Import specific function**
`from pizza import func1, func2...`

**Aliasing module**
`import pizza as pz`

**Aliasing function**
`from pizza import make_pizza as mp`

**Importing all function from a module**
`from pizza import *`

## Classes
`__init__() method` - Python’s default method name
```python
class Dog:
    """ A simple dog class to show dog actions """

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        print(f"{self.name} barks loud")

    def roll_over(self):
        print("Roll over my baby")


toto = Dog('Toto', 5)
toto.bark() # self arg. is automatically passed
```
### Inheritance
```python
class Car:
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def get_car_details(self):
        print(f"{self.make} makes {self.model}")

class ElectricCar(Car):
    def __init__(self, make, model):
        """
        Initialize attributes of the parent class.
        Then initialize attributes specific to an electric car.
        """
        super().__init__(make, model)
        self.battery_size = 75
```
## Reading and Writing File
**Reading entire file**
The keyword `with` closes the file once access to it is no longer needed.
```python
with open('data.txt') as obj:
    contents = obj.read()

print(contents)
```

**Reading line by line**
```python
with open('data.txt') as obj:
    for line in obj:
        print(line)
```
* `obj.readlines()` - makes the list of lines

**Writing to a file**

* Read 'r'
* Write 'w'
* Append 'a'
```python
with open('program.txt', 'w') as obj:
    obj.write("I Love Programming")
```
## Exception
**try-catch-else**
```python
try:
    res = a / b
except Exception:
    print("Divide error")
else:
    # if exception occurs else block donot execute
    print(res)
```
**Failing silently**
```python
try:
    res = a / b
except Exception:
    pass
```

## JSON
**Store data**
```python
import json

names = ['sandeep', 'khushbu', 'rinky', 'annu', 'zozo']
with open('program.json', 'w') as f:
    json.dump(names, f)
```
**Load data**
```python
with open('program.json', 'r') as f:
    data = json.load(f)
print(data)
```

    
