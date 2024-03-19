"""
In the last lesson we covered the most parts about the attributes of class and attributes of
instance. In this lecture we will cover the methods in a class in more detail. Please refer to
the below class and its corresponding code. We will discuss the nuances of the code as we go.
"""

import datetime


class Account:
    """
    Simple class to create a class, calculate withdrawals, deposits and show balance.
    """

    @staticmethod
    def _current_time():
        current_date_time = datetime.datetime.now()
        return current_date_time
    """
    The method in line 16 is a python static method. A python static method is similar to a 
    static method in JAVA. A static method in annotated with '@staticmethod'. Also, a static 
    method does not take self as its first parameter.
    Static methods belong to the class instead of the object. They are invoked through the
    class. Hence, they do not take 'self' as its first argument since it does not operate on 
    instance variables.
    """

    def __init__(self, name, balance):
        self._name = name
        self.__balance = balance
        self._transaction_list = [(Account._current_time(), balance)]
        print(f"Account created for {self._name}")
        self.show_balance()

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print("Deposit Successful")
            self.show_balance()
            self._transaction_list.append((Account._current_time(), amount))

    def withdrawal(self, amount):
        if amount < self.__balance:
            self.__balance -= amount
            self._transaction_list.append((Account._current_time(), -amount))
        else:
            print("Not enough balance in the account.")
        self.show_balance()

    def show_transactions(self):
        for date, amount in self._transaction_list:
            if amount > 0:
                trans_type = "deposited"
            else:
                trans_type = "withdrawn"
            print(f"Amount {amount} {trans_type} on {date} local time")

    def show_balance(self):
        print(f"Account balance: {self.__balance}")


"""
Important thing to note in line 16, 29, 30, 31 is that the method/variable name starts with a 
single '_' character. The prefix '_' is more than just a character and used to indicate that a
method or an attribute is protected.
This brings us to the question of access modifiers. We know the concept of access modifiers 
from JAVA. Python also supports the access modifiers concept but there are differences in 
the implementation between Python and JAVA.
In Python, attributes and methods inside a class are by default public in nature, 
meaning they can be accessed from anywhere, both inside the class and outside. There's no 
explicit keyword defining  public members. Instead, they are simply named without any 
preceding underscores.
Python does not have strict concept of private and protected members like Java and there are
keywords that are used to differentiate between private protected and public members. Instead,
python uses naming conventions to indicate how a member should be treated and leaves the 
choice of following conventions to the discretion of the programmers. We can very well use 
private and protected members outside of the class in python, but doing so will sooner or 
later cause logical issues in our code (not syntactical)
By convention private members in python should be prefixed with 2 underscore('__') characters.
Similarly protected members in python should be prefixed with one underscore('_') character.
Technically python does not enforce limits on access of methods and attributes. The naming 
conventions simply act as indicators for programmers to treat the data members as so.
Conventionally private members should only be accessed through methods in the same class and
not outside the class.
On the other hand protected members should only be accessed by the members of the class and 
the subclass (child class).
"""

if __name__ == '__main__':
    sitanshu = Account("Sitanshu", 10000)
    print(sitanshu._name)
    # print(sitanshu.__balance)
    print(sitanshu.__dict__)
    print(sitanshu._Account__balance)
    sitanshu.deposit(1000)
    sitanshu.withdrawal(2000)
    sitanshu.show_transactions()

"""
In the above code, in line 91 we can see that the editor is giving warning for accessing the 
protected attributes of the class directly outside the class. However, when we execute the code
we receive no error in output. Hence, although Python does not restrict us from accessing 
protected attributes/ methods of the class out side, it is still not a best practice.

We also see in line 92 some commented code where we are trying to access the private variable
'__balance'. The line of code when uncommented will give and error message "Unresolved 
attribute reference '__balance' for class 'Account'", meaning the compiler was not able to 
locate the variable '__balance' inside the class Account. When we check the namespaces of 
the instance in line 93 we see something line "_Account__balance': 10000" in the output.
This is called name mangling. Name mangling is a technique used in python that is 
effectively handled by the interpreter to make class members effectively private by adding a 
prefix "_<ClassName>" to the private variable name. This prefix makes it more difficult to 
access these members from outside the class, helping to prevent accidental name clashes and 
providing a level of encapsulation. However, as mentioned before we can still access the 
value outside of the class using the variable name "_Account__balance".

We use the statement "if __name__ == '__main__':" in line 89. It is a common idiom used in 
python scripts and modules. It checks if the script contained within the block is being run 
directly as the main program or if it is being imported as a module into another script.
In general when a python script is imported as a module, all the executable code within the 
script is executed automatically. For example, imagine the code from line 90 onwards was 
written outside the if block. When this particular 'oops_3_methods.py' file is imported as module to 
another script, those line of code will be executed automatically. That might not be desirable.

Lets understand the statement "if __name__ = '__main__':". '__name__' is a special built in 
variable in python that represents the name of the current module or script. The value 
returned by the '__name__' variable in the corresponding script or module will be '__main__'.
If the current script was imported to another script as a module, all the executable code in
this module should be analysed and executed as a part of that module. However, the '__name__'
variable will return the name of that module instead of '__main__'. This is will not satisfy
the 'if' condition and hence, the code within the block will not be executed when imported 
to another module.
"""
