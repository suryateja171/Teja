Basic programs

printhelloworld


print("hello,World")

write a program to add two no


num1 = 1
num2 = 5
sum = num1+num2
print(sum)

calculate the area of a circle

pi = 3.14
radius = int(input("Enter the radius :"))
area = pi*radius**2
print("Area :",area)



Swap two variables without using a temporary variable
a = 25
b = 30
a,b = b,a
print(b)



Swap two variables with using a temporary variable
a= 10
b= 20
temp = a
a=b
b = temp 
print(b)


convert celsius to fahreinheit


celsius = 40
Fahrenheit = (celsius*9/5)+32
print(Fahrenheit)

Decision Making
check if a no is even or odd


num = 8
if num% 2 == 0:
    print("Even")
else:
    print("Odd")

string = "MOM"

if string == string[::-1]:
    print("Palindrome")
else:
    print("Not a palindrome")


num = 28
if num > 0:
    print("Positive") 
elif num < 0:
    print("negative")
else:
    print("Zero")

type 1
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
op = input("Enter operator(+,-,*,/): ")

if op =='+':
    print("result:", num1 + num2)
elif op == '-':
    print("result:", num1 - num2)
elif op == '*':
    print("result:",num1*num2)
elif op =='/':
    print("result:", num1 / num2)
else:
    print("invalid operator") 

type 2
Simple Calculator Program

Input from the user
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
op = input("Enter operator (+, -, *, /): ")

# Perform operation based on operator
if op == '+':
    a= num1+num2
    print("Result:",a)
elif op == '-':
    b= num1-num2
    print("Result:", b)
elif op == '*':
    c=num1*num2
    print("Result:",c)
elif op == '/':
    d = num1/num2
    print("Result:",d)
    if num1==0 or num2==0:
        print("cannot divide by zero ")
    
# else:
#     print("Invalid operator")

# year = 2024
# if (year % 400 == 0) or (year % 100 != 0 and year % 4 == 0):
#     print("leap year")
# else:
#     print("not leap year")
    

str1  = "listeN"
str2 = "silent"
a = sorted(str1)
aa=a
print(a)

b= sorted(str2)
print(b)
if a == b:
    print("anagram")
else:
    print("not anagram")     



numbers = [x for x in range(100000, 1000001)]
print (numbers)








