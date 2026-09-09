#Write a program to remove all duplicate words from a sentence while maintaining their original order.
str1 = input("Enter a sentence: ")
print(str1)
word = ""
result = []
for ch in str1 + " ":
    if ch != " ":
        word += ch
    else:
        if word not in result:
            result.append(word)
        word = ""
ans = ""
for i in range(len(result)):
    ans += result[i]
    if i != len(result) - 1:
        ans += " "

print("Result:", ans)