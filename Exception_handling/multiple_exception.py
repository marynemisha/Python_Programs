try:
    num1=int(input("Enter the number:"))
    num2=int(input("Enter the number:"))
    print(num1/num2)
except ZeroDivisionError:
    print("You can't divide by zero")
except ValueError:
    print("Please enter a valid integer")