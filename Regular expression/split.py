import re
sentence="Python is a dynamically typed language"
x=re.split("\s",sentence)
y=re.split("is",sentence)
print(x)
print(y)

#split() function returns a list where the string has been
#split at each match