import requests

url = 'http://www.baidu.com'

response = requests.get(url)

#一个类型
# <class 'requests.models.Response'>
print(type(response))

#六个属性

#.text
#以str形式返回响应内容，
print(response.text)
#设置响应的编码格式
# response.encoding = 'utf-8'
print(response.text)


#.url返回一个url地址
print(response.url)

#.content返回子节形式的二进制代码（b开头）
print(response.content)

#.status_code获取响应的状态码 200正常
print(response.status_code)

#.headers获取响应头
print(response.headers)



