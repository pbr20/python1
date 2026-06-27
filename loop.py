for number in range(1, 10, 2):  # start at 1, stop before 10, step by 2
    print("Attemppt", number + 1, (number + 1) * ".")

for number in range(10, 0, -1):  # start at 10, stop before 0, step by -1
    print("Attemppt", number, number * ".")
    if number == 5:
        print("We have reached 5, stopping the loop.")
        break

# for else is executed when the loop is not terminated by a break statement
success = False
for number in range(4):
    print("Attempt)", number+1, (number+1) * ".")
    if success:
        print("Success!")
        break
else:
    print("Attempted 4 times and failed.")

# Nested loops
for x in range(5):
    for y in range(3):
        print(f"({x}, {y})")

# iterable

print(type(range(5)))  # <class 'range'>

# string is also iterable like range
for x in "Python":
    print(x)

# list is also iterable like range
for x in [1, 2, 3, 4, 5]:
    print(x)

# We can also iterate over a object

# While loop

number = 100

while number > 0:
    print(number)
    number //= 2


while True:
    command = input(">")
    print("ECHO", command)
    if command.lower() == "quit":
        break
