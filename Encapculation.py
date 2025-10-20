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
# s.display()



# Encapculation task 1


<<<<<<< HEAD
=======
<<<<<<< HEAD
>>>>>>> student
# class Student:
#     def __init__(self):
#         self.__marks = 0

#     def set_marks(self,marks):
#         self.__marks = marks

#     def get_marks(self):
#         return self.__marks
# s = Student()
# s.set_marks(85)
# print("Student Marks:", s.get_marks())

# print(s.__marks)



# class BankAccount:
#     def __init__(self):
#         self.__balance = 0
#     def deposit(self,balance):
#         self.__deposit += amount
#     def get_balance(self):
#         return self.__balance

# account = BankAccount()
# account.deposit(5000)
# print("")          
<<<<<<< HEAD
    

# 
=======
=======
class Student:
    def __init__(self):
        self.__marks = 0

    def set_marks(self,marks):
        self.__marks = marks

    def get_marks(self):
        return self.__marks
s = Student()
s.set_marks(85)
print("Student Marks:", s.get_marks())

print(s.__marks)



class BankAccount:
    def __init__(self):
        self.__balance = 0
    def deposit(self,balance):
        self.__deposit += amount
    def get_balance(self):
        return self.__balance

account = BankAccount()
account.deposit(5000)
print("")          
>>>>>>> junior
    

>>>>>>> student
