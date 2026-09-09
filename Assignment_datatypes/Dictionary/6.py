#Write a program to sort a dictionary by its keys
dict1 = {
    "C": 30,
    "A": 10,
    "D": 40,
    "B": 20
}
keys = []
temp=0
result = {}
for i in dict1:
    keys.append(i)
for i in range(len(keys)):
    for j in range(i + 1, len(keys)):
        if keys[i] > keys[j]:
            temp = keys[i]
            keys[i] = keys[j]
            keys[j] = temp
for i in keys:
    result[i] = dict1[i]
print(result)