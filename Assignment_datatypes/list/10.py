#Write a program to find the intersection of two lists without using sets.
list1=[1, 2, 3, 4, 5]
list2=[3, 4, 5, 6, 7]
print(list1)
print(list2)
print("Length of list1:",len(list1))
print("Length of list2:",len(list2))
result=[]
for i in list1:
    if i in list2:
        result.append(i)

print("Intersection:", result)
