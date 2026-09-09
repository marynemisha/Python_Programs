#Write a program to find the largest and smallest elements in a list without using max() and min()
list1=[11,20,35,4,50,22,32]
print(list1)
print("Number of elements:",len(list1))
largest=list1[0]
smallest=list1[0]
for i in range(len(list1)):
    if list1[i]>largest:
        largest=list1[i]
print("Largest=",largest)

for i in range(len(list1)):
    if list1[i]<smallest:
        smallest=list1[i]
print("Smallest=",smallest)