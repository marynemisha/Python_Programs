#Write a program to determine whether two strings are isomorphic.
str1 = input("Enter first string: ")
str2 = input("Enter second string: ")
if len(str1) != len(str2):
    print("Not Isomorphic")
else:
    d1 = {}
    d2 = {}
    same = True
    for i in range(len(str1)):
        ch1 = str1[i]
        ch2 = str2[i]
        if ch1 in d1:
            if d1[ch1] != ch2:
                same = False
                break
        else:
            d1[ch1] = ch2
        if ch2 in d2:
            if d2[ch2] != ch1:
                same = False
                break
        else:
            d2[ch2] = ch1
    if same:
        print("Isomorphic")
    else:
        print("Not Isomorphic")