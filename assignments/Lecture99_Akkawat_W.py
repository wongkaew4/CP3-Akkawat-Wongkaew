from tkinter import *
import math

def leftClickButton(event):
    heightValue = math.pow(float(textBoxHeight.get())/100,2)
    weightValue = float(textBoxWeight.get())
    bmiValue = weightValue/heightValue
    labelBMI.configure(text= "BMI = " +str('%.2f' %bmiValue))
    if bmiValue <= 18.50:
        bmiResult = "อยู่ในเกณฑ์น้ำหนักน้อย / ผอม"
    elif bmiValue <= 22.90:
        bmiResult = "อยู่ในเกณฑ์ปกติ (สุขภาพดี)"
    elif bmiValue <= 24.90:
        bmiResult = "อยู่ในเกณฑ์ท้วม / โรคอ้วนระดับ 1"
    elif bmiValue <= 29.90:
        bmiResult = "อยู่ในเกณฑ์อ้วน / โรคอ้วนระดับ 2"
    elif bmiValue > 29.90:
        bmiResult = "อยู่ในเกณฑ์อ้วนมาก / โรคอ้วนระดับ 3"
    labelResult.configure(text= bmiResult)

MainWindow = Tk()
labelHeight = Label(MainWindow, text= "ส่วนสูง (cm.)")
labelHeight.grid(row=0, column=0)
textBoxHeight = Entry(MainWindow)
textBoxHeight.grid(row=0, column=1)
labelWeight = Label(MainWindow, text= "น้ำหนัก (kg.)")
labelWeight.grid(row=1, column=0)
textBoxWeight = Entry(MainWindow)
textBoxWeight.grid(row=1, column=1)
calculateButton = Button(MainWindow, text = "คำนวณค่า BMI")
calculateButton.bind('<Button-1>', leftClickButton)
calculateButton.grid(row=2, column=0)
labelBMI = Label(MainWindow, text= "ผลลัพธ์")
labelBMI.grid(row=3, column=1)
labelResult = Label(MainWindow,text="เกณฑ์ BMI")
labelResult.grid(row=2, column=1)
MainWindow.mainloop()