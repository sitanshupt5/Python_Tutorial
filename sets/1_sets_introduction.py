"""
In Python, a set is an unordered collection of unique elements. It is defined by enclosing a
comma-separated list of elements within curly braces {}. Sets are useful when you want to store
multiple items without caring about the order or duplicates, and they provide various set
operations.
Python sets are very similar to dictionary keys. They both do not allow any duplicates.
However, the only difference between python sets and dictionary keys is that since Python
3.7 dictionary keys are ordered. On the other hand there is no guarantee of order in the
python sets.
Sets are limited in certain ways like there's no way to access individual elements in a set.
Sets have several characteristics that distinguish them from other data types. Here are the
key characteristics of sets in python:
1.  Unordered: Sets are unordered collections of unique elements. Unlike sequences like
    lists or tuples, there is no specific order maintained among the elements in a set. This
    means sets do not support indexing or slicing.
2.  Mutable: Sets are mutable, meaning we can add and remove elements after the sets is
    created. However, individual elements within the sets must be immutable (e.g. integer,
    strings or tuples). Meaning you cannot create a set of lists.
3.  No Duplicates: Sets do not allow duplicate elements. Incase we add an element that is
    already present in the set, it won't be added again and the set will remain unchanged.
4.  Dynamic Size: Sets can dynamically grow or shrink in size as elements are added or removed.
    There is no need to specify the size when creating a set.
Let's take a look at how we can create a set:
"""
# CREATING A SET USING CURLY BRACES '{}':
farm_animals = {"cow", "sheep", "goat", "horse", "hen", "dogs"}
# Output: {'horse', 'goat', 'cow', 'dogs', 'sheep', 'hen'}
print(farm_animals)
"""
It is important to note when creating a set with curly braces is that there should be 
atleast one comma to distinguish it from an empty dictionary. It causes a potential ambiguity 
with using curly braces for a single element because, by default, Python interprets it as a 
dictionary with a key-value pair. Hence, a set with a single element must be followed by a 
comma.
"""
animal = {"lion", }  # Output: {'lion'}
print(animal)
"""
We can also create empty sets using the curly braces. Since, sets are mutable we can add 
elements to the empty set later on.
"""
empty_set = {}
print(empty_set)    # Output: {}

# CREATING A SET USING set() CONSTRUCTOR:
wild_animals = set(["dogs", "wolves", "lions", "tigers", "horses", "cobras"])
print(wild_animals) # Output: {'tigers', 'wolves', 'cobras', 'horses', 'dogs', 'lions'}
"""
set() constructor can also be used to convert an existing iterable like list or tuple into a 
set. In the process any duplicate element in the list or tuple will be removed.
"""
list1 = ["Sitanshu", "Shivam", "Karthik", "Shivam"]
testing_set = set(list1)
testing_set2 = set({1, 2, 3, 4, 5})
print(testing_set)      # Output: {'Shivam', 'Sitanshu', 'Karthik'}
print(testing_set2)     # Output: {1, 2, 3, 4, 5}

"""
We can also create empty sets using the set() constructor:
"""
empty_set2 = set()
print(empty_set2)   # Output: set()
"""
In the above case in line 60 the output is printed as 'set()' instead of '{}' so as to 
distinguish it from an empty dictionary.
It is important to note that creating a set is quicker using the braces '{}' than using the 
set() constructor.
"""
