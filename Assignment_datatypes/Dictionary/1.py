#Write a program to find the sum of all values in a dictionary.
student = {
    "Math"   : 80,
    "English": 75,
    "Science": 90
}
print(student)
print("Length:",len(student))
total=0
for i in student.values():
    total+=i
print("Sum:",total)