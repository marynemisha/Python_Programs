#without list comprehension
students=["Althaf","Anu","Keerthi","Rishi","Manu","Nimmy","Kavya"]
newlist=[]
for name in students:
    if 'a' in name or'A' in name:
        newlist.append(name)
print(newlist)


#using list comprehension
new_data=[name for name in students if 'a' in name or 'A' in name]
print(new_data)