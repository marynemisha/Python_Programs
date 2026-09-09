string="pYThon"

upper=0
lower=0
others=0
for i in string:
    if i.isupper():
        upper+=1
    elif i.islower():
        lower+=1
    else:
       others+=1
print("Number of uppercase: ",upper)
print("Number of lowercase: ",lower)
print("Number of lowercase: ",others)
