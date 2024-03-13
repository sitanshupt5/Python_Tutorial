"""
It is possible to open multiple files together and in different modes. For this example we
are going to read data from OlympicMedals_2020.csv file, convert it into a list of
dictionaries and then write the data into medal_data_dict.py file. The data in this file
will be useful to understand the operation of DictWriter() constructor.
Please refer to the code below:
"""
import csv

ordering = ["Country", "Gold", "Silver", "Bronze", "Rank"]

with open("OlympicMedals_2020.csv", encoding="utf-8", newline='') as data, \
        open("medals_data_dict.py", "w", encoding="utf-8", newline='') as output_file:
    print(file=output_file)
    print('medals_table = [', file=output_file)

    reader = csv.DictReader(data)
    for row_dict in reader:
        new_dict = {}
        for key in ordering:
            value = row_dict[key]
            if value.isnumeric():
                value = int(value)
            new_dict[key.casefold()] = value
        print(f"    {new_dict},", file=output_file)

    print("]", file=output_file)
    print(file=output_file)
