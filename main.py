import requests
from json import dumps
from get_data import CardReader
from decouple import config
from sheets import SheetWorker
from requests   import request

scp = ['https://www.googleapis.com/auth/spreadsheets',
         "https://www.googleapis.com/auth/drive"]
work = CardReader("https://content-api.wildberries.ru/content/v2/get/cards/list", "post")
data = work.read_data(10, 0)
print(data["cards"][0]["nmID"])
print(data["cards"][0]["subjectName"])
print(data["cards"][0]["vendorCode"])
print(data["cards"][0]["createdAt"])
sheet = SheetWorker("asd.json", scp, "Table")
for x in data["cards"]:
    sheet.insert_data([x["nmID"], x["subjectName"], x["vendorCode"], x["createdAt"]])
# сслыка на таблицу https://docs.google.com/spreadsheets/d/18BdtQVtbsUpbobfCe6e8m7_ZEiBt-CfEEoqfFEb2mjM/edit?usp=sharing