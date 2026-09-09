#Write a program to remove a key from a dictionary without using the pop() method.
dict1 = {
    "A": 10,
    "B": 20,
    "C": 30,
    "D": 40
}
print(dict1)
print("Length:", len(dict1))
key = input("Enter the key: ")
result = {}
for i in dict1:
    if i != key:
        result[i] = dict1[i]
print("Result:", result)