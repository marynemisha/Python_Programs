#Write a program to capitalize the first letter of each word without using the title() method
str1 = input("Enter a sentence: ")
print("str1:",str1)
result = ""
print("Length:",len(str1))
for i in range(len(str1)):
    if i == 0 or str1[i-1] == " ":
        result += str1[i].upper()
    else:
        result += str1[i]
print(result)