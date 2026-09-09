#Write a program to remove all negative numbers from a list.
list1 = [10, -5, 20, 0,-8, 15, -3]
print(list1)
result=[]
for i in list1:
    if i>=0:
        result.append(i)
print(result)
