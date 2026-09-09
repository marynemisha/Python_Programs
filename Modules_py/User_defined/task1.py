import mymodule
import mymodule as x
from mymodule import subtraction

num1=int(input("Enter the number:"))
num2=int(input("Enter the number:"))
print(mymodule.addition(num1,num2))
print(x.addition(num1,num2))
print(subtraction(num1,num2))
