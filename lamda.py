add_two_nums = lambda a, b: a+b

print("Sum: ",add_two_nums(5,6))

def power(x):
    return lambda n : x ** n

print("Cube: ",power(2)(3))