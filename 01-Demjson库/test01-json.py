# @EnV      :   python3.9
# ---encooding:utf-8---
# @Author   :   2023/6/8 14:08    
# @Email    ：
# @Site     :    
# @File     :   test01-json.py
# @Project  :   python接口自动化
# @Software :   PyCharm

"""
json.dumps()：将 Python 对象编码成 JSON 字符串, dic -> json str

json.dump()  ：将 Python 对象保存成 JSON 字符串格式到文件中。

json.loads()  ：将已编码的 JSON 字符串解码为 Python 对象,  json str -> dic

json.load()    ：从文件中读取json数据
"""

import json

# json.dumps()
list1 = [{'a1': 1, 'a2': 2, 'a3': 3}, {'c': [111, 222, 333]}, {'b': 11}]
jstr1 = json.dumps(list1)
jstr2 = json.dumps(list1, sort_keys=True, indent=4)

print(" jstr1: " + jstr1 + "\n", "jstr2: " + jstr2)

# json.dump()
f = open("./jstr.txt", "a+")
jstr3 = json.dump(list1, f)
f.close()

# json.loads()
print(type(jstr1))  # <class 'str'>
print(type(json.loads(jstr1)))  # <class 'list'>
print(json.loads(jstr2))

# json.load()

with open("./jstr.txt", "r+") as f2:
    for i in f2:
        result = json.load(f2)
        print(result)
