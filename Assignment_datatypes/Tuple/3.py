#Write a program to find the maximum and minimum elements in a tuple.

tuple1 = (10, 20, 5, 40, 15)
print(tuple1)
print("Number of elements:", len(tuple1))
min=tuple1[0]
max=tuple1[0]
for i in tuple1:
    if i>max:
        max=i
    elif i<min:
        min=i
print("Minimum:",min)
print("Maximum:",max)