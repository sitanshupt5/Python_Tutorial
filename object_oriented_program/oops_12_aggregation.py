"""
Aggregation just like Composition is a design technique in object oriented programming that
represents a 'has-a' relationship. However, unlike Composition, in case of aggregation a
class contains a reference to the object of another rather than the object itself. That
means in this case the contained class can exist independently of the container class.
If the container class object is destroyed, the contained class object can still be used.
Please refer to the below example:
"""


class Address:
    def __init__(self, street, city, zip_code):
        self.street = street
        self.city = city
        self.zip_code = zip_code


class Person:
    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address


"""
In the above case the class Person contains only a reference to the Address class object 
which has been passed as an argument to the Person class constructor. Hence, this is an 
Aggregation.
Since Aggregation only contains a reference to the object of another class, it is often 
referred to as a weaker version of composition.
"""