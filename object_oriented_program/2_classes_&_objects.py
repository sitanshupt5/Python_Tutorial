"""
In Python we can create a class using the class keyword. Although there is no case
restriction for a class name in python unlike Java ( where a class name is mandated to start
with upper case character), its still common convention according to python style guide PEP
8 to have a class name start with upper case character in order to avoid convention and make
the code more readable. Also, while creating a class one must keep in mind to provide a
gap of 2 lines before and after the class definition just like in the case of functions.
Please refer to the below code:
"""


class Kettle(object):

    power_source = "electricity"

    def __init__(self, make, price):
        self.make = make
        self.price = price
        self.on = False

    def toggle_switch(self):
        if self.on:
            self.on = False
        else:
            self.on = True

    def display_values(self):
        print("Make: {0.make}, Price: {0.price}, Switch: {0.on}".format(self))


"""
There are a few things to understand regarding the above code snippet. We will cover them on by
one:
1.  In line 12 we declare the class Kettle using syntax 'class Kettle(object)', 
    we can refer to it as declaration1 from here on. We can also declare it as just 
    'class Kettle', which we will refer from here on as declaration 2. In python 2 there was a 
    difference between both forms of declaration, where declaration1 supported a few extra 
    features as compared to declaration 2 as declaration 1 explicitly inherits from the 
    built in object class. However, there is no difference between the 2 declarations in 
    python 3, as the built in object class is now implicitly inherited irrespective of the 
    declaration style.
2.  In line 16 we define a method __init__(self, _, _). This method serves a user 
    defined contructor for the class. We already know from java that a constructor is used to
    instantiate a class. The 'self' keyword here represents the current instance of the 
    class and allows to access attributes and methods of that instance within the method.
    Conventionally self keyword is added automatically in any IDE when a method is created.
    It is very similar to the 'this' keyword in JAVA. Hence, we use self.param in subsequent
    lines of code to refer to the parameter value for the instance.
3.  Finally it is important to note the print statement we used in line 28, where we have 
    implemented replacement values in a different style. It should be self explanatory that 
    we are only passing the instance into the format method and using it the call onto the 
    attributes of the instant in the replacement fields.

There are few terminologies in the above description that need to be cleared:
a.  Instance: instance is nothing but an object. Both names represent the same concept and 
    can be used interchangeably.
b.  Instantiate: Instantiation is just a fancy word for the process of creating an object.
c.  Attribute: Attributes are nothing but variables that are declared withing the scope of a
    class.
d.  Methods: Methods are functions that are declared within the scope of a class. Another 
    key difference between methods and functions is that the first argument of a method is
    'self'.

Now that we have understood the basics of creating a class and defining attributes and 
methods in it, we can move on to the basics of instantiating a class.
The most common and most basic method of creating an instance of the class is calling the 
class name followed by parenthesis. Please refer to the below code: 
"""

kettle1 = Kettle("Morphy Richards", 599)

"""
Instantiating an object calls the constructor of the class. We can pass values to the 
attributes of the instance by adding those attributes as arguments to the constructor and 
passing the corresponding values during the instantiation. That is what we have precisely 
done in the above code snippet.
Now that our attributes have been initialised we can print the values of these items by 
accessing them through the object. Please refer below:
"""
print("Make: {0.make}, Price: {0.price}, Switch: {0.on}".format(kettle1))

# Output: Make: Morphy Richards, Price: 599, Switch: False

"""
We can also access the methods in the class now that the instance has been created. For 
starters lets use the toggle_switch() method followed by the display_values() method. We 
will be invoking the methods in 2 different ways.
"""
# Method 1:
kettle1.toggle_switch()

# Method 2:
Kettle.display_values(kettle1)
# Output: Make: Morphy Richards, Price: 599, Switch: True

"""
In the code in line 90 we are calling a method through the class name. In such case the 
method needs to know the instance it is working on.
Generally, when we call a method through the object, the self argument of the method is 
passed implicitly and the method knows the instance whose attributes it has to work on.
On the other hand when calling the method through the class name we have explicitly pass the
instance we are working on.
So far, the concepts of class and objects in python that we have visited are very much 
similar to those in JAVA. But there are still differences. For example we can add variables 
to instance that are not present in the class. Please refer to the below example:
"""
pigeon = Kettle("Pigeon", 1099)
prestige = Kettle("Prestige", 999)

