list1=['Python', 'Java', 'Django', 'HTML', 'C++', 'CSS', 'JavaScript', 'PHP']
print(list1)

# for item in list1:
#     print(item)        #normal iteration using loop

for item in range(len(list1)):          #range(6)
     print(item,list1[item])             #list1[0,1,2,3....]