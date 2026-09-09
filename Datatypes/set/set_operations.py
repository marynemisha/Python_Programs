set1={"Adith","Anurenj","Sreena","Nemisha","Adith"}
set2={"Rahul","Teena","Reshma","Teena","Anurenj","Nemisha"}

#using union operation
print(set1.union(set2))          #using union() method
print(set1|set2)                 #using pipe operator

# using intersection operation
print(set1.intersection(set2))    #using intersection() method
print(set1& set2)                 #using and operator

#using difference operation
print(set1-set2)                  #using minus operator
print(set1.difference(set2))      #using difference() method

#using symmetric difference
print(set1^set2)                            #using ^ operator
print(set1.symmetric_difference(set2))      #using symmetric_difference() method