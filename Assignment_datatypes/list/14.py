#Write a program to swap the first and last elements of a list
list1 = [10, 20, 30, 40, 50]
print(list1)
print("Number of elements:",len(list1))
temp=list1[0]
list1[0]=list1[-1]
list1[-1]=temp
print("Swapping=",list1)