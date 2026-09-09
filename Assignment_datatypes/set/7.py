#Write a program to check whether two sets are disjoint
set1={1,2,3}
set2={3,4}
print(set1)
print(set2)
if set1 & set2:
    print("Disjoint...")
else:
    print("Not disjoint....")