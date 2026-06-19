# # """My First Day of Python"""
# # name = "Raghav"
# # age = 20
# # gpa = 9.4
# # print("My name is", name)
# # print("My age is", age)
# # print("My GPA is", gpa)

# # print(type(name))
# # print(type(age))
# # print(type(gpa))

# import random
# import time
# random_number = random.randint(1, 10)
# attempts = 0
# time.sleep(1)
# print("Welcome to the Number Guessing Game!")
# time.sleep(2)
# print("I have selected a random number between 1 and 10. Can you guess it?")
# time.sleep(2)
# print("You have unlimited attempts, but try to guess it in as few tries as possible!")
# time.sleep(2.5)
# print("Let's begin!")
# time.sleep(2)
# print("Setting up the game...")
# time.sleep(1.5)
# while True:
#     user_guess = int(input("Guess the number between 1 and 10: "))
#     print("Checking",end="")
#     time.sleep(0.5)
#     print(".",end="")
#     time.sleep(0.5)
#     print(".")
#     time.sleep(0.5)
#     if user_guess < random_number:
#         print("low! Try again.")
#         time.sleep(0.5)
#         attempts += 1
#         print("Setting up again")
#         time.sleep(0.5)
#     elif user_guess > random_number:
#         print("high! Try again.")f
#         time.sleep(0.5)
#         attempts += 1
#         print("Setting up again")
#         time.sleep(0.5)
#     else:
#         if attempts == 0:
#             print("Congratulations! You've guessed the correct number on your first try!")
#         else:
#             print(f"Congratulations! You've guessed the correct number in your {attempts} try.")
#         break

def add(a, b):
    """This function takes two numbers as input and returns their sum."""
    return a + b
def subtract(a, b):
    """This function takes two numbers as input and returns their difference."""
    return a - b
def multiply(a, b):
    """This function takes two numbers as input and returns their product."""
    return a * b
def divide(a, b):
    """This function takes two numbers as input and returns their quotient."""
    if b != 0:
        return a / b
    else:
        return "Error: Division by zero is not allowed."
def main():
    """This is the main function that runs the calculator program."""
    print("Welcome to the Basic Calculator!")
    while True:
        print("\nSelect operation:")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Exit")
        choice = input("Enter choice (1/2/3/4/5): ")
        if choice in ['1', '2', '3', '4']:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            ops = {'1': add, '2': subtract, '3': multiply, '4': divide}
            result = ops[choice](num1, num2)
            print(f"The result is: {result}")
        elif choice == '5':
            print("Exiting the calculator. Goodbye!")
            break
        else:
            print("Invalid input. Please try again.")

if __name__ == "__main__":
    main()
