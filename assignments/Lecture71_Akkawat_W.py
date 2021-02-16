menuList = []
priceList = []

def showBill():
    print("----My Food----")
    for number in range(len(menuList)):
        print(menuList[number], priceList[number])

def totalPrice():
    total = 0
    for price in priceList:
        total += int(price)
    print("Total Price :",total, "THB")

        

while True:
    menuName = input("Please Enter menu :")
    if menuName.lower() == "exit":
        break
    else:
        menuPrice = int(input("Price :"))
        menuList.append(menuName)
        priceList.append(menuPrice)


showBill()
totalPrice()