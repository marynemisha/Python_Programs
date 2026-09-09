#Write a program to print all words in a sentence that start with a vowel
str1 = input("Enter a sentence: ")
word = ""
for ch in str1:
    if ch != " ":
        word += ch
    else:
        if word[0] in "AEIOUaeiou":
            print(word)
        word = ""
if word != "":
    if word[0] in "AEIOUaeiou":
        print(word)