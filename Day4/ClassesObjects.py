# A class is a model or plan to create objects. The object of a class are also called instances.
# Class contains attributes which are nothing but a variable.
# A class contains methods which are useful to process variables.

# A class is created with keyword class and then writing the classname.
# self variable : When instance is created, it contains memory address , that address is internally passed to the self default variable.


class Student:

    def __init__(self):
        self.name = 'sohan'
        self.age = 28
        self.salary = 50000

    def talk(self):
        print("My name is {}".format(self.name))
        print("My age is {}".format(self.age))
        print("My salary is {}".format(self.salary))


# creating object of student class. Whenever we are creating the object of class , internally heap memory will be allocate
# then default costructor will be called __init__(self) which will initialize the variables ,then allocated memory location
# will be passed to object

s1 = Student()

# calling instance method
s1.talk()

# Accessing variables using instance name
print("Using instance name:", s1.name)


# parametarized  constructor : During the object creation we can pass the values to initialize the variables
class Student:

    def __init__(self, n="no name", a=25, s=1111):
        self.name = n
        self.age = a
        self.salary = s

    def talk(self):
        print("My name is {}".format(self.name))
        print("My age is {}".format(self.age))
        print("My salary is {}".format(self.salary))


# creating object of student class. Whenever we are creating the object of class , internally heap memory will be allocate
# then default costructor will be called __init__(self) which will initialize the variables ,then allocated memory location
# will be passed to object

s1 = Student()
s2 = Student('sohan', 28, 50000)

# calling instance method
print("Default constructor")
s1.talk()

print("parametarized constructor")
s2.talk()


# Types of variables
# 1) instance variables : instance variables whose separate copy is created in every instances. If  the variable in
# one instance is updated it will not affect the variable in another instance
# 2) class variables /static variables : whose single copy available to al instances. If we modify the copy of class
# variable in an instance it will modify all the copies in other instances

# Namespaces : represents memory block where names are mapped to objects
# Class and instances maintain their own namespaces

class Student:
    salary = 50000

    def __init__(self, n="no name", a=25):
        self.name = n
        self.age = a

    def talk(self):
        print("My name is {}".format(self.name))
        print("My age is {}".format(self.age))
        print("My salary is {}".format(self.salary))

    @classmethod
    def modify(cls):
        cls.salary += 10000

    def modify_instance(self):
        self.salary += 10000


s1 = Student('mohan', 29)
s2 = Student('sohan', 28)
print("code for class variable change : ")
print("s1 object variables before change: ")
s1.talk()
s2.talk()
print("s1 object variables after change: ")
Student.modify()

s1.talk()
s2.talk()

print("code for instance variable change : ")
print("modifying instance variable:")
s1.modify_instance()
s1.talk()
s2.talk()


# Types of methods :
# Instance Methods : to act on the instance variables , these methods are created. the memory address of the
# instance is pass through self keyword ,which is pass in every instance method as default parameter

# Example for student pass or fail

class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def display(self):
        print("%s got %d" % (self.name, self.marks))

    def calculate(self):
        if self.marks >= 300:
            print("{} is passed".format(self.name))
        else:
            print("{} is failed".format(self.name))


n = int(input("Enter the number of student:"))
i = 1
while i <= n:
    name = input("Enter the name of student:")
    marks = eval(input("Enter the marks: "))
    s1 = Student(name, marks)
    s1.display()
    s1.calculate()
    i += 1
