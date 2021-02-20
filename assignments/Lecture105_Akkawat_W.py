class Vehicle:
    licenseCode = ""
    serialCode = ""
    def turnOnAirConditioner(self):
        print("Turn ON : Air")

class Car(Vehicle):
    pass
class Picup(Vehicle):
    pass
class Van(Vehicle):
    pass
class Estatecar(Vehicle):
    pass

car1 = Car()
car1.turnOnAirConditioner()

picup1 = Picup()
picup1.turnOnAirConditioner()

van1 = Van()
van1.turnOnAirConditioner()

estatecar1 = Estatecar()
estatecar1.turnOnAirConditioner()