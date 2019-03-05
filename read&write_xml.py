import pandas as pd
import xml.etree.ElementTree as ET
import os

#读取XML数据，返回pd.DateFrame
def read_xml(xml_FileName):
    with open(xml_FileName,'r') as xml_filename:
        #读取数据，以树的结构存储
        tree = ET.parse(xml_filename)
        #访问树的根节点
        root = tree.getroot()
        #返回DataFrame格式数据
        return pd.DataFrame(list(iter_records(root)))


#遍历有记录的生成器
def iter_records(records):
    for record in records:
        #保持值的临时值
        temp_dict = {}
        #遍历所有字段
        for var in record:
            temp_dict[
                var.attrib["var_name"]
            ] = var.text
        #生成值
        yield temp_dict

#以XML格式保持数据
def write_xml(xmlFileName, data):
    with open(xmlFileName, "w") as xmlFile:
        #写头部
        xmlFile.write(
            '<?xml version="1.0" encoding="UTF-8"?>'
        )
        xmlFile.write('<records>\n')
        #写数据
        xmlFile.write(
            '\n'.join(data.apply(xml_encode, axis=1))
        )
        #写尾部
        xmlFile.write('\n</records>')

#以特定的嵌套格式将每一行编码成XML
def xml_encode(row):
    #第一步，输出record节点
    xmlItem = ['<record>']
    #第二步，给行中每个字段加上XML格式<field name=***>***</field>
    for field in row.index:
        xmlItem.append(
            '<var var_name="{0}">{1}</var> '.format(field, row[field])
        )
    #第三步，标记record节点的结束标签
    xmlItem.append(" </record>")
    return '\n'.join(xmlItem)

#获取当前文件父目录路径
father_path = os.getcwd()
#原始数据文件路径
rpath_xml = father_path + r'\realEstate_trans.xml'
#数据保持路径
wpath_xml = father_path + r'\temp_xml.xml'
#读取数据
xml_read = read_xml(rpath_xml)
print(xml_read.head(10))
#以XML格式写回文件
write_xml(wpath_xml, xml_read.head(10))











