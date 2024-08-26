# Begin by prompting the user to enter their name
name=str(input("Hello, please enter your name: "))

# Then ask them for three of their favorite numbers
print("Please enter your three favorite numbers below:")
num1=int(input("Enter first number: "))
num2=int(input("Enter second number: "))
num3=int(input("Enter third number: "))

# The program should greet the user with a personalized message that includes their name
print(f"Hello {name},I hope you are fine, its my pleasure to meet you.")
print("Lets explore some things about your favorite numbers.")

# The three numbers provided by the user should be stored in a list
numbers:list=[num1 , num2 , num3]

# The program should then check if any of the numbers are even or odd, and store this information in a separate list of tuples,
# where each tuple contains the number and a string indicating whether it is "even" or "odd"
even_odd_check=[]
for num in numbers:
    if num % 2 == 0:
        even_odd_check.append(f"{num},\"even\"")
    else:
        even_odd_check.append(f"{num},\"odd\"")   

# Print the list of tuples containing the number and its even/odd status
print("Even or Odd Information for your favorite numbers:")
for info in even_odd_check:
    print(f"Number: {info}")


# Create a tuple containing each number and its square    
number_squares=[]
for num in numbers:
    number_squares.append(f"{num}, {num ** 2}")


# printing squares and the numbers
print("Your favorite numbers and their squares:")
print(f"The number {num1} and its square: {number_squares[0]}")
print(f"The number {num2} and its square: {number_squares[1]}")
print(f"The number {num3} and its square: {number_squares[2]}")

# printing the sum of favorite numbers
sum = num1 + num2 + num3
print(f"Amazing! The sum of your favorite numbers is: {sum}")

if sum < 2:
    is_prime = False
elif sum == 2:
    is_prime = True
elif sum % 2 == 0:
    is_prime = False
else:
    is_prime = True
    i = 3
    while i * i <= sum:
        if sum % i == 0:
            is_prime = False
            break
        i += 2

if is_prime:
    print(f"Wow, {sum} is a prime number!")
else:
    print(f"{sum} is not a prime number.")


