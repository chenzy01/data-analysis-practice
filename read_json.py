import pandas as pd
import os

#获取当前文件父目录路径
father_path = os.getcwd()

#存储数据文件路径
rpath_json = father_path + r'\realEstate_trans.json'
json_read = pd.read_json(rpath_json)

#输入前10行
print(json_read.head(10))



