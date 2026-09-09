#default arguments
def student(name,place="TVM"):
    print("Student name:",name)
    print("Student place:",place)
student("Anu","Kochi")
#student("Ammu")   #typeError: student() missing 1 required positional argument: 'place'
student("Ammu")