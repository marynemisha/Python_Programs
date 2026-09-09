#Write a program to create a dictionary from two lists (one containing keys and the other values)
keys = ["A", "B", "C"]
values = [10, 20, 30]
print("Keys:", keys)
print("Values:", values)
dict1 = {}
for i in range(len(keys)):
    dict1[keys[i]] = values[i]
print("Dictionary:", dict1)