# coding=utf-8
import xml.etree.cElementTree as ET
import re

def parse_xml(xml_path, mapping_path):
    per = ET.parse(xml_path)
    header = per.findall(".//HEADER")
    item_data = per.findall(".//ITEM_DATA")
    item_price = per.findall(".//ITEM_PRICING")
    header_list = []
    item_data_list = []
    item_price_list = []

    for header_child in header[0].getchildren():
        header_list.append(header_child.text)

    for data in item_data:
        data_list = []
        for data_child in data.getchildren():
            data_list.append(data_child.text)
        item_data_list.append(data_list)

    for price in item_price:
        price_list = []
        for price_child in price.getchildren():
            price_list.append(price_child.text)
        item_price_list.append(price_list)

    ret = []
    for item in item_data_list:
        for price in item_price_list:
            if price[0] == item[0]:
                for i in price:
                    item.append(i)

        del item[0:2]
        del item[2]
        del item[3:10]
        del item[4:8]
        del item[5:9]
        del item[-1]
        tax_price = float(item[3])*1.16
        tax_price = round(tax_price, 4)
        item.append(tax_price)
        ret.append(item)

    with open(mapping_path) as f:
        content = f.read()

    content = content.replace("\t", ":").split("\n")
    ret1 = []
    for con in content:
        for item_1 in ret:
            if item_1[0] == con.split(":")[1]:
                item_1.append(con.split(":")[0])
                ret1.append(item_1)
    return ret1

# ret = parse_xml("./2002480010_AfterMapping.xml", "/home/jeffrey/mapping.txt")
