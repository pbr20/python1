temprature = 35
if temprature > 30:
    print("It's a hot day")
    print("Drink plenty of water")
elif temprature > 20:
    print("It's a nice day")
else:
    print("It's a cold day")

print("Enjoy your day")

# ternary operator
age = 15
message = "Eligiible to vote" if age >= 18 else "Not eligible to vote"
print(message)

# practice

person = {
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_married': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
}

if 'skills' in person:
    skills = person['skills']
    print("Middle skill: ", skills[len(skills)//2])
else:
    print("This person have no skill")

print("Does this person know python",
      'skills' in person and 'Python' in person['skills'])

if person['is_married'] and 'Finland' in person['country']:
    print(person['first_name'], person['last_name'],
          "lives in", person['country'] + ". He is married")
