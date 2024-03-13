"""
Parsing data means splitting it up into logical components. What it means in simple language is
making sense of the data. Please refer to the below example. We will be using the
country_info.txt file for this example:
"""
input_filename = "country_info.txt"
with open(input_filename, "r") as country_file:
    for row in country_file:
        data = row.strip("\n").split("|")
        print(data)

"""
With the above code fragment we were able to read the contents of the file, split the data 
in different rows and print them. The data printed is in the form of list corresponding to 
each individual country. However, that is not the most readable form. We need to make the 
data more readable to make sense out of it. Please refer the code below:
"""
countries = {}
with open(input_filename, "r") as country_file:
    country_file.readline()
    for row in country_file:
        data = row.strip("\n").split("|")
        country, capital, code, code3, dialing, timezone, currency = data
        country_dict = {
            "country": country,
            "capital": capital,
            "country_code": code,
            "cc3": code3,
            "dialing_code": dialing,
            "timezone": timezone,
            "currency": currency
        }
        countries[country.casefold()] = country_dict

# for key, value in countries.items():
#     print(f"{key}: {value}")

"""
Now we have managed parse the data and store it in a usable form for reuse. Now let's use 
this dictionary to print the country names and their respective capital cities. There are many
ways to do that as we have seen in the dictionaries section. Here are a few things to 
understand before we move to coding.
'countries' is a dictionary of dictionaries. Hence, each value in countries dictionary key 
value pair is a dictionary. This dictionary is supposed to have keys corresponding to their 
respective values i.e country, capital, code, code3, dialing, timezone, currency. 
Understanding this makes our work easier. First we iterate over the items in countries 
dictionary and then from the values of each individual item (which in turn is a dictionary)
we pick the data we need using the its appropriate key.
"""
for value in countries.values():
    print(f"{value["country"]}: {value["capital"]}")

"""
The above code prints out all the country names against their repsective capital cities.
We could also write code where we return the capital city or any detail of the country based
on user input. Please refer below:
"""
while True:
    chosen_country = input("Please enter the name of the country:").casefold()
    if chosen_country in countries:
        print(f"The capital city of {countries[chosen_country]["country"]} is : "
              f"{countries[chosen_country]["capital"]}")
    else:
        break