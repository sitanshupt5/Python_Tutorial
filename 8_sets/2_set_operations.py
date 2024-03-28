"""
Sets allow a range of operations to be conducted. Following are the operations that can be
conducted on sets:
"""
import copy

# ADDING ELEMENTS:
"""
In Python we can add elements to an existing set using the add() or update(). Generally, 
the add() method is used when only a single element needs to be added at a time to the set. On
the other hand, the update method is used when we need to add multiple elements in one go to an
existing set. Please refer to the following examples:
"""
naruto_chars = {"naruto", "sasuke", "sakura"}

#   1. Using the add() method:
naruto_chars.add("kakashi")
print(naruto_chars)
# Output: {'sasuke', 'kakashi', 'naruto', 'sakura'}

#   2. Using the update() method:
naruto_chars.update({"shikamaru", "ino", "choji"})
"""
The update() method accepts an iterable. Hence, it could be a set or a list or a tuple. 
Please refer below:
"""
naruto_chars.update(["jiraiya", "tsunade", "orichimaru"])  # passing a list in update() method
naruto_chars.update(("neji", "tenten", "lee"))  # passing a tuple in update method.
print(naruto_chars)
# Output: {'lee', 'sakura', 'tenten', 'sasuke', 'kakashi', 'shikamaru', 'tsunade', 'naruto', 'choji', 'jiraiya', 'ino', 'neji', 'orichimaru'}

# REMOVING ELEMENTS:
"""
In Python, sets provide several methods for removing elements, including discard(), pop()
and remove(). Please refer below illustrations for more details: 
"""
#   1. discard() method:
"""
The discard() method removes the element that is passed in the argument if it is present in 
the set. Please refer below:
"""
print("#" * 95)
naruto_chars.add("sai")
naruto_chars.discard("sai")
print(naruto_chars)
# Output: {'lee', 'sakura', 'tenten', 'sasuke', 'kakashi', 'shikamaru', 'tsunade', 'naruto', 'choji', 'jiraiya', 'ino', 'neji', 'orichimaru'}
"""
In case the element passed as argument to the discard method is not present in the set, 
no error will be returned. Please refer below:
"""
naruto_chars.discard("sai")
print(naruto_chars)
# Output: {'lee', 'sakura', 'tenten', 'sasuke', 'kakashi', 'shikamaru', 'tsunade', 'naruto', 'choji', 'jiraiya', 'ino', 'neji', 'orichimaru'}

#   2. remove() method:
"""
The remove() method in sets removes the specific element passed in the argument just like 
the discard() method.
"""
print("#" * 95)
naruto_chars.remove("sakura")
print(naruto_chars)
# Output: {'lee', 'tenten', 'sasuke', 'kakashi', 'shikamaru', 'tsunade', 'naruto', 'choji', 'jiraiya', 'ino', 'neji', 'orichimaru'}
"""
However, unlike the discard() method, the remove() method raises a KeyError in case the 
element is not present in the set.
"""

#   3. pop() method:
"""
The pop method() removes and returns a specific element from a set. Since, sets are 
unordered, the specific element removed is not guaranteed. Any arbitrary element could be 
removed.
"""
print("#" * 95)
character = naruto_chars.pop()
print(character)
# Output: lee
print(naruto_chars)
# Output: {'tenten', 'sasuke', 'kakashi', 'shikamaru', 'tsunade', 'naruto', 'choji', 'jiraiya', 'ino', 'neji', 'orichimaru'}
"""
However, if the set is empty and there is no element to remove or return, the pop() method 
raises a KeyError. The pop() method provides better performance than the remove() and 
discard() method as it removes the first arbitrary element it finds in the set.
"""


# SET MEMBERSHIP:
"""
In Python, you can check for membership in a set using the in keyword. This allows you to 
determine whether a specific element is present in the set. Please refer to the following 
example:
"""
demon_slayer_chars = {"tanjiro", "nezuko", "inosuke", "zenitsu"}
main_chars = {"naruto", "luffy", "ichigo", "tanjiro", "goku"}
print("#" * 95)
for char in main_chars:
    if char in demon_slayer_chars:
        print(f"{char} is the main character in demon slayer anime.")
    else:
        print(f"{char} is not the main character of demon slayer anime.")
