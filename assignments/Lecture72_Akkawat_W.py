menuList = []

def showBill():
    print("----My Food----")
    for number in range(len(menuList)):
        print(menuList[number])

def totalPrice():
    total = 0
    for price in range(len(menuList)):
        total += int(menuList[price][1])
    print("Total Price :",total, "THB")
    
while True:
    menuName = input("Please Enter menu :")
    if menuName.lower() == "exit":
        break
    else:
        menuPrice = int(input("Price :"))
        menuList.append([menuName, menuPrice])

showBill()
totalPrice()
