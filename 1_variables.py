"""
Variables in python must begin with character literals or an underscore.
Starting character of a variable can be both upper case or lower case.
It is not necessary to assign a type to a python variable. Python assigns the variable type
following the binding of data to the variable. Rather the best analogy would
be to say that the variables in python do not have a type. Rather the data bound to the
variable is the one that has a type. Hence, if the variable is bound to another data of a
different type following an initial bind, the type of the variable also changes.
This is contrary to languages like Java and C where once the type of the variable has been
declared it cannot be reassigned to a different type of data.
Due to these reasons it is rather said "variable is bound to the data" rather than
"data is assigned to the variable" because the variable serves as a label that has been
bound to a value.
"""
name = "Sitanshu"
age = 31

# The type of the variable that has been analysed by Python can be seen using the type function
print(type(name))
print(type(age))

# Now if we change the value of the variable age from integer to String:
age = "31 years"
print(type(age))