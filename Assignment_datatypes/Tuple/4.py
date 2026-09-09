#Write a program to convert a tuple into a list and remove duplicate elements.
tuple1 = (10, 20, 10, 30, 20, 40)
print(tuple1)
print("Number of elements:", len(tuple1))
list1 = list(tuple1)
result = []
for i in list1:
    if i not in result:
        result.append(i)

print("Result:", result)