#Write a program to find all prime numbers present in a list.
list1 = [10, 7, 15, 13, 20, 17]
print(list1)
print("Number of elements:", len(list1))
result=[]
for i in list1:
        if i>1:
            for j in range(2,i):
                if i % j==0:
                    break
            else:
                print(i)
