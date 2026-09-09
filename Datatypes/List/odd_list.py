list1=[11,20,35,4,50,22,32]
print("Number of elements in list1:",len(list1))

for i in range(1,len(list1),2):          #range(7)
    #odd positions are: 1,3,5
    print(i,"--->",list1[i])
    