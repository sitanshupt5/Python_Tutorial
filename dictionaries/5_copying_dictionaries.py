"""
Dictionaries cannot be copied by assigning the value of another dictionary reference to an
existing variable referring to a dictionary. In such a case both variable references refer
to the same dictionary. Hence, appending or updating the dictionary in any way through any
one of the variable references will reflect the change when referencing through the other.
Please refer to the below example:
"""
import copy

anime_characters = {
    "naruto": ["Sasuke", "Sakura", "Kakashi"],
    "one piece": ["Luffy", "Zoro", "Sanji"],
    "avatar": ["Aang", "Katara", "Toph"],
    "demon slayer": "Tanjiro"
}

animes = anime_characters
animes["demon slayer"] = "Inosuke"
print(anime_characters["demon slayer"])     # Output: Inosuke
print(animes["demon slayer"])               # Output: Inosuke

"""
In the above case for lines 17 and 18 as we can see, although the values were appended for 
the animes dictionary reference, it still reflects the values for both animes and 
anime_characters dictionary variable references. Hence, it can be concluded that both the 
variable are referencing the same dictionary.
In order to create an entirely new copy of the dictionary we can use the copy() method.
"""
animations = anime_characters.copy()
animations["demon slayer"] = "Zenitsu"
print("#"*95)
print(anime_characters["demon slayer"])     # Output: Tanjiro
print(animations["demon slayer"])           # Output: Zenitsu

"""
After using the copy() method we can see that in the above case the variables animations and 
anime_characters refer to separate dictionaries. Hence, when we update the string value for 
a key in one dictionary the changes are not reflected for the other.
However, the values against the keys "naruto", "one piece" and "avatar" are lists. What 
happens we append the lists in one dictionary?
"""
# SHALLOW COPY:-
anime_characters["naruto"].append("Sai")
print("#"*95)
print(anime_characters["naruto"])       # Output: ['Sasuke', 'Sakura', 'Kakashi', 'Sai']
print(animations["naruto"])             # Output: ['Sasuke', 'Sakura', 'Kakashi', 'Sai']

"""
We can see that in the above case in lines 48 and 49 the output is the same for both 
dictionaries although they are separate copies. This is because, although both dictionaries 
are separate copies they are referring to the same list. Hence, any updates to the lists 
will be reflected for both dictionaries. Effectively, the dictionaries can be interpreted as
the following:
naruto_chars = ["Sasuke", "Sakura", "Kakashi"]
one_piece_chars = ["Luffy", "Zoro", "Sanji"]
avatar_chars = ["Aang", "Katara", "Toph"]
anime_characters = {
    "naruto": naruto_chars,
    "one piece": one_piece_chars,
    "avatar": avatar_chars,
    "demon slayer": "Tanjiro"
}
Hence, any changes to the list naruto chars is being reflected by both anime_characters and 
animations dictionaries. This is because animations dictionary is a shallow copy of anime 
chars.
A shallow copy of an object is a copy that is created, 
but it does not create copies of the objects within the original object. Instead, it copies 
references to the objects. This means that changes made to the objects within the original 
object will be reflected in the shallow copy and vice versa. This can be helpful since it 
saves memory and is faster. However, depending on circumstances there may be requirement 
where all the objects contained withing the dictionary are unique as well.
"""
# DEEP COPY:-
"""
A deep copy, on the other hand, creates a new object along with new objects for all the objects
contained within the original object. Changes made to the objects inside the original object do
not affect the deep copy, and vice versa. Please refer to the following:
"""
deep_copy_anime = copy.deepcopy(anime_characters)
deep_copy_anime["one piece"].append("Nami")
print("#"*95)
print(anime_characters["one piece"])    # Output: ['Luffy', 'Zoro', 'Sanji']
print(deep_copy_anime["one piece"])     # Output: ['Luffy', 'Zoro', 'Sanji', 'Nami']

"""
As we can see above in lines 76 and 77 the outputs are different as the objects contained 
within the dictionary are also copied.
"""

