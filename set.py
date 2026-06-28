st = {}
print(st)

fruits = {'banana', 'orange', 'mango', 'lemon', 'kiwi'}
print(fruits)
print(len(fruits))

# checking an item
print("IS orange in fruits: ", 'orange' in fruits)

fruits.add('cherry')
print(fruits)

# update for multiple items to set
fruits.update(['grape', 'strawberry', 'blueberry'])
print(fruits)

# remove
fruits.remove('grape')
print(fruits)

# removing random items

removed_fruit = fruits.pop()
print("Removes fruits: ", removed_fruit)

# clearing set
fruits.clear()
print(fruits)

# deleting sets same as list

# list --> set
list1 = [1, 2, 3, 4, 5]
st1 = set(list1)
print(st1)

# joining set -> Union set

st1 = {1, 2, 3, 4, 5}
st2 = {6, 7, 8, 9, 10}
st3 = st1.union(st2)

print("Union Set: ", st3)
print("Union Set: ", st1 | st2)
# intersection method to find the common items

st2 = {2, 6, 4, 7, 8, 9}
print(st1.intersection(st2))  # return the intersection
print(st1 & st2)  # same result

# checking subset and superset

whole_numbers = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
even_numbers = {2, 4, 6, 8, 10}

print("Is it a subset: ", even_numbers.issubset(whole_numbers))
print("Is it superset", whole_numbers.issuperset(even_numbers))

# checking differnece

print("Odd Numbers: ", whole_numbers.difference(even_numbers))
# whole_numbers\even_numbers
print("Odd Numbers: ", whole_numbers-even_numbers)

odd_numbers = whole_numbers-even_numbers

# finding the Symmetric between two sets

st1 = {1, 2, 3, 4}
st2 = {5, 6, 2, 4}

print(st1.symmetric_difference(st2))  # (A/B)U(B/A)
print(st2 ^ st1)  # same

# Joining set or disjoint sets
# If two sets do not have a common item or items we call them disjoint sets. We can check if two sets are joint or disjoint using isdisjoint() method.
print("even numbers: ", even_numbers)
print("odd numbers: ", odd_numbers)
print("Is even numbers and odd numbers disjoint set: ",
      even_numbers.isdisjoint(odd_numbers))
print("Is whole numbers and even numbers are disjoint set: ",
      whole_numbers.isdisjoint(even_numbers))
