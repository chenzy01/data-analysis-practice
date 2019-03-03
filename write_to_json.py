import pandas as pd
import os

#获取当前文件父目录路径
father_path = os.getcwd()

#存储数据文件路径
wpath_json = father_path + r'\temp_trans.json'
data =[{"city": "SACRAMENTO", "longitude": -121.434879,
        "street": "3526 HIGH ST", "sq__ft": 836,
        "latitude": 38.631913, "sale_date": "Wed May 21 00:00:00 EDT 2008",
        "zip": 95838, "beds": 2,
        "type": "Residential", "state": "CA",
        "baths": 1, "price": 59222},
       {"city": "SACRAMENTO", "longitude": -121.431028,
        "street": "51 OMAHA CT", "sq__ft": 1167,
        "latitude": 38.478902, "sale_date": "Wed May 21 00:00:00 EDT 2008",
        "zip": 95823, "beds": 3,
        "type": "Residential", "state": "CA",
        "baths": 1, "price": 68212},
       {"city": "SACRAMENTO", "longitude": -121.443839,
        "street": "2796 BRANCH ST", "sq__ft": 796,
        "latitude": 38.618305, "sale_date": "Wed May 21 00:00:00 EDT 2008",
        "zip": 95815, "beds": 2,
        "type": "Residential", "state": "CA",
        "baths": 1, "price": 68880}]

df = pd.DataFrame(data)
df.to_json(wpath_json)

#json 的loads() 与 dumps()方法也可以实现

