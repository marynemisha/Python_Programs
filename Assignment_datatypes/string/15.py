#Write a program to determine whether one string is a rotation of another string
s1 = "abcd"
s2 = "cdab"
if len(s1) != len(s2):
    print("Not a rotation")
else:
    temp = s1 + s1
    if s2 in temp:
        print("It is a rotation")
    else:
        print("It is not a rotation")
