totalPrice = int(input("Input Price:"))
def vatCalculate(totalPrice):
    result = (totalPrice+(totalPrice*7/100))
    return result
print("Include Vat 7% :", vatCalculate(totalPrice))
