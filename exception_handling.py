import math
num = int(input("Enter an integer: "))
try:
  print(math.sqrt(num))
except:
  print("Bad value for square root")
  print("Using absoulte value instead")
  print(math.sqrt(abs(num)))
finally:
  print("done!!!")

#raise statement -> to create runtime error



try:
  print(math.sqrt(num))
except Exception as e:
  print(e)
  print("Bad value for square root")
  print("Using absoulte value instead")
  print(math.sqrt(abs(num)))
finally:
  print("done!!!")

#raise statement -> to create runtime error

if num < 0:
  raise RuntimeError("You cannot use a negative number")
else:
  print(math.sqrt(num))