#Write a program to merge two sorted lists into a single sorted list.
list1 = [10, 20, 30]
list2 = [15, 25, 35]
print(list1)
print(list2)
print("length of list1:",len(list1))
print("length of list2:",len(list2))
result=[]
temp=0
for i in list1:
    result.append(i)

for i in list2:
    result.append(i)
for i in range(len(result)):
    for j in range(i+1,len(result)):
        if result[i]>result[j]:
            temp = result[i]
            result[i] = result[j]
            result[j] = temp
print(result)