"""
The output of the above code fragment is as follows:
tanjiro is the main character in demon slayer anime.
goku is not the main character of demon slayer anime.
luffy is not the main character of demon slayer anime.
ichigo is not the main character of demon slayer anime.
naruto is not the main character of demon slayer anime.

In the above code fragment we are checking the membership of data using the 'in' keyword for 
'demon_slayer_chars' set. For sets, the in operation has an average time complexity of O(1),
assuming a good hash function. This means that the time it takes to check for membership in a 
set is generally constant and does not depend on the size of the set.
On the other hand the time complexity of the 'in' operation in lists and tuples increases as
the size of the data structure increases.
"""
# SET UNION:
"""
Union of 2 sets is a set containing all the unique elements from both the sets. This can be 
achieved using the union() method or the '|' operator. Union basically means an 'OR' operation.
One important thing to note is if an element is present in both sets then the union set will
contain only one occurence, since sets do not allow duplicates. Please refer below:
"""
print("#"*95)
team_hiruzen = {"jiraiya", "tsunade", "orochimaru", "hiruzen"}
team_jiraiya = {"minato", "jiraiya"}
team_minato = {"minato", "kakashi", "obito", "rin"}
# Using the union() method:
union_set1 = team_hiruzen.union(team_jiraiya)
print(union_set1)   # Output: {'tsunade', 'minato', 'jiraiya', 'orochimaru', 'hiruzen'}
# Using the '|' operator:
union_set2 = team_jiraiya | team_minato
print(union_set2)   # Output: {'kakashi', 'minato', 'jiraiya', 'obito', 'rin'}


# SET INTERSECTION:
"""
The intersection of 2 sets is an 'AND' operation. Hence, the result of intersection of 2 
sets is the common elements in both the sets. This can be achieved either by using the 
'&' operator or the intersection() method. Please refer below:
"""
print("#"*95)
# Using the intersection() method:
intersection_set1 = team_hiruzen.intersection(team_jiraiya)
print(intersection_set1)        # Output: {'jiraiya'}

# Using the '&' operator:
intersection_set2 = team_jiraiya.intersection(team_minato)
print(intersection_set2)        # Output: {'minato'}


# SET DIFFERENCE:
"""
Set difference operation on 2 sets returns the elements that are present in the first set 
but not in the second set. This operation can be performed using the difference() method or 
'-' operator.
"""
print("#"*95)
# Using the difference() method:
difference_set1 = team_hiruzen.difference(team_jiraiya)
print(difference_set1)      # Output: {'tsunade', 'orochimaru', 'hiruzen'}

# Using the '-' operator:
difference_set2 = team_jiraiya - team_minato
print(difference_set2)      # Output: {'jiraiya'}


# SET SYMMETRIC DIFFERENCE:
"""
Symmetric difference operation on 2 sets returns the elements that are present in one set 
but not in the other.This operation can be performed using the symmetric_difference() or the
'^' operator.
"""
print("#"*95)
# Using the symmetric_difference() method:
symmetric_difference_set1 = team_hiruzen.symmetric_difference(team_jiraiya)
print(symmetric_difference_set1)    # Output: {'tsunade', 'orochimaru', 'hiruzen', 'minato'}

# Using the '^' operator:
symmetric_difference_set2 = team_jiraiya ^ team_minato
print(symmetric_difference_set2)    # Output: {'kakashi', 'rin', 'jiraiya', 'obito'}

# SUBSETS:
"""
Set1 is the subset of set2 when set2 contains all the elements present in set1 along with 
other element. This can be checked using the issubset() method. Please refer below:
"""
print("#"*95)
konoha11 = {"naruto", "sakura", "neji", "lee", "tenten", "shikamaru", "ino", "choji",
            "kiba", "hinata", "shino"}
team10 = {"shikamaru", "ino", "choji"}
team7 = {"naruto", "sasuke", "sakura"}
print(team10.issubset(konoha11))    # Output: True
print(team7.issubset(konoha11))     # Output: False


# SUPERSETS:
"""
Similarly like subsets, when set2 contains all the elements present in set1 along with other
elements, then set2 is the superset of set1. This can be checked using the isuperset() method.
Please refer below:
"""
print("#"*95)
print(konoha11.issuperset(team10))  # Output: True
print(konoha11.issuperset(team7))   # Output: False


