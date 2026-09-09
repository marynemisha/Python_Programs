#Write a program to find the length of the longest substring without repeating characters.
str1 = input("Enter a string: ")
print(str1)
longest = 0
print("Length:",len(str1))
for i in range(len(str1)):
    sub = ""
    for j in range(i, len(str1)):
        if str1[j] not in sub:
            sub += str1[j]
        else:
            break
    if len(sub) > longest:
        longest = len(sub)

print("Result:", longest)