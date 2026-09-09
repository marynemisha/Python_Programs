#Write a program to check whether two strings are equal without using the == operator.
str1 = input("Enter first string: ")
str2 = input("Enter second string: ")
if len(str1) != len(str2):
    print("Strings are not equal")
else:
    equal = True
    for i in range(len(str1)):
        if str1[i] != str2[i]:
            equal = False
            break
    if equal:
        print("Equal")
    else:
        print("Not equal")