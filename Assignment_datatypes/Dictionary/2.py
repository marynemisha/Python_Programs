#Write a program to find the key with the highest value.
stud = {
    "Math": 80,
    "English": 75,
    "Science": 90
}
print(stud)
print("Length:",len(stud))
key = ""
maximum = 0

for i in stud:
    if stud[i] > maximum:
        maximum = stud[i]
        key = i
print("Highest:", maximum)
print("Key:",key)
