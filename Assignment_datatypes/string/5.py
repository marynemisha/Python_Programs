#Write a program to remove all duplicate characters from a string while preserving their first occurrence.
string=input("Enter the string:")
print("Length of string:",len(string))
print("String:",string)
result=""
for i in string:
    if i not in result:
        result+=i
print("Result=",result)