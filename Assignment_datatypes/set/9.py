#Write a program to count the number of unique words in a sentence
s = input("Enter a sentence: ")
word = ""
words = []
for i in s:
    if i == " ":
        words.append(word)
        word = ""
    else:
        word += i
print(len(set(words)))