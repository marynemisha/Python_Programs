#Write a program to check whether two tuples contain the same elements regardless of order.
tuple1 = (10, 20, 30)
tuple2 = (30, 10, 20)
print(tuple1)
print("Length:",len(tuple1))
print("Length:",len(tuple2))
count = 0
for i in tuple1:
    for j in tuple2:
        if i == j:
            count += 1
            break

if count == len(tuple1):
    print("Same elements....!")
else:
    print("Different elements....!")