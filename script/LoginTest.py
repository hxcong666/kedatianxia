#登录接口
#导包
import requests
#发送请求
url="http://kdtx-test.itheima.net/api/login"
headers={
    "Content-Type":"application/json",
}
loginData={
    "username":"admin",
    "password":"HM_2023_test",
    "code":"2",
    "uuid":"37cb173d9c9245278ed786ce39ff974e"   #运行ImageTest.py得到其中的uuid
}
response = requests.post(url=url,headers=headers,json=loginData)

#查看响应
print(response.status_code)
print(response.text)


