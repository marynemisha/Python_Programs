class Father:                                          #Parent1
    def father_skills(self):
        print("Driving.....")
class Mother:                                           #Parent2
    def mother_skills(self):
        print("Cooking.....")
class Child(Father,Mother):                             #child class
    def child_skills(self):
        print("Studying.....")
obj=Child()
obj.child_skills()
obj.father_skills()
obj.mother_skills()
