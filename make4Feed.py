import openpyxl
import sys

wb = openpyxl.load_workbook(sys.argv[1])
sheet = wb[wb.sheetnames[0]]

rowCnt = 2
text_dict = {}
discription_dict = {}

while True :
  pid = sheet["A" + str(rowCnt)].value
  if pid is None :
    break
  pid = pid.replace('c', '')
  text_dict[pid] = sheet["C" + str(rowCnt)].value
  discription_dict[pid] = sheet["E" + str(rowCnt)].value
  rowCnt = rowCnt + 1

textFile = open('text.txt', 'w')
for key, value in text_dict.items():
  textFile.write("'{0}' => '{1}'\n".format(key, value))

textFile.close()

discriptionFile = open('discription.txt', 'w')
for key, value in discription_dict.items():
  discriptionFile.write("'{0}' => '{1}'\n".format(key, value))

discriptionFile.close()

wb.close()