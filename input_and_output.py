# in python input function returned the value as string

user_name = input("please enter your name: ")
print("your name in all capitals is: ",user_name.upper())

#so u must typecast first if u want anorher data type

radius = float(input("enter the radius for a circle: "))
print("Diameter of her circle is: ",radius*2)

#print function seperate the values with default sapce like:

print("hello","friends")

#its possible to change the default seperator like:

print("Hello" , "friends", sep = "***")

#also the end line with is default to next line \n

print("Hello","world", end = "*** ")

#format specifier
price = 24
item = "banana"

print("The %s costs %d cents"%(item,price))

#here after % +10 refer how wide the value will be in character, right justified meaning extra will be coberted into space from left
#similarly    -10 is left justified
#after the redex point .3 the value gives three charater after decimal point
print("The %+10s costs %6.3f cents"%(item,price))

item_dict = {
  "item" : "banana",
  "cost" : 24
}

print("The %(item)-10s cost %(cost)2.3f cents"%(item_dict))