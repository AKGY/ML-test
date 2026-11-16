import openpyxl
workbook = openpyxl.Workbook()
sheet = workbook.active


sheet["A1"] = "테스트 파일"
sheet["D1"] = "전주대 컴공"

sheet.merge_cells("A1:C1")

sheet["A1"].font = openpyxl.styles.Font(size = 10, color = "FF0000")

workbook.save("newFile.xlsx")
