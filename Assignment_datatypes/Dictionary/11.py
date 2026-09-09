#Write a program to check whether a given key exists in a dictionary
dict1 = {
    "A": 10,
    "B": 20,
    "C": 30
}
print(dict1)
key=input("Enter the key:")

if key in dict1:
    print("key exists")
else:
    print("Not exists")