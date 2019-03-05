import pandas as pd
import os

#获取当前文件父目录路径
father_path = os.getcwd()

#原始数据文件路径
rpath_excel = father_path + r'\realEstate_trans.xlsx'
#数据保存路径
wpath_excel = father_path + r'\temp_excel.xlsx'

#打开excel文件
excel_file = pd.ExcelFile(rpath_excel)

#读取工作表内容
'''
ExcelFile对象的parse()方法读取指定工作表的内容
ExcelFile对象的sheet_names属性可以获取Excel文件中的所有工作表
'''
excel_read = {sheetName : excel_file.parse(sheetName) for sheetName in excel_file.sheet_names}

#输出Sacramento表格的price列的前10行记录
print(excel_read['Sacramento'].head(10)['price'])
print(type(excel_read['Sacramento'].head(10)['price']))

#写入表格的price列的前10行
excel_read['Sacramento'].head(10)['price'].to_excel(wpath_excel, "price", index=False)





