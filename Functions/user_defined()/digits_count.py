def count_digits(num):
    digits=0
    while num>0:   #num!=0(another method)
        num //= 10
        digits+=1
    return digits
num=int(input("Enter the number:"))
print(count_digits(num))
