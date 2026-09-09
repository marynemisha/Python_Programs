#Write a program to count the number of even and odd numbers in a tuple.
tuple1=(10, 15, 20, 25, 30, 35)
print(tuple1)
print("Length:",len(tuple1))
even=0
odd=0
for i in tuple1:
    if i%2==0:
        even+=1
    else:
        odd+=1
print("Even:",even)
print("Odd:",odd)