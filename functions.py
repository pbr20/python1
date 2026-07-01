import math


def greet(first_name, last_name):
    print(f"Hello {first_name} {last_name}")
    print("Welcome to the program.")


greet("Rithen", "Barua")


def get_greeting(name):
    return f"Hi {name}!"


messsage = get_greeting("Rithen")
file = open("greeting.txt", "w")
file.write(messsage)

# None returns when a function does not have a return statement. It is also the default return value of a function that does not explicitly return anything.
print(greet("Rithen", "Barua"))  # returns None

# keyword arguments


def increment(number, by=1):  # default value of by is 1
    return number + by  # all the optional parameters should be at the end of the parameter list


print(increment(number=2, by=1))
print(increment(number=2))  # uses default value of by

# def increment(number, by=1, another): #will raise a syntax error because all the optional parameters should be at the end of the parameter list. Here another is an optional parameter without a default value, so it should be placed after by.


def multiply(*numbers):
    total = 1
    for n in numbers:
        total *= n
    return total


print(multiply(1, 2, 3, 4, 5))  # prints 120


# finding root using newton method

def square_root(n):
    root = n/2  # initial guess

    for k in range(50):
        root = (1/2) * (root+(n/root))
    return root


print("Root by python: ", math.sqrt(3),
      "Root by customized function: ", square_root(3))


# dictionary unpacking
my_dict = {
    "first_name": "Rithen",
    "last_name": "Barua",
}


def greet(first_name, last_name):
    print(f"Hello {first_name} {last_name}")
    print("Welcome to the program.")


greet(**my_dict)

my_dict1 = {
    "first_name": "Rithen",
    "last_name": "Barua",
    "age": 22,
    "country": "Bangladesh",
    "is_student": True,
    "skills": ["Python", "JavaScript", "C++"]
}


def arbitrary_arguments(**args):
    for k, v in args.items():
        print(k, v)


arbitrary_arguments(**my_dict1)

# Understanding * vs **
# * unpacks the keys of the dictionary.
# ** unpacks the values of the dictionary.

# Function as a Parameter of Another Function


def do_smth(func, x):
    return func(x)


print(do_smth(square_root, 9))  # prints 3.0
