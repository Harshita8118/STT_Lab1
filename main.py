"""
This is a simple Python module that performs basic arithmetic operations
such as addition, subtraction, multiplication, and division. It also
includes a greeting function to greet a user by name.

Functions:
- greet(name): Returns a greeting message.
- add_numbers(a, b): Returns the sum of two numbers.
- subtract_numbers(a, b): Returns the difference between two numbers.
- multiply_numbers(a, b): Returns the product of two numbers.
- divide_numbers(a, b): Returns the division result of two numbers, handling division by zero.
"""

def greet(name):
    """
    Function to greet the user by name.
    """
    return f"Hello, {name}!"

def add_numbers(a, b):
    """
    Function to add two numbers.
    """
    return a + b

def subtract_numbers(a, b):
    """
    Function to subtract two numbers.
    """
    return a - b

def multiply_numbers(a, b):
    """
    Function to multiply two numbers.
    """
    return a * b

def divide_numbers(a, b):
    """
    Function to divide two numbers, with a check to avoid division by zero.
    """
    if b == 0:
        return "Cannot divide by zero"
    return a / b

def main():
    """
    Main function to test the arithmetic operations.
    """
    name = "Alice"
    print(greet(name))  # Call greet function

    num1, num2 = 10, 5
    prin(f"{num1} + {num2} = {add_numbers(num1, num2)}")
    print(f"{num1} - {num2} = {subtract_numbers(num1, num2)}")
    print(f"{num1} * {num2} = {multiply_numbers(num1, num2)}")
    print(f"{num1} / {num2} = {divide_numbers(num1, num2)}")

    # Testing division by zero
    num2 = 0
    print(f"{num1} / {num2} = {divide_numbers(num1, num2)}")

if __name__ == "__main__":
    main()
