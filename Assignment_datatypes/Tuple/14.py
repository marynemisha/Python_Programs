#Write a program to compare two tuples and display the common elements.
tuple1 = (10, 20, 30, 40, 50)
tuple2 = (30, 40, 50, 60, 70)
print("Tuple 1:", tuple1)
print("Tuple 2:", tuple2)
common = []
for i in tuple1:
    for j in tuple2:
        if i == j:
            if i not in common:
                common.append(i)
print("Common:", common)