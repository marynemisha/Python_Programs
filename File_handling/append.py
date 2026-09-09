f1=open("Demo.txt","a")
f1.write("\n It is interpreted")
f1.close()

a=open("Demo.txt")
print(a.read())
a.close()