#Write a Python program to determine whether a given year is a leap year.
y=int(input("Enter the year:"))
if y%400==0:
    print("Leap year...!")
elif y%100==0:
    print("Not a leap year...!")
elif y%4==0:
    print("Leap year...!")
else:
    print("Not a leap year...!")