#Write a program to create a new list containing only the duplicate elements from a given list
list1=[10, 20, 30, 20, 40, 10, 50]
print(list1)
print("Numbers of elements:",len(list1))
new=[]
for i in range(len(list1)):
    for j in range(i+1,len(list1)):
        if list1[i]==list1[j] and list1[i] not in new:
            new.append(list1[i])
print("Duplicate:",new)
