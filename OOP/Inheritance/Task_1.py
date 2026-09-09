class ATM:
    def __init__(self):
        self.account_number=0
        self.holder_name=""
        self.balance=0
    def create_account(self):
        self.account_number=int(input("Enter the number:"))
        self.holder_name=input("Enter the name:")
        self.balance = int(input("Enter the balance:"))
        print("Account created successfully....!")
    def deposit(self):
        amount=float(input("Enter the deposit:"))
        self.balance+=amount
        print("Deposit successfully....!")
    def withdraw(self):
        amount=float(input("Enter the amount:"))
        if amount<=self.balance:
            self.balance-=amount
        else:
            print("Insufficient balance....!")
    def balance_enquiry(self):
        print("Balance:", self.balance)
    def mini_statement(self):
        print("................Details..............")
        print("Account number:",self.account_number)
        print("Holder name:",self.holder_name)
        print("Balance:", self.balance)

obj=ATM()
while True:
    print("1.Create account")
    print("2.Deposit")
    print("3.Withdraw")
    print("4.Balance enquiry")
    print("5.Mini statement")
    print("6.Exit")

    choice=int(input("Enter your choice:"))
    if choice==1:
        obj.create_account()
    elif choice==2:
        obj.deposit()
    elif choice==3:
        obj.withdraw()
    elif choice==4:
        obj.balance_enquiry()
    elif choice==5:
        obj.mini_statement()
    elif choice==6:
        print("Thank you for ur time.....")
        break
    else:
        print("Invalid choice")




