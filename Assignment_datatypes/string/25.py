#Write a program to find the word with the maximum number of characters in a sentence.
str1 = input("Enter a sentence: ")
word = ""
longest = ""
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