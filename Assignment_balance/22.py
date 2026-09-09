#Generate 3 random integers between 100 and 999 which is divisible by 5
import random
count=0
while count<3:
    num=random.randint(100,999)
    if num%5==0:
        print(num)
        count+=1