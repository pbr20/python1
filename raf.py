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
