"""
In Python, we use the open() function to access an existing files for read or write operations.
The open() function accepts a lot of different types of arguments. However, the two
mandatory arguments are filepath and open mode. Please refer below:
"""
file = open("Jabberwocky.txt", "r")

for line in file:
    print(line)

file.close()

"""
The above code snippet copies and prints the contents of the file 'Jabberwocky.txt' to the 
console. In this case, when accessing the file using the open() function we are passing the 
mode as 'r' which means read mode. Similarly, there are other mode such as 'w' ( for opening
an existing file for writing) and 'x' (for opening a new file for writing).
In this case, since the file has been opened in read mode, no updates or write activities 
can be performed on the file.
We are iterating through the contents of the file line by line using a loop and printing 
them out.
Another important thing to note is compared to the text in the file, the lines of text in 
our output is double spaced i.e a blank line is added at the end of each line. This is 
because when parsing through the contents of the text file, the interpreter considers a line
change as a '\n' character. Hence, it prints it out. Problem is the print() function starts 
a newline everytime it executes.
This issue can be solved in two ways.
First we instruct the print function so as not to add a newline at the end of each line. 
Please refer below:
"""
print("#"*95)
file = open("Jabberwocky.txt", "r")

for line in file:
    print(line, end='')

file.close()
"""
Second, we can use the strip() method for strings. The strip() method removes the leading 
and trailing whitespace characters (space, tab, newline) from a string. 
Lets address another problem simultaneously. We can see a few wierd characters printed in 
our console such as 'â€“'. This is because the encoding of the file is not understood by 
python. In order for python to understand it we need to explicitly mention the encoding of 
the file.
Please refer to the application of the strip() method below:
"""
print("#"*95)
file = open("Jabberwocky.txt", "r")

for line in file:
    print(line.strip())

file.close()
"""
It is important to note that when accessing a file using the open method, we must always 
close the file once our operations are done. Otherwise, you may run out of file handles.
File handles are used by the operating system to keep track of the files that have been opened.
They're system-wide, meaning the available file handles are shared by every process running 
on the computer.
Running out of file handles could happen in a long running process that opens a lot of files.
Another consequence of failing to close a file when writing data to it is that the data 
might be lost forever. Hence, it is important to close the file.
"""
#   open() method using 'with' statement:
"""
However, there is a way in which python handles the closing of the file. This can be 
achieved using the 'with' statement. Please refer below:
"""
print("#"*95)
with open("Jabberwocky.txt", "r", encoding='utf-8') as file:
    for line in file:
        print(line.strip())

"""
The above code snippet gives us the same output as the code between line 43 to 49. 
In the above code the object returned by the open() function is assigned to the variable 
file and remains open until the code within the 'with' block is exited.
The advantage of using a with block is that it guarantees the safe closing of the file even 
if exception occurs in the code within the block itself.
"""
# read(), readline() and readlines() methods:
"""
In the above code snippets we have been reading from a file and printing the data on the 
console. However, in such a case the operations that we can perform upon the data itself can be
very limited. Storing the data in memory can help us perform operations that would be rather
difficult when processing the file line by line.
Please refer to the below example for the use of read(), readline() and readlines() methods:
"""

print("#"*95)
with open("Jabberwocky.txt", "r", encoding='utf-8') as file:
    text = file.read()          # Copies and returns the contents of the entire file as string.
    file.seek(0)
    sen = file.readline()       # Copies and returns the line from current position to next '\n' as string.
    file.seek(0)
    lines = file.readlines()    # Returns a list of all the lines from the file.

print(type(text))   # Type of object returned by the read() method
print(text)
print("="*95)
print(type(sen))    # Type of object returned by the readline() method
print(sen)
print("="*95)
print(type(lines))  # Type of object returned by the readlines() method
print(lines)
print("="*95)
print(lines[-1:])

for line in reversed(lines):
    print(line, end="")     # To print the contents of the file in reversed order.

"""
It is important to note that while using these methods one has be careful regarding the 
current position of control in the file. In the above example lines 88 - 92 illustrate that.
When we use the read() method, It reads from the beginning to end line by line. Hence, 
when the read is over, the control exists at the end of the line. Hence, using another read 
method like readline() or readlines() will result in an empty return. In order to bring back
the control to the first line we use the file.seek() method, and pass '0' as the argument.
This scenario holds true for both readline() and readlines() as well.

Although these methods can be useful, however they come with their fair share of disadvantages.
The most common loophole arises in the case of large files with millions of lines. The 
memory usage and speed become great concerns. In such cases it is impractical to use these 
methods
"""
