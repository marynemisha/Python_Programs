#Write a program to separate even and odd numbers into two different lists
list1 = [10, 15, 20, 25, 30, 35]
print(list1)
print("length of the list:",len(list1))
even=[]
odd=[]
for i in list1:
    if i%2==0:
        even.append(i)
    else:
        odd.append(i)

print("Even:",even)
print("Odd:",odd)