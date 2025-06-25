# class Person:
#     def display_info(self):
#         print("I am a person.")

# class Student(Person):
#     pass

# student_obj = Student()

# student_obj.display_info()



class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Student(Person):
    def __init__(self, name, age, grade):
        super().__init__(name,age)
        self.grade = grade

student_obj = Student("Alice", 20, "A")

print(f"Name: {student_obj.name}")
print(f"Age: {student_obj.age}")
print(f"Grade: {student_obj.grade}")


