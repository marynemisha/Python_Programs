#Write a program to count the number of keys and values in a nested dictionary
dict1 = {
    "Student1": {"Name": "Arun", "Age": 20},
    "Student2": {"Name": "Anu", "Age": 21}
}
print(dict1)
key = 0
value = 0
for i in dict1:
    key+= 1
    for j in dict1[i]:
        key += 1
        value+= 1

print("key:", key)
print("value:", value)