#Write a program to find the longest palindromic substring in a given string.
s = "banana"
print(s)
longest = ""
for i in range(len(s)):
    for j in range(i, len(s)):
        sub = s[i:j+1]
        if sub == sub[::-1] and len(sub) > len(longest):
            longest = sub
print("substring:", longest)
