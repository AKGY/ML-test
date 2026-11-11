import openpyxl
import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)


book = openpyxl.load_workbook("stats_104102.xlsx")
print(book.get_sheet_names())
print(book.get_sheet_by_name("Sheet0"))
sheet = book.worksheets[0]

for row in sheet.rows:
    for data in row:
        print(data.value, end=" ")
    print("", end="\n")
