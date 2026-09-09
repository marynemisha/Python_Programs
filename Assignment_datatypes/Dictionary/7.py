#Write a program to sort a dictionary by its values
dict1 = {
    "C": 30,
    "A": 10,
    "D": 40,
    "B": 20
}
values = []
keys=[]
result = {}
for i in dict1:
    keys.append(i)
    values.append(dict1[i])
for i in range(len(values)):
    for j in range(i + 1, len(values)):
        if values[i] > values[j]:
            values[i], values[j] = values[j], values[i]
            keys[i], keys[j] = keys[j], keys[i]
for i in range(len(keys)):
    result[keys[i]] = values[i]
print(result)