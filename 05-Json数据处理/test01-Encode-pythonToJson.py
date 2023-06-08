# @EnV      :   python3.9
# ---encooding:utf-8---
# @Author   :   2023/6/8 19:29    
# @Email    ：   
# @Site     :    
# @File     :   test01-Encode-pythonToJson.py
# @Project  :   python接口自动化
# @Software :   PyCharm

import requests
import json

# python字典
payload = {
    "yoyo": True,
    "json": False,
    "python": "226296743"
}
print(type(payload))
# 转换成json格式
data_json = json.dumps(payload)
print(type(data_json))
print(data_json)

