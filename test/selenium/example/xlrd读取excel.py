import xlrd

filePath="D:\软件测试\功能测试\类和板块.xlsx"
try:
    data = xlrd.open_workbook(filePath)
except Exception as e:
    print(str(e))
sheetNum = data.nsheets
list1 = []
for i in range(sheetNum):
    dict1 = {}
    sheetName=data.sheet_names()[i]
    table = data.sheets()[i]
    rows = table.nrows
    cols = table.ncols
    colNames = table.row_values(0)
    print(len(colNames))
    list = []
    for row in range(1, rows):
        rowValue = table.row_values(row)
        if rowValue:
            dict = {}
            for i in range(cols):
                dict[colNames[i]] = rowValue[i]
            list.append(dict)
    dict1[sheetName] = list
    list1.append(dict1)
print(list1)
"""
#只有一个sheet
path="D:\软件测试\功能测试\帖子.xlsx"
try:
    data=xlrd.open_workbook(path)
except Exception as e:
    print(str(e))
table=data.sheets()[0]
rows=table.nrows
cols=table.ncols
colNames=table.row_values(0)
print(len(colNames))
list=[]
for row in range(1,rows):
    rowValue=table.row_values(row)
    if rowValue:
        dict={}
        for i in range(cols):
            dict[colNames[i]]=rowValue[i]
        list.append(dict)
print(list)
"""