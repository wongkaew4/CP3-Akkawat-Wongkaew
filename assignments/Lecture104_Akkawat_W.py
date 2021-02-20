class Customer:
    name = ""
    lastName = ""
    age = 0

    def addCart(self):
        print("Added product to ",self.name,self.lastName,"'s cart")

customer1 = Customer()
customer1.name = "Akkawat"
customer1.lastName = "W"
customer1.age = 30
customer1.addCart()

customer2 = Customer()
customer2.name = "Cherprang"
customer2.lastName = "A"
customer2.age = 24
customer2.addCart()

customer3 = Customer()
customer3.name = "Jennis"
customer3.lastName = "O"
customer3.age = 20
customer3.addCart()