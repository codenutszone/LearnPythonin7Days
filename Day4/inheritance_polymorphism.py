# Inheritance : Deriving new class from the existing classes such that new classes inherit all the members of the existing classes
# When object of child/derived  class is created , copy of all class members are available to child class

class Teacher:
    def setName(self, n):
        self.name = n

    def setId(self, id):
        self.id = id

    def getName(self):
        return self.name

    def getId(self):
        return self.id


class Student(Teacher):
    def setMarks(self, m):
        self.marks = m

    def getMarks(self):
        return self.marks


s1 = Student()
s1.setId(1)
s1.setName('sohan')
s1.setMarks(99)

print(f"My id is {s1.getId()} ")
print(f"My name is {s1.getName()}")
print(f"My marks is {s1.getMarks()}")


# Constructor in Inheritance : like variables and methods,super class constructor is also available to the derived class

class Father:
    def __init__(self):
        self.property = 100000

    def display(self):
        print("Total property is {}".format(self.property))


class Son(Father):
    pass


s = Son()
s.display()


# Overriding Super class constructor and methods : if we write the constructor in sub class , only sub class constructor
# is available to sub class objects. That means super class constructor is replace by the child class constructor


class Father:
    def __init__(self):
        self.property = 100000

    def display(self):
        print("Total property is {}".format(self.property))


class Son(Father):
    def __init__(self):
        self.property = 800000


s = Son()
s.display()


# super method : if we want to use the super class constructor or method even after the overriding we have to use super() method

class Father:
    def __init__(self, property):
        self.property = property

    def display(self):
        print("Total property of father is  {}".format(self.property))
        print("Total property of son is  {}".format(self.property1))


class Son(Father):
    def __init__(self, property1=0, property=0):
        super().__init__(property)
        self.property1 = property1


s = Son(800000, 100000)
s.display()


# program to access base class constructor and method in child class using super()

class Square:
    def __init__(self, x):
        self.x = x

    def area(self):
        print("area of square is %d" % (self.x * self.x))


class Rectangle(Square):
    def __init__(self, x, y):
        super().__init__(x)
        self.x = x
        self.y = y

    def area(self):
        super().area()
        print("area of rectangle is %d" % (self.x * self.y))


x, y = [float(i) for i in input("enter the 2 element").split()]
r = Rectangle(x, y)
r.area()


# Types of inheritance :
# 1) single inheritance : Deriving one or more sub classes from a single base class is called single inheritance

class Bank:
    cash = 1000

    @classmethod
    def display_cash(cls):
        print(f"Total cash in Bank is  {cls.cash}")


class Sbi(Bank):
    pass


class Hdfc(Bank):
    cash = 200

    @classmethod
    def display_cash(cls):
        print("Total cash in Hdfc is {}".format(cls.cash + Bank.cash))


h = Hdfc()
h.display_cash()
s = Sbi()
s.display_cash()


# 2) Multiple inheritance :  Deriving sub classes from multiple base classes.
# but if sub class has a constructor , it overrides the super class constructor. hence super class constructor is not available to
# sub class. if we call the super class constructor , it will call the constructor of left side of the class only

# To overcome this problem , we use method resolution order approach (mro)

class A:
    def method(self):
        print("A class method")
        super().method()


class B:
    def method(self):
        print("B class method")
        super().method()


class C:
    def method(self):
        print("C class method")


class X(A, B):
    def method(self):
        print("X class method")
        super().method()


class Y(B, C):
    def method(self):
        print("Y class method")
        super().method()


class P(X, Y, C):
    def method(self):
        print("P class method")
        super().method()


p = P()
p.method()
P.mro()


####################################
# Polymorphism :something exhibits the various forms
####################################

# Duck typing philosophy of python :
# 1) In python type system is dynamic , since the variable is implicitly declared
# 2) type system is strong because every variable or object has a type

class Dog:
    def bark(self):
        print("bow bow")


class Duck:
    def talk(self):
        print("quack quack")


class Human:
    def talk(self):
        print("hello hi")


def call_talk(x):
    x.talk()


d = Duck()
h = Human()
dg = Dog()

for i in d, h, dg:
    if hasattr(i, 'talk'):
        call_talk(i)

# Operator overloading
a = "sohan"
b = "mohan"
print(a + b)

x = [1, 2, 3]
y = [4, 5, 6]
print(x + y)


# Internally + operator calling x__add__(y). To add the two objects we need to override the __add__() method

class BookX:
    def __init__(self, pages):
        self.pages = pages

    def __add__(self, other):
        return self.pages + other.pages


class BookY:
    def __init__(self, pages):
        self.pages = pages


b1 = BookX(100)
b2 = BookY(150)

print(f"Total pages is {b1+b2}")
