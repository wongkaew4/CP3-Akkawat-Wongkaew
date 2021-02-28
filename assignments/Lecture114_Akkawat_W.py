from forex_python.bitcoin import BtcConverter
import datetime
import matplotlib.pyplot as plt

print("BTC Chart Change (USD) PROGRAM")
print("โปรแกรมจะแสดงผลตั้งแต่วันที่เลือกไม่เกิน 2 ปี")
print("กรุณาเลือกก่อนวันที่ 6 มิถุนายน 2013 (ประมาณวันแรกๆ ที่ราคา BTC ถูกซื้อขาย)")
print("-"*80)
print("Input start date : (ex. 2013 6 24)")
start_date_year = int(input("Input year:"))
start_date_month = int(input("Input month:"))
start_date_day = int(input("Input day:"))

b = BtcConverter()
start_date = datetime.date(start_date_year, start_date_month, start_date_day)
end_date = datetime.date(start_date_year + 2, start_date_month, start_date_day)
result_price_list = b.get_previous_price_list("USD", start_date, end_date)

date_result = result_price_list.keys()
rate_result = result_price_list.values()

plt.figure("Akkawat Wongkaew")
plt.title("BTC Chart Change PROGRAM")
plt.plot(date_result, rate_result)
plt.xlabel("Date")
plt.ylabel("BTC / USD Rate")
plt.show()