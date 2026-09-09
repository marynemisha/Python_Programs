#Write a program to check whether a string is a palindrome without using slicing
str1 = input("Enter a string: ")
print("str1:",str1)
reverse = ""
for i in str1:
    reverse = i + reverse
if str1 == reverse:
    print("Palindrome")
else:
    print("Not a palindrome")