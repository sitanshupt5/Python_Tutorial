"""
Hashing is a process used in computer science and cryptography to transform input data of
arbitrary size into a fixed-size string of characters, which is typically a hexadecimal number.
The output of this process is commonly referred to as the "hash value" or simply "hash." Hash
functions are the algorithms or mathematical functions used to perform this transformation.
Following are the points to note about hashes and hash functions:
*   A hash function produces fixed-size hash values from its input. The hashes are usually
    integers, but they don't have to be.
*   There are many different ways to implement a hash function. There's no single way to
    write one, and different algorithms have their own strengths, weaknesses and applications.
*   A hash function produces values that can be used to index a fixed-size data structure
    called a hash table. If the hash table can hold 500 items, then the hash function should
    produce 500 distinct hashes.
*   A hash doesn't have to be unique. For example, two different strings can have the same
    hash value. This is known as collision.
*   There are several different strategies of handling collisions. One of the simplest ways
    is to dump all the keys with the same hash into the same bucket. You then compare each item
    in the bucket to the original key to see if it exists.
*   Because handling collisions is slower than indexing directly into the table, it is
    important that a hash function produces as few collisions as possible.
*   The best case is that every key has a unique hash.
*   The worst case is that every key has the same hash. In such a case the hashing function
    is not suitable for that particular application.
Although hashing is fundamental to dictionaries, generally user defined hashing functions
are not used. Python has built-in hashing function and there are many other hashing
functions available in different modules. However, we still need to understand how a hashing
function works. The following program shows the simplest implementation of a hashing function:
"""
data = [
    ("naruto", "Tailed Beast Bomb Rasenshuriken"),
    ("sasuke", "Indra's Arrow"),
    ("sakura", "Medical Ninjutsu"),
    ("choji", "Total Expansion Jutsu"),
    ("gai", "Hirudora")
]


def simple_hash(s: str) -> int:
    basic_hash = ord(s[0])
    return basic_hash % 10


for key, value in data:
    h = simple_hash(key)
    print(key, h)

"""
Now for the above data the output returned will be:
naruto 0
sasuke 5
sakura 5
choji 9
gai 3

In this case we can see that keys "naruto", "choji" and "gai" have unique hash values. 
However, 
there is a collision between the hash values for keys "sasuke" and "sakura".
As this is a very simple hash function this is expected. Generally, a hash function would 
use all the characters in the string to generate the hash value but here we are using only 
the first character. Also, in our case we are limiting the hash values between a range of 0-9.
Hence, any more than 10 entries and there is bound to be collision.
In the above code lets use the python's built in hash function instead of the simple hash 
function:
"""
print("#" * 95)
for key, value in data:
    h = hash(key)
    print(key, h)
"""
In this case the output we get will look somewhat like the following:
naruto -2661822395417666979
sasuke -2726797855501009330
sakura 211742282876124031
choji 602048758654005419
gai -8104258447068544519

In the above case since we are using 64 bit Python, the hash generated could be in the range 
quintillions (2^64) for both positive and negative side. Pythons hash function randomizes 
the hashes that is produces. That means that the hash values generated will during the 
course of an execution will be the same. However, the hash values generated for each key (
say a string) will change in each execution.
The following code simulates how hashes are used in the functioning of dictionary:
"""

keys = [""] * 10
values = keys.copy()


def get(k: str) -> str:
    hash_code = simple_hash(k)
    if values[hash_code]:
        return values[hash_code]
    else:
        return None


for key, value in data:
    h = simple_hash(key)
    print(key, h)
    keys[h] = key
    values[h] = value

print("#"*95)
print(keys)         # Output: ['naruto', '', '', 'gai', '', 'sakura', '', '', '', 'choji']
print(values)       # Output: ['Tailed Beast Bomb Rasenshuriken', '', '', 'Hirudora', '', 'Medical Ninjutsu', '', '', '', 'Total Expansion Jutsu']
print()
print(get("naruto"))    # Output: Tailed Beast Bomb Rasenshuriken
print(get("sasuke"))    # Output: Medical Ninjutsu

"""
In the above code and corresponding output we can see that we are successfully able to store
and retrieve the data using hash values. That being said the program is sufficient. It does 
not implement error handling and it does not have the code to handle collisions. Hence, 
we can see that although there are 5 items in our data we can only see 4 items stored in our
lists namely 'keys' and 'values'. Only one of the items whose keys collided was stored.
"""

