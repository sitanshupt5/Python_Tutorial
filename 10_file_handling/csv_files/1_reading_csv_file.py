"""
CSV stands for comma separated values. A csv file generally contains rows of comma separated
values. The commas in such a case represent the column value. They have to be same number of
values in each row. Although csv stands for comma separated values, we can use characters
than commas such as '|' to separate the values. It is completely acceptable.
In order to be able to read a file with .csv extension in python, we need to use the csv
module. For this example we are going to use the OlympicMedals_2020.csv file. Please refer
to the below code:
"""
import csv

csv_filename = "OlympicMedals_2020.csv"

with open(csv_filename, encoding="utf-8", newline='') as csv_file:
    headers = csv_file.readline().strip("\n").split(",")
    print(f"Colummn_Headers: {headers}")
    reader = csv.reader(csv_file)
    for row in reader:
        print(row)

"""
We have done 2 things different as compared to handling text files and json files over here.
First, we have passed keyword argument "newline = ''" to the open() method. Generally the 
newline argument does create any notable difference. However, not using it may cause 
problems at times. This is as per the python documentation. The newline argument takes the 
following values: 'None', '', '\n'. None activates the universal newline mode and converts 
different newline conventions to '\n'. Empty string disable all newline conversions and 
newline characters in the text are treated as is. '\n' on the other hand forces newline 
characters to be treated as '\n'. Since, different platforms have different conventions the 
newline argument is important.
Secondly, we are using the csv.reader() method to read data from the csv file. Just like in 
the case of json we used the json.load() or json.loads(). The csv.reader() method returns a 
reader object.
One important thing to note in the output of the above code is that contrary to the data in 
the file, the data printed in the console has all the numeric values quoted. This means that
the function automatically converted all the numeric values to strings. This might not be 
the ideal case when we need to perform operations on the numeric values.
The following example demonstrates how we can avoid the quoting of the numeric values. For 
this example we will be using the cereal_grains.csv file. It must be noted that compared to 
the data in the previous file, the string values in this file are quoted.
"""
print("#"*95)
print()
with open("cereal_grains.csv", encoding="utf-8", newline='') as csv_file:
    reader = csv.reader(csv_file, quoting=csv.QUOTE_NONNUMERIC)
    for row in reader:
        print(row)

"""
In the output of the above code we see that the numeric values are no longer quoted. 
Although this method is helpful, it still has its limitations. Firstly, it works if all the 
non numeric values in the file are already quoted. Secondly, if the numeric values in the 
file are wrapped in double quotes, it wont work i.e the numeric values in the output will 
still be quoted regardless of passing the argument. Finally, it converts all numeric values 
to float type.
Incase of parameter values like csv.QUOTE_ALL, it sometimes leads to over quoting i.e it 
quotes all values that may or may not be required to be quoted.
Hence, this is not the best method. We can fix these problems using Sniffers and Dialects.
We will cover them in the next module.
Moving on, it is also possible to read the contents of a csv file in the form of a list 
dictionaries where the column headings serve as the keys and the contents of the each row 
serve as the corresponding values.
This can be done using the DictReader() constructor of csv module. Please refer to the below 
code.
"""

print("#"*95)
print()
with open("cereal_grains.csv", encoding="utf-8", newline='') as csv_file:
    reader = csv.DictReader(csv_file)
    for row in reader:
        print(row)

"""
The output of the above code fragment as we can see is a series of rows where each row is a 
dictionary corresponding to the row in the csv file.
The DictReader() automatically takes the column headings as the keys.
We can take another example to further understand how the DictReader() can be used. This 
time we will take the country_info.csv file.
"""
print("#"*95)
print()
countries = {}
with open("country_info.csv", encoding="utf-8", newline='') as csv_file:
    reader = csv.DictReader(csv_file, delimiter="|")
    for row in reader:
        countries[row['Country'].casefold()] = row

for country, details in countries.items():
    print(f"{country}: {details}")

while True:
    chosen_country = input("Please enter the name of the country:").casefold()
    if chosen_country in countries:
        print(f"The capital city of {countries[chosen_country]["Country"]} is : "
              f"{countries[chosen_country]["Capital"]}")
    else:
        break

"""
The only important thing to note in the above code is that in line 84. Since, 
the country_info.csv file used "|" character as the delimiter instead of comma, it has to be
explicitly mentioned.
"""
