lst = []
print(lst)

lst = [1, 2, 3, 4, 5]
print(lst)

print(len(lst))

print(lst[0])
print(lst[len(lst)//2])
print(lst[-1])

mixed_data_types = ["Rithen", 22, 5.7, False, "Bangladesh"]
print(mixed_data_types)

it_companies = ["Facebook", "Google", "Microsoft",
                "Apple", "IBM", "Oracle", "Amazon"]
print(it_companies)
print("Number of companies:", len(it_companies))
print("First company:", it_companies[0])
print("Last company:", it_companies[-1])
print("Middle company:", it_companies[len(it_companies)//2])

it_companies[0] = "Meta"
print(it_companies)

it_companies.append("Twitter")
print(it_companies)

it_companies.insert(len(it_companies)//2, "LinkedIn")
print(it_companies)

it_companies[0] = it_companies[0].upper()
print(it_companies[0])

sentence = "#; ".join(it_companies)
print(sentence)

print("IS Twitter exists: ", '#;Twitter' in it_companies)

it_companies.sort()
print(it_companies)

it_companies.reverse()
print(it_companies)

print("First three companies:", it_companies[:3])
print("Last three companies", it_companies[-3:])
print("Middle companies", it_companies[1:-1])

it_companies.pop(0)
print(it_companies)

it_companies.pop(len(it_companies)//2)
print(it_companies)

it_companies.pop(len(it_companies)-1)
print(it_companies)

it_companies.clear()
print(it_companies)

del it_companies


front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node', 'Express', 'MongoDB']

all_end = front_end + back_end
print(all_end)

full_stack = all_end.copy()
full_stack.insert(5, "Python")
full_stack.insert(6, "SQL")
print(full_stack)


# Tuple practice

tup = ()
print(tup)

sisters = ("Ipshita", "Ishika", "faye", "aicy")
print(sisters)
brother = ("kuya", "Tristan")
print(brother)
siblings = sisters + brother
print(siblings)

print("I have ", len(siblings), " siblings")

family_members = list(siblings)
family_members.append("rupam")
family_members.append("sumi")
print(family_members)

frist_sister, second_sister, third_sister, fourth_sister, first_brother, second_brother, father, mother = family_members
print(first_brother)
print(fourth_sister)
print(father)

# Set practice

# sets
it_companies = {'Facebook', 'Google', 'Microsoft',
                'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

print("Length of IT companies: ", len(it_companies))
it_companies.add('Twitter')
print(it_companies)
it_companies.update(['Meta', 'Linux'])
print(it_companies)
it_companies.remove('Meta')
print(it_companies)
# with discard no error raise even if the item already doesn't exist
it_companies.discard('Instagram')
print(it_companies)

print(A | B)
print(A.union(B))
print(A & B)
print(A.intersection(B))
print("Is A subset of B: ", A.issubset(B))
print("Are A and B disjoint set: ", A.isdisjoint(B))
print(A | B)
print(B | A)
print("Symmetric difference: ", A ^ B)
print(A.symmetric_difference(B))
del (A)


# disctionary

dog = {}
print(type(dog))

dog['name'] = 'musica'
dog['color'] = 'golden'
dog['breed'] = 'golden retriver'
dog['legs'] = 4
dog['age'] = 5
print(dog)

student = {
    'first_name': 'Rithen',
    'last_name': 'Barua',
    'gender': 'male',
    'age': 22,
    'marital_status': 'unmarried',
    'skills': ['Java', 'CPP', 'C', 'Python'],
    'country': 'Bangladesh',
    'city': 'Chattogram',
    'address': {
        'street': 'Avoy-Mitra Ghat',
        'postal code': '4000'
    }
}

print(len(student))

print(type(student['skills']))

student['skills'].append('SQL')
print(student['skills'])

keys = student.keys()
print(keys)

values = student.values()
print(values)

print(student.items())
del student['marital_status']

print(student)

del student
