# List comprehension in Python is a compact way of creating a list from a sequence.
# It is a short way to create a new list.
# List comprehension is considerably faster than processing a list using the for loop.

squares = [i * i for i in range(11)]
print(squares)

# with if exxxpression
numbers = [-8, -7, -3, -1, 0, 1, 3, 4, 5, 7, 6, 8, 10]
positive_even_numbers = [i for i in numbers if i % 2 == 0 and i > 0]

print(positive_even_numbers)
