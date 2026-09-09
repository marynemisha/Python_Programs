num=int(input("Enter a number:"))
temp=num
sum=0
length=len(str(num))
print("Number of digits:",length)
while num>0:
    digit=num%10
    sum+=digit**length
    num//=10
    length-=1
if sum==temp:
    print("Disarium number....")
else:
    print("Not a disarium number....")