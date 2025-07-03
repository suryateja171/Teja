# class Person:
#     def display_info(self):
#         print("I am a person.")

# class Student(Person):
#     pass

# student= Student()

# student.display_info()



# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

# class Student(Person):
#     def __init__(self, name, age, grade):
#         super().__init__(name,age)
#         self.grade = grade
#     def details(self):
#         print(f"Name: {self.name }, Age :{self.age}, Grade : {self.grade}")

# Student=Student("Alice",18,"A")
# Student.details()





# class person:
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age

# class Student(person):
#     def __init__(self,name,age,average,grade):
#         super().__init__(name,age)
#         self.average = average
#         self.grade = grade
#     def details(self):
#         print(f"Name: {self.name }, Age :{self.age}, Average :{self.average}, Grade :{self.grade}")

# Student=Student("Bob",20,85.0,"B")
# Student.details()


# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age


# #MULTIPLE INHEHITANCE

#Task 1



      
# class Father:
#     def __init__(self):
#         print("Skilled in driving")
# class Mother:
#     def __init__(self):
#         print("Skilled in cooking")

# class Child(Father,Mother):
#     def details(self):
#         Father.__init__(self)
#         Mother.__init__(self)
# Child=Child()
# Child.details()



#Task 2


# class Employee:
#     def __init__(self,name,id):
#         self.name=name
#         self.id=id
# class Department:
#     def __init__(self,department):
#         self.department=department
# class Manager(Employee,Department):
#     def __init__(self,name,id,department):
#         Employee.__init__(self,name,id)
#         Department.__init__(self,department)
#     def details(self):
#         print(f"Name : {self.name}, ID : {self.id}, Department : {self.department}")
# i=Manager("John","101","HR")
# i.details()


#Task 3


# class Person:
#     def __init__(self, name):
#         self.name=name
# class Employee:
#     def __init__(self, id):
#         self.id=id
# class Professor(Person,Employee):
#     def __init__(self, name,id,subject):
#         Person.__init__(self,name)
#         Employee.__init__(self, id)
#         self.subject=subject
#     def display_info(self):    
#         print(f"Name : {self.name}, ID : {self.id}, Subject : {self.subject}")
# prof1 = Professor("Dr.Smith","P102","Physics")        
# prof1.display_info() 


# multilevel 
# task 1



# class Animal:
#     def sound(self):
#         print("Animals make sounds")

# class Mammal(Animal):
#     pass
# class Dog(Mammal):
#     def bark(self):
#         print("Dog says: Woof Woof!")

# my_dog=Dog()
# my_dog.bark()                



#task 2


# class Shape:
#     def describe(self):
#         print("I am a shape")

# class Circle(Shape):
#     def describe(self):
#         print("I am a Circle")

# class Square(Shape):
#     def describe(self):
#         print("I am a Square")


# c = Circle()
# s = Square()


# c.describe()
# s.describe()


#task 3

# class Employee:
#     def job_role(self):
#         print("I am an Employee")


# class Developer(Employee):
#     def job_role(self):
#         print("I am a Developer")

# class Tester(Employee):
#     def job_role(self):
#         print("I am a Tester")


# dev = Developer()
# test = Tester()


# dev.job_role()
# test.job_role()



#task 3



# class LibraryMember:
#     def __init__(self, name):
#         self.name = name

# class StudentMember(LibraryMember):
#     def __init__(self, name, borrow_limit):
#         super().__init__(name)  
#         self.borrow_limit = borrow_limit

#     def display_info(self):
#         print(f"Student Name   : {self.name}")
#         print(f"Borrow Limit   : {self.borrow_limit} books")

# class FacultyMember(LibraryMember):
#     def __init__(self, name, borrow_limit):
#         super().__init__(name) 
#         self.borrow_limit = borrow_limit

#     def display_info(self):
#         print(f"Faculty Name   : {self.name}")
#         print(f"Borrow Limit   : {self.borrow_limit} books")

# student = StudentMember("Ravi Kumar", 3)
# faculty = FacultyMember("Dr. Priya", 10)

# student.display_info()
# print()  # Line break
# faculty.display_info()


# hybrid in heritance
#task 1


#


