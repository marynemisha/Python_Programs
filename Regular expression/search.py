import re

sentence="Python is a dynamically typed language"
x=re.search("is",sentence)
y=re.search("helo",sentence)
z=re.search("\s",sentence)
print(x)
print(y)
print(z)

#search for the first substring in the string
#if no matches are found,the value NONE is returned
