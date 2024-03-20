"""
Inheritance in Python is a fundamental concept in object-oriented programming (OOP) where
a new class, known as the derived class or subclass, can inherit attributes and methods from
an existing class, known as the base class or superclass. This enables code reuse and allows
for creating a hierarchy of classes where subclasses can extend or modify the behavior of
their superclass. The basic syntax in order to inherit a class is as follows:
class <ClassName>(<SuperClassName>):
Python supports several types on inheritance:
1.  Single Inheritance: When a subclass/child class inherits from a single superclass/parent
    class, it is called single inheritance.
2.  Multilevel Inheritance: In multilevel inheritance a subclass inherits from another
    subclass. Meaning if we have 3 class A, B and C. C inherits from B and B inherits from A.
    Hence, C is the subclass of B and B is the subclass of A.
3.  Hierarchical Inheritance: When multiple subclasses inherit from a single superclass it
    is called hierarchical inheritance. example: A is a superclass and B, C and D are
    subclasses that inherit from class A.
4.  Multiple Inheritance: When there are more than one superclass for a single subclass,
    it is called multiple inheritance. example: A and B are superclasses and C is a subclass
    that inherits from both A and B.
5.  Hybrid Inheritance: Hybrid inheritance is a combination of 2 or more types of inheritance.

Although Python supports all these kinds of inheritance, generally use of multiple
inheritance is discouraged. We know that Java doesn't support multiple inheritance for classes.
Similarly, combinations in hybrid inheritance that include multiple inheritance are also
discouraged in python.

When class B inherits from class A, all the members of class A become available to class B
for use.
In the following program we have are going to use an example of Hierarchical Inheritance. We
are using the examples of a Monsters class.
"""
import random


class Monster(object):
    def __init__(self, name="Goblin", hit_points=1, lives=1):
        self.name = name
        self.hit_points = hit_points
        self.lives = lives
        self.reset_hp = hit_points
        self.alive = True

    def damage(self, damage):
        remaining_hp = self.hit_points - damage
        if remaining_hp > 0:
            self.hit_points = remaining_hp
            print(f"Took damage of {damage}")
        else:
            self.lives -= 1
            if self.lives > 0:
                self.hit_points = self.reset_hp
                print(f"Lost a life. Hp reset to {self.hit_points}")
            else:
                print(f"{self.name} is dead.")
                self.hit_points = 0
                self.alive = False

    def __str__(self):
        return "Name: {0.name}, Lives: {0.lives}, Hit points: {0.hit_points}".format(self)


"""
The above class Monster will acts as the parent class in our program example. We will now 
proceed to create The sub classes for the Monster.
"""


class Goblin(Monster):
    pass


"""
The above class Goblin inherits from the class Monster. Notice that we do not provide a 
definition inside the Goblin class, rather we provide the pass keyword. The 'pass' keyword is a 
null operation. It doesn't do anything when executed. It's typically used as a placeholder 
where syntactically some code is required, but you don't want to execute any code.
"""


class Slime(Monster):
    def __init__(self, name, hit_points):
        Monster.__init__(name=name, hit_points=hit_points)


"""
The above class Slime is a subclass of the Monster class. It inherits the properties and 
methods of the Monster class. In this class we have defined the __init__ method which in 
turn calls the __init__ method of the Monster Class(superclass) to initialise the instance 
of the Troll object. We can see the result in line 
"""


class Troll(Monster):
    def __init__(self, name):
        super(Troll, self).__init__(name=name, hit_points=20, lives=1)

    def grunts(self):
        print(f"Me {self.name}. {self.name} stomp you")


"""
The above Troll class is also a subclass of the Monster class. It inherits the properties 
and methods of the Monster class. In the class we have defined the __init__ method the same 
way as that of the Slime class. The only difference is we have used the super() method with 
the class name and the current instance passed as arguments to access the superclass 
constructor.
Also, we can notice another difference. Although the Slime class does not differ from the 
Monster class in any respect. The Troll class has one additional behavior, the 'grunts()' 
method. Child classes can have their own set of methods and attributes that are different 
from the parent class. We can see the result in line 
"""


