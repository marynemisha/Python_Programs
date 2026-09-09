#Write a program to merge two dictionaries. If a key exists in both, add their values.
dict1 = {
    "A": 10,
    "B": 20,
    "C": 30
}

dict2 = {
    "B": 15,
    "C": 25,
    "D": 40
}

print(dict1)
print(dict2)
result = {}
for i in dict1:
    result[i] = dict1[i]
for i in dict2:
    if i in result:
        result[i] = result[i] + dict2[i]
    else:
        result[i] = dict2[i]

print("Merge:", result)