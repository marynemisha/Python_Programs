#Write a program to split a list into two equal halves
list1 = [10, 20, 30, 40, 50, 60]
print(list1)
print("Number of elements:",len(list1))
mid=len(list1)//2
print("Mid:",mid)
first=[]
second=[]
for i in range(len(list1)):
    if i<mid:
        first.append(list1[i])
    else:
        second.append(list1[i])
print("First :",first)
print("Second:",second)