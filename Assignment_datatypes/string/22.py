#Write a program to remove all spaces from a string without using the replace() method.
str1 = input("Enter a string: ")
result = ""
for ch in str1:
    if ch != " ":
        result += ch

print("String:", result)