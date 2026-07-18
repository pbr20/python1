#A regular expression or RegEx is a special text string that helps to find patterns in data. A RegEx can be used to check if some pattern exists in a different data type. To use RegEx in python first we should import the RegEx module which is called re.

import re

#re.match(): searches only in the beginning of the first line of the string and returns matched objects if found, else returns None.

txt = 'I hate python and java'
match = re.match('I hate python', txt, re.I)
print(match)


