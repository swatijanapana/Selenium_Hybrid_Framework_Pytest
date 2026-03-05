import openpyxl

def get_login_data():
   wb = openpyxl.load_workbook("TestData/login_data.xlsx")
   ws = wb["LoginData"]

   data = []

   for row in ws.iter_rows(min_row=2, values_only=True):
      data.append(row) # row = (scenario, username, password, expected)
   return  data