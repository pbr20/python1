course = "Python Programming"
print(course.upper())
print(course.lower())
print(course.title())  # converts the first letter of each word to uppercase
print(course.strip())  # removes whitespace from the beginning and end
print(course.replace("Python", "Java"))
print("Python" in course)
# returns True if the substring is not found in the string
print("Java" not in course)
print(course.find("Python"))
print(course.find("Java"))  # returns -1 if not found
print(course.split())  # splits the string into a list of words
print(course)
