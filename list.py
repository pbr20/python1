# syntax
lst = []
print(len(lst))

fruits = ["apple", "mango", "cherry", "banana", "orange"]
animals = ["cat", "dog", "rabbit"]

print("Number of fruits:", len(fruits))
print("Fruits:", fruits)
print("Number of animals:", len(animals))
print("Animals:", animals)

# they can also have items of different data types
mixed_list = [1, "apple", 3.14, True]
print("Mixed list:", mixed_list)

# accessing items in a list

print("First fruit:", fruits[0])  # first item
print("Last fruit:", fruits[len(fruits)-1])  # last item
print("Last fruit:", fruits[-1])  # last item

# unpacking a list
first_fruit, second_fruit, third_fruit, *rest = fruits
print("First fruit:", first_fruit)
print("Second fruit:", second_fruit)
print("Third fruit:", third_fruit)
print("Rest of the fruits:", rest)  # rest of the items in the list

first_animal, second_animal, third_animal = animals
print("First animal:", first_animal)
print("Second animal:", second_animal)
print("Third animal:", third_animal)

# slicing items in a list
print("First two fruits:", fruits[0:2])  # first two items
print("Last two fruits:", fruits[-2:])  # last two items
print("All fruits:", fruits[:])  # all items
print("Every second fruit:", fruits[::2])  # every second item
print("Reversed fruits:", fruits[::-1])  # reversed list
print("Every third fruit:", fruits[::3])  # every third item

# Modifying items in a list
fruits[0] = "kiwi"  # change first item
print("Modified fruits:", fruits)

# checking items in a list
print("Is 'mango' in fruits?", "mango" in fruits)
print("Is 'lime' in fruits?", "lime" in fruits)

# Adding items to a list
fruits.append("lime")  # add item to the end
print("Fruits after appending 'lime':", fruits)

# inserting items to a list
fruits.insert(1, "grape")  # insert item at index 1
print("Fruits after inserting 'grape' at index 1:", fruits)

# Removing items from a list
fruits.remove("banana")  # remove item by value
print("Fruits after removing 'banana':", fruits)

# removing items from a list by index
del fruits[2]  # remove item at index 2
print("Fruits after deleting item at index 2:", fruits)
del fruits  # delete the entire list
# popping items from a list
fruits = ["apple", "mango", "cherry", "banana", "orange"]
popped_fruit = fruits.pop()  # remove and return the last item
print("Popped fruit:", popped_fruit)

fruits = ["apple", "mango", "cherry", "banana", "orange"]
fruits.pop(1)  # remove and return the item at index 1
print("Fruits after popping item at index 1:", fruits)

# clearing a list
fruits.clear()  # remove all items from the list
print("Fruits after clearing:", fruits)

fruits = ["apple", "mango", "cherry", "banana", "orange"]

# copying a list
fruits_copy = fruits.copy()  # create a shallow copy of the list
print("Fruits copy:", fruits_copy)

# joining lists
positive_numbers = [1, 2, 3]
negative_numbers = [-1, -2, -3]
zero = [0]
numbers = negative_numbers + zero + positive_numbers
print("Joined list of numbers:", numbers)

# counting items in a list
ages = [22, 18, 22, 30, 18, 22]
print("Count of 22 in ages:", ages.count(22))

# finding the index of an item in a list
print("Index of 30 in ages:", ages.index(30))

# reversing a list
ages.reverse()
print("Reversed ages:", ages)

# sorting a list
ages.sort()
print("Sorted ages:", ages)
ages.sort(reverse=True)
print("Sorted ages in descending order:", ages)

# returns a new sorted list without modifying the original list
print(sorted(fruits))
print(sorted(fruits, reverse=True))
