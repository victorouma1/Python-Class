class Product:
    _product_count = {}
    def __init__(self, name, price, stock):
        self.name = name
        self.price = price
        self.stock = stock
        self._product_count = self.stock
    def sell(self, quantity):
        self.quantity = quantity
        if self._product_count >= self.quantity:
            self._product_count -= self.quantity
        else:
            print("Not enough products available")
        return self._product_count
    def restock(self, quantity): 
        self.quantity = quantity
        self._product_count[self.name] = self.quantity
        for keys in self._product_count:
            if self.name == keys:
                self._product_count[keys] += self.quantity
        return self._product_count
    def __str__(self): 
        return f"{self.name} is valued at {self.price} and there are {self._product_count} in stock"
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
        return f"You have ordered{self.quantity} {self.product}"

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
    def __init__(self, VIP_name, email, discount_rate,c_name, VIP_email,product, quantity, customer, name,price,stock):
        super().__init__(c_name, VIP_email,product, quantity, customer, name,price,stock)
        self.VIP_name = VIP_name
        self.email = email
        self.discount_rate = discount_rate
    def total_spent(self):
        self.price *= (1-self.discount_rate)

print("Store closed, about to open")

Employee_choice = input("Stock is empty do you wan to restock? Y/N")
if Employee_choice == "Y":
    x = True
    while x:
        Product_name_input = input("What product do you want to restock? ")
        Price_input = int(input("What is the price of the product? "))
        Stock_Input = int(input("How much do you want to restock? "))
        Employee_Restock = Product(Product_name_input, Price_input, Stock_Input)
        Employee_Restock.restock(Stock_Input)
        print(str(Employee_Restock))
        Done_restocking = input("Are you done restocking? Y/N ").upper()
        if Done_restocking == 'Y':
            continue
        if Done_restocking == 'N':
            x = False
            break

#First_question = input("Are you a customer or employee?").title()
#if First_question == "Customer":


        
        

        

