#Write a program to count the frequency of each word in a sentence using a dictionary
sent = input("Enter a sentence: ")
print(sent)
freq = {}
word = ""

for i in sent:
    if i != " ":
        word = word + i
    else:
        if word in freq:
            freq[word] += 1
        else:
            freq[word] = 1
        word = ""


if word != "":
    if word in freq:
        freq[word] += 1
    else:
        freq[word] = 1

print(freq)