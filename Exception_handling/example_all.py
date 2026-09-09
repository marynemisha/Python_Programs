try:
    num=int(input("Enter a number:"))
    result=200/num
except ValueError:
    print("Invalid input....")
except ZeroDivisionError:
    print("Division by zero....")
else:
    print("Result is:",result)
finally:
    print("Division completed....")

