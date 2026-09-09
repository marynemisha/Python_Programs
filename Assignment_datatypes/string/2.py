#Write a program to reverse each word in a sentence without changing the order of the words.
string="Python Django FullStack"
print("My string:",string)
print("Number of characters:",len(string))
temp=""
for i in string:
    if i!=" ":
        temp += i
    else:
        print(temp[::-1], end=" ")
        temp=""
print(temp[::-1])