#Write a Python program to reverse a string.
def reverse(s):
    rev=""
    for i in s:
        rev=i+rev
    print("Reverse:",rev)
s=input("Enter the string:")
reverse(s)
