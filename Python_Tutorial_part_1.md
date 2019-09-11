# Python

## What is python?
Python is a generic programming language! You can script with it or build entire applications. It's a *glue* language in that it works very well for transferring data between systems. The docs are available at https://docs.python.org/3/


## Where do you get python?
Python can be downloaded from https://www.python.org/downloads/

Once you have downloaded python and installed it, you can run the interpreter by typing ```python``` in an cmd or terminal. You might have to restart you computer before you can use python from the command line.

```shell
PS C:\> python
Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 22:22:05) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> print("Hello World")
Hello World
>>>       
```

If you cannot install or run Python 3 locally, you can still follow this tutorial via repl.it at https://repl.it/languages/python3


## What is Legacy Python and what is Python 3?
Python was created in the 1980s. Since then it has gone through many iterations. Currently, there are two major versions: *Legacy* Python (Python 2) or  and Python 3. The Current version as of 5 Sept is 3.7. Version 3.8 is due by the end of the year.

Legacy Python and Python 3 are very similar, but have a few breaking changes between them making code from one incompatible with the other. 


## Running Python

Python can be used in a few different ways. The code can be written and executed directly in a terminal by typing ```python```.
That will start the interactive interpreter.
```shell
PS C:\> python
Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 22:22:05) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> 
```
From there, you can type in and execute python commands line by line, for example, if you type in  ```print("Hello There!")``` and press enter, you will see the output printed in the console below yor command.

Python can also be run with files as input. Writing scripts and executing them the python command can be much more efficient than typing the commands into the interpreter it self. 

Try running the below code in your terminal:

```powershell
PS D:\Workspace\Python\Python_Tutorial> python .\python_example_1.py
Hello again!
1 + 5 = 6
PS D:\Workspace\Python\Python_Tutorial> 
```

## What are the structures of a python application?

Python scripts and applications have a few major structures that found commonly in programing languages.
- Classes - Everything is an object, the class is the type of object.
- Functions - Functions are actions, they do something... they are also objects.
- Variables - Variables store and reference data.

We will be focusing specifically on functions and variables. 

### Functions and Variables
Functions are actions! They do something or make something happen. One function you have seen at this point is the ```print``` function. It takes some input, in the cases before, a string or text, and writes it to the console!

Functions are defined with the def keyword. Once the function is defined, it can be called later in the code. 

```python
# Function Definition
def prints_hello():
    print("Hello")

# Function Call
prints_hello()
```

The example above can be run with python ./scripts/run_some_function.py

Functions should be:
- Short, if it does not fit on the screen, it's probably too large.
- The function name should describe what the function does.
- Function names should be lowercase with underscores between words.

#### Functions can accept inputs as arguments

```python
# Adds the two numbers provided, x and y
def add_two_numbers(x, y):
    return x + y

print(add_two_numbers(2, 4))
```

#### Arguments can also be explicitly named

```python
print(add_two_numbers(y = 2, x = 4))
```

If arguments are keyed, then positional arguments can not come after the keyed arguments.

```python
# Okay
print(add_two_numbers(4, y = 2))

# Will fail
print(add_two_numbers(y = 2, 4))
```

If you pass an incorrect type to a function, an exception will be raised. 

```python
# Okay, but not the name of the functions should changed if strings will be passed to the function. 
print(add_two_numbers("Hello, ", "World"))

# Will fail
print(add_two_numbers(2, "World"))
```

If you want to explicitly specify the type, you can specify the type in the arguments.
The functions can still be called with different types than specified, but editors like vscode or Pycharm will highlight functions where you are calling a function with the incorrect types.
```python
# Adds the two numbers provided, x and y
def add_two_numbers(x: int, y: int) -> int:
    return x + y

# Join two strings together
def join_two_strings(x: str, y: str) -> str:
    return x + y

```

#### To retrieve the return value of a function, the *return* value is used. 

```python
# Adds the two numbers provided, x and y
def add_two_numbers(x: int, y: int) -> int:
    return x + y # Returns the sum of the two numbers provided.

# Join two strings together
def join_two_strings(x: str, y: str) -> str:
    return x + y # returns the combined string 

```


### Variables

Variables are used to hold values. Variables can also be passed as function arguments and they can store the return values of functions. 

```python
my_value = "Hello"
my_other_value = ", world"

my_third_value = join_two_strings(my_value, my_other_value)

```

Typically, variables that represent some constant are CAPITALIZED. This is a style used to tell the developer that a value should not be changed after used, but the language does not enforce it!

```python

NEVER_CHANGING = "My constant value!"
my_other_value = "This one can change!"

the_output = join_two_strings(my_value, my_other_value)

```


## Importing Packages and Modules

One of the most powerful features of python is the huge number of libraries, packages, and modules available. Now we will look at importing a module to print dates. 

```python

# Here we are importing the datetime module. This module includes functions and classes to handle working with dates. 
import datetime

the_current_date_and_time = datetime.datetime.now().strftime("%b %d %Y %H:%M:%S")

print(the_current_date_and_time)

```

## Classes

Classes are the building blocks and structures of objects in python. 

```python
class Dog:
    name = "Rufus"

    def bark(cls):
        print("WOOF!")
    
    def get_name(self):
        print(f"Dogs name is {self.name}")
```

Classes can contain both functions and variables. Depending on the arguments passed to the class methods, the may behave differently. 

## Bringing it all together with a Simple Webserver

```python

import http.server
import socketserver
import datetime

PORT = 8080
Handler = http.server.SimpleHTTPRequestHandler

my_server = socketserver.TCPServer(("", PORT), Handler):

print(f"Your server has started on port {PORT} at {datetime.datetime.now().strftime("%b %d %Y %H:%M:%S")}")

my_server.serve_forever()
```



[Main Tutorial Page](README.md)