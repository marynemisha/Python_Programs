student={"Name":"Nemisha",
         "Age":20,
         "Gender":"Female",
         "Course":"Python Fullstack",
         "Institute":"Luminar",
         "Skills":["Python","HTML","Django"]
         }
print(student)

#adding element
student["Mobile"]=9876543212
print(student)
print(student["Mobile"])        #accessing mobile number

#updating element
student["Name"]="Mary Nemisha"
print(student)                            #update name


#removing element
del student["Gender"]
print(student)          #delete gender

student.clear()
print(student)         #empty dict

del student
print(student)      #name 'student' is not defined

