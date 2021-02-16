systemMenu = {"salad":60, "steak":120, "bread":55, "pepsi":25}
menuList = []

def showBill():
    print("----My Food----")
    totalPrice = 0
    for number in range(len(menuList)):
        print(menuList[number][0], menuList[number][1])
        totalPrice += (menuList[number][1])
    print(totalPrice)
    
while True:
    menuName = input("Please Enter menu :")
    if menuName.lower() == "exit":
        break
    else:
        menuList.append([menuName, systemMenu[menuName]])

showBill()