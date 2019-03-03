import pandas as pd
import os
#import dataframe as df


#获取当前文件父目录路径
father_path = os.getcwd()

#原始数据文件路径,拼成的路径：G:\Python\Data_Analysis\city_station.csv
rpath_csv = father_path + r'\city_station.csv'
#rpath_csv = father_path + r'\city_station.tsv'
#读取数据
csv_read = pd.read_csv(rpath_csv)
#tsv_read = pd.read_csv(rpath_csv, sep='\t')
#输出前10条
print(csv_read.head(10))
#print(tsv_read.head(10))
#函数解析:
#read_csv(filepath_or_buffer,sep,header,names,skiprows,na_value,encoding,nrows)





