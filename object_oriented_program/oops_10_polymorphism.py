"""
Polymorphism in python refers to the ability of different objects to respond to the same
method or function call in different ways. It allows objects of different classes with no
common parent to be treated as objects of a common superclass. Polymorphism enables code to be
written in a way that is more flexible, extensible, and reusable.
Polymorphism in python has two main forms:
1. Overriding
2. Duck Typing

We have already discussed how overriding of methods works in python in the inheritance module.
Duck Typing is a form of polymorphism in python where the type or class of an object is less
important than the methods it defines. If an object implements a particular method,
it can be used in a context where that particular method is expected, regardless of its
actual class or type.
Please refer to the below code example:
"""


class Duck(object):

    def walk(self):
        print("Waddle, waddle, waddle")

    def swim(self):
        print("Come on in, the water's lovely")

    def quack(self):
        print("Quack, quack")


class Penguin(object):

    def walk(self):
        print("Waddle, waddle, I waddle too")

    def swim(self):
        print("Come on in, but its a bit chilly this far south")

    def quack(self):
        print("Are you having a laugh? I am a penguin.")


def duck_test(duck):
    print("#"*95)
    duck.walk()
    duck.swim()
    duck.quack()


if __name__ == '__main__':
    donald = Duck()
    duck_test(donald)

    pingu = Penguin()
    duck_test(pingu)

"""
In the above example we see 2 classes each having the same methods walk(), swim() and quack().
Although it is clear that the functions execute different code for the individual classes. 
The function duck_test() takes an object as an argument and executes the walk(), swim() and 
quack() methods of the class for that particular object.
We can see that the code above between lines 51 to 55 give valid output. We are passing 
objects of different classes Duck and Penguin to the duck test method and both get executed.
Since both classes have the same methods, their instances are accepted as valid arguments.
This would be impossible in case of Java as it would lead to a type mismatch in arguments.
Since python is not a strongly typed language, this works.
Over here the function duck_test() gives different output for different arguments that have 
been passed. However, the code within the function remains the same. This is polymorphism.
"""