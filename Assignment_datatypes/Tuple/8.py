#Write a program to find the sum of all numeric elements in a tuple.
tuple1=(10,20,30,40,50)
print(tuple1)
print("Length:",len(tuple1))
total=0
for i in tuple1:
    total+=i

print("Total:",total)