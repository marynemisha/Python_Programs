#reverse pattern program
string="python"
print("My string:",string)
print("Number of characters:",len(string))
for i in range(len(string),0,-1):     #start=6,end=0,step=-1
    print(string[:i])