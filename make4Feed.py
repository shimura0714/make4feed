import openpyxl
import sys

wb = openpyxl.load_workbook(sys.argv[1])
sheet = wb[wb.sheetnames[0]]

rowCnt = 1
text_dict = {}
discription_dict = {}

while True :
  pid = sheet["A" + str(rowCnt)].value
  if pid is None :
    break
  rowCnt = rowCnt + 1
  pid = pid.replace('c', '')
  text_dict[pid] = sheet["E" + str(rowCnt)].value

for key, value in text_dict.items():
  print (key)
  print (value)

wb.close()