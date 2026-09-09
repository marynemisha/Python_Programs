list1=['Python', 'Java', 'Django', 'HTML', 'C++', 'CSS', 'JavaScript', 'PHP']
print(list1)

#using del keyword
del list1[0]
print(list1)
del list1[1:3]
print(list1)

# using remove method
list1.remove("C++")
print(list1)

#using pop method
list1.pop(1)
print(list1)

# using clear method
list1.clear()
print(list1)

#using del
# del list
# print(list)      #we have 'list' method so its shows <class 'list'>

del list1
print(list1)         #NameError: name 'list1' is not defined. Did you mean: 'list'?

