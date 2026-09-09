physics=float(input("Enter the mark of physics     :"))
chemistry=float(input("Enter the mark of chemistry :"))
maths=float(input("Enter the mark of maths         :"))
english=float(input("Enter the mark of english     :"))
computer=float(input("Enter the mark of computer   :"))

total=physics+chemistry+maths+english+computer
percentage=(total/500)*100
print("Total marks     :",total)
print("Percentage      :",percentage)

if percentage>=90:
    print("Grade  : A")
elif percentage>=80:
    print("Grade  : B")
elif percentage>=70:
    print("Grade  : C")
elif percentage>=60:
    print("Grade  : D")
else:
    print("Failed....!")