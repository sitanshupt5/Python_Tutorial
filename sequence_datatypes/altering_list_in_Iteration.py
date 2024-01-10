"""
When removing specfic items in a list while iterating over the list or any other kind of
sequence or collection it is imperative for one to be careful. The operations could give
results synonymous to ConcurrentModificationException in java. Consider the following example
: We have a list of 10 numbers. We only need to have even numbers in the list and remove the
remaining. We try to achieve this using a loop. Now, say the loop has 5 even and 5 odd
numbers and the total size of the loop is 10 items. And the first odd number is encountered at
the 3rd index. As soon as the item at 3rd index is removed the items at the subsequent
indexes have to shift one index backward. So, item at index 4 shifts to index 3 , item at
index 5 shifts to index 4 and so on. Now, after removing the value at index 3 the control
moves to index 4 while the original value at index 4 shifts to index 3. In such a case
if the new number at index 3 is an odd number, it will be ignored in the loop.
Consider the following code snippet.
"""
data = [4, 5, 104, 105, 110, 120, 130, 130, 150,
        160, 170, 183, 185, 187, 188, 191, 350, 360]

data1 = data.copy()

min_valid = 100
max_valid = 200

for index, value in enumerate(data):
    if value<=100 and value<=200:
        data.remove(value)
print(data)
# Output: [5, 104, 105, 110, 120, 130, 130, 150, 160, 170, 183, 185, 187, 188, 191, 350, 360]
"""
The above mentioned list is sorted and hence the values that are to be removed are placed
consecutively. Due to this reason the unecessary values cannot be removed efficiently.
Hence, we can try the following few approaches to remove the data efficiently.
"""
# Deleting slices in a sorted list outside of the loop.
stop = 0
for index, value in enumerate(data1):
    if value >= min_valid:
        stop = index
        break
del data1[:stop]

for index, value in enumerate(data1):
    if value >= max_valid:
        stop = index
        break
del data1[stop:]

print(data1)

# Output: [104, 105, 110, 120, 130, 130, 150, 160, 170, 183, 185, 187, 188, 191]
"""
As we can see above this time all the unnecessary values that are out of range have been
removed. In such type of operations where entire ranges have to be removed this method of
deleting slices is the most efficient in terms of time complexity. The conditions to use 
this method are:
1. The list should be sorted. The method does not work on unsorted list.
2. If the intention is to remove items outside a certain range.

In circumstances where items are to be removed based on certain trends or conditions but
the unnecessary items cannot be lined together, this method cannot be used. for example:
removing even numbers from a list of odd and even numbers.
In those circumstances the following methods are to be used.
"""
# Iterating backwards:
data2 = [104, 101, 4, 105, 308, 103, 5,
         107, 100, 306, 106, 102, 108]
data3 = data2.copy()
for index in range(len(data2)-1, -1, -1):
    if (data2[index] < min_valid) or (data2[index] > max_valid):
        print(index, data2)
        del data2[index]
print(data2)

# Using the Python built-in reversed() function:
top_index = len(data3)-1
for index, value in enumerate(reversed(data3)):
    if value < min_valid or value > max_valid:
        print(top_index-index, value)
        del data3[top_index-index]
print(data3)

"""
The time complexity of the above 2 methods can vary from O(n) to O(n^2) where n is the 
number of elements in the collection. The variation depends on the operation being performed.
If the operation is removal of items then it depends on how the items are being removed.
Also, if the number of elements is very large than the time complexity can go upto O(n^2)
irrespective of the removal method. 
"""