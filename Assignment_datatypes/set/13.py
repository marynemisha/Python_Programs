#Write a program to convert a list into a set and then back into a list without duplicate elements.
list1 = [10, 20, 30, 20, 40, 10, 50]
set1=set(list1)
print("set:",set1)
list2=list(set1)
print("list:",list2)
