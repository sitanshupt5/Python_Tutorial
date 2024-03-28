"""
This module aims to cover the basic operations that can be carried out on the dictionaries
in python. For this module we will use the dictionary called vehicles.
"""
vehicles = {
    'dream': "Honda 250T",
    'roadster': 'BMW R1100',
    'er5': 'Kawasaki ER5',
    'cam-am': 'Bombardier Can-Am 250',
    'virago': 'Yamaha XV250',
    'tenere': 'Yamaha XT650',
    'jimny': 'Suzuki Jimny 1.5',
    'fiesta': 'Ford Fiesta Ghia 1.4'
}

# APPENDING ITEMS TO THE DICTIONARY:-

#   1. Direct Assignment by creating a new index and assigning value:
vehicles["bullet"] = "RE Bullet 350"
vehicles["shotgun"] = "RE Shotgun 650"
vehicles["meteor"] = "RE Super Meteor 650"

#   2. Using the update() method:
bike = {"himalayan": "RE Himalayan"}
vehicles.update(bike)

print("#"*95)
for key in vehicles:
    print(f"{key}: {vehicles.get(key)}")

#   3. Using the setdefault() method:
my_dict = {'a': 1, 'b': 4, 'c': 3}
x = my_dict.setdefault('d', 5)
print(my_dict)
"""
The setdefault() method is a dictionary method that allows you to retrieve the value of a 
key in a dictionary. If the key is present, it returns the corresponding value; if the key is 
not present, it inserts the key with a specified default value and returns that value.
"""


# UPDATING ITEMS IN THE DICTIONARY:-
"""
Values in a dictionary item can be updated against the keyname. As long as the keyname in 
the index matches an existing index key, the value against the index will be updated. This 
can be achieved through the following methods.
"""

#   1. Update through direct assignment using the index value:
vehicles["virago"] = "Yamaha XV535"


#   2. Update using the update() method:
vehicle = {"bullet": "RE Bullet Classic 350"}
vehicles.update(vehicle)

#   3. Using the setdefault() method:
vehicles[porche] = vehicles.setdefault('porche', 'Porche Carrera GT')
"""
This feature of setdefault() is especially useful when updating quantities. For example:
ingredients[almonds] = ingredients.setdefault('almonds', 0) + amount
Where,
ingredients is a dictionary containing item names as keys and their quantities as values.
almonds is a key name in the dictionary
amount is the quantity.
The line of dummy code in line 61 does 2 things. First, if the dictionary 'ingredients' does 
not have an entry for 'almonds', then it creates a new item in the dictionary with key name as 
'almonds' and assigns default value as 0. It then returns the value of the newly created 
item in the dictionary that is '0'. Incase, and item with keyname 'almonds' already exists 
in the dictionary ingredients in that case the setdefault method simply returns the value of 
that item. Finally, the initial value of the item with key 'almonds' is added to the amount 
and the value is reassigned to the same item.  
"""

"""
Note: Update method takes a dictionary as an argument. As long the keys in the dictionary 
match the keys in the existing dictionary the values in the existing dictionary against the 
corresponding indices will be updated. If the keyname in the new dictionary does not match 
any in the existing dictionary a new item is added to the existing dictionary with the key 
value pair.
"""

print("#"*95)
for key in vehicles:
    print(f"{key}: {vehicles.get(key)}")


# REMOVING ITEMS FROM THE DICTIONARY:-
"""
This can be achieved in 2 ways:
1.  By using the 'del' keyword.
2.  By using the pop() method.
Let's take a look at both of them below:
"""
#   1. By using the 'del' keyword:
del vehicles["himalayan"]
print("#"*95)
for key in vehicles:
    print(f"{key}: {vehicles.get(key)}")

"""
The code in line 68 would remove the item with key name "himalayan" from the dictionary 
vehicles.
The only issue we face in this case is that, if the key "himalayan" is not present in the 
dictionary vehicles then this will lead the program to crash. Which is may or may not be 
ideal based on the requirement.
"""
#   2. By using the pop() method:
vehicles.pop("bullet")
"""
The code fragment in line 81 will remove the item with key name "bullet" from the dictionary 
vehicles.
Passing an index to the pop() method that does not exist in the dictionary would lead to the
same outcome as using the 'del' keyword i.e the program will crash. However, there is way to
avoid this. For this we need to understand how the pop() method operates.
The pop() method in Python is used to remove and return the value associated with a 
specified key from a dictionary. The general syntax of the pop() method is as follows:
value = dictionary.pop(key, default_value)
In the above syntax:
key: The index of the item in the dictionary that needs to be removed.
default_value: The value that is to be returned if the index is not found in the dictionary.

Since, the pop() needs to return the value of the item that is removed, Incase the item is 
not found due to invalid key, it returns the default value. If the default value is not 
passed as the argument to the function, then the program crashes and produces a 'KeyError'.
Please refer below:
"""
value = vehicles.pop("classic", "Item not found.")
print(value)

# CHECKING PRESENCE OF KEY OR VALUE IN THE DICTIONARY:-
"""
Please refer to the following code fragment.
"""
computer_parts = {
    "1": "monitor",
    "2": "keyboard",
    "3": "mouse",
    "4": "printer",
    "5": "hdmi cable",
    "6": "dvd drive"
}

print("#"*95)
for i in range(1, 10):
    if str(i) in computer_parts:
        print(computer_parts[str(i)])

"""
In the above code fragment the 'in' keyword by default checks for the keys in case of 
dictionary. Hence, the value on the left is searched for among the keys in the dictionary.
So "if str(i) in computer_parts" is same as "if str(i) in computer_parts.keys()"
"""
