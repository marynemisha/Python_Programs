#Write a program to find the first non-repeating character in a string using a dictionary.
s = "swiss"
print(s)
freq = {}
for ch in s:
    if ch in freq:
        freq[ch] += 1
    else:
        freq[ch] = 1
for ch in s:
    if freq[ch] == 1:
        print("Non-repeating character:", ch)
        break
else:
    print("No non-repeating character found")
