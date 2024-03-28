"""
Writing data into a csv file is easier than reading data from it. In this case we are
preparing the data and decide how it should be written to the csv file.
We can format and write different data structures into a csv file. In order to do that we
need to use the csv.writer() method to create a writer object which can write rows into the
csv file. In the below code fragment we are writing a list of lists that contain same number
elements to a csv file.
"""
import csv
from medals_data_dict import medals_table

data = [
    ['Barley', 556.0, 1.7, 32.9, 10.1, 13.8],
    ['Durum', 339.0, 5.0, 27.4, 4.09, 9.7],
    ['Fonio', 240.0, 1.0, 4.0, 1.7, 0.05],
    ['Maize', 442.0, 7.4, 37.45, 6.15, 11.03],
    ['Millet', 484.0, 2.0, 37.9, 13.4, 9.15],
    ['Oats', 231.0, 9.2, 35.1, 10.3, 3.73],
    ['Rice (Brown)', 346.0, 2.8, 38.1, 9.9, 0.8],
    ['Rice (White)', 345.0, 3.6, 37.6, 5.4, 0.1],
    ['Rye', 422.0, 2.0, 31.4, 18.2, 21.2],
    ['Sorghum', 316.0, 3.0, 37.8, 9.92, 9.15],
    ['Triticale', 338.0, 1.81, 36.6, 19.0, 0.9],
    ['Wheat', 407.0, 1.2, 27.8, 12.9, 13.8],
]

csv_headers = ['Cereal', 'Calories', 'Fat', 'Protein', 'Fibre', 'Vitamin E']

with open("my_cereals.csv", 'w', encoding="utf-8", newline='') as csv_file:
    writer = csv.writer(csv_file, quoting=csv.QUOTE_NONNUMERIC, delimiter='|')
    writer.writerow(csv_headers)
    writer.writerows(data)

"""
The above code is simple to understand.
It is important to note that in line 29 we are instructing the writer object to quote all 
non-numberic values and to use '|' character as the delimiter instead of the default ','.

We can also create a csv file from a list of dictionaries using the DictWriter() constructor.
It is fairly easy and gives us the freedom to choose which rows to include and not include.
We will import the data to write into a csv file from the medal_data_dict.py file.
"""
columns = ["country", "gold", "silver", "bronze", "rank"]
with open("country_medals.csv", "w", encoding="utf-8", newline='') as output_file:
    writer = csv.DictWriter(output_file, fieldnames=columns)
    writer.writeheader()
    writer.writerows(medals_table)
# Instead of using the writerows() method we can also loop over the medals_table list and
# write individual rows to the file one by one using the writerow() method instead.

"""
We can also skip a row and its details if we want while writing into a csv file. For that we
will have to pass keyword argument 'extrasaction' with value 'ignore' to the DictWriter().
Please refer below to the below code:
"""
column_headers = ["country", "gold", "bronze", "rank"]
with open("country_medals.csv", "w", encoding="utf-8", newline='') as output_file:
    writer = csv.DictWriter(output_file, fieldnames=column_headers, extrasaction='ignore')
    writer.writeheader()
    writer.writerows(medals_table)

"""
In the above code, the medals_table had data for 5 columns namely country, gold, silver, 
bronze and rank respectively. However, we removed the column name silver from the list while
the key name still existed in the medals_table.
If we send run the above code without passing the keyword argument extrasaction as 'ignore',
error will be returned in the output where it will be specified that the column silver is 
missing from the columns list. If we send the extrasaction value ignore to the DictWriter(),
it will ingore key-values from the medals table that are not present in the columns list.

In the above code snippets we demonstrated how to create a csv file from a list of 
dictionaries using the DictWriter(). But what if our data is not in the form of a list of 
dictionaries. In that case DictWriter() is apparently rendered useless. However, there is a 
way to transform other data structures to form a list of dictionaries which can in turn be 
used to create csv files. This is where the zip function comes into play. Please refer to 
the below code fragment:
"""
albums = [
    ("Welcome to my Nightmare", "Alice Cooper", 1975),
    ("Bad Company", "Bad Company", 1974),
    ("Nightflight", "Budgie", 1981),
    ("More Mayhem", "Imelda May", 2011),
    ("Ride the Lightning", "Metallica", 1984)
]
keys = ["album", "artist", "year"]

for row in albums:
    zip_object = zip(keys, row)
    albums_dict = dict(zip_object)
    print(albums_dict)

"""
In the above case we have the album list which contains 5 tuples with 3 elements each 
corresponding to album, artist, year. When we use the zip() function to zip each tuple in 
albums with the keys and in turn produces a zip object for each tuple in the albums list.
This zip object contains 3 tuples with each containing 2 elements i.e (keyname, value).
Here are the contents of the zip object for the first tuple in the list albums:
('album', 'Welcome to my Nightmare')
('artist', 'Alice Cooper')
('year', 1975)
Note that the number of tuples in each zip_object will be equal the the number of keys. The 
total number of zip objects will be the number of tuples in the albums list.
Now each zip_object 3 tuples which are a key and value pairs. This is precisely what we need to
create a dictionary. In line 89 we pass the zip_object as an argument to the dict() 
function. This is acceptable as zip_object is an iterable with key and value pairs.
Now we know it is possible to easily transform other data structures into a list of 
dictionaries which we can then use to write into a csv file with the DictWriter().
Lets write the code.
"""

filename = "albums.csv"

with open(filename, "w", encoding="utf-8", newline='') as output_file:
    writer = csv.DictWriter(output_file, fieldnames=keys)
    writer.writeheader()
    for row in albums:
        albums_dict = dict(zip(keys, row))
        writer.writerow(albums_dict)

"""
Using 2 additional lines of code we can make the data usable for DictWriter() and create a 
csv file.
"""

