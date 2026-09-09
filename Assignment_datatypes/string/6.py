#Write a program to find the second most frequently occurring character in a string.
string=input("Enter the string:")
print("Length of string:",len(string))
print("String:",string)
freq=""
first=0
second=0
count=0
for i in string:
    if i not in freq:
        print(i,"=",string.count(i))
        count = string.count(i)
        if count>first:
            second = first
            first=count

        elif count>second and count!=first:
            second=count

        freq+=i
for i in string:
    if string.count(i)==second:
        print("second=",i)
        break
