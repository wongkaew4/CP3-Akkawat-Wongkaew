print("Login")
usernameInput = input("Username :")
passwordInput = input("Password :")

garmin = "GARMIN Smartwatch instinct Solar Tidal"
garminPrice = 13990
suunto = "SUUNTO Smartwatch 7"
suuntoPrice = 16900
ticwatch = "TICWATCH Smartwatch Pro3 GPS"
ticwatchPrice = 11900
fitbit = "FITBIT Smartwatch Ionic"
fitbitPrice = 10990
vat = 7/100

if usernameInput == "admin4" and passwordInput == "1234":
    print("-------------------Welcome to SmartWatch shop-------------------")
    print("----------------------------All item----------------------------")
    print("1", garmin, "price/piece =", garminPrice, "baht")
    print("2", suunto, "price/piece =", suuntoPrice, "baht")
    print("3", ticwatch, "price/piece =", ticwatchPrice, "baht")
    print("4", fitbit, "price/piece =", fitbitPrice, "baht")

    userSelected = int(input("Please select no. item from the list? >>"))
    if userSelected ==1:
        qty = int(input("How many do you want?"))
        print(garmin, "x", qty, "=", qty*garminPrice, "baht")
        print("vat 7% =", (qty*garminPrice)*vat)
        print("total =", (qty*garminPrice) + (qty*garminPrice)*vat, "baht")
        print("--------------------------Thank you--------------------------")
    elif userSelected ==2:
        qty = int(input("How many do you want?"))
        print(suunto, "x", qty, "=", qty*suuntoPrice, "baht")
        print("vat 7% =", (qty*suuntoPrice)*vat)
        print("total =", (qty*suuntoPrice) + (qty*suuntoPrice)*vat, "baht")
        print("--------------------------Thank you--------------------------")
    elif userSelected ==3:
        qty = int(input("How many do you want?"))
        print(ticwatch, "x", qty, "=", qty*ticwatchPrice, "baht")
        print("vat 7% =", (qty*ticwatchPrice)*vat)
        print("total =", (qty*ticwatchPrice) + (qty*ticwatchPrice)*vat, "baht")
        print("--------------------------Thank you--------------------------")
    elif userSelected ==4:
        qty = int(input("How many do you want?"))
        print(fitbit, "x", qty, "=", qty*fitbitPrice, "baht")
        print("vat 7% =", (qty*fitbitPrice)*vat)
        print("total =", (qty*fitbitPrice) + (qty*fitbitPrice)*vat, "baht")
        print("--------------------------Thank you--------------------------")
    else:
        print("--------------------------No item--------------------------")
        print("--------------------------Thank you--------------------------")
else:
    print("Error!!")
    print("Username or Password is incorect")