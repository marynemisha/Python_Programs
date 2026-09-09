num=int(input("Enter the number:"))
largest=int(input("Enter the largest number:"))
smallest=int(input("Enter the smallest number:"))
while num>0:
    digit=num%10
    if digit>largest:
        largest=digit
    elif digit<smallest:
        smallest=digit
    else:
        num=num//10
print("largest:",largest)
print("smallest:",smallest)
