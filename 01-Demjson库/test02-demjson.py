# @EnV      :   python3.9
# ---encooding:utf-8---
# @Author   :   2023/6/8 15:35    
# @Email    ：   
# @Site     :    
# @File     :   test02-demjson.py
# @Project  :   python接口自动化
# @Software :   PyCharm

"""
Demjson 是 python 的第三方模块库，可用于编码和解码 JSON 数据，包含了 JSONLint 的格式化及校验功能。

demjson.encode()

demjson.encode_to_file()

demjson.decode()

demjson.decode_file()
"""
import time

import demjson

# encode
d1 = [{'1': 1, '4': 4, '3': 3, '2': 2}]
d2 = [{'c': 2, 'a': 5, 'b': 3}]

print(demjson.encode(d1))
demjson.encode_to_file('demjson.txt', d1)
demjson.encode_to_file('demjson.txt', d2, overwrite=True)

# decode
jstr = '{"a":1,"d":4,"c":3,"b":2}'
print(demjson.decode(jstr))

