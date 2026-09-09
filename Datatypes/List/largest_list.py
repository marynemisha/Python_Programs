list1=[11,20,35,4,50,22,32]
print("Number of elements in list1:",len(list1))
largest=list1[0]     #11
for i in range(len(list1)):    #i=0,1,2,3,4,5,6
    if list1[i]>largest:
        largest=list1[i]
print("Largest=",largest)