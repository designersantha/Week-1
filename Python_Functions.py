# Python program using functions

# Function to greet the user
def greet(name):
    print(f"Hello, {name}! Welcome to the program.")

# Function to add two numbers
def add(a, b):
    return a + b

# Function to check if a number is even or odd
def check_even_odd(number):
    if number % 2 == 0:
        return "even"
    else:
        return "odd"

# Main function to control the flow
def main():
    # Get user input
    name = input("Enter your name: ")
    greet(name)

    # Input two numbers and add them
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    result = add(num1, num2)
    print(f"The sum of {num1} and {num2} is {result}.")

    # Check if a number is even or odd
    number_to_check = int(input("Enter a number to check even/odd: "))
    result = check_even_odd(number_to_check)
    print(f"The number {number_to_check} is {result}.")

# Call the main function to run the program
main()
