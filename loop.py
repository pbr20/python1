from countries_data import countries1

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

count = 0

while count < 5:
    print(count)
    count = count + 1
else:
    print(count)

# for loop in set


person = {
    'first_name': 'Puspak',
    'last_name': 'Barua',
    'age': 22,
    'country': 'Bangladesh',
    'is_married': False,
    'skills': ['Cpp', 'C', 'Python', 'SQL', 'HTML', 'CSS', 'JavaScript'],
    'address': {
        'street': "Avoymitra ghat",
        'postalcode': '4000'
    }
}

for key, value in person.items():
    print(key, value)

print("Here is all skills below:")

for keys in person:
    if keys == 'skills':
        i = 1
        for skill in person['skills']:
            print(i, skill)
            i = i + 1

# pass when there is no code in a loop

for number in range(6):
    pass

# practice

sumo = 0
sume = 0

for i in range(101):
    if i % 2 == 0:
        sumo = sumo + i
    else:
        sume = sume + i

print("Sum of all even numbers: ", sume)
print("sum of all odd numbers: ", sumo)


countries = [
    'Afghanistan',
    'Albania',
    'Algeria',
    'Andorra',
    'Angola',
    'Antigua and Barbuda',
    'Argentina',
    'Armenia',
    'Australia',
    'Austria',
    'Azerbaijan',
    'Bahamas',
    'Bahrain',
    'Bangladesh',
    'Barbados',
    'Belarus',
    'Belgium',
    'Belize',
    'Benin',
    'Bhutan',
    'Bolivia',
    'Bosnia and Herzegovina',
    'Botswana',
    'Brazil',
    'Brunei',
    'Bulgaria',
    'Burkina Faso',
    'Burundi',
    'Cabo Verde',
    'Cambodia',
    'Cameroon',
    'Canada',
    'Central African Republic',
    'Chad',
    'Chile',
    'China',
    'Colombia',
    'Comoros',
    'Congo, Democratic Republic of the',
    'Congo, Republic of the',
    'Costa Rica',
    "Côte d'Ivoire",
    'Croatia',
    'Cuba',
    'Cyprus',
    'Czech Republic',
    'Denmark',
    'Djibouti',
    'Dominica',
    'Dominican Republic',
    'East Timor (Timor-Leste)',
    'Ecuador',
    'Egypt',
    'El Salvador',
    'Equatorial Guinea',
    'Eritrea',
    'Estonia',
    'Eswatini',
    'Ethiopia',
    'Fiji',
    'Finland',
    'France',
    'Gabon',
    'Gambia',
    'Georgia',
    'Germany',
    'Ghana',
    'Greece',
    'Grenada',
    'Guatemala',
    'Guinea',
    'Guinea-Bissau',
    'Guyana',
    'Haiti',
    'Honduras',
    'Hungary',
    'Iceland',
    'India',
    'Indonesia',
    'Iran',
    'Iraq',
    'Ireland',
    'Israel',
    'Italy',
    'Jamaica',
    'Japan',
    'Jordan',
    'Kazakhstan',
    'Kenya',
    'Kiribati',
    'Korea, North',
    'Korea, South',
    'Kuwait',
    'Kyrgyzstan',
    'Laos',
    'Latvia',
    'Lebanon',
    'Lesotho',
    'Liberia',
    'Libya',
    'Liechtenstein',
    'Lithuania',
    'Luxembourg',
    'Madagascar',
    'Malawi',
    'Malaysia',
    'Maldives',
    'Mali',
    'Malta',
    'Marshall Islands',
    'Mauritania',
    'Mauritius',
    'Mexico',
    'Micronesia',
    'Moldova',
    'Monaco',
    'Mongolia',
    'Montenegro',
    'Morocco',
    'Mozambique',
    'Myanmar',
    'Namibia',
    'Nauru',
    'Nepal',
    'Netherlands',
    'New Zealand',
    'Nicaragua',
    'Niger',
    'Nigeria',
    'North Macedonia',
    'Norway',
    'Oman',
    'Pakistan',
    'Palau',
    'Palestine',
    'Panama',
    'Papua New Guinea',
    'Paraguay',
    'Peru',
    'Philippines',
    'Poland',
    'Portugal',
    'Qatar',
    'Romania',
    'Russia',
    'Rwanda',
    'Saint Kitts and Nevis',
    'Saint Lucia',
    'Saint Vincent and the Grenadines',
    'Samoa',
    'San Marino',
    'Sao Tome and Principe',
    'Saudi Arabia',
    'Senegal',
    'Serbia',
    'Seychelles',
    'Sierra Leone',
    'Singapore',
    'Slovakia',
    'Slovenia',
    'Solomon Islands',
    'Somalia',
    'South Africa',
    'South Sudan',
    'Spain',
    'Sri Lanka',
    'Sudan',
    'Suriname',
    'Sweden',
    'Switzerland',
    'Syria',
    'Tajikistan',
    'Tanzania',
    'Thailand',
    'Togo',
    'Tonga',
    'Trinidad and Tobago',
    'Tunisia',
    'Turkey',
    'Turkmenistan',
    'Tuvalu',
    'Uganda',
    'Ukraine',
    'United Arab Emirates',
    'United Kingdom',
    'United States',
    'Uruguay',
    'Uzbekistan',
    'Vanuatu',
    'Vatican City',
    'Venezuela',
    'Vietnam',
    'Yemen',
    'Zambia',
    'Zimbabwe'
]


for country in countries:
    if "land" in country:
        print(country)

fruits = ['banana', 'orange', 'mango', 'lemon']

i = 0
for fruit in fruits:
    fruits[i] = fruits[len(fruits)-i-1]
    i += 1
    fruits[len(fruits)-i] = fruit
    if i == len(fruits) // 2:
        break
print(fruits)

languages = set()

for country in countries1:
    for language in country["languages"]:
        languages.add(language)

print("Total number of languages: ", len(languages))
