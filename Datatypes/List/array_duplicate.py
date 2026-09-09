array1=[1,2,3,4,5,6]
array2=[7,8,9,2,3,5]

common=[]
print("Number of elements:",len(array1))
print("Number of elements:",len(array2))
for i in range(len(array1)):
    for j in range(len(array2)):
        if array1[i]==array2[j] and array1[i] not in common:
            common.append(array1[i])
print(common)


# another method or simple method
# array1=[1,2,3,4,5,6]
# array2=[7,8,9,2,3,5]
#
# common=[]
#
# for i in array1:
#     for j in array2:
#         if i==j and i not in common:
#             common.append(i)
# print(common)