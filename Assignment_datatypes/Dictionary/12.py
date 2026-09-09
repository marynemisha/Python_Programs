#Write a program to create a dictionary of numbers from 1 to 10 and their squares.
dict1 = {}
for i in range(1, 11):
    dict1[i] = i * i

print("Square:",dict1)