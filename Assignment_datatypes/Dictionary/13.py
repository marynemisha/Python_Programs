#Write a program to update the value of a key only if the key exists in the dictionary
dict1 = {
    "A": 10,
    "B": 20,
    "C": 30
}
print(dict1)
key = input("Enter the key: ")
if key in dict1:
    value = int(input("Enter the new value: "))
    dict1[key] = value
    print("Updated :", dict1)
else:
    print("Key does not exist")