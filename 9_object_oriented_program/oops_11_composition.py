"""
Composition is design technique in object-oriented programming where a class contains an
object of another class. In composition the contained object does not exist independently of
container class. If the container class instance is destroyed then the contained class
object is also destroyed. Please refer to the following example:
"""


class Engine:
    def __init__(self, capacity):
        self.capacity = capacity

    def start(self):
        print("Engine started")


class Car:
    def __init__(self, capacity):
        self.engine = Engine(capacity)

    def start(self):
        print("Car started")
        self.engine.start()


my_car = Car(2000)
my_car.start()

"""
As illustrated in the above code, we have 2 classes namely Engine and Car. We create an 
instance of class Engine inside the Car class Constructor and initialise it. We access the 
start() method of the Engine class from the start() method of the Car class.
In this case the lifetime of the Engine class instance is the same as that of the Car class 
instance. The Engine class object will be destroyed once the Car class object is destroyed.

Inheritance and Composition both the concepts aim to achieve code reuse and build 
relationships between classes. However, they are both different in their approach and 
implementation.
1.  Inheritance is an 'is-a' relationship where as Composition is a 'has-a' relationship.
2.  Composition focuses on reusing functionality by assembling objects, while inheritance
    focuses on reusing behavior by deriving classes.
3.  Composition promotes loose coupling between classes, as the contained objects can be 
    replaced or modified without affecting the container class. On the other hand, 
    inheritance can lead to tight coupling between classes, as changes in the base class can
    affect all its subclasses.

Let's use another example. Please refer below:
"""


class Wing(object):
    def __init__(self, ratio):
        self.ratio = ratio

    def fly(self):
        if self.ratio > 1:
            print("Weeee, this is fun")
        elif self.ratio == 1:
            print("This is hard work. But i am flying.")
        else:
            print("I will just walk.")


class Duck(object):

    def __init__(self):
        self._wing = Wing(1.8)

    def walk(self):
        print("Waddle, waddle, waddle")

    def swim(self):
        print("Come on in, the water's lovely")

    def quack(self):
        print("Quack, quack")

    def fly(self):
        self._wing.fly()


donald = Duck()
donald.fly()

"""
A more real world application of a composition will be in reading an html document. Html 
document has a header, has a body and has a line containing the html version information. 
Note we use the term 'has a' which should ring a bell. We use compositions wherever we 
encounter a 'has-a' relationship. Lets check that out:
"""


class Tag(object):
    def __init__(self, name, content):
        self.start_tag = "<{}>".format(name)
        self.end_tag = "</{}>".format(name)
        self.content = content

    def __str__(self):
        return "{0.start_tag}{0.content}{0.end_tag}".format(self)

    def display(self, file=None):
        print(self, file=file)


"""
Class Tag will serve as a superclass for the remaining classes of this program. Tag class has
3 attributes, start_tag, end_tag and content.
It also has a display method which can either print the html tags to the console or a file.
"""


class DocType(Tag):
    def __init__(self):
        super().__init__('!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01//EN" '
                         'http://www.w3.org/TR/html4/strict.dtd', '')
        self.end_tag = ''


"""
An html document is broadly divided into 3 entities. The document type, the header and the 
body. The above class deals with the document type. The document type is the first line of 
an html document and usually doesn't have an ending tag. The DocType class is a subclass of 
the class Tag and uses the Tag class constructor to initialise the object.
"""


class Head(Tag):

    def __init__(self, title=None):
        super().__init__('head', '')
        if title:
            self._title_tag = Tag('title', title)
            self.content = str(self._title_tag)


"""
The head is the 2nd entity of an html document and is dealt by the above class Head. The 
Head class inherits the class Tag and makes use of the the Tag class constructor to 
initialise the object of the class. However, simultaneously it also possesses implementation
of its own in its constructor for its contents.
"""


class Body(Tag):

    def __init__(self):
        super().__init__('body', '')   # body contents will be built up separately
        self._body_contents = []

    def add_tag(self, name, contents):
        new_tag = Tag(name, contents)
        self._body_contents.append(new_tag)

    def display(self, file=None):
        for tag in self._body_contents:
            self.content += str(tag)

        super().display(file=file)


"""
The Body class is a subclass of the Tag class. However, it also implements composition in 
order to add contents to the body of the html document. This is a good example that 
inheritance and composition can also be used in conjunction to achieve our required goals 
and one need not have to choose between the two.
"""


class HtmlDoc(object):

    def __init__(self, title=None):
        self._doc_type = DocType()
        self._head = Head(title)
        self._body = Body()

    def add_tag(self, name, contents):
        self._body.add_tag(name, contents)

    def display(self, file=None):
        self._doc_type.display(file=file)
        print('<html>', file=file)
        self._head.display(file=file)
        self._body.display(file=file)
        print('</html>', file=file)


"""
The HtmlDoc class does not inherit any user defined class and purely uses composition to 
create the final html document. It initialises the objects of all the above mentioned 
classes and uses them to create a final html doc.
"""


if __name__ == '__main__':
    my_page = HtmlDoc('Demo Html Document')
    my_page.add_tag('h1', 'Main heading')
    my_page.add_tag('h2', 'sub-heading')
    my_page.add_tag('p', 'This is a paragraph that will appear on the page')
    with open("test.html", "w", encoding="utf-8") as test_doc:
        my_page.display(file=test_doc)