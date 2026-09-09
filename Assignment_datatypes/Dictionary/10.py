#Write a program to count the number of occurrences of each character in a string using a dictionary.
string = input("Enter a string: ")
freq = {}
for i in string:
    if i in freq:
        freq[i] += 1
    else:
        freq[i] = 1
print("Frequency:", freq)