import openpyxl
#load workbook 만드는 방법
#workbook openpyxl workbook class
workbook = openpyxl.Workbook()
sheet = workbook.active

#데이터 쓰기
#workbook.save(filename)

sheet["A1"] = "테스트 파일"
sheet["D1"] = "전주대 컴공"

sheet.merge_cells("A1:C1")

#font openpyxl styles.font
sheet["A1"].font = openpyxl.styles.Font(size=20, color="FF0000",)
sheet["A1"].alignment = openpyxl.styles.Alignment(horizontal="center", vertical="center")

workbook.save("newFile.xlsx")