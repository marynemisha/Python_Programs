limit=int(input("Enter the limit :"))
a=0
b=1
print("Fibonacci series:")
for i in range(limit):
    print(a)
    c=a+b
    a=b
    b=c