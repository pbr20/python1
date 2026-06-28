# A dictionary is a collection of unordered, modifiable(mutable) paired (key: value) data type.

dit = {}
print(type(dit))

person = {
    'first_name': 'Puspak',
    'last_name': 'Barua',
    'age': 22,
    'country': 'Bangladesh',
    'is_married': False,
    'skills': ['JavaScript', 'Cpp', 'C', 'Python', 'SQL', 'HTML', 'CSS', 'JavaScript'],
    'address': {
        'street': "Avoymitra ghat",
        'postalcode': '4000'
    }
}

print(person)
print(len(person))

# Accessing dict item

print("First Name: ", person['first_name'])
person['status'] = 'student'
person['skills'].append('Matlab')

print(person)

# modifying items

person['first_name'] = 'Rithen'
print(person)

# checking items in dict

print("Is status in person: ", 'status' in person)

# removing items

person.popitem()  # removes the last item
person.pop('last_name')
del person['is_married']

print(person)

# dict to list
print(person.items())

# clearing dct

print(person.clear())
print(person)

person = {
    'first_name': 'Puspak',
    'last_name': 'Barua',
    'age': 22,
    'country': 'Bangladesh',
    'is_married': False,
    'skills': ['JavaScript', 'Cpp', 'C', 'Python', 'SQL', 'HTML', 'CSS', 'JavaScript'],
    'address': {
        'street': "Avoymitra ghat",
        'postalcode': '4000'
    }
}

del person

# copying

person = {
    'first_name': 'Puspak',
    'last_name': 'Barua',
    'age': 22,
    'country': 'Bangladesh',
    'is_married': False,
    'skills': ['JavaScript', 'Cpp', 'C', 'Python', 'SQL', 'HTML', 'CSS', 'JavaScript'],
    'address': {
        'street': "Avoymitra ghat",
        'postalcode': '4000'
    }
}

person_copy = person.copy()

print(person_copy)


# getting keys and values as list

keys = person.keys()
print(keys)

values = person.values()
print(values)
