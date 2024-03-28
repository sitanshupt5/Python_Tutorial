"""
Serialization is the process of converting an object's state or data, typically in the form of
a data structure or object, into a format that can be easily stored, transmitted, or
reconstructed later. The primary purpose of serialization is to enable the preservation of an
object's state so that it can be reconstructed in the same or another environment.
JSON is a lightweight and human-readable data interchange format. It is widely used for
serialization due to its simplicity and ease of parsing. Objects are converted into a
JSON-formatted string using key-value pairs.
In order to serialize json data we will need to import the json module in python. We are
going to be using 2 sets of data that we will be importing from the 'json_data.py' module.
"""
import json
from json_data import languages, orders

"""
In order to create a json file from our existing data we need to use the json.dump() method.
The dump() method takes 2 arguments. First, the data that is to be written in to the file 
and second the file itself.
It takes basic data like dictionaries, lists etc as arguments and converts them into a json 
format and then stores it in to file passed in the argument.
It is important to note that this method can serialize almost all our basic data types and 
data structures. Example: Imagine we have a list of tuples. Since json format does not 
support tuples, the dump() method converts the tuples into lists and then serializes them.
Please refer below example:
"""

with open("orders.json", "w", encoding="utf-8") as testfile:
    json.dump(orders, testfile)

with open("languages.json", "w", encoding="utf-8") as testfile:
    json.dump(languages, testfile)

"""
Reading a json file is as easy as reading any other text file. In order to read the data 
from a json file we need to use the json.load() method.The load() method returns data in the
form of lists, dicts etc which can then be stored or used. Please refer the below examples.
"""

with open("orders.json", "r", encoding="utf-8") as file:
    data1 = json.load(file)

with open("languages.json", "r", encoding="utf-8") as file:
    data2 = json.load(file)

print(data1)
print(type(data1))  # Output: <class 'dict'>
print("#"*95)
print(data2)
print(type(data2))  # Output: <class 'list'>
