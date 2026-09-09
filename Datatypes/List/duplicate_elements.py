list1=[32,21,20,32,20]
new_list=[]
print("Number of elements:",len(list1))
for i in range(len(list1)):
    for j in range(i+1,len(list1)):
        if list1[i]==list1[j] and list1[i] not  in new_list:
            new_list.append(list1[i])
print(new_list)