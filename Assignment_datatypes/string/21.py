#Write a program to count the number of uppercase and lowercase letters in a string.
str1 = input("Enter a string: ")
upper = 0
lower = 0
for i in str1:
    if i.isupper():
        upper += 1
    elif i.islower():
        lower += 1

print("Uppercase:", upper)
print("Lowercase:", lower)