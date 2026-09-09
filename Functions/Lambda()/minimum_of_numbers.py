small=lambda a,b,c:a if a<b and a<c else b if b<c else c
print(small(2,45,21))

small=lambda a,b,c:min(a,b,c)
print(small(2,3,5))