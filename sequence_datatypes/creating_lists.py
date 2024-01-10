"""
Lists in python can be created using many different ways. For example they can be newly
created or they can be derived from existing lists. Refer below for all the different ways
in which new lists can be created:
"""
# Standard method:
new_list = [1, 2, 3, 4, 5]
print(list)

# Using append method:
empty_list = []
empty_list.append(1)
empty_list.append(2)
empty_list.append(3)
empty_list.append(4)
empty_list.append(5)
print(empty_list)

# Using Nested Lists:
nested_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(nested_list)

# Using range function:
numbers = list(range(2, 10, 2))
print(numbers)

"""
There are others ways of creating lists such as the using list comprehensions and list 
constructors. but they will be covered later.
"""

"""
Lists can be derived in python using the following methods. Keep in my for all the below 
methods there has to be an existing list which could be used to derive a new list.
"""
# Using the sorted function:
numbers = [3, 1, 4, 1, 5, 9]
sorted_numbers = sorted(numbers)

# Using the extend method:
list1 = [1, 2, 3]
list2 = [4, 5, 6]
list1.extend(list2)
print(list1)

# Using slicing:
list3 = numbers[1:4]
print(list3)

"""
There are other ways of generating lists from existing lists such as by using filter()
function, map() functions, list comprehensions and generators. These will be covered later.
"""