# @EnV      :   python3.9
# ---encooding:utf-8---
# @Author   :   2023/6/8 19:53    
# @Email    ：   
# @Site     :    
# @File     :   test03-参考代码.py
# @Project  :   python接口自动化
# @Software :   PyCharm

import requests

url = "http://www.kuaidi.com/index-ajaxselectcourierinfo-1202247993797-yunda.html"
headers = {
    "User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"
}

s = requests.session()
res = s.get(url, headers=headers, verify=False)
result = res.json()
data = result["data"]
print(data)
print(data[0])
get_result = data[0]['context']
print(get_result)

if "已签收" in get_result:
    print("快递单已签收成功")
else:
    print("未签收")