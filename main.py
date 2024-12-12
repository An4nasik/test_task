from get_data import CardReader
from sheets import SheetWorker


scp = ['https://www.googleapis.com/auth/spreadsheets',
         "https://www.googleapis.com/auth/drive"]
work = CardReader("https://content-api.wildberries.ru/content/v2/get/cards/list", "post")
data = work.read_data(1, False)
print(data)

sheet = SheetWorker("asd.json", scp, "TestTable")
sheet.insert_data([1])
sheet.insert_data([2])
sheet.insert_data([3])
sheet.insert_data([4])