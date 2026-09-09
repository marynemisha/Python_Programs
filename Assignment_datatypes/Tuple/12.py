# Write a program to find all duplicate elements in a tuple.
tuple1 = (10, 20, 10, 30, 20, 40, 50, 10)
print(tuple1)
print("Length:", len(tuple1))
duplicate=[]
for i in range(len(tuple1)):
    for j in range(i + 1, len(tuple1)):
        if tuple1[i] == tuple1[j] and tuple1[i] not in duplicate:
            duplicate.append(tuple1[i])

print("Duplicate:", duplicate)