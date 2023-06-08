# @EnV      :   python3.9
# ---encooding:utf-8---
# @Author   :   2023/6/8 19:34    
# @Email    ：   
# @Site     :    
# @File     :   test02-Decode-jsonToPython.py
# @Project  :   python接口自动化
# @Software :   PyCharm

import requests
import json

url = "https://test.crm.galaxy-immi.com/administrator/auth/login"
data = {
    "account": "navy6",
    "password": "12345678"
}
s = requests.session()
res = s.post(url, json=data, verify=False)
print(type(res.content))  # <class 'bytes'>
print(res.content)   # b'{"code":200,"msg":"\\u767b\\u5f55\\u6210\\u529f","data":{"token":"eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJodHRwOi8vMTcyLjE4Ljg1LjYzOjkzMDQvYWRtaW5pc3RyYXRvci9hdXRoL2xvZ2luIiwiaWF0IjoxNjg2MjI0NjE3LCJleHAiOjE2ODY4Mjk0MTcsIm5iZiI6MTY4NjIyNDYxNywianRpIjoiYU9vR3liRnZ6RGlzU29idSIsInN1YiI6MTIxNiwicHJ2IjoiMjNiZDVjODk0OWY2MDBhZGIzOWU3MDFjNDAwODcyZGI3YTU5NzZmNyJ9.aWdAYPnoRx4gqYvjVnsx3Ff5WL3OdA2yrSJovXzkCqw","expires_in":604800,"user":{"id":1216,"company":"SZ","account":"navy6","name":"\\u90ed\\u6d77\\u541b","email":"navy6.ghj@galaxyoversea.com","next_online_datetime":null,"leave_time":null,"online_status":2,"is_leader":0,"leader_path":"1,","leader_id":1,"english_name":"navy6","status":1,"avatar":"","created_at":"2022-10-24 17:43:36","updated_at":"2023-06-08 19:42:58","wework_key":"64d6390c081b4f4eadcc82db3789f04b","login_at":"2023-06-08 19:42:58","wework_name":"Navy\\u90ed\\u6d77\\u541b","mobile":"15576748707","mobile2":"","scrm_id":"","scrm_wx_id":"","is_new_employee":0,"head_image":"","wx_image":"https:\\/\\/upload.cdn.galaxy-immi.com\\/master-choose-school\\/test\\/1666668618769.png","is_new_owner":0,"is_new_charge":0,"wx_qrcode":"https:\\/\\/upload.cdn.galaxy-immi.com\\/crm\\/test\\/images\\/1666668867234.png","green_wx_qrcode":"","wechat_wise_openid":"","wechat_wise_unionid":"","department_id":141,"department_name":"\\u6d4b\\u8bd5\\u90e8","jump":"","handle":0,"rolesname":"\\u8d85\\u7ea7\\u7ba1\\u7406\\u5458","status_cn":"\\u4f7f\\u7528\\u4e2d"}}}'


print(type(res.text))  # <class 'str'>
print(res.text) # {"code":200,"msg":"\u767b\u5f55\u6210\u529f","data":{"token":"eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJodHRwOi8vMTcyLjE4Ljg1LjYzOjkzMDQvYWRtaW5pc3RyYXRvci9hdXRoL2xvZ2luIiwiaWF0IjoxNjg2MjI0NzE4LCJleHAiOjE2ODY4Mjk1MTgsIm5iZiI6MTY4NjIyNDcxOCwianRpIjoidTRycWlSVFlmZWhJUlQxciIsInN1YiI6MTIxNiwicHJ2IjoiMjNiZDVjODk0OWY2MDBhZGIzOWU3MDFjNDAwODcyZGI3YTU5NzZmNyJ9.8ospyZjQCk72199W_ZQ5fmcx8bRI-XPPDTriE17s5uk","expires_in":604800,"user":{"id":1216,"company":"SZ","account":"navy6","name":"\u90ed\u6d77\u541b","email":"navy6.ghj@galaxyoversea.com","next_online_datetime":null,"leave_time":null,"online_status":2,"is_leader":0,"leader_path":"1,","leader_id":1,"english_name":"navy6","status":1,"avatar":"","created_at":"2022-10-24 17:43:36","updated_at":"2023-06-08 19:43:37","wework_key":"64d6390c081b4f4eadcc82db3789f04b","login_at":"2023-06-08 19:43:37","wework_name":"Navy\u90ed\u6d77\u541b","mobile":"15576748707","mobile2":"","scrm_id":"","scrm_wx_id":"","is_new_employee":0,"head_image":"","wx_image":"https:\/\/upload.cdn.galaxy-immi.com\/master-choose-school\/test\/1666668618769.png","is_new_owner":0,"is_new_charge":0,"wx_qrcode":"https:\/\/upload.cdn.galaxy-immi.com\/crm\/test\/images\/1666668867234.png","green_wx_qrcode":"","wechat_wise_openid":"","wechat_wise_unionid":"","department_id":141,"department_name":"\u6d4b\u8bd5\u90e8","jump":"","handle":0,"rolesname":"\u8d85\u7ea7\u7ba1\u7406\u5458","status_cn":"\u4f7f\u7528\u4e2d"}}}

print(type(res.json()))  # <class 'dict'>
print(res.json())  # {'code': 200, 'msg': '登录成功', 'data': {'token': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJodHRwOi8vMTcyLjE4Ljg1LjYzOjkzMDQvYWRtaW5pc3RyYXRvci9hdXRoL2xvZ2luIiwiaWF0IjoxNjg2MjI0NzU0LCJleHAiOjE2ODY4Mjk1NTQsIm5iZiI6MTY4NjIyNDc1NCwianRpIjoiTUNPRmtwMTlUMjdIRFNWSSIsInN1YiI6MTIxNiwicHJ2IjoiMjNiZDVjODk0OWY2MDBhZGIzOWU3MDFjNDAwODcyZGI3YTU5NzZmNyJ9.HTHsQJ2GUpFEBWGn4tyyo1XzSo2lWlegb8oU9kj2K28', 'expires_in': 604800, 'user': {'id': 1216, 'company': 'SZ', 'account': 'navy6', 'name': '郭海君', 'email': 'navy6.ghj@galaxyoversea.com', 'next_online_datetime': None, 'leave_time': None, 'online_status': 2, 'is_leader': 0, 'leader_path': '1,', 'leader_id': 1, 'english_name': 'navy6', 'status': 1, 'avatar': '', 'created_at': '2022-10-24 17:43:36', 'updated_at': '2023-06-08 19:45:18', 'wework_key': '64d6390c081b4f4eadcc82db3789f04b', 'login_at': '2023-06-08 19:45:18', 'wework_name': 'Navy郭海君', 'mobile': '15576748707', 'mobile2': '', 'scrm_id': '', 'scrm_wx_id': '', 'is_new_employee': 0, 'head_image': '', 'wx_image': 'https://upload.cdn.galaxy-immi.com/master-choose-school/test/1666668618769.png', 'is_new_owner': 0, 'is_new_charge': 0, 'wx_qrcode': 'https://upload.cdn.galaxy-immi.com/crm/test/images/1666668867234.png', 'green_wx_qrcode': '', 'wechat_wise_openid': '', 'wechat_wise_unionid': '', 'department_id': 141, 'department_name': '测试部', 'jump': '', 'handle': 0, 'rolesname': '超级管理员', 'status_cn': '使用中'}}}