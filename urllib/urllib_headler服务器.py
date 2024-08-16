import urllib.request

url = 'http://www.baidu.com'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
}

request = urllib.request.Request(url=url, headers=headers)

#handler     build_opener      open
#获取handler对象
handler = urllib.request.HTTPHandler()
#获取opener对象
opener = urllib.request.build_opener(handler)
#调用opener的open方法
respomse = opener.open(request)

content = respomse.read().decode('utf-8')

print(content)
