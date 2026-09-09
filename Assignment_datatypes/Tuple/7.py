#Write a program to reverse a tuple without using slicing.
tuple1=(10, 20, 30, 40, 50)
print(tuple1)
print("Length:",len(tuple1))
rev=0
result=[]
for i in range(len(tuple1)-1,-1,-1):
    result.append(tuple1[i])
    rev=tuple(result)
print(rev)