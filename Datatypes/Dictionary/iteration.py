student={"Name":"Nemisha",
         "Age":20,
         "Gender":"Female",
         "Course":"Python Fullstack",
         "Institute":"Luminar",
         "Skills":["Python","HTML","Django"]
         }
# for i in student:      #keys  only
# for i in student.keys():    #keys
# for i in student.values():   #values
for i in student.items():     #keys and values
    print(i)
    # print(type(i))