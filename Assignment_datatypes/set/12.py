#Write a program to remove all elements from a set one by one.
set1={10,20,30}
print(set1)
print("Length:",len(set1))
while len(set1) > 0:
    item = set1.pop()
    print("Removed:", item)
print("Set:", set1)