import urllib.request
import urllib.parse

#https://www.baidu.com/s?wd=%E5%91%A8%E6%9D%B0%E4%BC%A6

#需要 获取 https://www.baidu.com/s?wd=周杰伦

url = 'https://www.baidu.com/s?wd='

#请求对象定制是反爬的第一步
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36'
}
#将周杰伦变成Unicode编码
name = urllib.parse.quote('周杰伦')
url = url + name
request = urllib.request.Request(url=url,headers=headers)
#模拟浏览器向服务器发送请求
response = urllib.request.urlopen(request)

content = response.read().decode('utf-8')
print(content)




