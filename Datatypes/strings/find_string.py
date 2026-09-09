str1=("Introduction to python programming,welcome python"
      "simple and easy to use and learn....")

print(str1)
print(str1.find("to"))                   #returns first occurance
print(str1.find("luminar"))

print(str1.index("to"))
#print(str1.index("luminar"))          #ValueError: substring not found

print(str1.rfind("to"))                 #returns last occurance
print(str1.rfind("luminar"))

print(str1.count("to"))                #count the value in the string
print(str1.count("luminar"))