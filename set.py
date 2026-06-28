st = {}
print(st)

fruits = {'banana', 'orange', 'mango', 'lemon', 'kiwi'}
print(fruits)
print(len(fruits))

#checking an item
print("IS orange in fruits: ", 'orange' in fruits)

fruits.add('cherry')
print(fruits)

#update for multiple items to set
fruits.update(['grape', 'strawberry', 'blueberry'])
print(fruits)

#remove
fruits.remove('grape')
print(fruits)

#removing random items

removed_fruit = fruits.pop()
print("Removes fruits: ",removed_fruit)

#clearing set
fruits.clear()
print(fruits)



