# Write a program to check whether two strings are anagrams

str1 = input("Enter the string1: ")
str2 = input("Enter the string2: ")

print("Length of str1:", len(str1))
print("Length of str2:", len(str2))
print("str1 =", str1)
print("str2 =", str2)
if len(str1) != len(str2):
    print("Not Anagram")
else:
    for i in str1:
       if  str1.count(i)!=str2.count(i):
         print("Not Anagram")
         break
    else:
        print("Anagram")