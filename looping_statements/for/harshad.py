num=int(input("Enter a number :"))
sum=0
for i in str(num):
    sum=sum+int(i)
print("Sum of it's digits =",sum)

if num % sum == 0:
    print("Harshad number....!")
else:
    print("Not a Harshad number....!")