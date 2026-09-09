class Shape:
    def draw(self):
        print("Draw a shape...!")
class Circle(Shape):
    def draw(self):
        print("Draw a circle...!")
obj1=Shape()         #parent class calling
obj1.draw()

obj2=Circle()      #override chyth child class print chyum
obj2.draw()