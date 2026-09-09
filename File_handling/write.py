file=open("Demo.txt","w")
file.write("File handling in python.")
file.close()

a=open("Demo.txt")
print(a.read())
a.close()