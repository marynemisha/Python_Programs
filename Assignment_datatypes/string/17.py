#Write a program to find the minimum number of character insertions require to make a string a palindrome.
str1 = input("Enter a string: ")
print(str1)
count = 0
temp = str1
while temp != temp[::-1]:
    temp = temp + temp[0]
    count += 1
print("Minimum insertions:", count)