"""
The split() method is a built-in string method that is used to split a string into a list
of substrings based on a specified delimiter. Then syntax of the split method is as follows:
string.split(separator, maxsplit)
In this syntax:
'separator'  is the delimiter or character(s) based on which the string will be split.
If this parameter is not specified, any whitespace (space, tab, newline) is used as the
default separator.
'maxsplit' is an optional parameter that specifies the maximum number of splits to be done.
If not provided, there is no limit on the number of splits.
Please refer to the following examples:
"""

pangram = "the quick brown fox jumped over the lazy dog."

words1 = pangram.split()
words2 = pangram.split("t")
words3 = pangram.split(" ", 3)

print(words1)
print()
print(words2)
print()
print(words3)
print()