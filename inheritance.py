# class Person:
#     def display_info(self):
#         print("I am a person.")

# class Student(Person):
#     pass

# student_obj = Student()

# student_obj.display_info()



# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

# class Student(Person):
#     def __init__(self, name, age, grade):
#         super().__init__(name,age)
#         self.grade = grade

# student_obj = Student("Alice", 18, "A")

# print(f"Name: {student_obj.name}")
# print(f"Age: {student_obj.age}")
# print(f"Grade: {student_obj.grade}")



# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age


# class Student(Person):
#     def __init__(self, name, age):
#         super().__init__(name, age)
#         self.grade = None 

#  def calculate_grade(self, marks):
#         average = sum(marks) / len(marks)
        
#         if average >= 90:
#             self.grade = "A"
#         elif average >= 80:
#             self.grade = "B"
#         elif average >= 70:
#             self.grade = "C"
#         elif average >= 60:
#             self.grade = "D"
#         else:
#             self.grade = "F"
        
#         print(f"Average Marks: {average}")
#         print(f"Grade: {self.grade}")

#     def show_info(self):
#         print(f"Name: {self.name}")
#         print(f"Age: {self.age}")
#         print(f"Grade: {self.grade}"
              

# marks_list = [85, 78, 92, 88, 76]
# student1 = Student("Alice", 18)
# student1.calculate_grade(marks_list)
# student1.show_info()


class Father:
    def skills(self):
        print("Skilled in driving")

class Mother:
    def skills(self):
        print("Skilled in cooking")

class Child(Father, Mother):
    def skills(self):
        # Call Father’s skills method
        Father.skills(self)
        # Call Mother’s skills method
        Mother.skills(self)
        # Child’s own message (optional)
        print("Skilled in painting")

# Create an object of Child
c = Child()

# Call the skills method
c.skills()









