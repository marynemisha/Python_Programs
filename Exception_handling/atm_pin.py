def atm():
    correct_pin=1234
    balance=5000

    try:
        pin=int(input("Enter pin number:"))
        if pin!=correct_pin:
            raise ValueError("Wrong pin number")
        print("Login successful....!")

        amount=int(input("Enter amount to withdraw:"))
        if amount>balance:
            raise ValueError("Insufficient balance....!")
        balance-=amount
        print("Withdrawal successful....!")
        print("Remaining balance:",balance)

    except Exception as e:
        print("Error:",e)

    finally:
        print("Thank you for your time....!")

atm()
