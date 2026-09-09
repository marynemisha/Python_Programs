class Bank:
    def __init__(self):
        self.bank_name=""
        self.branch=""
        self.contact=""
        self.IFSC=""
        self.manager=""
    def bank_data(self):
        self.bank_name =input("Enter the bank name:")
        self.branch = input("Enter the branch name:")
        self.contact =int(input("Enter the contact number:"))
        self.IFSC =input("Enter the IFSC:")
        self.manager =input("Enter the manager name:")
    def bank_info(self):
        print("..............Bank details..............")
        print("Bank name:",self.bank_name)
        print("Branch:",self.branch)
        print("Contact_number:",self.contact)
        print("IFSC:",self.IFSC)
        print("Manager name:",self.manager)
class Savings:
    def __init__(self):
        self.account_number = ""
        self.customer_name = ""
        self.balance = ""
        self.mobile = ""
        self.interest_rate = ""
    def savings_data(self):
        self.account_number = input("Enter Account Number: ")
        self.customer_name = input("Enter Customer Name: ")
        self.balance = int(input("Enter Balance: "))
        self.mobile = input("Enter Mobile Number: ")
        self.interest_rate = int(input("Enter Interest Rate: "))
    def savings_info(self):
        print("............Savings account details............")
        print("Account Number :", self.account_number)
        print("Customer Name :", self.customer_name)
        print("Balance :", self.balance)
        print("Mobile :", self.mobile)
        print("Interest Rate :", self.interest_rate)
class Current:
    def __init__(self):
        self.acc_number = ""
        self.customer_name = ""
        self.balance = ""
        self.business_name = ""
    def current_data(self):
        self.acc_number = input("Enter Account Number: ")
        self.customer_name = input("Enter Customer Name: ")
        self.balance = int(input("Enter Balance: "))
        self.business_name = input("Enter Business Name: ")
    def current_info(self):
        print("..........Current account details..........")
        print("Account Number :", self.acc_number)
        print("Customer Name :", self.customer_name)
        print("Balance :", self.balance)
        print("Business Name :", self.business_name)
class Loan:
    def __init__(self):
        self.loan_number = ""
        self.customer_name = ""
        self.loan_amount = ""
        self.interest_rate = ""
        self.loan_type = ""
        self.duration = ""
    def loan_data(self):
        self.loan_number = input("Enter Loan Number: ")
        self.customer_name = input("Enter Customer Name: ")
        self.loan_amount = int(input("Enter Loan Amount: "))
        self.interest_rate = int(input("Enter Interest Rate: "))
        self.loan_type = input("Enter Loan Type: ")
        self.duration = input("Enter Loan Duration: ")
    def loan_info(self):
        print("..............Loan account details..............")
        print("Loan Number :", self.loan_number)
        print("Customer Name :", self.customer_name)
        print("Loan Amount :", self.loan_amount)
        print("Interest Rate :", self.interest_rate)
        print("Loan Type :", self.loan_type)
        print("Duration :", self.duration)


obj1 = Savings()
obj1.bank_data()
obj1.savings_data()
obj1.bank_info()
obj1.savings_info()

obj2 = Current()
obj2.bank_data()
obj2.current_data()
obj2.bank_info()
obj2.current_info()

obj3 = Loan()
obj3.bank_data()
obj3.loan_data()
obj3.bank_info()
obj3.loan_info()