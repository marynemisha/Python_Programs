#online shopping
class Customer:
    def __init__(self):
        self.name=""
        self.mobile=""
        self.address=""
        self.email=""
    def customer_data(self):
        self.name =input("Enter the name:")
        self.mobile =int(input("Enter the mobile number:"))
        self.address =input("Enter the address:")
        self.email = input("Enter the email id:")
    def customer_info(self):
        print("..................Customer details.................")
        print("Name             :",self.name)
        print("Mobile           :",self.mobile)
        print("Address          :",self.address)
        print("Email id         :",self.email)
class Product:
    def __init__(self):
        self.product_name=""
        self.price=""
        self.description=""
    def product_data(self):
        self.product_name =input("Enter the product name:")
        self.price =int(input("Enter the price:"))
        self.description =input("Enter the description:")
    def product_info(self):
        print("..................Product details.................")
        print("Product name             :",self.product_name)
        print("Price                    :",self.price)
        print("Description              :",self.description)
class Order:
    def __init__(self):
        self.order_id=""
        self.quantity=""
        self.total=""
        self.date=""
    def order_data(self):
        self.order_id =input("Enter the order id:")
        self.quantity =int(input("Enter the quantity:"))
        self.total =int(input("Enter the total price:"))
        self.date =input("Enter the order date:")
    def order_info(self):
        print("..................Order details.................")
        print("Order id                 :",self.order_id)
        print("Quantity                 :",self.quantity)
        print("Total price              :",self.total)
        print("Order date               :",self.date)

obj=Order()
obj1=Customer()
obj2=Product()
obj.order_data()
obj1.customer_data()
obj2.product_data()
obj.order_info()
obj1.customer_info()
obj2.product_info()
