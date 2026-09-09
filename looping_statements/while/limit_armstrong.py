lower=int(input("Enter a number:"))
upper=int(input("Enter a number:"))
for num in range(lower,upper+1):
    temp=num
    length=len(str(num))
    sum=0
    while num>0:
        digit=num%10
        sum+=digit**length
        num//=10
    if sum==temp:
        print(sum)


