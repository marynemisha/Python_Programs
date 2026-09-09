#Write a program to find the frequency of each element in a list.
list1 = [10, 20, 10, 30, 20, 10]
print(list1)
print("Number of elements:",len(list1))
freq=[]
for i in list1:
    if i not in freq:
        print(i,"=",list1.count(i))
    freq.append(i)