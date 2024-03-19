"""
Getters and Setters are methods in a class that are used to access private and protected
members in a class. For those experienced in Java it is a common concept. Python also
implements the same concept for its classes. However, using getters and setters in a program
is not as popular methodology in Python as it is in Java. The reason being, while Java
enforces the rules laid the access specifiers on the attributes of a class, python does not
forcibly restrict access to the private and protected members. Hence, although we will learn
the concept of getters and setters from a python perspective, we will not delve into in depth
details of getters and setters.
A getter is a class method that is used to read the private and protected data
attributes of the class. Similarly, a setter is a class method that is used to assign
value to a class attribute. Please refer to the following program.
"""


class MyClass:
    def __init__(self):
        self._my_variable = None

    # Getter method:
    def get_my_variable(self):
        return self._my_variable

    # Setter Method:
    def set_my_variable(self, value):
        self._my_variable = value

    my_variable = property(get_my_variable, set_my_variable)


obj = MyClass()
obj.my_variable = 50
print(obj.my_variable)  # Output: 50

"""
In the above program we have a class 'MyClass' with only one protected attribute '_my_variable'
that is initialised to 'None'. The getter and setter methods are self explanatory.
In line 28 we use the property() method to create a property object 'my_variable'. 
In Python, the property() method is a built-in function that creates and returns a property 
object. Properties are special attributes that provide getter, setter, and deleter methods for
accessing and modifying class attributes. The property() method allows you to define these 
getter, setter, and deleter methods in a more concise and readable way. It has 4 arguments 
namely:
1.  'fget': A method to get the attribute value.
2.  'fset': A method to set the attribute value.
3.  'fdel': A method to delete the attribute value.
4.  'doc':  A docstring for the property.

In the above code The my_variable property behaves like a regular attribute but internally 
calls the getter and setter methods to access and modify the value of _my_variable. We 
create the property object by passing the optional getter and setter method names as arguments.
Assigning value to the my_variable through the class object uses the setter method to assign
value to the _my_variable protected attribute. When accessing the value with the property 
object using the class object, the getter method is used to access the _my_variable 
protected attribute value.
There is another way to use the property method and that is through the decorators. Please 
refer to the code below.
"""


class NewClass(object):
    def __init__(self):
        self.__my_variable = None

    @property
    def my_variable(self):
        return self.__my_variable

    @my_variable.setter
    def my_variable(self, value):
        self.__my_variable = value


obj1 = NewClass()
obj1.my_variable = 20
print(obj1.my_variable)

"""
When using the decorators one must keep in mind that the method names for both the setter 
and the getter should be same. In the above code we are using the name 'my_variable' as the 
name for both the setter and the getter. It serves as the property name which will then be 
used to access the methods.
The getter method should be created first followed by the setter method for the attribute. 
The decorator '@property' should be used to mark the getter method. This tells the 
interpreter that the name of the getter method is now the property name.The setter 
method should be marked with the decorator @<property_name>.setter (in our case property 
name is 'my_variable'.
'my_variable' can then be used as the attribute of the class which when accessed through the
class object will invoke the getter or the setter method based on requirement as shown above
in line 75 and 76.
"""

