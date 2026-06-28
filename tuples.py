#A tuple is a collection of different data types which is ordered and unchangeable (immutable). Tuples are written with round brackets, (). Once a tuple is created, we cannot change its values. We cannot use add, insert, remove methods in a tuple because it is not modifiable (mutable). Unlike list, tuple has few methods. Methods related to tuples:

#tuple(): to create an empty tuple
#count(): to count the number of a specified item in a tuple
#index(): to find the index of a specified item in a tuple
#+ operator: to join two or more tuples and to create a new tuple

tup = () #empty tuple
print(tup)

fruits = ("cherry", "mango", "Orange", "banana", "Kiwi")
print(fruits)
print(type(fruits))
print(len(fruits))

print("first fruit: ", fruits[0])
print("Middle fruit: ", fruits[len(fruits)//2])
print("Last fruits: ", fruits[len(fruits)-1])

#Negative indexing same as list

#Slicing 
print("Every odd fruits: ",fruits[0::2])
Efruits = ", ".join(fruits[1::2])
print("Every Even fruits: ",Efruits)

#Negative Slicing
print("Reverse Order fruits: ",fruits[-5:])

#Changing Tuples to list
tpl = (1, 2, 3, 4, 5)
lst = list(tpl)
print(type(lst))

print("Is Lime is fruits: ", "Lime" in fruits)

#fruits[0] = "Lime"  # TypeError: 'tuple' object does not support item assignmen
#print(fruits)

#joing Tuple -> same as list

#deleting

del fruits
#print(fruits)