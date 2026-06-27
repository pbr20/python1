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