pigeon.power = 1200

print(pigeon.power)     # Output: 1200
# print(prestige.power)   Output: AttributeError: 'Kettle' object has no attribute 'power'

"""
In the above case in line 107 we had created another variable 'power' that unique to the 
pigeon instance and  assigned value to it. We are also able to print the value in line 109.
However, if we try to print the value of power for the prestige instance we receive and 
instance error. Variables in python come into existence once they are initialised. 'power' 
is an instance variable that is unique to the pigeon instance and cannot be accessed by any 
other instance unless it has been initialised for that instance.
Hence, there can be instances created from the same class templates but have additional/ 
different attributes.
So far we have seen attributes that belong to an instance. However there can also be 
attributes that belong to the class. The values of such attributes are shared by all the 
instances of the class. These are called class attributes.This would be the equivalent of a 
static variable in JAVA. The variable 'power_source' in line 14 is a class attribute. Please
refer to the below code to understand the properties of a class attribute.
"""
# print the value of the power_source attribute using the class.
print(Kettle.power_source)      # Output: electricity
# print the value of the power_source attribute using the instance pigeon
print(pigeon.power_source)      # Output: electricity
# print the value of the power_source attribute using the instance prestige.
print(prestige.power_source)    # Output: electricity

# Changing the value of the power_source attribute using the prestige instance.
prestige.power_source = "solar power"

# print the value of the power_source attribute using the class.
print(Kettle.power_source)      # Output: electricity
# print the value of the power_source attribute using the instance pigeon
print(pigeon.power_source)      # Output: electricity
# print the value of the power_source attribute using the instance prestige.
print(prestige.power_source)    # Output: solar power

"""
In the above code we can see that for a class attribute, if update the value using an 
instance of the class, the value of the attribute get updated only for that instance. This 
is because we are not able to make any changes to the class attribute value through the 
instance. Instead we are creating and initialising an instance variable with the same name as 
the class variable. We can prove that using the '__dict__' method. Please refer to the code 
below.
"""
# printing the namespaces of the Kettle class in the form of a dictionary.
print(Kettle.__dict__)      # Output: {'__module__': '__main__', 'power_source': 'electricity', '__init__': <function Kettle.__init__ at 0x000001CDA6B094E0>, 'toggle_switch': <function Kettle.toggle_switch at 0x000001CDA6B0A340>, 'display_values': <function Kettle.display_values at 0x000001CDA6B0A3E0>, '__dict__': <attribute '__dict__' of 'Kettle' objects>, '__weakref__': <attribute '__weakref__' of 'Kettle' objects>, '__doc__': None}
# printing the namespaces for the pigeon instance.
print(pigeon.__dict__)      # Output: {'make': 'Pigeon', 'price': 1099, 'on': False, 'power': 1200}
# printing the namespaces for the prestige instance.
print(prestige.__dict__)    # Output: {'make': 'Prestige', 'price': 999, 'on': False, 'power_source': 'solar power'}
""" 
In the above outputs we can see that the namespaces of the pigeon instance does not contain a 
power_source attribute and it is not supposed to since 'power_source' is a class attribute.
But since we explicitly declared and initialised a value of power_source for the prestige 
instance, it gets added to the namespace. Hence, the value of 'power_source' that we print 
in line 145 is the variable of the instance 'prestige' rather the the class attribute.
What happens when we update the value through the class. Lets have a look:
"""
# Changing the value of the power_source attribute through the class:
Kettle.power_source = "battery power"

# print the value of the power_source attribute using the class.
print(Kettle.power_source)      # Output: battery power
# print the value of the power_source attribute using the instance pigeon
print(pigeon.power_source)      # Output: battery power
# print the value of the power_source attribute using the instance prestige.
print(prestige.power_source)    # Output: solar power

"""
This time we see that the value of the class attribute is updated for all instances except 
for the ones whose values for that attribute have been set explicitly. Hence, when we 
updated the class attribute power_source value to 'battery power', it also got reflected for
pigeon instance. However, since we had explicitly set the value of power_source for the 
prestige instance, the change in value in line 153 was not reflected for it.
"""