#Write a program to remove duplicate elements from a list while preserving the original order.
list1=[10, 20, 30, 20, 40, 10, 50]
result=[]
print(list1)
print("Numbers of elements:",len(list1))
for i in range(len(list1)):
        if list1[i] not in result:
            result.append(list1[i])
print(result)