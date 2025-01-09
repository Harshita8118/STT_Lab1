
def greet(name):
    return f"Hello, {name}!"

def add_numbers(a, b):
    return a + b

def multiply_numbers(a, b):
    return a * b

def divide_numbers(a, b):
    if b == 0:
        return "Cannot divide by zero"
    return a / b

if __name__ == "__main__":
    print(greet("Alice"))
    print(add_numbers(3, 5))
    print(multiply_numbers(3, 4))
    print(divide_numbers(10, 2))
    print(divide_numbers(10, 0))
