def greet_user():
    print("Hello, user!")

# greet_user()

def greet_user(name):
    print(f"Hello, welcome back {name}!")

# greet_user("user")

# Adding default values
def greet_user(name="shazain"):
    print(f"Hello, welcome back {name}!")

# greet_user()

# Returning values
def square (number):
    return number*number

# print(square(5))

# Recursive function
def factorial(number):
    if number == 1:
        return 1
    else:
        return number*factorial(number-1)

# print(factorial(5))

# lambda function 
x = lambda a : a + 10
print(x(5))

x = lambda a, b : a*b
print(x(5, 6))