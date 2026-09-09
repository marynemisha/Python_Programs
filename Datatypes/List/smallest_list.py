list1=[11,20,35,4,50,22,32]
smallest=list1[0]
for i in range(len(list1)):
    if list1[i] <smallest:
        smallest = list1[i]
print("smallest=", smallest)