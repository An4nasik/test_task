import gspread
from oauth2client.service_account import ServiceAccountCredentials

scp = ['https://www.googleapis.com/auth/spreadsheets',
         "https://www.googleapis.com/auth/drive"]
class SheetWorker:
    def __init__(self, filename: str, scope: list, tablename: str):
        #filename - имя json файла с конфигом
        #scope - к чему мы привязываем аккаунт
        #table_name - как назовем эту таблицу
        self.credentials = ServiceAccountCredentials.from_json_keyfile_name(filename, scope)
        self.client = gspread.authorize(self.credentials)
        self.tablename = tablename
        #Следующий блок пытается открыть таблицу, если она не существует, он ее создаст
        try:
            sheet = self.client.open(self.tablename)
        except gspread.exceptions.SpreadsheetNotFound:
            self.client.create(self.tablename)
            sheet = self.client.open(self.tablename)
            ws = sheet.sheet1
            # Добавление в таблицу заголовков
            # предполагается, что в уже созданных таблицах, заголовки присутствуют изначально
            ws.insert_row(["Артикул WB", "Наименование товара", "Артикул продавца", "Дата выгрузки"], index=1)



    def insert_data(self, data):
        sheet = self.client.open(self.tablename)
        ws = sheet.sheet1
        ws.insert_row(data, index=2)


    def share(self, email: str, role: str = "writer", perm_type: str = "user"):
        sheet = self.client.open(self.tablename)
        sheet.share(email, role=role, perm_type=perm_type, )