# DISJOINT SETS:
"""
Disjoint sets, also known as mutually exclusive sets, are sets that have no elements in common.
In other words, two sets are disjoint if their intersection is an empty set. This can be 
checked using the isdisjoint() method:
"""
print("#"*95)
print(team10.isdisjoint(team7))                 # Output: True
print(team_jiraiya.isdisjoint(team_minato))     # Output: False


# CONVERSION:
"""
We can convert different data structures like lists or tuples into sets using the set() method.
In the process the duplicate values are removed from the final set.
"""
print("#"*95)
list1 = [1, 2, 3, 4, 5]
tuple1 = (6, 7, 8, 9)
set1 = set(list1)
set2 = set(tuple1)
print(set1)     # Output: {1, 2, 3, 4, 5}
print(set2)     # Output: {8, 9, 6, 7}


# COPYING SETS:
"""
We can create copies of sets the same way we create copies of dictionaries. Simply assigning a
variable reference pointing to a set to another variable does not create a copy of the set. 
Instead, both the variables in that case refer to the same set. Hence, any modifications 
to set through on variable can be referenced through the other. This is just like in the 
case of dictionaries. Please refer to '5_copying_dictionaries.py' for more details.
In order to create an actual copy of the set we need to use the copy() method to  create a 
shallow copy. Please refer below:
"""
# Shallow copying using copy() method:
print("#"*95)
young_ninja = konoha11.copy()
young_ninja.add("sasuke")
print(young_ninja)
# Output: {'sasuke', 'shikamaru', 'lee', 'choji', 'naruto', 'sakura', 'hinata', 'tenten', 'shino', 'ino', 'neji', 'kiba'}
print(konoha11)
# Output: {'shikamaru', 'lee', 'choji', 'naruto', 'sakura', 'hinata', 'tenten', 'shino', 'ino', 'neji', 'kiba'}

"""
In the above case using the copy() method to create a shallow copy is enough as the set 
contains basic datatype. Incase of a set containing complex data types such as tuples or a 
frozenset of lists, a shallow copy will not be enough. It lead to the same problems as in 
the case of dictionaries. Although a different copy of the set will be created, the complex 
objects contained within the 2 sets will referenced jointly by both sets. Hence, in such a 
case a deepcopy might be necessary.
"""
print("#"*95)
team_asuma = ("shikamaru", "ino", "choji")
team_kurenai = ("kiba", "shino", "hinata")
team_kakashi = ("naruto", "sasuke", "sakura")
rookie9 = {team_asuma, team_kurenai, team_kakashi}
young_teams = copy.deepcopy(rookie9)
young_teams.update({"lee", "neji", "tenten"})
print(rookie9)
# Output: {('shikamaru', 'ino', 'choji'), ('naruto', 'sasuke', 'sakura'), ('kiba', 'shino', 'hinata')}
print(young_teams)
# Output: {('shikamaru', 'ino', 'choji'), 'tenten', 'lee', 'neji', ('naruto', 'sasuke', 'sakura'), ('kiba', 'shino', 'hinata')}

"""
However, it is important to note that sets only allow immutable data objects like tuples. 
Hence, although we can add or remove elements from the set, we can't make any changes to the 
elements themselves. Hence, a deepcopy or a shallow copy does not make a difference.
"""


# CLEARING A SET:
"""
To clear all elements from a set in Python, you can use the clear() method. The clear() method
removes all elements from the set, leaving it empty. Please refer below:
"""
print("#" * 95)
new_set = rookie9
rookie9.clear()
print(rookie9)  # Output: set()
print(new_set)  # Output: set()

"""
In the above case we can see that we are adding another reference to the set which variable 
rookie9 is pointing to. Hence, the same set can be referenced using both the variable. Now 
when we clear the set using the reference of the rookie9 variable, we can also see the 
changes through the new_set variable reference. This is because the set object has been 
cleared and both the variable a referencing an empty set.
This is not to be confused with assigning an empty set with the set() method, as in that 
case the original set remains intact and a new empty set is created and assigned to the 
variable reference. Please refer below.
"""
print("#" * 95)
new_set2 = young_teams
young_teams = set()
print(young_teams)
# Output: set()
print(new_set2)
# Output: {('shikamaru', 'ino', 'choji'), 'tenten', 'lee', 'neji', ('naruto', 'sasuke', 'sakura'), ('kiba', 'shino', 'hinata')}

"""
In the above case we can see that
"""