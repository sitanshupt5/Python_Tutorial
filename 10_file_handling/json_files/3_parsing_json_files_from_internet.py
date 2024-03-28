"""
Just like parsing json data from a file we can parse json data directly sourced from the
internet in the form of a stream. This can be achieved using the urllib.request module in
python. Our example is going to be the same as the previous lesson except this time we
are going to be sourcing the json data directly from the internet rather than a file.
"""
import json
import urllib.request

json_data_source = "https://www.ncei.noaa.gov/access/monitoring/climate-at-a-glance/global/time-series/globe/land_ocean/1/10/1880-2022.json"

with urllib.request.urlopen(json_data_source) as json_stream:
    data = json_stream.read().decode("utf-8")
    anomalies = json.loads(data)

"""
In this case the urllib.request.urlopen() method returns a stream. On line 13 we read the 
stream and decode it. The data is then deserialized and stored in line 14.
An important thing to note is that here we use json.loads() instead of json.load(). This is 
because json.load() is used to read data from a file whereas json.loads is used to read data
from a stream.
Once, the json data has been deserialized, we can use it to perform operations.
"""

print(f"The type of anomalies object is : {type(anomalies)}")
print(f"The type of description object is : {type(anomalies["description"])}")
print(f"The type of data object is : {type(anomalies["data"])}")
print("#"*95)
for key, value in anomalies['description'].items():
    print(f"{key}: {value}")

for year, value in anomalies['data'].items():
    print(f"{int(year)} ...{float(value):6.2f}")

"""
It is important to note that in this case we haven't used any error handling. In an ideal 
real world case we will need to use error handling. There might be several error that we 
might come across when reading a file or reading a stream from the internet. The server 
might be timed out, the file might not be present. etc.
For production quality code, error handling is necessary.
"""

