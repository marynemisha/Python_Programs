#Write a program to find the frequency of each character in a string.
string="Python"
print("Length of string:",len(string))
print("String:",string)
freq=""
for i in string:
    if i not in freq:
        print(i,"=",string.count(i))
        freq+=i

