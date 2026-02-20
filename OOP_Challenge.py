class Product:
    def __init__(self, name, price, stock):
        self.name = name
        self.price = price
        self.stock = stock
        self._product_count = []
    def sell(self, quantity):
        self.quantity = quantity
        if self._product_count[0][self.name] >= self.quantity:
            self._product_count[0][self.name] -= self.quantity
        else:
            print("Not enough products available")
        return self._product_count
    def restock(self, quantity): 
        self.quantity = quantity
        self._product_count.append({self.name:self.quantity})
        
        for keys in self._product_count:
            if self.name == keys:
                self._product_count[keys] += self.quantity
        return self._product_count
    def __str__(self): 
        for prod in self._product_count:
            for k in prod:
                if k == self.name :
                    return f"{self.name} is valued at {self.price} and there are {prod[k]} in stock"
    @property
    def stock_value(self):
        return self._product_count
    @stock_value.setter
    def stock_value(self):
        print("Stock Value is: ")
        return self.price * self._product_count
    
class Order(Product):
    def __init__(self, product, quantity, customer, name,price,stock):
        super().__init__(name,price,stock)
        self.product = product
        self.quantity = quantity
        self.customer = customer
    def total_price(self):
        print("Total price is: ")
        return self.price * self.quantity
    def __str__(self):
        return f"You have ordered {self.quantity} {self.product}."
    

class Customer(Order):
    def __init__(self, c_name, email,product, quantity, customer, name,price,stock):
        super().__init__(product, quantity, customer, name,price,stock)
        self.name = c_name
        self.email = email
        self.purchase_history = []
    def add_order(self, order):
        print("What would you like to order? ")
        self.order = order
        self.purchase_history.append({self.name:[self.order,self.price]})
    def total_spent(self):
        for i in range(len(self.purchase_history)):
            return sum(self.purchase_history[i][self.name])
    def __str__(self):
        for i in range(len(self.purchase_history)):
            return f"{self.name} has spent a total of {sum(self.purchase_history[i][self.name][1])}"
class VIP(Customer):
    def __init__(self, VIP_name, VIP_email, discount_rate,c_name, email ,product, quantity, customer, name,price,stock):
        super().__init__(c_name, email,product, quantity, customer, name,price,stock)
        self.VIP_name = VIP_name
        self.VIP_email = VIP_email
        self.discount_rate = discount_rate
    def total_spent(self):
        return (self.price * (1 - self.discount_rate)) * self.quantity

print("Store closed, about to open")

Employee_choice = input("Stock is empty do you want to restock? (Y/N) ").upper()

if Employee_choice == "Y":
    x = True
    while x:
        Product_name_input = input("What product do you want to restock? ")
        Price_input = int(input("What is the price of the product? "))
        Stock_Input = int(input("How much do you want to restock? "))
        Employee_Restock = Product(Product_name_input, Price_input, Stock_Input)
        Employee_Restock.restock(Stock_Input)
        print(str(Employee_Restock))
        Customer_Id = input("Hello customer, are you a Vip customer? (Y/N) ").upper()
        if Customer_Id == 'Y': 
            VIP_Name = input("What is your name? ")
            VIP_email = input("What is your email? ")
            VIP_input = input("Would you like to make an order? (Y/N) ").upper()
            if VIP_input == "Y":
                Amount_of_Product = int(input(f"How much {Employee_Restock.name} would you like?"))
                Order1 = Order(Employee_Restock.name, Amount_of_Product, VIP_Name, Employee_Restock.name, Employee_Restock.price, Employee_Restock.stock)
                Employee_Restock.sell(Amount_of_Product)
                VIP_Status = VIP(VIP_Name, VIP_email, 0.2,VIP_Name,VIP_email, Employee_Restock.name, Amount_of_Product, VIP_Name, Employee_Restock.name, Employee_Restock.price, Employee_Restock.stock )
                print(str(Order1))
                print(f"You have spent {VIP_Status.total_spent()}")
                print(str(Employee_Restock))
                print(str())
            if VIP_input == "N":
                x = False
                break
        if Customer_Id == 'N':
            Name1 = input("What is your name? ")
            email1 = input("What is your email? ")
            input1 = input("Would you like to make an order? (Y/N) ").upper()
            if input1 == "Y":
                Amount_of_Product = int(input(f"How much {Employee_Restock.name} would you like?"))
                Order1 = Order(Employee_Restock.name, Amount_of_Product, Name1, Employee_Restock.name, Employee_Restock.price, Employee_Restock.stock)
                Employee_Restock.sell(Amount_of_Product)
                C_Status = Customer(Name1,email1, Employee_Restock.name, Amount_of_Product, Name1, Employee_Restock.name, Employee_Restock.price, Employee_Restock.stock )
                print(str(Order1))
                Adding_ORDER = C_Status.add_order(1)
                print(f"You have spent {C_Status.total_spent()}")
                print(str(Employee_Restock))
                print(str())
        Done_restocking = input("Are you done restocking? (Y/N) ").upper()
        if Done_restocking == 'N':
            continue
        if Done_restocking == 'Y':
            x = False
            break
        
        

        

