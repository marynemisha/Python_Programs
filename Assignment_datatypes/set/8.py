#Write a program to find the maximum and minimum elements in a set
set1 = {10, 30, 5, 20}
print(set1)
max=0
min=0
for i in set1:
    if i>max:
        max=i
    else:
        min=i
print("Maximum:",max)
print("Minimum:",min)