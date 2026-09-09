import re
sentence="Python is a dynamically typed language"
x=re.findall("is",sentence)
print(x)
print(len(x))


#THE LIST CONTAINS THE MATCHES IN THE ORDER THEY ARE FOUND
#IF NO MATCHES ARE FOUND,AN EMPTY LIST IS RETURNED