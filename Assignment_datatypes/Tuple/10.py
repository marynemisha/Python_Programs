#Write a program to convert a tuple of strings into a single string.
tuple1 = ("Hello", " ", "World", "!")
print(tuple1)
print("Length:",len(tuple1))
result=""
for i in tuple1:
    result+=i
print("Result:",result)