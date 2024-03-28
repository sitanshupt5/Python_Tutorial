"""
In the context of programming and computer science, parsing typically refers to the analysis of
structured data, such as code or documents, to understand its syntactic and semantic structure.
In order to parse a json file and use the data it contains we first need to deserialize the
json data as discussed in the previous lesson.
For this particular lesson we will use the data in the file temperature_anomaly.json. Please
refer to the below example:
"""
import json

json_data_source = "temperature_anomaly.json"

with open(json_data_source, "r", encoding="utf-8") as file:
    anomalies = json.load(file)

"""
Now we have managed to deserialize the data and store it in a variable anomalies. However, in 
order to parse the data and make use of it we need to understand the type of data that has been
stored.
For starters, anomalies is a dictionary with 3 keys. The first key 'description' corresponds to
the value of another dictionary. Same for second key 'data'. The third key 'citation' 
corresponds to a string value.
"""

print(f"The type of anomalies object is : {type(anomalies)}")
print(f"The type of description object is : {type(anomalies["description"])}")
print(f"The type of data object is : {type(anomalies["data"])}")
print(f"The type of citation object is : {type(anomalies["citation"])}")
print("#"*95)
for key, value in anomalies['description'].items():
    print(f"{key}: {value}")

for year, value in anomalies['data'].items():
    print(f"{int(year)} ...{float(value):6.2f}")

print(f"citation: {anomalies["citation"]}")
