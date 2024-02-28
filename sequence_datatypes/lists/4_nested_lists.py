"""
Nested list in python is a list that contains other lists or iterables as its elements.
Essentially, you have lists within lists, forming a multi-dimensional structure. It could
more or less represent 2 dimensional arrays as in C or C++.
Nested lists are can be consisted of only lists or different datatypes along with lists.
"""
# Creating a nested list:
nested_list1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]    # list containing only lists
nested_list2 = [1, 2, 3, [4, 5, 6], 7, 8, 9]        # list containing list and integers.

"""
Items in a nested list can be accessed using 2 indexes. 1st for the outer list and the
2nd for the inner list.
"""
print(nested_list1[0][1])
print(nested_list2[3][2])
"""
Elements in a nested list can be modified the same way as a normal one dimensional list.
"""
nested_list2[3][2] = 11
print(nested_list2)
"""
To iterate through the items in the outer and inner lists we can use nested loops.
"""
for list in nested_list1:   # loop to print items in outer list
    print(list)
    for item in list:       # loop to print items in inner list
        print(item)

"""
We can get the length of a nested list using the built-in function len.
"""

print(len(nested_list1))
print(len(nested_list2))

"""
Nested lists can also be created using list comprehensions. However that part will be
covered under comprehensions.
"""