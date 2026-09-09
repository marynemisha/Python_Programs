#without list comprehension
list1=[1,2,3,4,5]
new_list=[]

for i in list1:
    new_list.append(i**2)
print(new_list)             #append kodutha kond athil add avum

#using list comprehension
x=[i**2 for i in list1]     #new_list=[expression for item in iterable]
print(x)