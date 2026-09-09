#Define a function to find the BMI value.
# bmi=weight/(height)**2
def bmi(w, h):
    bmi= w / (h) ** 2
    return bmi
w = float(input("Enter weight: "))
h = float(input("Enter height: "))
print("BMI =", bmi(w, h))