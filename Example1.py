import pandas as pd
import os
#import dataframe as df

'''
#获取当前文件父目录路径
father_path = os.getcwd()

#原始数据文件路径,拼成的路径：G:\Python\Data_Analysis\city_station.csv
rpath_csv = father_path + r'\city_station.csv'
#读取数据
csv_read = pd.read_csv(rpath_csv)
#输出前10条
print(csv_read.head(10))

函数解析:
read_csv(filepath_or_buffer,sep,header,names,skiprows,na_value,encoding,nrows)
'''

#获取当前文件父目录路径
father_path = os.getcwd()

#保存数据文件路径,拼成的路径：G:\Python\Data_Analysis\temp_city.csv
path_csv = father_path + r'\temp_city.csv'
#写入数据（列名+值）
data = {'站点名': ["北京北", "北京东", "北京", "北京南", '北京西'],
        '代号': ['VAP', 'BOP', "BJP", "VNP", 'BXP']
}

#将数据初始化为DataFrame对象
df = pd.DataFrame(data)
#数据写入temp_city.csv
df.to_csv(path_csv)

#函数解析:
#to_csv(path_or_buf,sep,header,na_rep,columns,header,index)
