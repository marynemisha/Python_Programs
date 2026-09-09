#Write a Python program that prompts the user to input an integer and raises a
# ValueError exception if the input is not a valid integer.
try:
    n=input("Enter the number:")
    print("Original number:",n)
    if not n.isdigit():
        raise ValueError("It is not a valid integer....!")
    n=int(n)
    print("New:",n)
except Exception as e:
    print("Error",e)
else:
    print("It is a integer:",n)


