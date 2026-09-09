#Write a program to find all substrings of a given string without using built-in libraries.
str1 = input("Enter a string: ")
print(str1)
for i in range(len(str1)):
    sub = ""
    for j in range(i, len(str1)):
        sub += str1[j]
        print(sub)