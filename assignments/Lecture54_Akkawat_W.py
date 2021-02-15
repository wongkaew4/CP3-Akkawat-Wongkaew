def login():
    usernameInput = input("Username : ")
    passwordInput = input("Password : ")
    if usernameInput == "admin" and passwordInput == "1234":
        return True
    else:
        print("Username or Password that you've entered is incorrect!!")
        return login()

def showMenu():
    print("----- iShop -----")
    print("1. Vat Calculator")
    print("2. Price Calculator")

def menuSelect():
    userSelected = int(input(">>"))
    return userSelected

def vatCalculator(totalPrice):
    vat = 7
    result = totalPrice + (totalPrice * vat / 100)
    return result

def priceCalculator():
    price1 = int(input("First Product Price : "))
    price2 = int(input("Second Product Price : "))
    return vatCalculator(price1 + price2)

login()
showMenu()
result = menuSelect()
if result == 1:
    price = int(input("Please key your price : "))
    print(vatCalculator("Price include Vat 7% :",price))
elif result == 2:
    print ("Price include Vat 7% :" ,priceCalculator())
else:
    print("No list in iShop menu")
print("-----Thank you-----")
