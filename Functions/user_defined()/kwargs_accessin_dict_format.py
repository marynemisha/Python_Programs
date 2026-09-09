def student(**data):
    print(data)
    for key,value in data.items( ):
        print(key," : ",value)

student(Name="Anju",age=23,place="Kochi")