# object oriented programming
class Person:

    # constructor
    def __init__(self,name,age,gender,height):
        # properties
        self.name = name
        self.age =  age
        self.gender = gender
        self.height = height

    # function
    def eat(self):
        print("eat")

    def walk(self):
        print("walk")

    def getName(self):
        return self.name
    def getAge(self):
        return self.age

# object
person = Person("Harish",20,"male",6.5)

person.eat()
person.walk()
print(person.name)
print('\n')

person2 = Person("Peter",25,"male",6)
person2.eat()
person2.walk()
print(person2.name)
print('\n')

# OOP inheritance
class Person:

    # constructor
    def __init__(self,name,age,gender,height):
        # properties
        self.name = name
        self.age =  age
        self.gender = gender
        self.height = height

    # function
    def eat(self):
        print("eat")
    def walk(self):
        print("walk")

    def getName(self):
        return self.name
    def getAge(self):
        return self.age

class Student(Person):  # the Student class hv all the properties & functions of the Person class
    # properties
    rollNo = 0
    marks = 100

    # functions
    def takeclass(self):
        print('Attend the class')

# Inhertance obeject
student = Student('tejal',15,'female',5.4)
student.eat()
student.takeclass()

