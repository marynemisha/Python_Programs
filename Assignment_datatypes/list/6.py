#Write a program to rotate a list to the left by k positions
list1 = [10, 20, 30, 40, 50]
k = 2
list1 = list1[k:] + list1[:k]
print(list1)
