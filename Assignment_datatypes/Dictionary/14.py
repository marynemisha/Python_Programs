#Write a program to print all keys whose values are greater than a given number
dict1 = {
    "A": 10,
    "B": 25,
    "C": 30,
    "D": 15
}
print(dict1)
num = int(input("Enter the number: "))
for i in dict1:
    if dict1[i] > num:
        print("keys:",i)