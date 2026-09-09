#write a program to count the occurrence of a given element in a tuple without using the count() method.
tuple1 = (10, 20, 10, 30, 20, 10)
print(tuple1)
print("Length:",len(tuple1))
num=int(input("Enter the element:"))
count=0
for i in tuple1:
    if i == num:
        count += 1
print("count=",count)