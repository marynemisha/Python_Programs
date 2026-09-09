#Write a program to compress a string by replacing consecutive repeated characters with their occurrence count.
str1= ("python")
print(str1)
com= ""
count = 1
for i in range(len(str1)):
    if i < len(str1) - 1 and str1[i] == str1[i + 1]:
        count += 1
    else:
        com+= str1[i] + str(count)
        count = 1
print(com)