class Vampire(Monster):
    def __init__(self, name):
        super().__init__(name=name, hit_points=15, lives=3)

    def dodge(self):
        if random.randint(1, 3) == 3:
            print(f"***{self.name} dodged the attack***")
            return True
        else:
            return False

    def damage(self, damage):
        if not self.dodge():
            super().damage(damage=damage)


"""
The above Vampire class is a subclass of the Monster class. The __init__ method of the 
Vampire class is very similar to that of the Troll class except, we are calling the super() 
method without any arguments. This illustrates that providing arguments in the super() 
method is entirely optional.
The Vampire class also has a method dodge() which calculates the chances of a vampire dodging 
the attack. The Vampire uses its own implementation of the damage() method. Whenever the 
damage() method will be called using the Vampire class object, the damage() method in the 
Vampire class will be invoked rather than that of the Monster class. From a real world 
perspective, a vampire has the chance of dodging an attack, and if the attack is dodged the 
vampire will not take any damage. This is called method overriding. Method overriding 
happens when the parent and the child class have methods with the same signature. When the 
method is invoked through the child class, then the parent class method will be overridden 
and the child class method will be executed. We will see the results in line  
"""


class Slime(Monster):
    def __init__(self, name, hit_points=10):
        super().__init__(name=name, hit_points=hit_points, lives=3)

    def recovery(self, damage):
        if damage < 5:
            recovered_hp = 1
        else:
            recovered_hp = int(damage*0.2)
        adjusted_damage = int(damage - recovered_hp)
        print(f"Recovered hp by {recovered_hp}")
        return adjusted_damage

    def damage(self, damage):
        super().damage(damage=self.recovery(damage))


"""
The Slime class is a subclass of the Monster class. The Slime class is very similar to the 
Vampire class in its implementation of the __init__ method. 
Slime is given the ability to recover any damage. Hence, any damage inflicted on a Slime 
will have its effects reduced by 2self percent. Accordingly the damage method has been 
overridden for the Slime class to make the adjustment. We will see the results in line
"""


class DemonSlime(Slime):
    def __init__(self, name):
        super().__init__(name=name, hit_points=15)

    def damage(self, damage):
        if random.randint(1, 3) == 3:
            print(f"***{self.name} dodged the attack***")
        else:
            super().damage(damage=damage)


"""
The Demon Slime class is the subclass of Slime. In turn Slime class is the subclass of Monster.
This inheritance is and example of Multilevel inheritance. DemonSlimes are very similar to 
Slimes in almost all the attributes and behaviors except Demon Slimes are also capable of 
dodging attacks. The damage() method has been overridden to accommodate this behavior of 
Demon Slimes. We will see the results in line  
"""


goblin = Goblin("Gobo")
print(goblin)  # Output: Name: Gobo, Lives: 1, Hit points: 1
goblin.damage(2)
print(goblin)

print("#"*95)
troll = Troll("Rock")
print(troll)
troll.grunts()
troll.damage(5)
print(troll)

print("#"*95)
vampire = Vampire("Dracula")
print(vampire)
while vampire.alive:
    vampire.damage(4)
    print(vampire)

print("#"*95)
slime = Slime("Roxi")
print(slime)
while slime.alive:
    slime.damage(2)
    print(slime)


print("#"*95)
demonslime = DemonSlime("Rimuru")
print(demonslime)
while demonslime.alive:
    demonslime.damage(2)
    print(demonslime)

"""
If we run all the above code it will run just fine.
There are a few important things to understand:
1.  A subclass may or may not have any members.
2.  Subclass may or may not have any constructors. In that case the objects of the class are 
    initialised using the parent class constructor.
3.  We can invoke the __init__ method of the parent class through the init method of the 
    child class. In order to do that we can use the Parent class name, super() method with 
    child class name and current instance as arguments or just the super() method without 
    any arguments.
4.  Child classes can have their own set of unique attributes or methods.
5.  We can override existing parent class methods by creating methods with the same 
    signature in the child class.
6.  We can also invoke the parent class version of the overridden method from within the 
    child class version of the overridden method.
7.  The __str__ method is used to print the contents of a class object. 
"""


