print("~~~Mini Calculator~~~")

num1=int(input("Enter your first number here: "))

num2=int(input("Enter your second number here: "))

print("Press 1 for ADDITION\nPress 2 for SUBTRACTION\nPress 3 for MULTIPLICATION\n Press 4 for DIVISION")

choice=int(input("Enter your choice here from 1-4: "))

if choice == 1:
    print(num1 + num2)
elif choice == 2:
    print(num1 -num2)
elif choice == 3:
    print(num1 * num2)
elif choice == 4:
    print(num1 / num2)
else:
    print("Invalid Input")