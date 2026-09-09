import random
print(random.randint(1,50))
#returns a number between 1 and 50(inclusive)

print(random.random())
#returns a random value between 0.0 and 1.0

students=["Anju","Anu","Sree","Nemisha"]
print(students)
random.shuffle(students)
print(students)

employees=["Anju","Anu","Sree","Nemisha"]
print(random.choice(employees))