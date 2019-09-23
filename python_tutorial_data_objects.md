# Intro to commonly used Python data objects

In this tutorial, I will go over the core data storage objects in Python I use in python the most, the list and the dictionary. There are many built in data structures in Python, and the full list can be fount in the Docs at [https://docs.python.org/3/](https://docs.python.org/3/)


## Lists
Python lists are ordered collections of objects. 

They can be created directly with brackets, [ ]. The example below creates an empty list.
```python 
my_list = []
```

The objects in a python list no not all need to be the same type, and they can be created with initial items.

```python 
my_list_with_initial_values = ["value_1", 2, 3.0]
```

Iterating through lists can be done in a few ways:

```python
a_list_of_values = ["foo", "bar", 5.99]
for item in a_list_of_values:
    print(item)
```

```python
a_list_of_values = ["foo", "bar", 5.99]
for index, value in enumerate(a_list_of_values):
    print(a_list_of_values[index])
```

```python
a_list_of_values = ["foo", "bar", 5.99]
for index in range(0, len(a_list_of_values)):
    print(a_list_of_values[index])
```
Output of the above scripts:
```shell
foo
bar
5.99
```


Lists also have a built in way to retrieve sub-lists of a list, the slice operator.

```python
a_list_of_values = [1, 2, 3, 4]
print(a_list_of_values)
print("A subset of the above list!")
print(a_list_of_values[1:3])
```

```shell
[1, 2, 3, 4]
A subset of the above list!
[2, 3]
```

Returning the reverse of a list can also be done with the slice operator.

```python
a_list_of_values = [1, 2, 3, 4]
print(a_list_of_values)
print("A reversed version of the above list!")
print(a_list_of_values[::-1])
```

```shell
[1, 2, 3, 4]
A reversed version of the above list!
[4, 3, 2, 1]
```

The slice operator uses a ```start:stop:step``` format to define how the returned list is created from the source list. For example, using the slice operator with ```::-1``` reverses it, but using ```::-2``` reverses it, and iterates through the resulting list with a step of 2. 


```python
a_list_of_values = [1, 2, 3, 4]
print(a_list_of_values)
print("A reversed version of the above list!")
print(a_list_of_values[::-1])
print("A reversed version of the above list with step -2")
print(a_list_of_values[::-2])
```

```shell
[1, 2, 3, 4]
A reversed version of the above list!
[4, 3, 2, 1]
A reversed version of the above list with step -2
[4, 2]
```

If the step parameter is not passed, then it defaults to 1.

### List Compositions

One of the most powerful features in my opinion for the List object in python is the *List Composition*.


List compositions are a way of creating or *composing* lists from other lists, or list like objects. Think of them as a way of pulling items of one list into another based on some condition. For each number in a list of numbers, if it is odd, add it to my_odd_list, or if the values is a string, add it to my_string_list.

```python 
list_of_numbers = [1, 2, 3, 4, 5, 6, 7]
print(list_of_numbers)

# Select the number from the list of numbers if the number is odd.
my_odd_numbers = [number for number in list_of_numbers if number % 2 != 0 ]
print(my_odd_numbers)
```

Output:
```shell
[1, 2, 3, 4, 5, 6, 7]
[1, 3, 5, 7]
```

## Dictionaries

Dictionaries aka Dicts, are probably the most important data structure in Python. They are sets of key-value pairs, that store data.

A unique key in a *set* of keys maps to a specific value in a *list* of object values.

```python

a_dict_of_ids_to_names = {
    "0123A": "Bob",
    "0123B": "Alice",
    "0123C": "John",
}

print(a_dict_of_ids_to_names)
```

```shell
{'0123A': 'Bob', '0123B': 'Alice', '0123C': 'John'}
```

Dictionaries have many different ways of accessing and manipulating the data contained.

```python
a_dict = {}

# Add a value to a_dict
print(a_dict)
a_dict["new_value"] = "fizz"
print(a_dict)
a_dict["new_value_2"] = "buzz"
print(a_dict)

# Remove a value
del a_dict["new_value"]
print(a_dict)
```


Output
```shell
{}
{'new_value': 'fizz'}
{'new_value': 'fizz', 'new_value_2': 'buzz'}
{'new_value_2': 'buzz'}
```

You can also access the list of keys with the *keys()* method, the list of values with the *values()* method, and the list of items with the *items()* method.

```python
a_dict_of_ids_to_names = {
    "0123A": "Bob",
    "0123B": "Alice",
    "0123C": "John",
}

print("Key List: ", a_dict_of_ids_to_names.keys())
print("Value List: ", a_dict_of_ids_to_names.values())
print("Item List: ", a_dict_of_ids_to_names.items())
```

Output
```shell
Key List:  dict_keys(['0123A', '0123B', '0123C'])
Value List:  dict_values(['Bob', 'Alice', 'John'])
Item List:  dict_items([('0123A', 'Bob'), ('0123B', 'Alice'), ('0123C', 'John')])
```


### Using List Comprehensions with Dictionaries.

Lists and dictionaries are very useful by them selves. But when used together, compositions can be used to filter data.


```python
list_of_people = [
    {
        "name": "Luke Skywalker",
        "occupation": "Jedi",
        "alignment": "good",
        "homeworld": "Tatooine",
        "survey_response": 4
    },
    {
        "name": "Tony Stark",
        "occupation": "Avenger",
        "alignment": "good",
        "survey_response": 2
    },
    {
        "name": "Sauron",
        "occupation": "Lord of the Rings",
        "alignment": "evil",
        "homeworld": "Middle Earth",
        "survey_response": 1
    },
]

print(list_of_people)

```


```python
# I just want to print out the people. 
for person in list_of_people:
    print(f"{person['name']} is a {person['occupation']}")
```

```python
# I want to print out the good guys. 
for person in [character for character in list_of_people if character["alignment"] == "good"]:
    print(f"{person['name']} is a {person['occupation']}")
```

```python
# I want to get where they are from. 
for person in [character for character in list_of_people if "homeworld" in character.keys()]:
    print(f"{person['name']} is from {person['homeworld']}")
```





[Main Tutorial Page](README.md)