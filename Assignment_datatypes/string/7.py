#Write a program to replace all occurrences of a given word with another word in a sentence without using the replace() method
sentence = "I love programming because programming is simple"
print("Sentence:",sentence)
old = input("Enter the old word:")
new = input("Enter the new word:")
result = ""
word = ""
for i in sentence:
    if i != " ":
        word += i
    else:
        if word == old:
            result += new + " "
        else:
            result += word + " "
        word = ""
if word == old:
    result += new
else:
    result += word
print("Result:", result)
