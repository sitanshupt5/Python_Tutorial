"""
In the previous lesson we saw the issues in quoting that might be presented when reading a
csv file. Apart from that there other problems that are more real world and need to be
addressed. For example, incase we are handling a large number of csv files, we cannot check
the details of each csv file. Python has to do it for us. The data might be delimited using
characters other than comma. The data might be quoted or unquoted.
To handle all these metadata regarding the csv file we can use the sniff() method of the
Sniffer class in csv module. The sniff() method returns a dialect object which can then be
used to parse the csv file.
Please refer to the below example. In this example we will use the country_info.csv file.
"""
import csv

input_filename = 'country_info.csv'

with open(input_filename, encoding="utf-8", newline='') as countries_data:
    sample = ""
    for line in range(3):
        sample += countries_data.readline()
    country_dialect = csv.Sniffer().sniff(sample)

attributes = [
    "delimiter",
    "doublequote",
    "escapechar",
    "lineterminator",
    "quotechar",
    "quoting",
    "skipinitialspace",
    ]
for attribute in attributes:
    print(f"{attribute}: {getattr(country_dialect, attribute)}")

"""
In the above code we use the sniff() method to get the dialect of the csv file. The dialect 
object contains data as mentioned in the attributes list. These are "delimiter", "doublequote",
"escapechar", "lineterminator", "quotechar", "quoting" and "skipinitialspace".
As we can see from the output value the sniff() method correctly identifies the '|' 
character as the delimiter in our csv file.
Now, we can use this to read our csv file. Please refer to the below code.
"""
print("#"*95)
with open(input_filename, encoding="utf-8", newline='') as countries_data:
    sample = ""
    for line in range(3):
        sample += countries_data.readline()
    country_dialect = csv.Sniffer().sniff(sample)
    country_dialect.skipinitialspace = True
    countries_data.seek(0)
    country_reader = csv.reader(countries_data, country_dialect)
    for row in country_reader:
        print(row)

"""
There are a few things to note in the above code. 
First we are using the sniff method on a sample rather than a whole file. We are using the 
readline() method in loop for the first 3 lines to gather a string sample. We can very well 
use the read() method instead of readline() and use sniff() method on it. However, that might 
not be the best practice. Since csv files maintain uniformity, the dialect of the first 3 
lines will be the same as that of all the other lines. Also, using read() method and storing
the contents of a large file into a variable will consume a lot of memory. Hence, the first 
3 lines are enough to get the dialect of the entire csv file.
Second, in line 48 we are setting the value of 'country_dialect.skipinitialspace' to TRUE. 
the default value is FALSE. This attribute tells the reader remove any trailing space in a 
string.
Thirdly, in line 49 we are using the seek() method to return the cursor to the beginning of 
the file. This is because after using the readline() method the cursor is not positioned at 
the beginning of the file. This would prevent further read operation to read the first 3 lines.

Lets use another example of the cereal_grains.csv file. Please refer below:
"""
print("#"*95)
with open("cereal_grains.csv", encoding="utf-8", newline='') as csv_file:
    sample = ''
    for line in range(3):
        sample += csv_file.readline()
    dialect = csv.Sniffer().sniff(sample)
    dialect.quoting = csv.QUOTE_NONNUMERIC
    csv_file.seek(0)
    csv_reader = csv.reader(csv_file, dialect)
    for row in csv_reader:
        print(row)

"""
We can also use dialects for DictReader(). However, currently we are not equipped with OOP 
knowledge to create a user defined dialect. Instead we can use the pre defined dialects in 
the csv module. For this example we will use the country_info.csv file.Please refer to the 
below code:
"""
print("#"*95)
dial = csv.excel
dial.delimiter = "|"

countries = {}

with open("country_info.csv", encoding="utf-8", newline='') as csv_file:
    headings = csv_file.readline().strip('\n').split(dial.delimiter)
    for index, heading in enumerate(headings):
        headings[index] = heading.casefold()
    dictreader = csv.DictReader(csv_file, dialect=dial, fieldnames=headings)
    for row in dictreader:
        countries[row["country"].casefold()] = row

for country, details in countries.items():
    print(f"{country}: {details}")
