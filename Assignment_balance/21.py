#Create a function to generate a list of squares of numbers from 1 to n using list
# comprehension.
def square(num):
    return[i**2 for i in range(1,num+1)]

num=int(input("Enter the number:"))
print("Squares:",square(num))