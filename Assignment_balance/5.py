#Write a Python program to create a class representing a Circle. Include methods
# to calculate its area and perimeter
class Circle:
    def __init__(self):
        self.r=radius
    def area(self):
        area=3.14 * self.r * self.r
        print("Area:",area)
    def perimeter(self):
        perimeter=2 * 3.14 * self.r
        print("Perimeter:",perimeter)
radius=int(input("Enter the radius:"))

obj=Circle()
obj.area()
obj.perimeter()