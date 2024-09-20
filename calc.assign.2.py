print("~~~Mini Calculator~~~")

num1=int(input("Enter your first number here: "))

num2=int(input("Enter your second number here: "))

print("Press 1 for ADDITION\nPress 2 for SUBTRACTION\nPress 3 for MULTIPLICATION\n Press 4 for DIVISION")

choice=int(input("Enter your choice here from 1-4: "))

def multiply(a,b):
    print(a*b)
def add(a,b):
    print(a+b)
def subtract(a,b):
    print(a-b)
def divide(a,b):
    print(a/b)
def invalid_input():
    print("Invalid Input")

if choice == 1:
    add(num1,num2)
elif choice == 2:
    subtract(num1,num2)
elif choice == 3:
    multiply(num1,num2)
elif choice == 4:
    divide(num1,num2)
else:
    invalid_input()