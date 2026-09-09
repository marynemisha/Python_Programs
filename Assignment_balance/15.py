#Write a Python program to print the next 5 days starting today.
import datetime
today = datetime.datetime.now()
for i in range(5):
    print(today + datetime.timedelta(days=i))
