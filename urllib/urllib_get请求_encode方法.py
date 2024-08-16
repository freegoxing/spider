import urllib.parse
import urllib.request
#应用场景 多个参数

#https://www.baidu.com/s?wd=周杰伦&sex=男

# data = {
#     'wd':'周杰伦',
#     'sex':'男',
#     'location':'中国'
# }

#urllib.parse.urlencode(data) 将字典转换为url参数


#获取https://www.baidu.com/s?wd=%E5%91%A8%E6%9D%B0%E4%BC%A6&sex=%E7%94%B7 的网页源码

base_url = 'https://www.baidu.com/s?'
data = {
    'wd':'周杰伦',
    'sex':'男'
}
date = urllib.parse.urlencode(data)
url = base_url + date

headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 Edg/126.0.0.0'
}
request = urllib.request.Request(url=url,headers=headers)
response = urllib.request.urlopen(request)

#获取网页源码
content = response.read().decode('utf-8')
print(content)

