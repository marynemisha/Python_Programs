#using if-else statement

largest=lambda x,y:x if x>y else y
print(largest(10,20))


largest=lambda x,y,z:x if x>y and x>z else y if  y>z else z
print(largest(10,20,30))

#using max()


largest=lambda a,b,c:max(a,b,c)
print(largest(4,5,6))