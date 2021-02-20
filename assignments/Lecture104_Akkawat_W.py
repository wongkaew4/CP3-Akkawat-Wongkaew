class Customer:
    name = ""
    lastName = ""
    age = 0

    def addCart(self):
        print("Added product to ",self.name,self.lastName,"'s cart")

Customer1 = Customer()
Customer1.name = "Akkawat"
Customer1.lastName = "W"
Customer1.addCart()

Customer2 = Customer()
Customer2.name = "Cherprang"
Customer2.lastName = "A"
Customer2.addCart()

Customer3 = Customer()
Customer3.name = "Jennis"
Customer3.lastName = "O"
Customer3.addCart()