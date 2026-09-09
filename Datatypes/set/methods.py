set1=x={"python","css","php","Html","python"}
print(x)
print(type(x))

#using add() method
set1.add("javascript")
print(set1)

set1.add("c++")
print(set1)

#using update() method
set1.update(["Bootstrap","c"])
print(set1)

set1.update({"Bootstrap","c"})
print(set1)

#using remove() method
set1.remove("php")
print(set1)

# set1.remove("luminar")
# print(set1)

#using discard method
set1.discard("Html")
print(set1)

set1.discard("luminar")
print(set1)

# using clear() method
set1.clear()
print(set1)