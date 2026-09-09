#Write a program to count the number of even and odd numbers in a list.
list1=[2,34,35,11,68]
print(list1)
print("Number of elements:",len(list1))
even=0
odd=0
for i in range(len(list1)):
    if list1[i] %2==0:
        even+=1
    else:
        odd+=1
print("Even=",even)
print("Odd=",odd)

