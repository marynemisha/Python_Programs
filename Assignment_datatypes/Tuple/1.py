#Write a program to count the frequency of each element in a tuple.
tuple1 = (10, 20, 10, 30, 20, 10)
print(tuple1)
print("Number of elements:",len(tuple1))
freq = {}

for i in tuple1:
    if i in freq:
        freq[i] += 1
    else:
        freq[i] = 1

print("Frequency of each element:",freq)
