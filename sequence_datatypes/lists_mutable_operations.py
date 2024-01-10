"""
There are a few operations unique to mutable sequences in python, these are:-
del, slice, append(), clear(), copy(), insert(), pop(), remove(), reverse().
Refer to the below examples:
"""
grocery_list = ["rice", "salt", "vegetables", "soap", "toothpaste"]
another_grocery_list = grocery_list
"""
In the above 2 initializations both variable names are bound to the same object, i.e.
["rice", "salt", "vegetables", "soap", "toothpaste"]. The variable names are just names
bound to these objects. This can be prooved using the id function in python.
"""
print(grocery_list)
print(id(grocery_list))
print(another_grocery_list)
print(id(another_grocery_list))

""" 
We will see that ids for both the variable names are same. This is because both variables
are just names bound to the same object. Hence, any mutations to the object can be referenced
through both the variables.
"""
# append() function: Adds element to the end of the sequence.
grocery_list.append("wheat")
print(grocery_list)
print(id(grocery_list))
print(another_grocery_list)
print(id(another_grocery_list))
"""
For the results from line 24 to 28 it can be seen that changes referenced to the object
through variable name grocery_list are also reflected by the variable another_grocery_list.
Also, the ids incase of both the variables are same. Hence, the object gets mutated and
all its references reflect the changes.
This behavior will stand true for all mutations to the object. Please refer to the
following operations.
"""
# remove(x) function: removes the first occurence of element passed in the argument.
another_grocery_list.remove("wheat")
print(another_grocery_list)

# insert(i,x) function: inserts element at the specific index mentioned in the argument.
grocery_list.insert(3, "wheat")
print(grocery_list)

# pop(i) function: removes and returns element from sequence. Default removed last index.
grocery_list.pop(3) # value at index 3 is removed.
print(grocery_list)
grocery_list.pop()  # value at last index is removed.
print(grocery_list)

# copy() function: creates an entirely new copy of a sequence object.
new_list = grocery_list.copy()
print(new_list)
"""
It is to be noted that the object referenced by variable grocery_list and object referenced
by new list are different although they may have the same values. This is because copy()
function creates a new object and copies the values. Hence, any changes to object 
referenced by grocery_list cannot be referenced by new_list. 
It can be proved that grocery_list and new_list do not reference the same object using the
keyword is. Refer below
"""
print(new_list is grocery_list)  # The result will be false.

# clear() function: used to empty a sequence by removing all the data.
grocery_list.clear()
print(grocery_list)

# del keyword: Used on slices to remove a particular slice from a sequence.
print(new_list[1:3])
del new_list[1:3]
print(new_list)