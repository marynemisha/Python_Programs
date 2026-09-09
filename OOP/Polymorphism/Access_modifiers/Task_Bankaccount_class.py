class Bank_account:
    def __init__(self):
        self.__account_number=987654321234
        self.__balance=0
    def deposit(self):
        print("....Deposit details....")
        amount=float(input("Enter your deposit amount:"))
        self.__balance+=amount
        print("Deposited amount:",amount)
    def withdraw(self):
        print("....Withdrawal details....")
        amount=float(input("Enter your withdrawal amount:"))
        if amount <= self.__balance:
            self.__balance-=amount
            print("Withdrawn:", amount)
        else:
            print("Insufficient balance")
    def display_balance(self):
        print("....Balance details....")
        print("Account Number:", self.__account_number)
        print("Balance:", self.__balance)

obj=Bank_account()
obj.deposit()
obj.withdraw()
obj.display_balance()



