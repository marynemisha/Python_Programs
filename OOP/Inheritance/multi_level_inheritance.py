class Grandfather:
    def house(self):
        print("Grandfather's house........")
class Father(Grandfather):
    def bike(self):
        print("Father's bike.........")
class Son(Father):
    def laptop(self):
        print("Son's laptop.........")
object1=Son()
object1.laptop()
object1.bike()
object1.house()