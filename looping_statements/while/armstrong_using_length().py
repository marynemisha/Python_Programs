num=int(input("Enter the number:"))
temp=num
sum=0
length=len(str(num))
print("Number of digits is:",length)
while num>0:
    digit=num%10
    sum+=digit**length
    num//=10
if sum==temp:
    print("Armstrong number")
else:
    print("Not an armstrong number")