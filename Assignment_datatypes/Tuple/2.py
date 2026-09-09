#Write a program to merge two tuples without using the + operator
tuple1 = (10, 20, 30)
tuple2 = (40, 50, 60)

print(tuple1)
print(tuple2)
result=[]
for i in tuple1:
    result.append(i)
for i in tuple2:
    result.append(i)

merge=tuple(result)
print("Merge=",result)