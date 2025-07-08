# class Student:
#     def __init__(self, name, age):
#         self.name = name         # public variable
#         self.__age = age         # private variable (using __ makes it private)

#     def display(self):
#         print("Name:", self.name)
#         print("Age:", self.__age)

#     def set_age(self, new_age):
#         if new_age > 0:
#             self.__age = new_age  # safe update
#         else:
#             print("Invalid age!")

# # Creating object
# s = Student("Teja", 20)

# s.display()

# # Try to change age directly (not allowed)
# s.__age = 25  # This won't change the real __age
# s.display()

# # Use method to change it safely
# s.set_age(25)