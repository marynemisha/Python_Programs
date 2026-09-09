num=int(input("Enter a number :"))
if num < 0:
    print("Please enter a positive number...!")
elif num == 0:
    print("Number is zero...!")
elif num == 1:
    print("1 is a composite number...!")
else:
    for i in range(2,num):
        if num % i ==0:
            print("Not a prime number...!")
            break
    else:
        print(num,"is a prime number...!")