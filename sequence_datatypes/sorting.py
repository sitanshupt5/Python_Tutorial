"""
Sorting means to arrange the elements in certain order, maybe ascending or descending.
Python provides 2 ways to sort the elements of a list. 1st method is to use the sort()
function for lists. 2nd method is to use the python built in function sorted.
Please refer to the below examples:
"""
players = ["rohit", "gill", "kohli", "iyer", "rahul", "pandya",
           "bumrah", "shami", "jadeja", "yadav" ]

longitudes = [7.32, 54.03, 12.11, 2.3, 111.89, 3.4]

# using sort() function:
players.sort()
print(players)

# using sorted() function:
sorted_longitudes = sorted(longitudes)
print(sorted_longitudes)

# It is also possible to sort in reverse order
players.sort(reverse=True)
print(players)

print(sorted(longitudes, reverse=True))

"""
The difference between sort() and sorted functions is that sort() is an in-place sorting
function. Meaning, sort() function does not create a copy of the list. Instead, it just
rearranges the elements in the same list. Hence, sort() function does not have a return type.
On the other hand sorted is an in- built function and creates a copy list to to sort and then
returns the sorted list which is an entirely different object.
In cases of strings where there is a mix of upper case and lower case characters the
precedence goes to the upper case characters. Meaning, first the upper case characters are
sorted and then the lower case characters. Please refer below.
"""
names = ["Graham",
         "John",
         "terry",
         "eric",
         "Terry",
         "michael"
         ]
pangram = "The quick brown fox jumps over the lazy dog"
list2 = ["Graham",
         "John",
         "terry",
         "eric",
         "Terry",
         "michael"
         ]
line2 = "My wife's name is Srujaya Dash"
names.sort()
print(names)

# sort() function is only unique to lists. It cannot be used for other sequences.
# for other sequences python inbuilt function sorted() has to be used.
print(sorted(pangram))
# sorted() function doesn't just work on other types of sequences but also on lists.
print(sorted(list2))

"""
If we want to sort irrespective of the case of the string then we have to pass str.casefold
as argument. Please refer below.
"""
list2.sort(key=str.casefold)
print(list2)
print(sorted(pangram, key=str.casefold))