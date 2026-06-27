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
