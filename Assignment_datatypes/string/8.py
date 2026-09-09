#Write a program to find the longest word in a sentence.
str1= "I love programming"
print(str1)
print("Length:",len(str1))
longest = ""
word = ""
for ch in str1:
    if ch != " ":
        word += ch
    else:
        if len(word) > len(longest):
            longest = word
        word = ""
if len(word) > len(longest):
    longest = word
print("Longest word:", longest)
