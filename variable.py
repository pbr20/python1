students_count = 1000
rating = 4.9
is_published = True
course_name = "Python Programming"
message = """
Hi Friend,

This is Rithen from the future. I am learning Python and it's amazing! I hope you are doing well.

Please let me know if you have any questions or if you want to learn Python together.
"""

print(len(message))
# indexing starts from 0 here, at index 0 is a new line character
print(message[1:10])
print(message[-10:-1])  # it prints from the back
print(message[0:])  # it prints the whole message
print(message[:])  # it also prints the whole message

course = 'Python "Programming"'
course2 = "Python \"Programming"

# \"
# \'
# \\
# \n

print(course2)

first = "Rithen"
last = "Barua"
full_name = first + " " + last
print(full_name)

full = f"{first} {last} is a Python programmer"
print(full)
