"""
Data can be printed to text files in python using the open() function alongside the 'with'
statement. Printing data to file is easy. It can be achieved in 2 ways. We will discuss both
one by one. For this example we will use the dataset below:
"""
data = [
    "Andromeda - Shrub",
    "Bellflower - Flower",
    "China Pink - Flower",
    "Daffodil - Flower",
    "Evening Primrose - Flower",
    "French Marigold - Flower",
    "Hydrangea - Shrub",
    "Iris - Flower",
    "Japanese Camellia - Shrub",
    "Lavender - Shrub",
    "Lilac- Shrub",
    "Magnolia - Shrub",
    "Peony - Shrub",
    "Queen Anne's Lace - Flower",
    "Red Hot Poker - Flower",
    "Snapdragon - Flower",
    "Sunflower - Flower",
    "Tiger Lily - Flower",
    "Witch Hazel - Shrub",
]

# PRINTING DATA TO FILE USING THE THE PRINT() METHOD:
output_filename = "flower_print.txt"

with open(output_filename, "w") as plants:
    for plant in data:
        print(plant, file=plants)

"""
The print function has the keyword argument that takes file object as parameter in order to 
print to a file. If we run this code, we will find a text file in our filepath containing 
the text within the 'data' list.
We can test the contents of that file through our code. 
"""
with open("flower_print.txt") as input_file:
    for line in input_file:
        print(line.strip())

"""
The above code prints the contents of the 'flower_print.txt' file and confirms our write 
operation worked.
"""

# PRINTING DATA TO A FILE USING THE WRITE() METHOD:
"""
The write() method in its syntax is almost similar to the print method. Please refer below
"""
output_filename = "flower_write.txt"

with open(output_filename, "w") as plants:
    for plant in data:
        plants.write(plant)

"""
Running the above code fragment would generate a new file 'flower_write.txt' and the 
contents of the list 'data' will be copied into the file. However, it would look totally 
different from the contents of the file 'flower_print.txt'. Lets understand the reason.

The print() function provides a string representation of the data that is to be printed. It 
includes separators(default being space) between multiple arguments. It also ends the line.
On the other hand the write method does not carry out any such actions on the data unless 
it is explicitly directed to do so. It prints exactly what it gets.
Another difference between the print() and write functions is that the print function prints
string representation of any object. Hence, if you try to print an integer using the print() 
function it will first convert the integer values to string and then print the values.
However, write() method does not perform any conversions. It will try to integer values to a
file that is open in text mode (default) raising errors.
"""
"""
The files modes supported by the open() function are as follows:
'r': Open the file for reading.
'w': Open the file for writing. Truncate the file (delete content) if the file already exists.
'x': Creates a new file for writing. Raises error if the file already exists.
'a': Opens the file for writing. Appends to the end of the file if it already exists.

"""
