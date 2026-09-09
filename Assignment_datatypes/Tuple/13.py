#Write a program to convert a tuple into a list, sort it, and convert it back into a tuple
tuple1 = (40, 10, 30, 20)
print(tuple1)
print("Length:",len(tuple1))
list1 = list(tuple1)
for i in range(len(list1)):
    for j in range(i + 1, len(list1)):
        if list1[i] > list1[j]:
            temp = list1[i]
            list1[i] = list1[j]
            list1[j] = temp
result = tuple(list1)
print("Sorted Tuple:", result)