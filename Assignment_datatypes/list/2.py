#Write a program to find the second largest and second smallest elements in a list without using the sort() method.
list1 = [10, 40, 20, 60, 30]
print("List:", list1)
print("Number of elements:", len(list1))
large =0
second_largest =0
small=list1[0]
second_smallest=list1[1]
#largest
for i in list1:
    if i>large:
        second_largest = large
        large = i

    elif i>second_largest and i!=large:
        second_largest = i

#smallest
for i in list1:
    if i < small:
        second_smallest = small
        small = i

    elif i < second_smallest and i!=small:
        second_smallest = i

print("Largest =", large)
print("Second Largest =", second_largest)
print("Smallest =", small)
print("Second Smallest =", second_smallest)