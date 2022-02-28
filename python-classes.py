from email.policy import default
from abc import ABC, abstractclassmethod
from operator import contains


class Point:
    # class attribute shared across all instances/objects
    default_color = "red"

    def __init__(self, x, y):
        # instance attributes
        self.x = x
        self.y = y

    # Class methods - when initilizing instance method is complex= also called factory method
    @classmethod
    def zero(cls):
        return cls(0, 0)

    # __str_ magic method
    def __str__(self):
        return f"({self.x}, {self.y})"
    # compare magic

    def __eq__(self, __o: object):
        return self.x == __o.x and self.y == __o.y

    def draw(self):
        print(f"Instance attributes=> x is: {self.x}, y is : {self.y}")
        print(f"Class attributes=> default_color is: {self.default_color}")


print()
# create object
# change the class attribute

Point.default_color = "yellow"
point = Point(1, 2)
point.draw()
point2 = Point(3, 4)
point2.draw()
# classs method
print()
print("Factory method")
point_class_method = Point.zero()
point_class_method.draw()

print()
print("__str__ magic method")
print(point.__str__)
print(str(point))
print()
print("Comparing objects")
point1 = Point(1, 3)
point2 = Point(1, 3)

print("object1 equal to object 2 ", point1 == point2)
print()

# Making custom containers


class CloudTag:
    def __init__(self) -> None:
        self.__tags = {}

    def add(self, tag):
        self.__tags[tag.lower()] = self.__tags.get(tag.lower(), 0) + 1

    def getitem(self, tag):
        return self.__tags.get(tag.lower(), 0)

    def setitem(self, tag, count):
        self.__tags[tag.lower()] = count

    def len(self):
        return len(self.__tags)


cloud = CloudTag()

cloud.add("Python")
cloud.add("Python")
cloud.add("python")
cloud.add("mwangi")
# exception as it's private
# print(cloud.tags)
print(cloud.getitem("sam"))
cloud.setitem("mwanGi", 3)
# print(cloud.tags)
print(cloud.len())

# property - private we prefix the attributes or methods using __(double underscore)
print(cloud.__dict__)
print(cloud._CloudTag__tags)

# inheritance
# base class


class Animal:
    def __init__(self) -> None:
        print("Animal contructor")
        self.age = 1

    def eat(self):
        print("eats")
# inheritace
# child class


class Mammal(Animal):
    def __init__(self):
        super().__init__()
        self.weight = 10
        print("Mammal contructor")

    def walk(self):
        print("walks")


class Fish(Animal):
    def swim(self):
        print("swims")


animal = Animal()
mammal = Mammal()
print(mammal.age)
print(mammal.eat())
print(mammal.walk())
print(isinstance(mammal, Animal))
print(issubclass(Mammal, Animal))
print(issubclass(Animal, object))
# method overriding
print(mammal.weight)
print(mammal.age)

print()
# Abstract class and polymorphism
# duck typing we can do away with abstract class
#  below UIControl and remove it to the 2 classes below and it will still work
print("Abstract class and polymorphism")


class UIControl(ABC):
    @abstractclassmethod
    def draw(self):
        pass


class Dropdown(UIControl):
    def draw(self):
        print("drop down")


class TextBox(UIControl):
    def draw(self):
        print("Textbox")


def draw_stat(controls):
    for control in controls:
        control.draw()


dropdown = Dropdown()
textbox = TextBox()
draw_stat([dropdown, textbox])
print(isinstance(dropdown, UIControl))

# extending built-in class

print()
print("Extend built-in classes")


class Text(str):
    def duplicate(self):
        return self+self


text = Text("Mwangi")
dupres = text.duplicate()
print(dupres)


class TrackList(list):
    def append(self, __object):
        print("append called")
        return super().append(__object)


list = TrackList()
list.append("1")
